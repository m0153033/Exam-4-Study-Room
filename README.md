# Study Room

A free group quiz site for PN III. Pick **Exam 1, 2, 3, 4, 5** or the **Final**. No accounts needed.

- **Host a group:** open the site, tap *Host a group*, pick the exam and share the one-word room password.
- **Join a group:** open the site, tap *Join a group*, and type the password.
- **Solo:** practice on your own.
- **Final:** one question per concept from every exam you pick, so every topic is covered once.
- **Med Pass:** `medpass.html`, learn, sort and test the medications, separated by exam. A drug taught in more than one lecture or exam is one card with one set of questions.

Phones connect directly to the host's screen, so the host keeps their tab open while the group plays.
If someone can't connect on school or hospital Wi-Fi, switching to phone data usually fixes it.

## Updating questions
Exam 1 and Exam 4 questions are written per lecture in `src/*_bank.py`; Exams 2 and 3 live in `src/imported/`.
Run `python3 src/gen_questions.py` to rebuild `questions.js`. Exam 5 lectures get their own `src/ex5*_bank.py` files.

## Updating Med Pass
Per-exam drug data lives in `src/medpass/` (`mp1_data.py`, `mp2.json` + `mp2_extra.py`, `mp3.json`, `mp4.json`). `merge.py` combines them; `build_mp.py` builds `medpass.html`.
