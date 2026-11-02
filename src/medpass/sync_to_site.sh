#!/bin/sh
# Copies the latest Med Pass 4 build into the Study Room repo with a "back to Study Room" link.
python3 - <<'PY'
m=open('/home/claude/medpass4/medpass4.html').read()
import re
old=re.search(r'      <div class="eyebrow">PN III · Exam 4 · \d+ meds</div>',m).group(0)
m=m.replace(old,'      <a class="eyebrow back-home" href="./">← Exam 4 Study Room</a>\n'+old)
m=m.replace('.eyebrow{','.back-home{display:inline-block;text-decoration:none;color:var(--amber);padding:6px 0;font-weight:700}\n.eyebrow{',1)
open('/home/claude/exam-4-study-room/medpass.html','w').write(m)
PY
