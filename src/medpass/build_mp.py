"""Builds Med Pass (all exams, separated by exam) from Med Pass 3's app shell + the merged data in merge.py."""
import base64, json, re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import merge as M
M.DRUGS = M.DRUGS
sys.path.insert(0, "/home/claude/exam4-src")
from fmt import format_question
F = lambda t: format_question([t])[0] if isinstance(t, str) else t
for d in M.DRUGS:
    for k in ("use", "tip", "warn"): d[k] = F(d[k])
    d["f"] = [F(x) for x in d["f"]]
for l in M.LESSONS:
    l["how"] = F(l["how"]); l["why"] = [[F(a), F(b)] for a, b in l["why"]]; l["watch"] = [F(x) for x in l["watch"]]
for grps in M.SORT.values():
    for g in grps: g["l"] = F(g["l"]); g["w"] = F(g["w"])
for x in M.LOOK:
    x["d"] = {g: [F(f) for f in fs] for g, fs in x["d"].items()}

SRC_MAIN, SRC_BS, SRC_SI, OUT = sys.argv[1:5]
J = lambda x: json.dumps(x, ensure_ascii=False)
weeks = [w for w, _ in M.WEEKS]
EXLBL = "Exams " + "–".join([weeks[0], weeks[-1]]) if len(weeks) > 1 else "Exam " + weeks[0]
WK = {d["g"]: (d["w"] if isinstance(d["w"], list) else [d["w"]]) for d in M.DRUGS}
N = len(M.DRUGS)

def rep(s, old, new, count=1):
    n = s.count(old)
    if n != count: raise SystemExit(f"expected {count} of {old[:60]!r}, found {n}")
    return s.replace(old, new)

def cut(s, start, end_marker):
    """Replace s[start_of(start) : start_of(end_marker)] — returns (before, after)."""
    i = s.index(start); j = s.index(end_marker, i)
    return s[:i], s[j:]

# ---------- Learn (Baby Steps) ----------
bs = open(SRC_BS, encoding="utf-8").read()
bs = rep(bs, "PN III · Exam 3 · 46 meds tested", f"PN III · {EXLBL} · {N} meds")
bsD = [{k: d[k] for k in ("g", "cls", "grp", "u", "use", "tip", "warn")} for d in M.DRUGS]
a, b = cut(bs, "const D=[", "const SK=")
bs = a + f"const D={J(bsD)};\nconst LESSONS={J([{'id':l['id'],'t':l['t'],'d':l['d'],'ex':l['ex']} for l in M.LESSONS])};\n" + b
a, b = cut(bs, "const WK=", "const inW=")
bs = a + f"const WK={J(WK)};\nlet SEL={J(weeks)};\n" + b
bs = rep(bs, "length<7?", f"length<{len(weeks)}?")
bs = rep(bs, 'const KEY="babysteps.v1"', 'const KEY="babystepsx.v1"')
bs = bs.replace("medpass3.v1", "medpassx.v1")
bs = re.sub(r"<title>[^<]*</title>", "<title>Learn Meds</title>", bs, count=1)

# ---------- Sort It ----------
si = open(SRC_SI, encoding="utf-8").read()
si = rep(si, "PN III · Exam 3 · 46 meds tested", f"PN III · {EXLBL} · {N} meds")
a, b = cut(si, "const G={", "/* ---------- weeks:")
drugs_map = {d["g"]: d["cls"] for d in M.DRUGS}
si = a + (f"const G={J(M.SORT)};\n/* tricky sets: groups that are easy to confuse */\nconst TRICKY={J(M.TRICKY)};\n"
          f"/* look-alikes: every fact belongs to exactly one drug in the set */\nconst LOOK={J(M.LOOK)};\nconst DRUGS={J(drugs_map)};\n\n") + b
a, b = cut(si, "const WK=", "const inW=")
si = a + f"const WK={J(WK)};\nlet SEL={J(weeks)};\n" + b
a, b = cut(si, "const XCLS=[", "const CLS_ALL=")
si = a + f"const XCLS={J(M.XCLS)};\n" + b
a, b = cut(si, "const CLS_SECT=[", "const CLASSOF=")
si = a + f"const CLS_SECT={J(M.CLS_SECT)};\n" + b
si = rep(si, 'const KEY="sortit.v1"', 'const KEY="sortitx.v1"')
si = si.replace("medpass3.v1", "medpassx.v1")
si = re.sub(r"<title>[^<]*</title>", "<title>Sort It Meds</title>", si, count=1)

# ---------- main Med Pass ----------
mp = open(SRC_MAIN, encoding="utf-8").read()
mp = rep(mp, "<title>Med Pass 3</title>", "<title>Med Pass</title>")
mp = rep(mp, "PN III · Exam 3 · 46 meds tested", f"PN III · {EXLBL} · {N} meds")
a, b = cut(mp, "const WEEKS=", "/* ---------- lessons:")
mainD = []
for d in M.DRUGS:
    x = {k: v for k, v in d.items() if k != "warn" and v is not None}
    mainD.append(x)
mp = a + (f"const WEEKS={J(M.WEEKS)};\nconst EXAM_WEEKS=WEEKS.map(w=>w[0]);\n\n"
          "/* g generic · b brand · w week · cls class · grp family · u overlap tags: drugs sharing a tag are never\n"
          "   used as each other's wrong answers · use · f facts · tip · cno classes that would also be true */\n"
          f"const D={J(mainD)};\n\n") + b
a, b = cut(mp, "const LESSONS=[", "const lessonOf=")
lessons = [{k: v for k, v in l.items()} for l in M.LESSONS]
mp = a + f"const LESSONS={J(lessons)};\n" + b
mp = rep(mp, '$("nt-note").hidden=selWeeks.has("NT");', '$("nt-note").hidden=true;')
import re as _re
mp = _re.sub(r'<p class="reset-note" id="nt-note"[^\n]*</p>', '<p class="reset-note" id="nt-note" hidden></p>', mp, count=1)
mp = rep(mp, 'const KEY="medpass3.v1"', 'const KEY="medpassx.v1"')
mp = rep(mp, '["medpass3.v1","medpass3.v1.weeks","babysteps.v1","sortit.v1"]', '["medpassx.v1","medpassx.v1.weeks","babystepsx.v1","sortitx.v1"]')
# ---------- "Test it" replaces Survival: continuous round (+1 per miss) or a set number of questions ----------
mp = mp.replace('localStorage.getItem("babysteps.v1")', 'localStorage.getItem("babystepsx.v1")').replace('localStorage.getItem("sortit.v1")', 'localStorage.getItem("sortitx.v1")')
mp = rep(mp, '<button class="mode" id="m-surv"><b>Survival</b><span>3 lives. How far can you go?</span><i id="best-surv">best —</i></button>',
 '<button class="mode" id="m-surv" aria-expanded="false" aria-controls="test-pick"><b>Test it</b><span>Continuous round, or pick how many questions</span><i id="best-surv"></i></button>\n'
 '        <div class="test-pick" id="test-pick" hidden>\n'
 '          <button class="mode" id="t-cont"><b>Continuous</b><span>Every drug in your weeks once. Miss one and another question on it is added.</span><i id="cont-n"></i></button>\n'
 '          <div class="t-count"><div class="t-lbl">Or set how many questions</div><div class="t-nums" id="t-nums">'
 '<button class="chip" data-n="10">10</button><button class="chip" data-n="20">20</button><button class="chip" data-n="30">30</button><button class="chip" data-n="50">50</button></div></div>\n'
 '        </div>')
mp = rep(mp, '.mode i{', '.test-pick{display:flex;flex-direction:column;gap:10px;padding:12px;border:1.5px dashed var(--line);border-radius:14px}\n'
 '.t-count{display:flex;flex-direction:column;gap:8px}.t-lbl{font-size:14px;color:var(--muted)}.t-nums{display:flex;gap:8px;flex-wrap:wrap}\n.mode i{')
mp = rep(mp, '$("best-surv").textContent="best "+(store.best.surv||"—");',
 '$("best-surv").textContent=store.lastTest?store.lastTest:"";$("cont-n").textContent=n+" drugs";$("test-pick").hidden=true;$("m-surv").setAttribute("aria-expanded","false");')
mp = rep(mp, '$("m-surv").addEventListener("click",()=>start("surv"));',
 '$("m-surv").addEventListener("click",()=>{const p=$("test-pick");p.hidden=!p.hidden;$("m-surv").setAttribute("aria-expanded",String(!p.hidden))});\n'
 '$("t-cont").addEventListener("click",()=>start("cont"));\n'
 '$("t-nums").addEventListener("click",e=>{const b=e.target.closest("[data-n]");if(b)start("count",+b.dataset.n)});')
mp = rep(mp, 'function start(mode){', 'function start(mode,count){')
mp = rep(mp, '  if(mode==="miss")list=shuffle(store.missed.map(byG).filter(Boolean));',
 '  if(mode==="miss")list=shuffle(store.missed.map(byG).filter(Boolean));\n'
 '  if(mode==="cont")list=shuffle(pool());\n'
 '  if(mode==="count"){let p=[];while(p.length<count)p=p.concat(shuffle(pool()));list=p.slice(0,count)}')
mp = rep(mp, 'G={mode,list,i:0,', 'G={mode,count,used:{},list,i:0,')
mp = rep(mp, '    t=G.list[G.i];G.q=makeQ(t);',
 '    t=G.list[G.i];const used=G.used[t.g]||(G.used[t.g]=[]);G.q=makeQ(t,undefined,undefined,used);used.push(G.q.id);\n'
 '    if(G.mode==="cont"&&G.extra&&G.extra.has(G.i))label="Extra · ";')
mp = rep(mp, '    G.streak=0;if(G.mode==="surv")G.lives--;',
 '    G.streak=0;if(G.mode==="surv")G.lives--;\n'
 '    if(G.mode==="cont"){G.extra=G.extra||new Set();let pos=Math.min(G.list.length,G.i+4);'
 'while(pos<G.list.length&&(G.list[pos-1].g===t.g||G.list[pos].g===t.g))pos++;'
 'G.list.splice(pos,0,t);G.extra=new Set([...G.extra].map(k=>k>=pos?k+1:k));G.extra.add(pos);'
 'added=`<div class="added">+1 question on ${esc(t.g)} added a few questions from now.</div>`;}')
mp = rep(mp, '$("res-mode").textContent={surv:"Survival",miss:"Missed pile"}[G.mode]+" · results";',
 '$("res-mode").textContent=({surv:"Survival",miss:"Missed pile",cont:"Continuous",count:G.count+" questions"}[G.mode])+" · results";\n'
 '  if(G.mode==="cont"||G.mode==="count"){store.lastTest=`last ${acc}%`;save();}')
mp = rep(mp, '$("again").dataset.mode=G.mode;', '$("again").dataset.mode=G.mode;$("again").dataset.n=G.count||"";')
mp = rep(mp, '$("again").addEventListener("click",e=>start(e.currentTarget.dataset.mode));',
 '$("again").addEventListener("click",e=>start(e.currentTarget.dataset.mode,+e.currentTarget.dataset.n||undefined));')
mp = rep(mp, "Erases progress in Learn, Sort It, Survival, and the Missed pile.", "Erases progress in Learn, Sort It, Test it, and the Missed pile.")
mp = rep(mp, "answered in Survival + Missed pile", "answered in Test it + Missed pile")

# ---------- exams instead of weeks ----------
for name in ("bs", "si"):
    t = bs if name == "bs" else si
    t = t.replace("No weeks are selected. Pick weeks on the Med Pass home screen.", "No exams are selected. Pick exams on the Med Pass home screen.")
    t = t.replace("your chosen weeks", "your chosen exams").replace("in your weeks", "in your exams").replace("Add weeks on the Med Pass home screen.", "Add exams on the Med Pass home screen.")
    t = t.replace("· your weeks`", "· your exams`")
    if name == "bs": bs = t
    else: si = t
bs = rep(bs, "let c=D.filter(d=>famOf(d.g).id!==fid&&!share(d,t)&&d[s]&&d[s]!==t[s]);",
         "let c=D.filter(d=>famOf(d.g).id!==fid&&!share(d,t)&&d[s]&&d[s]!==t[s]&&(WK[d.g]||[]).some(w=>(WK[t.g]||[]).includes(w)&&(!SEL||SEL.includes(w))));")
mp = rep(mp, '<div class="eyebrow">Weeks to include · applies to everything below</div>', '<div class="eyebrow">Exams to include · applies to everything below</div>')
mp = rep(mp, '>All exam weeks</button>', '>All exams</button>')
mp = rep(mp, '${n}<small>${w==="NT"?"per tips":w}</small>', '${n}')
mp = rep(mp, '$("q-meta").textContent=label+"Week "+wk(t).join(" · ");', '$("q-meta").textContent=label+"Exam "+wk(t).join(" · Exam ");')
mp = mp.replace("Every drug in your weeks once.", "Every drug in your exams once.")
i = mp.index("function makeQ("); j = mp.index("/* ---------- game", i)
mp = mp[:i] + "const DX=t=>{const ok=wk(t).filter(w=>selWeeks.has(w));const ex=ok.length?ok:wk(t);return D.filter(d=>wk(d).some(w=>ex.includes(w)))};\n" + mp[i:j].replace("D.filter(", "DX(t).filter(") + mp[j:]

OWN = "const OWN=sel=>{const own={};[...LESSONS].sort((a,b)=>b.ex.localeCompare(a.ex)).forEach(l=>{if(sel&&!sel.includes(l.ex))return;l.d.forEach(g=>{if(!own[g]&&(!sel||(WK[g]||[]).some(w=>sel.includes(w))))own[g]=l.id})});return own};\n"
bs = rep(bs, "const LV=()=>LESSONS.map(l=>({...l,d:l.d.filter(inW)})).filter(l=>l.d.length);",
         OWN + "const LV=()=>{const own=OWN(SEL);return LESSONS.map(l=>({...l,d:l.d.filter(g=>own[g]===l.id)})).filter(l=>l.d.length)};")
mp = rep(mp, "const famsInWeeks=()=>{const p=new Set(pool().map(d=>d.g));return LESSONS.filter(l=>l.d.some(g=>p.has(g)))};",
         "const famsInWeeks=()=>{const sel=[...selWeeks],own={};[...LESSONS].sort((a,b)=>b.ex.localeCompare(a.ex)).forEach(l=>{if(!sel.includes(l.ex))return;l.d.forEach(g=>{if(!own[g]&&D.some(d=>d.g===g&&wk(d).some(w=>sel.includes(w))))own[g]=l.id})});return LESSONS.filter(l=>l.d.some(g=>own[g]===l.id))};")

enc = lambda s: base64.b64encode(s.encode("utf-8")).decode()
mp = re.sub(r'(<script type="application/octet-stream" id="src-bs">)[^<]*(</script>)', lambda m: m.group(1) + enc(bs) + m.group(2), mp, count=1)
mp = re.sub(r'(<script type="application/octet-stream" id="src-si">)[^<]*(</script>)', lambda m: m.group(1) + enc(si) + m.group(2), mp, count=1)
for name, txt in (("main", mp), ("learn", bs), ("sort", si)):
    for bad in ["46 meds tested", "medpass3", "medpass4", "babysteps4", "sortit4", "Week "]:
        if name == "main" and bad == "Week ": continue
        if bad in txt: raise SystemExit(f"leftover in {name}: {bad}")
open(OUT, "w", encoding="utf-8").write(mp)
open(OUT.replace(".html", "_bs.html"), "w", encoding="utf-8").write(bs)
open(OUT.replace(".html", "_si.html"), "w", encoding="utf-8").write(si)
print("ok", N, "drugs", len(mp), "bytes")
