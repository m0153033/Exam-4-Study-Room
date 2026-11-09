"""Builds questions.js for the Study Room from:
 - every *_bank.py in this folder (Exam 1 and Exam 4 lectures, written from the lecture files), and
 - imported/ (the Exam 2 and Exam 3 question banks from the earlier study rooms, dosage math left out).
Output path: $OUT, or ../exam4-site/questions.js by default."""
import json, glob, os, importlib.util
from fmt import format_question
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("OUT") or os.path.join(HERE, "..", "exam4-site", "questions.js")

# ---------- exams, in order ----------
EXAMS = [
 {"id":"e1","name":"Exam 1","weeks":"Wk 1.1–2.3","date":"","topics":["vision","resp","dys1","cardinf","male"]},
 {"id":"e2","name":"Exam 2","weeks":"Wk 4.1–6.1","date":"","topics":["e2w41","e2w42","e2w43","e2w51","e2w52","e2w53","e2w61"]},
 {"id":"e3","name":"Exam 3","weeks":"Wk 6.2–9.2","date":"","topics":["e3w62","e3w71","e3w72","e3w73","e3w81","e3w82","e3w91","e3w92"]},
 {"id":"e4","name":"Exam 4","weeks":"Wk 9.3–11.3","date":"Nov 9","topics":["hf","neuro","giinf","digest","glucose","blood","teams"]},
 {"id":"e5","name":"Exam 5","weeks":"","date":"Nov 30","topics":["e5imm","e5bowel","e5viral","e5skin","e5slera","e5ibd","e5hiv"]},
]
TOPICS = {
 "vision":"Wk 1.1 Visual Variations","resp":"Wk 1.2 Pharm: Respiratory System","dys1":"Wk 2.1 Dysrhythmias Part 1",
 "cardinf":"Wk 2.2 Cardiac Infection","male":"Wk 2.3 Male Sexual Function",
 "hf":"Wk 9.3 Cardiomyopathy / Heart Failure","neuro":"Wk 10.1 Pharm: Neurological System Part 1","giinf":"Wk 10.2 GI Infection",
 "digest":"Wk 10.3 Infection of the Digestive System","glucose":"Wk 11.1 Glucose Regulation","blood":"Wk 11.2 Blood Products & Administration",
 "teams":"Wk 11.3 Collaborative Health Care Teams",
 "e5imm":"Pharmacology: Immune System","e5bowel":"Bowel Obstruction","e5viral":"Viral Syndromes","e5skin":"Skin Cancer",
 "e5slera":"SLE & Rheumatoid Arthritis","e5ibd":"Ulcerative Colitis & Crohn's","e5hiv":"HIV",
}
BLUEPRINT = {"neuro":[8,1],"hf":[7,2],"giinf":[7,1],"digest":[5,0],"glucose":[12,2],"blood":[5,1],"teams":[4,0],
 "e5imm":[8,1],"e5bowel":[7,1],"e5viral":[7,1],"e5skin":[5,1],"e5slera":[7,1],"e5ibd":[7,1],"e5hiv":[7,1]}
# abbreviations that mean different things in different lectures
EXTRA = {"vision":{"MD":"macular degeneration"},"dys1":{"AV":"atrioventricular"},"male":{"ED":"erectile dysfunction"},
 "e2w51":{"AV":"atrioventricular"},"e3w82":{"AV":"arteriovenous","PD":"peritoneal dialysis","RRT":"renal replacement therapy","HD":"hemodialysis"},
 "e3w92":{"PD":"personality disorder"},"e3w91":{"AD":"Alzheimer's disease"}}
EXCLUDE = {"e3a_n1","e3b_A1","e3a_o48","e3a_o64"}   # arithmetic (MAP / CBI totals): math is left out
SKIP = {"e2":{"epinephrine"},"e3":{"epinephrine"}}
exam_of = {t: e["id"] for e in EXAMS for t in e["topics"]}

concepts, hi, rows, counts = {}, {}, {}, {}
def emit(t, qid, c, stem, o, a, r, w, sata):
    f = format_question([stem] + o + [r] + w, skip=SKIP.get(exam_of[t], ()), extra=EXTRA.get(t))
    stem, o, r, w = f[0], f[1:1 + len(o)], f[1 + len(o)], f[2 + len(o):]
    rows.setdefault(t, []).append(json.dumps({"id": qid, "t": t, "c": c, "type": "sata" if sata else "mc", "q": stem, "o": o,
                                  "a": a if sata else a[0], "r": r, "w": w}, ensure_ascii=False) + ",")
    counts[t] = counts.get(t, 0) + 1

# ---------- lecture banks written here ----------
for f in sorted(glob.glob(os.path.join(HERE, "*_bank.py"))):
    spec = importlib.util.spec_from_file_location(os.path.basename(f), f); b = importlib.util.module_from_spec(spec); spec.loader.exec_module(b)
    t = b.T; assert t in exam_of, t
    concepts[t] = b.CONCEPTS; hi[t] = b.HI
    for c in b.HI: assert c in b.CONCEPTS, (t, c)
    used = set()
    for n, (c, stem, opts, r) in enumerate(b.Q, 1):
        assert c in b.CONCEPTS, (t, c); used.add(c)
        o, a, w = [], [], []
        for i, x in enumerate(opts):
            if x.startswith("*"): a.append(i); o.append(x[1:].split("||")[0].strip())
            else:
                txt, _, why = x.partition("||"); o.append(txt.strip()); w.append(why.strip()); assert why.strip(), (stem, x)
        sata = "Select all that apply" in stem
        assert a and (len(a) >= 2 if sata else len(a) == 1), stem
        emit(t, f"{t}{n}", c, stem, o, a, r, w, sata)
    missing = set(b.CONCEPTS) - used; assert not missing, (t, missing)

# ---------- imported Exam 2 / Exam 3 banks ----------
def load_why(*names):
    d = {}
    for n in names:
        p = os.path.join(HERE, "imported", n)
        if not os.path.exists(p): continue
        spec = importlib.util.spec_from_file_location(n, p); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); d.update(m.WHY)
    return d
def strip_week(name): return name
def import_bank(exam, files, why):
    for tag, fn in files:
        m = json.load(open(os.path.join(HERE, "imported", fn), encoding="utf-8"))
        for k, name in m["TOPICS"].items():
            if k == "math": continue
            t = exam + k; TOPICS.setdefault(t, name)
            concepts.setdefault(t, dict(m["CONCEPTS"][k]))
            if m.get("HI") and k in m["HI"]: hi[t] = sorted(set(hi.get(t, [])) | set(m["HI"][k]))
            hi.setdefault(t, [])
        whymap = dict(m.get("WHY") or {}); whymap.update(why)
        for q in m["BANK"]:
            if q["t"] == "math" or q.get("type") not in ("mc", "sata"): continue
            t = exam + q["t"]; a = q["a"] if isinstance(q["a"], list) else [q["a"]]
            w = q.get("w") or whymap.get(q["id"]) or []
            nw = len(q["o"]) - len(a)
            if len(w) != nw: w = []      # never misalign notes with options
            stem = q["q"]; sata = q["type"] == "sata"
            if sata and "Select all that apply" not in stem: stem += " Select all that apply."
            if f"{exam}{tag}_{q['id']}" in EXCLUDE: continue
            emit(t, f"{exam}{tag}_{q['id']}", q["c"], stem, list(q["o"]), a, q["r"], list(w), sata)
import_bank("e2", [("", "ex2.json")], load_why("ex2_why_a.py", "ex2_why_b.py"))
import_bank("e3", [("a", "ex3a.json"), ("b", "ex3b.json")], {})

# ---------- write ----------
for e in EXAMS:
    for t in e["topics"]: concepts.setdefault(t, {}); hi.setdefault(t, [])
order = [t for e in EXAMS for t in e["topics"]]
body = []
for t in order:
    if t in rows: body.append(f"/* ---------------- {TOPICS[t].upper()} ---------------- */"); body += rows[t]
js = f"""/* =====================================================================
   PN III · STUDY ROOM QUESTION BANK  (Exams 1–5 + Final)
   Exam 1 and Exam 4 are built from the lecture files one lecture at a time; Exams 2 and 3 come
   from the earlier Exam 2 and Exam 3 study rooms. No dosage math. Generated; do not hand-edit.
   ===================================================================== */
const EXAMS = {json.dumps(EXAMS, ensure_ascii=False)};
const TOPICS = {json.dumps({t: TOPICS[t] for t in order}, ensure_ascii=False, indent=1)};
const BLUEPRINT = {json.dumps(BLUEPRINT)};
const CONCEPTS = {json.dumps({t: concepts[t] for t in order}, ensure_ascii=False, indent=1)};
const HI = {json.dumps({t: hi[t] for t in order})};
const BANK = [
{chr(10).join(body)}
];
"""
open(OUT, "w", encoding="utf-8").write(js)
print({e["name"]: {t: counts.get(t, 0) for t in e["topics"]} for e in EXAMS})
