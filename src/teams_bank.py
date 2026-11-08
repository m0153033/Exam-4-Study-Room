# Week 11.3 Collaborative Health Care Teams in Emergencies — Prof. Hanikeh's slides + AHA six-person CPR team chart.
T = "teams"
CONCEPTS = {
 "three":"RRT vs Code Blue vs ERT",
 "rrtwhy":"RRT purpose & who can call",
 "rrttrig":"RRT triggers",
 "rrtroles":"RRT roles & how it works",
 "cbwhen":"When to call a Code Blue",
 "cbsteps":"Code Blue step by step",
 "cpr":"CPR quality",
 "cbroles":"Code Blue roles",
 "aha":"AHA six-person team",
 "comm":"SBAR & closed-loop communication",
 "debrief":"Debriefing",
 "ert":"Emergency Response Team",
 "codes":"Hospital emergency codes",
 "which":"Which code to call: deteriorating vs arrest (FOCUS)",
 "which2":"Which code to call: visitors, staff & other codes (FOCUS)",
}
# VERSION 2 (Nov 8): every question re-worded with new scenarios/distractors.
# Classmate update (Nov 3): know which code to call from a patient scenario.
HI = ["three","which","which2","rrttrig","cbwhen","comm","aha","cbsteps"]

SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

RRT="Call the Rapid Response Team"; CB="Call a Code Blue and start CPR"; ERT_="Call the Emergency Response Team"; NONE="Document it and recheck later || This change needs a team called now."

# ---------- RRT vs Code Blue vs ERT ----------
q("three","Which statement correctly matches each team?",
 ["*RRT: an inpatient getting worse · Code Blue: an inpatient in arrest · ERT: a visitor or staff member who needs help","RRT: arrest · Code Blue: getting worse || Reversed.",
  "ERT: inpatients in arrest || That's Code Blue.","Code Blue: visitors who faint || That's ERT."],
 "RRT prevents the arrest; Code Blue treats it; ERT covers non-patients.")
q("three","A patient was talking a minute ago and is now limp, not breathing and has no carotid pulse. What should the nurse do first?",
 ["*"+CB,RRT+" || The patient is in arrest.","Put on oxygen and get vitals || Delays CPR.","Move the patient to the stretcher || Delays CPR."],
 "Immediate CPR and a Code Blue are critical in arrest.")
q("three","Over the last hour a patient has become more and more confused. What is the best action?",
 ["*"+RRT,CB+" || Not in arrest.","Put on 2 L of oxygen only || Doesn't address the change.","Keep routine monitoring || A change needs action."],
 "New mental status changes are early warning signs.")
q("three","Which finding means a Code Blue, not a Rapid Response?",
 ["*No breathing and no pulse","BP 88/58 || RRT.","HR 136 || RRT.","RR 30 || RRT."],
 "Code Blue = no pulse and/or not breathing.")
q("three","A patient is breathing and has a pulse but is suddenly very hard to wake. Which team?",
 ["*The Rapid Response Team","Code Blue || Still breathing with a pulse.","ERT || For non-patients.","No team; check in an hour || Sudden change is a trigger."],
 "If the breathing or pulse stops, it becomes a Code Blue.")
q("three","Which pairs of team and situation are correct? "+SATA,
 ["*RRT: an inpatient with early signs of decline","*Code Blue: cardiac or respiratory arrest","*ERT: a visitor or staff member needing medical help","ERT: an inpatient in arrest || Code Blue.","Code Blue: a dizzy visitor || ERT."],
 "Pick the team by WHO it is and WHETHER they have a pulse and are breathing.")

# ---------- which code to call (FOCUS) ----------
q("which","A patient's heart rate is 36 and they feel lightheaded, but they're awake with a pulse. What should the nurse do?",
 ["*"+RRT,CB+" || Has a pulse and is awake.",ERT_+" || For non-patients.",NONE],
 "RRT trigger: HR under 40 or over 130.")
q("which","A patient's heart rate is 142 and they look anxious. They're breathing and have a pulse. What should the nurse do?",
 ["*"+RRT,CB+" || Not in arrest.",ERT_+" || For non-patients.",NONE],
 "HR over 130 is an RRT trigger.")
q("which","A post-op patient's O2 sat is 85% on 3 L of oxygen and RR is 30. They're awake. What should the nurse do?",
 ["*"+RRT,CB+" || Breathing with a pulse.",ERT_+" || For non-patients.",NONE],
 "O2 sat under 90% despite oxygen and RR over 28 are RRT triggers.")
q("which","A patient's respiratory rate drops to 6 after an opioid dose. They have a pulse. Which team?",
 ["*"+RRT,CB+" || Still breathing with a pulse.",ERT_+" || For non-patients.",NONE],
 "RR under 8 is an RRT trigger.")
q("which","A patient's systolic BP is 82 and they're newly confused. What should the nurse do?",
 ["*"+RRT,CB+" || Not in arrest.",ERT_+" || For non-patients.",NONE],
 "SBP under 90 and new confusion are RRT triggers.")
q("which","A patient suddenly has slurred speech and a facial droop. They're breathing with a pulse. Which team?",
 ["*The Rapid Response Team","Code Blue || Not in arrest.","ERT || For non-patients.","No team; reassess later || A sudden neuro change."],
 "Sudden slurred speech can mean a stroke.")
q("which","A patient on the medical floor starts having a seizure. They're breathing and have a pulse. Which team?",
 ["*The Rapid Response Team","Code Blue || Not in arrest.","ERT || For visitors and staff.","None || A new seizure is a trigger."],
 "New seizure activity is an RRT trigger.")
q("which","A patient has chest pain that nitroglycerin isn't relieving. They're awake with a pulse. Which team?",
 ["*The Rapid Response Team","Code Blue || Not in arrest.","ERT || For non-patients.","Wait for the morning rounds || Act now."],
 "Unrelieved chest pain is an RRT trigger.")
q("which","The nurse finds a patient unresponsive with only occasional gasping breaths and no pulse. What should the nurse do?",
 ["*"+CB,RRT+" || In arrest.",ERT_+" || For non-patients.","Count the respirations first || Gasping is not breathing; start CPR."],
 "Agonal gasps don't count as breathing.")
q("which","All vital signs are normal, but the nurse is truly worried the patient is getting worse. What can the nurse do?",
 ["*Call the Rapid Response Team based on concern","Wait until a vital sign is abnormal || Concern is enough.","Call a Code Blue || Not in arrest.","Let the family decide || The nurse decides."],
 "Staff concern is a valid RRT trigger.")
q("which","The RRT is on the way for a patient with chest pain. The patient becomes unresponsive with no pulse. What now?",
 ["*Start CPR and call a Code Blue","Wait for the RRT || It's now an arrest.","Give oxygen and recheck || Delays CPR.","Call the ERT || For non-patients."],
 "Once there's no pulse, it's a Code Blue.")
q("which","A patient's urine output suddenly drops to almost nothing and the patient looks pale. Which team?",
 ["*The Rapid Response Team","Code Blue || Not in arrest.","ERT || For non-patients.","No team; recheck tomorrow || A sudden change is a trigger."],
 "A sudden change in urine output is an RRT trigger.")
q("which","A patient's dressing is soaked with bright red blood and the BP is falling. They're awake. Which team?",
 ["*The Rapid Response Team","Code Blue || Not in arrest.","ERT || For non-patients.","Just reinforce the dressing || Needs a team."],
 "Acute bleeding is an RRT trigger.")
q("which2","A visitor collapses in the hospital cafeteria. Which team is called?",
 ["*The Emergency Response Team (ERT)","Rapid Response Team || For inpatients.","Code Red || Fire.","Code Black || Bomb threat."],
 "ERT: visitors, staff and others who faint, seize, fall or collapse.")
q("which2","A nurse on break in the staff lounge has a seizure. Which team is called?",
 ["*The Emergency Response Team (ERT)","Rapid Response Team || For inpatients.","Code Blue only || Not unless in arrest.","No team; let them rest || Needs help."],
 "Call the emergency number and keep the area safe.")
q("which2","A visitor slips and falls in the parking garage and seems confused. Which team is called?",
 ["*The Emergency Response Team (ERT)","Rapid Response Team || For inpatients.","Code Red || Fire.","Security only || A medical team is needed."],
 "The ERT decides whether the person goes to the ED.")
q("which2","Which situation and call are matched correctly?",
 ["*Inpatient with HR 135 and new confusion: Rapid Response","Visitor fainting in the lobby: Code Blue || ERT.","Inpatient with no pulse: Rapid Response || Code Blue.","Staff member falling in the hallway: Rapid Response || ERT."],
 "RRT = inpatient getting worse; Code Blue = arrest; ERT = non-patient.")
q("which2","The nurse sees smoke coming from a patient's room. Which code is called?",
 ["*Code Red","Code Blue || Arrest.","Code Black || Bomb threat.","Rapid Response || Patient decline."],
 "Code Red = fire.")
q("which2","Someone calls the front desk saying there's a bomb in the hospital. Which code is called?",
 ["*Code Black","Code Red || Fire.","Code Blue || Arrest.","ERT || Medical help."],
 "Code colors vary by hospital; follow your facility's policy.")
q("which2","Which pairs of code and meaning are correct? "+SATA,
 ["*Code Blue: cardiac or respiratory arrest","*Code Red: fire","*Code Black: bomb threat","Code Red: bomb threat || Code Black.","Code Black: fire || Code Red."],
 "Always follow your facility's chart.")

# ---------- RRT purpose ----------
q("rrtwhy","What is the main goal of a Rapid Response Team?",
 ["*Catch a patient getting worse early and act to prevent an arrest","Run the code when there's no pulse || Code Blue.","Help visitors who fall || ERT.","Take over the nurse's patient || The primary nurse stays."],
 "Brings critical care expertise to the bedside fast.")
q("rrtwhy","Who is allowed to call a Rapid Response?",
 ["*Any staff member","Only the provider || Not per the lecture.","Only the charge nurse || Not per the lecture.","Only the family || Not per the lecture."],
 "Many hospitals also let families call.")
q("rrtwhy","A patient is suddenly confused. The glucose is 132 mg/dL. What should the nurse do?",
 ["*Call the Rapid Response Team","Give juice || Glucose isn't low.","Recheck in 4 hours || Act now.","Call a Code Blue || Not in arrest."],
 "New confusion with normal glucose means something else is wrong.")
q("rrtwhy","Which are goals of a Rapid Response Team? "+SATA,
 ["*Prevent cardiac arrest","*Prevent ICU transfer or death","*Bring critical care help to the bedside fast","*Support nurses who are worried about a patient"],
 "From the purpose slide.")

# ---------- RRT triggers ----------
q("rrttrig","Which vital signs meet Rapid Response criteria? "+SATA,
 ["*HR 38","*RR 30","*Systolic BP 86","*O2 sat 87% on oxygen","HR 96 || Normal.","RR 16 || Normal."],
 "HR under 40 or over 130; RR under 8 or over 28; SBP under 90; O2 sat under 90% despite oxygen.")
q("rrttrig","A post-op patient is being assessed. Which findings should prompt a Rapid Response? "+SATA,
 ["*Sudden slurred speech","*O2 sat of 86% on room air","*HR of 42 with dizziness","*New confusion","BP 98/62 alone || Not usually a trigger.","Temperature 100.4°F alone || Not usually a trigger."],
 "Slurred speech may mean stroke.")
q("rrttrig","Which neurological changes trigger a Rapid Response? "+SATA,
 ["*Sudden confusion","*A new seizure","*Suddenly won't respond","Long-standing dementia that hasn't changed || Not sudden."],
 "Key words: sudden or new.")
q("rrttrig","Which breathing findings trigger a Rapid Response? "+SATA,
 ["*Using neck muscles to breathe","*Bluish lips","*Can't finish a sentence","*New stridor"],
 "Also increased work of breathing or new wheezing.")
q("rrttrig","Which other findings trigger a Rapid Response? "+SATA,
 ["*Signs of internal bleeding","*Chest pain that won't go away","*A sudden temperature change with possible sepsis","*A sudden drop in urine output","Pain controlled by the ordered medicine || Not a trigger."],
 "Look for sudden changes.")

# ---------- RRT roles ----------
q("rrtroles","The Rapid Response Team arrives. What does the patient's primary nurse do?",
 ["*Give an SBAR report and stay to help","Leave for other patients || Stays.","Manage the airway || Respiratory therapist.","Write orders || The provider."],
 "The primary nurse knows the patient best.")
q("rrtroles","Which RRT members and jobs are matched correctly? "+SATA,
 ["*RRT nurse: assesses and starts interventions","*Respiratory therapist: airway and oxygen","*Provider: gives orders and evaluates","*Charge nurse: coordinates support and transfers","Respiratory therapist: writes medication orders || The provider."],
 "From the RRT roles slide.")
q("rrtroles","What can happen after a Rapid Response assessment? "+SATA,
 ["*The patient stabilizes and stays on the unit","*The patient moves to the ICU","*The patient gets worse and a Code Blue is called","The team must leave within 1 minute || Not a rule."],
 "Labs, fluids, oxygen and meds can start right away.")
q("rrtroles","How is a Rapid Response called?",
 ["*Dial the specific number or press the button","Send an email || Too slow.","Wait for rounds || Too slow.","Only the family can call || Any staff member can."],
 "The team arrives within minutes.")

# ---------- Code Blue when ----------
q("cbwhen","Which situations call for a Code Blue? "+SATA,
 ["*Unresponsive","*No pulse","*Not breathing or only gasping","*Sudden collapse","HR 134 with a pulse and normal breathing || RRT."],
 "Code Blue = not breathing and/or no pulse.")
q("cbwhen","A patient has no pulse but is taking occasional gasping breaths. What does the nurse do?",
 ["*Call a Code Blue and start CPR","Wait, since they're breathing || Gasping isn't breathing.","Call the RRT || In arrest.","Give oxygen and recheck || Delays CPR."],
 "No pulse = Code Blue now.")

# ---------- Code Blue steps ----------
q("cbsteps","A nurse walks in and finds a patient slumped over. What is the FIRST step?",
 ["*Check responsiveness (tap and shout) and the ABCs","Grab the crash cart || After recognizing and calling.","Assign roles || Step 5.","Call the family || Not first."],
 "Recognize · call · start BLS · get equipment · assign roles · ROSC or termination.")
q("cbsteps","Which is the correct way to call a Code Blue?",
 ["*Say the location clearly, like 'Code Blue, Room 312, North Wing'","Yell 'Help!' only || No location.","Text the provider || Too slow.","Wait for the charge nurse || Call right away."],
 "Press the code button, pull the cord or dial the emergency number.")
q("cbsteps","A nurse is alone when a patient goes into arrest. What should the nurse do?",
 ["*Start compressions and call out for help (or have someone call)","Leave to find help first || Delays CPR.","Wait for the code team || Delays CPR.","Get the crash cart first || Compressions first."],
 "Start compressions immediately.")
q("cbsteps","A nurse isn't doing CPR during a code. How can they help? "+SATA,
 ["*Bring the crash cart","*Bring the defibrillator or AED","*Set up suction","*Set up oxygen"],
 "Get the equipment ready.")
q("cbsteps","The patient has a pulse again (ROSC). What happens next? "+SATA,
 ["*Support breathing and watch vitals","*Transfer to the ICU","*Continue post-resuscitation care","Stop monitoring; the code is over || Care continues."],
 "If there's no ROSC after a long effort, the team may stop.")
q("cbsteps","Who calls the time of death when a code is stopped?",
 ["*The MD","The primary nurse || Not per the lecture.","The recorder || Documents only.","The family || Not per the lecture."],
 "The team decides based on judgment and protocol.")

# ---------- CPR quality ----------
q("cpr","How fast should chest compressions be?",
 ["*100–120 per minute","60–80 per minute || Too slow.","140–160 per minute || Too fast.","30 per minute || Too slow."],
 "Depth 2 inches with full recoil.")
q("cpr","Which are signs of high-quality adult compressions? "+SATA,
 ["*2 inches (5 cm) deep","*Full chest recoil","*100–120 per minute","1 inch deep || Too shallow.","Leaning on the chest between compressions || Blocks recoil."],
 "From the BLS step.")
q("cpr","How often should compressors switch?",
 ["*About every 2 minutes (5 cycles)","Every 30 seconds || Too often.","Every 10 minutes || Quality drops.","Never || Fatigue lowers quality."],
 "The compressor switches with the AED/monitor person.")

# ---------- Code Blue roles ----------
q("cbroles","According to the lecture's Code Blue table, what is the primary RN's job?",
 ["*Chest compressions","Directing the code || The provider.","Giving ACLS medications || The ICU RN.","Intubating || The anesthesiologist."],
 "The primary RN also knows what led up to the arrest.")
q("cbroles","Which Code Blue members and roles are matched correctly? "+SATA,
 ["*Provider: runs the code and makes medical decisions","*ICU RN: gives certain ACLS medications","*Respiratory therapist: airway and rescue breaths","*Anesthesiologist: may intubate","*Security: crowd control"],
 "The charge RN helps assist.")
q("cbroles","Who documents the times of medications, shocks and rhythm changes?",
 ["*The recorder","The compressor || Does CPR.","The medication nurse || Gives meds.","The team leader || Directs."],
 "The recorder also tells the leader key times.")
q("cbroles","Which role runs the code, assigns jobs and reads the heart rhythm?",
 ["*The team leader","The recorder || Documents.","The airway role || Breathing.","The compressor || CPR."],
 "The leader decides when to shock or give meds.")
q("cbroles","Which medications does the medication role give during a code?",
 ["*ACLS drugs such as epinephrine and amiodarone","Insulin and potassium || Not listed.","Antibiotics || Not listed.","Blood || Not listed."],
 "They also manage IV access.")

# ---------- AHA six-person ----------
q("aha","Which three positions make up the AHA 'resuscitation triangle'? "+SATA,
 ["*Compressor","*AED/monitor/defibrillator","*Airway","Team leader || Leadership.","Recorder || Leadership."],
 "Leadership: team leader, recorder, IV/IO/medications.")
q("aha","Which statements about the AHA team leader are correct? "+SATA,
 ["*Every team needs a clear leader","*Assigns roles","*Makes treatment decisions","*Gives feedback","Does compressions the whole time || Directs."],
 "From the AHA six-person chart.")
q("aha","Where does the AHA chart say to place the monitor?",
 ["*Where the whole team can see it","Behind the leader || Visible to all.","Outside the room || Not per the chart.","Facing the family || Not per the chart."],
 "Position 2 runs the AED/monitor.")
q("aha","What does the recorder (position 5) track? "+SATA,
 ["*Times of interventions and medications","*How often and how long compressions are paused","*Reports these to the leader","Opens the airway || Position 3."],
 "Keeps the team on time.")
q("aha","What is the AHA rule about leaving the resuscitation triangle?",
 ["*No one leaves except for their own safety","Anyone can leave when help arrives || Not the rule.","The compressor never switches || Switches every 5 cycles.","Only the leader stays || The whole team stays."],
 "The team owns the code.")

# ---------- communication ----------
q("comm","A nurse calls the Rapid Response Team. Which tool should they use to give report?",
 ["*SBAR","Teach-back || Patient teaching.","CHOLY || Cholecystitis.","Closed-loop only || For orders during a code."],
 "Situation, Background, Assessment, Recommendation.")
q("comm","The leader says, 'Give 300 mg amiodarone IV.' Which reply is closed-loop communication?",
 ["*'300 mg amiodarone IV, giving now,' then confirming when it's given","'Okay.' || Too vague.","No reply, just give it || Unsafe.","'Sure, in a minute.' || Doesn't repeat the order."],
 "The leader then says, 'Thank you.'")
q("comm","Which communication practices are correct during a Code Blue? "+SATA,
 ["*Say your name and role when you arrive","*Read back medication orders","*The recorder reports key times to the leader","*Avoid vague replies like 'okay'"],
 "Example: 'I'm the primary nurse,' 'I'm recording.'")
q("comm","Which SBAR parts are matched correctly? "+SATA,
 ["*Situation: what's happening now","*Background: history and recent changes","*Assessment: findings and vital signs","*Recommendation: what you need done","Background: what you want done || Recommendation."],
 "A structured handoff.")
q("comm","A nurse calls the provider: 'I'm calling about Mr. Lee in room 214. He is suddenly short of breath.' Which part of SBAR is this?",
 ["*Situation","Background || History.","Assessment || Detailed findings.","Recommendation || What you need."],
 "Situation = what's happening right now.")
q("comm","Why does each Code Blue member need one clear role?",
 ["*To avoid confusion and overlap so care is fast and coordinated","So people can leave early || Not the reason.","To skip closed-loop communication || They work together.","So no leader is needed || A leader is needed."],
 "The right people in the right roles saves lives.")

# ---------- debrief ----------
q("debrief","What is the purpose of a debrief after a code?",
 ["*Find what went well and what to improve","Decide who's to blame || Not about blame.","Do billing || Not the purpose.","Call the family || Not the purpose."],
 "Discuss delays, miscommunication and equipment problems.")
q("debrief","Who should be part of a code debrief? "+SATA,
 ["*Nurses and physicians","*Respiratory therapists and pharmacists","*PCTs","*Anyone who played a big role or saw the event"],
 "Everyone involved.")
q("debrief","Which are goals of a debrief? "+SATA,
 ["*Recognize what worked","*Find delays or equipment problems","*Improve team learning and safety","*Acknowledge the emotional toll and offer support"],
 "Also suggest future improvements.")

# ---------- ERT ----------
q("ert","A visitor in the waiting room suddenly faints. Which team responds?",
 ["*The Emergency Response Team","The Rapid Response Team || Inpatients.","Code Blue || Unless in arrest.","No team || They need help."],
 "ERT = non-patient medical emergencies.")
q("ert","When can an ERT be called for a visitor or staff member? "+SATA,
 ["*They faint","*They have a seizure","*They fall or look ill","*They become short of breath"],
 "Call the emergency number and keep the area safe.")
q("ert","What happens after an ERT is called?",
 ["*The ER team comes, intervenes, and decides whether the person needs the ED","The person goes straight to the ICU || Not automatic.","The person is sent home || Not the process.","A Code Blue is always called || Only for arrest."],
 "Example: 'Medical emergency, adult visitor unresponsive, 3rd floor hallway.'")

# ---------- codes ----------
q("codes","What does a Code Red mean?",
 ["*Fire","Cardiac arrest || Code Blue.","Bomb threat || Code Black.","Missing child || Not on this chart."],
 "Codes vary by hospital.")
q("codes","What does a Code Black mean?",
 ["*Bomb threat","Fire || Code Red.","Cardiac arrest || Code Blue.","Chemical spill || Not Code Black."],
 "Both charts list Code Black as a bomb threat.")
q("codes","Why do hospitals use color codes? "+SATA,
 ["*To share urgent information quickly and clearly","*To avoid panicking patients and visitors","Because every hospital uses the same colors || They vary."],
 "Follow your facility's protocols.")
