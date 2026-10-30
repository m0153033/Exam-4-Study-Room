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
}
HI = ["three","rrttrig","cbwhen","comm","aha","cbsteps"]

SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

# ---------- RRT vs Code Blue vs ERT ----------
q("three","A patient suddenly collapses and is unresponsive with no pulse. What is the nurse's FIRST action?",
 ["Call a Rapid Response Team || The patient is in arrest; that's a Code Blue.","*Start CPR and call a Code Blue",
  "Move the patient to a stretcher || Delays CPR.","Give oxygen by nasal cannula || Not enough for arrest."],
 "From the professor's quiz: immediate CPR and activating Code Blue are critical for cardiac arrest.")
q("three","A nurse notices a patient becoming increasingly confused and disoriented over the past hour. What is the best action?",
 ["*Call the Rapid Response Team","Call a Code Blue || The patient isn't in arrest.","Give 2 L by nasal cannula only || Doesn't address the deterioration.","Document and continue routine monitoring || A change needs action."],
 "Acute mental status changes can be early signs of deterioration; immediate intervention matters.")
q("three","Which vital sign finding would MOST likely trigger a Code Blue?",
 ["BP 90/60 mmHg || May warrant assessment, not a code.","HR 120 bpm || Not an arrest.","RR 24 breaths/min || Not an arrest.","*The patient is apneic and pulseless"],
 "Absence of breathing and pulse indicates cardiac arrest.")
q("three","Match each team to its situation. Which pairs are correct? "+SATA,
 ["*Rapid Response Team: an inpatient showing early signs of deterioration","*Code Blue: cardiac or respiratory arrest","*Emergency Response Team: a visitor or staff member who needs medical help",
  "Emergency Response Team: an inpatient in cardiac arrest || That's a Code Blue.","Code Blue: a visitor who feels faint || That's an ERT call."],
 "RRT prevents the arrest; Code Blue treats it; ERT covers non-patient medical emergencies.")
q("three","A patient on the unit is breathing and has a pulse, but is suddenly hard to arouse. Which team?",
 ["*Rapid Response Team","Code Blue || There's still a pulse and breathing.","Emergency Response Team || That's for visitors and staff.","None; reassess in an hour || Sudden unresponsiveness is a trigger."],
 "Sudden unresponsiveness is an RRT trigger. If breathing or pulse stops, it becomes a Code Blue.")

# ---------- RRT purpose ----------
q("rrtwhy","What is the primary purpose of a Rapid Response Team?",
 ["*To assess and intervene early when a patient shows signs of deterioration, preventing cardiac or respiratory arrest",
  "To run a code when a patient has no pulse || That's Code Blue.","To help visitors who fall || That's ERT.","To replace the primary nurse || The primary nurse stays and continues care."],
 "It brings critical care expertise to the bedside without delay and supports concerned bedside nurses.")
q("rrtwhy","Who can call a Rapid Response Team?",
 ["Only the provider || Not per the lecture.","Only the charge nurse || Not per the lecture.","*Any staff member","Only the family || Not per the lecture."],
 "Many hospitals also allow families to call, but the professor's answer is 'any staff member.'")
q("rrtwhy","Can a Rapid Response Team be activated even if the vital signs are normal?",
 ["*Yes; staff concern is a valid reason to call","No; vital signs must be abnormal || Not per the lecture.","Only if the provider agrees first || Not required.","Only at night || Not a rule."],
 "Many hospitals list 'staff concern' as a trigger; you don't need to wait for abnormal vitals.")
q("rrtwhy","A patient has new-onset confusion. The blood glucose is 125 mg/dL. What should the nurse do?",
 ["Give orange juice || Glucose isn't low.","*Call the Rapid Response Team","Document and recheck in 4 hours || A sudden change needs action now.","Call a Code Blue || The patient isn't in arrest."],
 "The professor's example: new confusion with a normal glucose means something else is wrong. Call the RRT.")
q("rrtwhy","Which goals does the Rapid Response Team serve? "+SATA,
 ["*Prevent cardiac arrest","*Prevent ICU transfer or death","*Bring critical care expertise to the bedside without delay","*Support bedside nurses who are concerned about a patient"],
 "From the 'Purpose of the RRT' slide.")

# ---------- RRT triggers ----------
q("rrttrig","Which vital signs are Rapid Response triggers, per the lecture? "+SATA,
 ["*Heart rate under 40 or over 130 bpm","*Respiratory rate under 8 or over 28/min","*Systolic BP under 90 mmHg","*Oxygen saturation under 90% despite oxygen",
  "Heart rate of 98 bpm || Normal.","Respiratory rate of 18/min || Normal."],
 "Acute temperature changes, especially with sepsis, are also triggers.")
q("rrttrig","A nurse is assessing a post-op patient. Which findings warrant calling the Rapid Response Team? "+SATA,
 ["*Sudden onset of slurred speech","*Oxygen saturation of 86% on room air","*Heart rate of 44 bpm with dizziness","*New onset of confusion",
  "Blood pressure of 96/60 mmHg || Low-normal BP alone doesn't usually trigger RRT.","Temperature of 38.5°C (101.3°F) || Mild fever alone doesn't usually trigger RRT."],
 "Professor's answer: A, C, D, E. Slurred speech = possible stroke; O2 under 90%; bradycardia with symptoms; new confusion.")
q("rrttrig","Which neurological changes are Rapid Response triggers? "+SATA,
 ["*Sudden change in level of consciousness or confusion","*New seizure activity","*Sudden unresponsiveness",
  "Chronic dementia that's unchanged || Not a sudden change."],
 "The key word is sudden or new.")
q("rrttrig","Which breathing or airway findings are Rapid Response triggers? "+SATA,
 ["*Labored breathing or use of accessory muscles","*Increased work of breathing or cyanosis","*Unable to speak in full sentences","*New stridor or wheezing"],
 "From the 'Breathing or airway concerns' list.")
q("rrttrig","Which other findings on the slide trigger a Rapid Response? "+SATA,
 ["*Acute bleeding or signs of internal hemorrhage","*Chest pain unrelieved by interventions","*Acute temperature change, especially with sepsis","*A sudden change in urine output",
  "Pain relieved by the ordered medication || Not a trigger."],
 "Triggers include sudden changes in HR, BP, RR, oxygen saturation, level of consciousness and urine output.")

# ---------- RRT roles ----------
q("rrtroles","During a Rapid Response, what is the primary nurse's role?",
 ["Leave to care for other patients || Stays at the bedside.","*Give an SBAR report and continue care at the bedside",
  "Manage the airway and ventilation || The respiratory therapist does this.","Write new medical orders || The provider does this."],
 "The primary nurse knows the patient best.")
q("rrtroles","Match each RRT member to their responsibility. Which pairs are correct? "+SATA,
 ["*Critical care nurse (RRT RN): assesses the patient and starts interventions","*Respiratory therapist: manages the airway and gives oxygen or ventilation","*Provider (physician, NP or PA): gives medical orders and evaluates the condition","*Charge nurse: oversees and coordinates unit support or transfers",
  "Respiratory therapist: writes medication orders || The provider does this."],
 "From the RRT roles slide.")
q("rrtroles","What may happen after the Rapid Response Team assesses a patient? "+SATA,
 ["*The patient stabilizes on the floor","*The patient is transferred to a higher level of care (ICU)","*The condition worsens into a Code Blue",
  "The RRT must leave within 1 minute || Not part of how the RRT works."],
 "The team arrives within minutes, and assessment and interventions (labs, fluids, oxygen, medications) begin immediately.")
q("rrtroles","How is a Rapid Response Team activated?",
 ["*By calling a specific number or pressing a button","By sending an email to the unit || Too slow.","By waiting for the provider's rounds || Too slow.","Only by the family || Any staff member can call."],
 "Team members arrive within minutes.")

# ---------- Code Blue when ----------
q("cbwhen","When is a Code Blue called? "+SATA,
 ["*Unresponsive patient","*No pulse","*No breathing or abnormal breathing (agonal gasps)","*Sudden collapse",
  "Heart rate of 132 with a pulse and normal breathing || A Rapid Response trigger, not a code."],
 "In simple terms: Code Blue = a patient is not breathing and/or has no pulse.")
q("cbwhen","A patient is making occasional gasping breaths and has no pulse. What does the nurse do?",
 ["Wait; the patient is still breathing || Agonal gasps are not normal breathing.","*Call a Code Blue and start CPR",
  "Call the Rapid Response Team || The patient is in arrest.","Give oxygen and recheck in 5 minutes || Delays CPR."],
 "No pulse and no breathing = initiate Code Blue immediately.")

# ---------- steps ----------
q("cbsteps","What is the FIRST step when a nurse finds a patient who may be in arrest?",
 ["*Recognize the emergency: check responsiveness (tap and shout) and assess ABCs","Get the crash cart || Comes after recognizing and calling.","Assign team roles || Step 5.","Call time of death || Not a nursing step."],
 "Steps: 1 Recognize · 2 Call Code Blue · 3 Begin BLS · 4 Get equipment · 5 Assign roles · 6 ROSC or termination.")
q("cbsteps","How should a nurse announce a Code Blue?",
 ["*State the location clearly, such as \"Code Blue, Room 204, East Wing\"","Just say \"Help!\" || Doesn't give the location.","Text the provider || Too slow.","Wait for the charge nurse to call || Activate immediately."],
 "Press the Code Blue button or pull the emergency cord, or call the emergency number (e.g., 2222).")
q("cbsteps","A nurse is alone when a patient arrests. What should the nurse do?",
 ["Leave to find help, then start CPR || Delays compressions.","*Start compressions while calling for help, or delegate someone to call",
  "Wait for the code team before touching the patient || Delays CPR.","Get the crash cart first || Compressions come first."],
 "Start chest compressions immediately.")
q("cbsteps","Which equipment is brought for a Code Blue? "+SATA,
 ["*Crash cart","*Defibrillator or AED","*Suction","*Oxygen setup"],
 "If you're not doing CPR, help by retrieving or setting up this equipment.")
q("cbsteps","Return of spontaneous circulation (ROSC) is achieved. What happens next? "+SATA,
 ["*Support breathing and monitor vitals","*Transfer to the ICU","*Continue post-resuscitation care",
  "Stop monitoring because the code is over || Post-resuscitation care continues."],
 "If there's no ROSC after extended effort, the team may terminate the code; the MD calls time of death.")
q("cbsteps","Who calls the time of death when a code is terminated?",
 ["The primary nurse || Not per the lecture.","The recorder || Documents, doesn't call it.","*The MD","The family || Not per the lecture."],
 "The team may terminate based on clinical judgment and protocols.")

# ---------- CPR quality ----------
q("cpr","What compression rate does the lecture teach?",
 ["60–80 per minute || Too slow.","*100–120 per minute","130–150 per minute || Too fast.","30 per minute || Too slow."],
 "Depth 2 inches (5 cm), allowing full chest recoil.")
q("cpr","Which compression technique is correct for adult CPR? "+SATA,
 ["*Depth of 2 inches (5 cm)","*Allow full chest recoil","*Rate of 100–120 per minute",
  "Depth of 1 inch || Too shallow.","Lean on the chest between compressions || Prevents recoil."],
 "From Step 3: Begin Basic Life Support.")
q("cpr","About how often should the compressor switch to keep compressions high quality?",
 ["Every 30 seconds || Too often.","*Every 2 minutes (5 cycles)","Every 10 minutes || Too long; quality drops.","Only when the code ends || Fatigue lowers quality."],
 "The AHA chart: the compressor rotates with the AED/monitor person every 5 cycles.")

# ---------- Code Blue roles ----------
q("cbroles","Per the lecture's Code Blue team table, what does the primary RN do?",
 ["Directs the code || The provider does this.","*Performs chest compressions (CPR)","Administers ACLS medications || The ICU RN does this.","Performs intubation || The anesthesiologist does this."],
 "The primary RN also knows the patient's history and events leading up to the arrest.")
q("cbroles","Match each Code Blue team member to their role, per the lecture. Which pairs are correct? "+SATA,
 ["*Provider (MD/NP/PA): directs the code and makes medical decisions","*ICU RN: ACLS-certified, administers certain medications","*Respiratory therapist: maintains the airway and gives rescue breaths","*Anesthesiologist: possible intubation","*Security: crowd control"],
 "The charge RN aids in assisting.")
q("cbroles","What does the code recorder do?",
 ["Gives compressions || That's the compressor.","*Documents times of medications, compressions, shocks and rhythm changes",
  "Inserts the IV || That's the medication role.","Leads the code || That's the team leader."],
 "The recorder also communicates key information to the leader, such as \"Epinephrine given at 14:05.\"")
q("cbroles","Which role directs the code, assigns roles and interprets cardiac rhythms?",
 ["Recorder || Documents.","*Code (team) leader","Airway || Manages ventilation.","Compressor || Performs CPR."],
 "The leader decides when to shock or give medications.")
q("cbroles","Which medications does the medication role give during a code, per the lecture?",
 ["*ACLS medications such as epinephrine and amiodarone","Insulin and potassium || Not listed.","Antibiotics || Not listed.","Blood products || Not listed."],
 "The medication role also manages IV access.")

# ---------- AHA six-person ----------
q("aha","In the AHA six-person CPR team, which positions form the resuscitation triangle? "+SATA,
 ["*Position 1: compressor","*Position 2: AED/monitor/defibrillator","*Position 3: airway",
  "Position 4: team leader || A leadership role.","Position 5: recorder || A leadership role."],
 "Leadership roles: team leader (4), code recorder (5), IV/IO/medications (6).")
q("aha","Which statements about the AHA team leader are correct? "+SATA,
 ["*Every resuscitation team must have a defined leader","*Assigns roles to team members","*Makes treatment decisions","*Provides feedback to the team as needed",
  "Performs compressions the entire time || The leader directs."],
 "From the AHA Positions for Six-Person High-Quality CPR Teams chart.")
q("aha","Where should the monitor be placed, per the AHA chart?",
 ["*Where the entire team can see it","Behind the team leader || Should be visible to all.","Out of the room || Not per the chart.","Facing the family || Not per the chart."],
 "Position 2 brings and operates the AED/monitor/defibrillator.")
q("aha","What does position 5, the code recorder, track per the AHA chart? "+SATA,
 ["*Times of interventions and medications","*Frequency and duration of interruptions in compressions","*Communicates these to the team leader",
  "Opens the airway || Position 3."],
 "Recording keeps the team on time and avoids duplication.")
q("aha","Which statement reflects the AHA chart's rule about the resuscitation triangle?",
 ["*The team owns the code; no member leaves the triangle except to protect their safety",
  "Members leave whenever another nurse arrives || Not the rule.","The compressor never rotates || Rotates every 5 cycles.","Only the leader stays || The whole team stays."],
 "Position 6 (IV/IO/medications) is an ACLS provider role.")

# ---------- communication ----------
q("comm","Which communication tool should be used when giving a report to the Rapid Response Team?",
 ["*SBAR","Teach-back || For patient teaching.","Closed-loop only || Used during codes for orders.","CHOLY || A cholecystitis mnemonic."],
 "SBAR: Situation, Background, Assessment, Recommendation.")
q("comm","The team leader says, \"Give 1 mg epinephrine IV.\" What is the correct closed-loop response?",
 ["\"Okay.\" || Vague; avoid it.","*\"1 mg epinephrine IV, giving now,\" then confirm when it's given",
  "Give it without saying anything || No reply is unsafe.","\"Got it, I'll get to it.\" || Doesn't repeat the order."],
 "Closed-loop communication ensures messages are heard, understood and acted on. The leader then says \"Thank you.\"")
q("comm","Which statements about communication during a Code Blue are correct? "+SATA,
 ["*Each member identifies themselves and their role on arrival","*The medication nurse reads back orders to reduce errors","*The recorder communicates key information to the leader","*Avoid vague responses like \"okay\" or no reply"],
 "Examples: \"I'm the primary nurse,\" \"I'll take over compressions,\" \"I'm recording.\"")
q("comm","Match each SBAR part to its content. Which pairs are correct? "+SATA,
 ["*Situation: what's happening right now","*Background: relevant history and recent changes","*Assessment: current findings and vital signs","*Recommendation: what you need done next",
  "Background: what you want the provider to do || That's Recommendation."],
 "SBAR is a structured handoff.")
q("comm","Why does each Code Blue team member need a focused role?",
 ["*It avoids confusion and overlap, so care is coordinated and timely","It lets everyone leave early || Not the reason.","It replaces closed-loop communication || They work together.","It means no leader is needed || Every team needs a leader."],
 "Having the right people, trained, in the right roles saves lives.")

# ---------- debrief ----------
q("debrief","What is the purpose of debriefing after a Code Blue?",
 ["*To identify what went well and what could be improved","To decide who is to blame || Debriefing isn't about blame.","To complete billing || Not the purpose.","To notify the family || Not the purpose."],
 "Discuss effective actions, delays or miscommunication, equipment issues, and whether protocols were followed.")
q("debrief","Who should participate in a code debrief? "+SATA,
 ["*Nurses and physicians","*Respiratory therapists and pharmacists","*PCTs","*Anyone who played a significant role or witnessed the event"],
 "All team members involved in the response.")
q("debrief","Which are goals of a debrief? "+SATA,
 ["*Highlight successful interventions and coordination","*Identify delays, miscommunication or equipment problems","*Promote team learning and patient safety","*Acknowledge the emotional toll and offer support resources"],
 "Debriefing also includes suggestions for future improvement.")

# ---------- ERT ----------
q("ert","A visitor faints in the main lobby. Which team is called?",
 ["Rapid Response Team || For inpatients showing deterioration.","Code Blue || For patients in arrest.","*Emergency Response Team (ERT)","No team; call the visitor's family || The visitor needs help."],
 "An ERT is called for a visitor or staff member who needs medical help (a non-patient medical emergency).")
q("ert","When can an ERT be called for a staff member or visitor? "+SATA,
 ["*Faints","*Has a seizure","*Falls or appears ill","*Becomes short of breath"],
 "Call the designated emergency number and ensure safety while awaiting help.")
q("ert","What happens when an ERT is called, per the lecture?",
 ["*The ER team is notified, intervenes, and decides whether the person needs to go to the ED","The person is admitted to the ICU || Not automatically.",
  "The person is sent home || Not the process.","The Code Blue team always comes || Only if the person is in arrest."],
 "Example call: \"Medical emergency, adult visitor unresponsive on 3rd floor hallway.\"")

# ---------- codes ----------
q("codes","What does Code Red mean?",
 ["Cardiac arrest || That's Code Blue.","*Fire","Bomb threat || That's Code Black.","Evacuation || Varies by chart."],
 "Codes vary by hospital, so always follow your facility's protocols.")
q("codes","What does Code Black mean?",
 ["Fire || Code Red.","*Bomb threat","Cardiac arrest || Code Blue.","Hazardous spill || Not Code Black."],
 "Both charts on the slide list Code Black as a bomb threat.")
q("codes","Why do hospitals use emergency codes? "+SATA,
 ["*To communicate urgent situations clearly and quickly","*To prevent panic among patients and visitors",
  "Because every hospital uses identical colors || Codes vary by hospital or region."],
 "Always follow your facility's protocols.")
