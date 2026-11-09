"""Merges the per-exam Med Pass data into one set, separated by exam.
A drug that shows up in more than one lecture or exam becomes ONE entry (one set of questions) tagged with every exam it
belongs to. Overlap tags and families are prefixed by exam, so distractors stay correct inside each exam's own data."""
import json, os, sys, copy
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import mp1_data, mp2_extra, mp5_data
J = lambda f: json.load(open(os.path.join(HERE, f), encoding="utf-8"))

EXAMS = []   # (id, label, drugs, lessons, sort, tricky, look, xcls, sect)
# ---- Exam 5 (added lecture by lecture) ----
EXAMS.append(("5", "Exam 5", mp5_data.DRUGS, mp5_data.LESSONS, mp5_data.SORT, mp5_data.TRICKY, mp5_data.LOOK, mp5_data.XCLS, mp5_data.CLS_SECT))
# ---- Exam 4 ----
m4 = J("mp4.json")
EXAMS.append(("4", "Exam 4", m4["D"], m4["LESSONS"], m4["SORT"], m4["TRICKY"], m4["LOOK"], m4["XCLS"], m4["CLS_SECT"]))
# ---- Exam 3 (the professors' "not tested" list stays out) ----
m3 = J("mp3.json"); warn3 = {d["g"]: d.get("warn") for d in m3["bs"]["D"]}
d3 = [dict(d, warn=warn3.get(d["g"])) for d in m3["main"]["D"] if "NT" not in ([d["w"]] if isinstance(d["w"], str) else d["w"])]
EXAMS.append(("3", "Exam 3", d3, m3["main"]["LESSONS"], m3["si"]["G"], m3["si"]["TRICKY"], m3["si"]["LOOK"], m3["si"]["XCLS"], m3["si"]["CLS_SECT"]))
# ---- Exam 2 ----
m2 = J("mp2.json"); d2 = [dict(d, warn=mp2_extra.WARN.get(d["g"], "")) for d in m2["D"]]
EXAMS.append(("2", "Exam 2", d2, mp2_extra.LESSONS, mp2_extra.SORT, mp2_extra.TRICKY, mp2_extra.LOOK, mp2_extra.XCLS, mp2_extra.CLS_SECT))
# ---- Exam 1 ----
EXAMS.append(("1", "Exam 1", mp1_data.DRUGS, mp1_data.LESSONS, mp1_data.SORT, mp1_data.TRICKY, mp1_data.LOOK, mp1_data.XCLS, mp1_data.CLS_SECT))

DRUGS, by = [], {}
for ex, _, drugs, *_ in EXAMS:
    for d0 in drugs:
        d = copy.deepcopy(d0)
        tags = [f"e{ex}:{x}" for x in d.get("u", [])] + [f"e{ex}:grp:{d['grp']}"]
        g = d["g"]
        if g not in by:
            n = {"g": g, "b": d.get("b"), "w": [ex], "cls": d["cls"], "grp": f"e{ex}:{d['grp']}", "u": tags,
                 "use": d.get("use"), "f": list(d.get("f", [])), "tip": d.get("tip"), "warn": d.get("warn") or ""}
            if d.get("cno"): n["cno"] = list(d["cno"])
            by[g] = n; DRUGS.append(n)
        else:
            n = by[g]
            if ex not in n["w"]: n["w"].append(ex)
            n["u"] += [t for t in tags if t not in n["u"]]
            for x in d.get("f", []):
                if x not in n["f"]: n["f"].append(x)
            if d["cls"] != n["cls"]: n["cno"] = sorted(set(n.get("cno", []) + [d["cls"]]))
            for c in d.get("cno", []):
                if c != n["cls"]: n["cno"] = sorted(set(n.get("cno", []) + [c]))
            u2 = d.get("use")
            if u2 and not n["use"]: n["use"] = u2
            elif u2 and u2.lower() not in n["use"].lower() and n["use"].count(";") < 2: n["use"] = n["use"] + "; " + u2
            n["b"] = n["b"] or d.get("b"); n["tip"] = n["tip"] or d.get("tip"); n["warn"] = n["warn"] or d.get("warn") or ""
for n in DRUGS:
    n["w"] = sorted(n["w"])
    if n.get("cno"): n["cno"] = [c for c in n["cno"] if c != n["cls"]] or None
    if not n.get("cno"): n.pop("cno", None)
    if not n["b"]: n.pop("b")
    n["tip"] = n["tip"] or ""
NAMES = set(by)

# ---- Learn families: each exam keeps its own families. When several selected exams teach the same drug, the
#      most recent exam's family shows it (the app decides from the exams chosen), so nothing repeats ----
LESSONS, used = [], set()
for ex, label, _, lessons, *_ in sorted(EXAMS, key=lambda e: e[0]):
    for l in lessons:
        ds = [g for g in l["d"] if g in NAMES]
        if not ds: continue
        used.update(ds); x = copy.deepcopy(l); x["id"] = f"e{ex}_{l['id']}"; x["d"] = ds; x["ex"] = ex; LESSONS.append(x)

# ---- Sort It: groups with the same name across exams merge; each drug sits in one group per sort ----
SORT, KEYMAP = {}, {}
for mode in ("cls", "use", "warn"):
    out, bylabel, seen = [], {}, set()
    for ex, label, _, _, sort, *_ in EXAMS:
        for grp in sort.get(mode, []):
            key = f"e{ex}_{grp['k']}"; lab = grp["l"].strip().lower()
            ds = [g for g in grp["d"] if g in NAMES and (mode != "cls" or g not in seen)]
            if lab in bylabel:
                tgt = bylabel[lab]; KEYMAP[(mode, key)] = tgt["k"]; tgt["d"] += [g for g in ds if g not in tgt["d"]]; seen.update(ds); continue
            x = copy.deepcopy(grp); x["k"] = key; x["d"] = ds; seen.update(ds)
            bylabel[lab] = x; KEYMAP[(mode, key)] = key; out.append(x)
    SORT[mode] = [x for x in out if x["d"]]
alive = {m: {x["k"] for x in SORT[m]} for m in SORT}
TRICKY = {}
for ex, _, _, _, _, tricky, *_ in EXAMS:
    for mode, sets in tricky.items():
        for s in sets:
            ks = []
            for k in s:
                t = KEYMAP.get((mode, f"e{ex}_{k}"))
                if t in alive.get(mode, ()) and t not in ks: ks.append(t)
            if len(ks) >= 2: TRICKY.setdefault(mode, []).append(ks)

LOOK = []
for ex, _, _, _, _, _, look, *_ in EXAMS:
    for lk in look:
        d = {g: fs for g, fs in lk["d"].items() if g in NAMES}
        if len(d) >= 2 and lk["t"] not in [x["t"] for x in LOOK]: LOOK.append({"t": lk["t"], "d": d})

# ---- Sort It "all at once" board ----
on_board = {g for x in SORT["cls"] for g in x["d"]}
XCLS = []
for ex, _, _, _, _, _, _, xcls, _ in EXAMS:
    for x in xcls:
        ds = [g for g in x["d"] if g in NAMES and g not in on_board]
        if not ds: continue
        on_board.update(ds); lab = x["l"].strip().lower()
        same = [g for g in SORT["cls"] + XCLS if g["l"].strip().lower() == lab]
        if same: same[0]["d"] += ds; KEYMAP[("cls", f"e{ex}_{x['k']}")] = same[0]["k"]; continue
        y = dict(x); y["k"] = f"e{ex}_{x['k']}"; y["d"] = ds; XCLS.append(y)
xalive = {x["k"] for x in XCLS} | alive["cls"]
CLS_SECT = []
for ex, label, *rest in sorted(EXAMS, key=lambda e: e[0]):
    for name, keys in rest[-1]:
        ks = []
        for k in keys:
            t = KEYMAP.get(("cls", f"e{ex}_{k}"), f"e{ex}_{k}")
            if t in xalive and t not in ks and not any(t in s[1] for s in CLS_SECT): ks.append(t)
        if ks: CLS_SECT.append([f"{label} · {name}", ks])
WEEKS = [[ex, label] for ex, label, *_ in sorted(EXAMS, key=lambda e: e[0])]

if __name__ == "__main__":
    print(len(DRUGS), "drugs ·", {ex: sum(ex in d["w"] for d in DRUGS) for ex, *_ in EXAMS})
    print("multi-exam:", [(d["g"], d["w"]) for d in DRUGS if len(d["w"]) > 1])
    print(len(LESSONS), "families;", {m: len(v) for m, v in SORT.items()}, "sort groups;", len(LOOK), "look-alike sets;", len(XCLS), "xcls;", len(CLS_SECT), "sections")
    nol = [d["g"] for d in DRUGS if d["g"] not in used]; print("not in any family:", nol)
