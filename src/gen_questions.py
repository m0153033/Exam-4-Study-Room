"""Builds ../exam4-site/questions.js from every *_bank.py in this folder (one per lecture)."""
import json, glob, os, importlib.util
from fmt import format_question
HERE = os.path.dirname(os.path.abspath(__file__))
ORDER = ["neuro","hf","giinf","digest","glucose","blood","teams"]
TOPICS = {"neuro":"Pharmacology: Neurological System Part 1","hf":"Cardiomyopathy / Heart Failure","giinf":"Gastrointestinal Infection",
  "digest":"Infection of the Digestive System","glucose":"Alterations in Glucose Regulation","blood":"Blood Products & Administration","teams":"Collaborative Health Care Teams"}
BLUEPRINT = {"neuro":[8,1],"hf":[7,2],"giinf":[7,1],"digest":[5,0],"glucose":[12,2],"blood":[5,1],"teams":[4,0]}
banks = {}
for f in glob.glob(os.path.join(HERE, "*_bank.py")):
    spec = importlib.util.spec_from_file_location(os.path.basename(f), f); b = importlib.util.module_from_spec(spec); spec.loader.exec_module(b)
    banks[b.T] = b
concepts = {t: (banks[t].CONCEPTS if t in banks else {}) for t in ORDER}
hi = {t: banks[t].HI for t in ORDER if t in banks}
rows = []
for t in ORDER:
    if t not in banks: continue
    b = banks[t]; rows.append(f"/* ---------------- {TOPICS[t].upper()} ---------------- */")
    for n, (c, stem, opts, r) in enumerate(b.Q, 1):
        assert c in b.CONCEPTS, c
        o, a, w = [], [], []
        for i, x in enumerate(opts):
            if x.startswith("*"): a.append(i); o.append(x[1:].split("||")[0].strip())
            else:
                txt, _, why = x.partition("||"); o.append(txt.strip()); w.append(why.strip()); assert why.strip(), (stem, x)
        sata = "Select all that apply" in stem
        assert a and (len(a) >= 2 if sata else len(a) == 1), stem
        f = format_question([stem] + o + [r] + w)
        stem, o, r, w = f[0], f[1:1 + len(o)], f[1 + len(o)], f[2 + len(o):]
        rows.append(json.dumps({"id": f"{t}{n}", "t": t, "c": c, "type": "sata" if sata else "mc", "q": stem, "o": o,
                                "a": a if sata else a[0], "r": r, "w": w}, ensure_ascii=False) + ",")
js = f"""/* =====================================================================
   PN III · EXAM 4 QUESTION BANK  (exam: November 9, 2026)
   Generated from the lecture materials, one lecture at a time. Do not hand-edit.
   ===================================================================== */
const EXAM = {{ name: "Exam 4", course: "PN III", date: "Nov 9" }};
const TOPICS = {json.dumps({t: TOPICS[t] for t in ORDER}, ensure_ascii=False, indent=1)};
const BLUEPRINT = {json.dumps(BLUEPRINT)};
const CONCEPTS = {json.dumps(concepts, ensure_ascii=False, indent=1)};
const HI = {json.dumps(hi)};
const BANK = [
{chr(10).join(rows)}
];
"""
open(os.path.join(HERE, "..", "questions.js"), "w", encoding="utf-8").write(js)
print({t: len(banks[t].Q) for t in banks})
