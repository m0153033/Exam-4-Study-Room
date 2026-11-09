#!/bin/sh
# Copies the latest Med Pass build into the Study Room repo with a "back to Study Room" link.
python3 - <<'PY'
import re
m=open('/home/claude/medpass/medpass.html').read()
old=re.search(r'      <div class="eyebrow">PN III · Exams? [^<]* · \d+ meds</div>',m).group(0)
m=m.replace(old,'      <a class="eyebrow back-home" href="./">← Study Room</a>\n'+old,1)
m=m.replace('.eyebrow{','.back-home{display:inline-block;text-decoration:none;color:var(--amber);padding:6px 0;font-weight:700}\n.eyebrow{',1)
open('/home/claude/exam-4-study-room/medpass.html','w').write(m)
PY
