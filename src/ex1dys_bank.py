# Week 2.1 Dysrhythmias Part 1 — lecture transcript, lesson plan, PowerPoint, notes.
EXAM = "e1"
T = "dys1"
CONCEPTS = {
 "grid":"ECG grid & 6-second rate",
 "waves":"P wave, PR & QRS",
 "blocks":"PR patterns: 1st degree vs Mobitz I vs Mobitz II",
 "wide":"Wide, fast QRS",
 "stt":"ST elevation & T-wave changes",
 "qt":"QT/QTc & torsades",
 "tele":"Five-lead telemetry placement",
 "teletech":"Electrode technique",
 "sinus":"Normal sinus & sinus tachycardia",
 "brady":"Sinus bradycardia: treat the patient",
 "afib":"Atrial fibrillation findings & risks",
 "afibdx":"AFib diagnostics & clot check",
 "laa":"Left atrial appendage & stroke",
 "valv":"Valvular vs nonvalvular AFib",
 "goals":"Three AFib goals",
 "proc":"Watchman & catheter ablation",
 "amio":"Amiodarone action & adverse effects",
 "amioteach":"Amiodarone monitoring & teaching",
 "heparin":"IV heparin",
 "oral":"Warfarin vs apixaban/rivaroxaban",
 "rate":"Metoprolol vs diltiazem",
 "flutter":"Atrial flutter",
 "team":"Interdisciplinary team",
}
HI = ["afib","laa","valv","amio","heparin","oral","rate","brady","qt","tele"]

SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

# ---------- grid ----------
q("grid","On ECG paper, how long is one small square and one large box?",
 ["*Small square 0.04 second; large box 0.20 second","Small 0.20; large 0.04 || Reversed.","Small 0.10; large 1 second || Not the lecture values.","Both 0.04 second || A large box is five small squares."],
 "1 small square = 0.04 sec; 1 large box = 0.20 sec; 6 seconds = 30 large boxes.")
q("grid","A 6-second strip shows 8 QRS complexes. What is the heart rate using the 6-second method?",
 ["*80 bpm","48 bpm || That multiplies by 6.","8 bpm || The count must be multiplied by 10.","60 bpm || Not the 6-second calculation."],
 "6-second method: count QRS complexes × 10.")
q("grid","How many large boxes make up a 6-second strip?",
 ["*30","6 || That's seconds.","60 || Too many.","150 || Not the lecture value."],
 "30 large boxes × 0.20 sec = 6 seconds.")

# ---------- waves ----------
q("waves","What does the P wave represent?",
 ["*The SA node firing and atrial depolarization","Ventricular depolarization || That's the QRS.","Ventricular repolarization || That's the T wave.","The AV delay || That's the PR interval."],
 "P wave: small, rounded, upright in lead II, <0.12 sec, one before each QRS.")
q("waves","What is the normal PR interval?",
 ["*0.12–0.20 second and constant","0.06–0.10 second || That's the QRS.","Over 0.20 second || That's a 1st-degree block.","Under 0.04 second || Too short."],
 "PR = start of P to start of QRS; the AV delay lets the ventricles fill.")
q("waves","What is the normal QRS duration?",
 ["*0.06–0.10 second (narrow)","0.12–0.20 second || That's PR.","Over 0.12 second || That's wide.","0.20–0.40 second || Too wide."],
 "QRS = ventricular depolarization; >0.12 sec = wide.")
q("waves","Which statement about electrical and mechanical activity is correct?",
 ["*Electrical activity comes before the mechanical squeeze","The ECG directly shows the heart squeezing || It shows electrical activity.","Mechanical contraction always comes first || Electrical first.","They're the same thing || They're different."],
 "Always pair the strip with perfusion: treat the patient, not only the number.")

# ---------- blocks ----------
q("blocks","The PR interval is 0.26 second on every beat and no beats are dropped. This is:",
 ["*1st-degree AV block","Mobitz I (Wenckebach) || PR lengthens until a beat drops.","Mobitz II || Fixed PR with sudden dropped beats.","Normal sinus rhythm || PR >0.20 isn't normal."],
 "1st degree = PR >0.20 but steady.")
q("blocks","The PR gets longer with each beat until a QRS is dropped. This is:",
 ["*Mobitz I (Wenckebach)","Mobitz II || PR stays fixed.","1st-degree block || No dropped beats.","Atrial flutter || Sawtooth waves."],
 "Mobitz I = progressive PR lengthening → dropped beat.")
q("blocks","Which PR pattern is MORE serious?",
 ["*Mobitz II: fixed PR with a sudden dropped beat","Mobitz I: progressive PR lengthening || Less serious than Mobitz II.","1st-degree block || Steady, no drops.","Normal PR 0.16 || Normal."],
 "Mobitz II is the more serious pattern.")

# ---------- wide QRS ----------
q("wide","A client's monitor shows a very fast rhythm with wide QRS complexes. How should the nurse treat it?",
 ["*As ventricular tachycardia until clarified: assess perfusion and escalate","As sinus tachycardia; give fluids || Wide QRS isn't sinus tach.","As artifact; reattach leads first and wait || Assess the patient first.","As normal for this client || Not normal."],
 "Assess perfusion, call rapid response/ACLS, get a 12-lead ECG, check electrolytes.")
q("wide","A wide QRS (>0.12 sec) can mean which of the following? "+SATA,
 ["*Bundle branch block","*A ventricular rhythm such as V-tach","*Slow or detoured ventricular conduction","Normal atrial depolarization || That's the P wave."],
 "Wide QRS = slow or detoured ventricular conduction.")

# ---------- ST/T ----------
q("stt","A client with chest discomfort has new ST elevation. What should the nurse do? "+SATA,
 ["*Assess immediately and alert the provider","*Get a STAT 12-lead ECG and troponins","*Likely call a rapid response","*Treat as MI until ruled out","Recheck the strip tomorrow || This is urgent."],
 "New ST elevation + symptoms = MI until ruled out.")
q("stt","Besides MI, which condition can cause ST elevation?",
 ["*Pericarditis","Hypokalemia || Causes flat T waves.","Sinus bradycardia || Not an ST cause.","Conjunctivitis || Unrelated."],
 "ST elevation isn't always MI; pericarditis can alter the ST too.")
q("stt","Tall, peaked T waves suggest:",
 ["*Hyperkalemia","Hypokalemia || Causes flat or inverted T waves.","Hypercalcemia only || Not the lecture link.","Normal repolarization || Peaked isn't normal."],
 "Tall/peaked T → hyperkalemia. Flat/inverted → ischemia or hypokalemia. Check electrolytes and use telemetry.")
q("stt","Which T-wave change can point to ischemia or low potassium?",
 ["*Flat or inverted T waves","Tall, peaked T waves || Hyperkalemia.","A narrow QRS || Normal conduction.","A PR of 0.16 || Normal."],
 "Correlate T-wave changes with ST changes and symptoms.")

# ---------- QT ----------
q("qt","A prolonged QT puts the client at risk for which rhythm?",
 ["*Torsades de pointes / ventricular tachycardia","Sinus bradycardia || Not the main risk.","1st-degree block || Not the risk.","Atrial flutter || Not the risk."],
 "QTc >500 ms = prolonged/high risk. First-line drug for torsades is magnesium.")
q("qt","Which medications can prolong the QT? "+SATA,
 ["*Azithromycin","*Levofloxacin or ciprofloxacin","*Ondansetron","*Antiarrhythmics such as amiodarone","Acetaminophen || Not listed."],
 "Assess the ECG/QTc before starting a QT-prolonging medication.")
q("qt","Which electrolyte problems can prolong the QT? "+SATA,
 ["*Low potassium","*Low magnesium","*Low calcium","High sodium || Not listed."],
 "Other causes: congenital factors, bradycardia, medications.")
q("qt","A client's QTc is 520 ms. What should the nurse anticipate? "+SATA,
 ["*Avoid QT-prolonging drugs","*Replace low potassium and magnesium","*Continuous telemetry","Give ondansetron for nausea || It prolongs QT."],
 "Practical target <450 ms (men) and <470 ms (women).")
q("qt","What is the first-line medication for torsades de pointes?",
 ["*Magnesium","Atropine || For symptomatic bradycardia.","Heparin || An anticoagulant.","Diltiazem || A rate-control drug."],
 "Magnesium is first-line for torsades.")

# ---------- telemetry ----------
q("tele","Where does the WHITE (RA) electrode go on 5-lead telemetry?",
 ["*Below the right clavicle","Below the left clavicle || That's black (LA).","Lower left torso || That's red (LL).","4th intercostal space, right sternal border || That's brown (V1)."],
 "White on right; smoke (black) over fire (red); snow (white) over grass (green).")
q("tele","Which placement is correct? "+SATA,
 ["*Black (LA): below the left clavicle","*Red (LL): lower left torso below the ribs","*Green (RL): lower right torso below the ribs","*Brown (V1): 4th intercostal space, right sternal border","White (RA): lower left abdomen || White goes below the right clavicle."],
 "The four limb leads go on the torso, not the limbs.")
q("tele","Why is the V1 (brown) lead useful?",
 ["*It shows atrial activity and helps with AFib/flutter and wide-complex/BBB distinction","It measures blood pressure || It doesn't.","It replaces the 12-lead ECG || It doesn't.","It grounds the system only || That's the RL lead's role in mnemonics, not V1."],
 "V1 sits near the heart at the 4th ICS, right sternal border.")
q("tele","What is the purpose of 5-lead telemetry?",
 ["*Continuous monitoring for dysrhythmias, ischemia and rate/rhythm changes without repeated 12-leads","To diagnose MI alone || A 12-lead and troponins are needed.","To pace the heart || Not a pacemaker.","To measure oxygen saturation || That's a pulse oximeter."],
 "Telemetry detects problems early.")

# ---------- electrode technique ----------
q("teletech","Which electrode technique is correct? "+SATA,
 ["*Clip hair rather than shave","*Clean and dry the skin","*Place electrodes below or lateral to breast tissue","*Change electrodes daily or when loose or sweaty","Place electrodes over bony areas for stability || Avoid bones, joints and skin folds."],
 "Lotion, sweat and oil reduce adhesion.")
q("teletech","The monitor shows artifact and false alarms. What is a likely cause?",
 ["*Poor electrode placement or contact","A true lethal rhythm in every case || Check the patient, but artifact is common with poor contact.","Too many electrodes || Not the cause.","Clipped hair || Clipping helps adhesion."],
 "Poor contact → artifact, false alarms, unreliable tracings. Always check the patient first.")

# ---------- sinus ----------
q("sinus","Which strip findings describe normal sinus rhythm? "+SATA,
 ["*Rate 60–100 and regular","*An upright P before every QRS","*PR 0.12–0.20 and constant","*QRS 0.06–0.10","Sawtooth waves || That's atrial flutter."],
 "NSR = normal SA-node rhythm.")
q("sinus","A febrile, dehydrated client has a regular rhythm at 124 with a P before every QRS. What is the priority?",
 ["*Treat the cause, such as fever and dehydration, and assess perfusion","Give atropine || For symptomatic bradycardia.","Prepare for ablation || Not for sinus tach.","Ignore it; it's normal || Persistent tachycardia lowers cardiac output."],
 "Sinus tach causes: fever, hypovolemia, hyperthyroidism, pain, anxiety, exertion, caffeine.")
q("sinus","Why does persistent tachycardia lower cardiac output?",
 ["*Less diastolic filling time","More filling time || Opposite.","It raises stroke volume || Less filling lowers stroke volume.","It doesn't affect output || It does."],
 "Faster rate → shorter diastole → less filling → lower output/perfusion.")

# ---------- brady ----------
q("brady","A marathon runner has a HR of 50, is alert and has no symptoms. What should the nurse do?",
 ["*Continue to monitor; asymptomatic bradycardia may need nothing","Give atropine now || Only for symptomatic brady.","Call a Code Blue || Not in arrest.","Start a pacemaker || Not indicated."],
 "Treat the patient, not the number. Bradycardia can be normal in endurance athletes.")
q("brady","Which findings make sinus bradycardia SYMPTOMATIC? "+SATA,
 ["*Dizziness or syncope","*Confusion","*Chest pain","*Sweating","Warm, pink skin and alert mentation || Signs of good perfusion."],
 "Symptomatic bradycardia → atropine.")
q("brady","A client with HR 44 and dizziness is due for metoprolol. What should the nurse do?",
 ["*Hold the dose and notify the ordering provider","Give it and recheck in an hour || It could slow the HR further.","Cut the dose in half on their own || Nurses don't change prescriptions.","Give it with atropine || Not appropriate."],
 "Rate-slowing drugs: beta blockers, calcium channel blockers, digoxin, amiodarone. Also start fall precautions.")
q("brady","Which drug treats symptomatic bradycardia?",
 ["*Atropine","Magnesium || Torsades.","Amiodarone || Slows the rate further.","Diltiazem || Slows the rate further."],
 "Atropine is the lecture's drug for symptomatic brady.")
q("brady","Which can cause sinus bradycardia? "+SATA,
 ["*Prior MI","*Sleep apnea","*Hypothyroidism","*Vagal stimulation or Valsalva","Fever || Causes tachycardia."],
 "Also medications and being an endurance athlete.")

# ---------- AFib ----------
q("afib","Which ECG findings fit atrial fibrillation?",
 ["*Irregularly irregular rhythm with no distinct P waves","Regular sawtooth waves || That's flutter.","Regular rhythm, P before every QRS || That's sinus.","PR that lengthens until a beat drops || Mobitz I."],
 "Hundreds of disorganized atrial impulses make the atria quiver.")
q("afib","Which are risk factors for AFib? "+SATA,
 ["*Recovery from cardiac surgery","*Sleep apnea","*Hyperthyroidism","*Excessive alcohol","*Hypertension","Regular exercise || Not a listed risk."],
 "Also diabetes, heart failure, smoking.")
q("afib","Why does sleep apnea increase AFib risk?",
 ["*Repeated oxygen drops strain the atrial walls and make tissue irritable","It slows the heart permanently || Not the mechanism.","It causes bleeding || Not the mechanism.","It has no link || It's a listed risk."],
 "Cardiac surgery also irritates atrial pathways through manipulation and inflammation.")
q("afib","Which statement about AFib is correct?",
 ["*It's the most common treated arrhythmia and can be asymptomatic","It always causes chest pain || Can be asymptomatic.","A controlled rate means no stroke risk || Anticoagulation is still central.","It's a ventricular rhythm || It's atrial."],
 "AFib may be controlled (<100) or rapid (>100); rapid rate lowers output further.")

# ---------- AFib dx ----------
q("afibdx","Before cardioversion for AFib, why is a TEE done?",
 ["*To check for an atrial thrombus that could dislodge and cause a stroke","To measure QTc || That's the ECG.","To place the Watchman || A separate procedure.","To give amiodarone || Not a drug route."],
 "Restoring contraction could dislodge a clot → embolic stroke.")
q("afibdx","A client has palpitations that come and go. Which test records the rhythm at home for 24–72 hours?",
 ["*Holter monitor","Telemetry || Inpatient continuous monitoring.","Echocardiogram || Atrial size and function.","Troponin || A lab, not a rhythm recording."],
 "Holter = outpatient; telemetry = inpatient real time.")
q("afibdx","Which tests help evaluate AFib? "+SATA,
 ["*12-lead ECG","*Echocardiogram","*Holter monitor","Amsler grid || An eye test."],
 "12-lead confirms rhythm; echo shows atrial size/function; TEE looks closer for thrombus.")

# ---------- LAA ----------
q("laa","Where do 90–95% of AFib-related strokes originate?",
 ["*Clots in the left atrial appendage","The right ventricle || Not the source.","The carotid artery || Not the AFib source.","The aorta || Not the AFib source."],
 "Atrial quiver → blood pools in the LAA → clot → brain → ischemic stroke.")
q("laa","Why is anticoagulation central in AFib even without symptoms?",
 ["*Blood stagnates in the LAA and can clot regardless of symptoms","It lowers heart rate || Anticoagulants don't control rate.","It converts the rhythm || It doesn't.","It's only for symptomatic clients || Asymptomatic clients still clot."],
 "Prescribers use the CHA₂DS₂-VASc score to guide anticoagulation.")
q("laa","What tool do prescribers use to quantify stroke risk in AFib?",
 ["*CHA₂DS₂-VASc score","Glasgow Coma Scale || Consciousness.","Amsler grid || Eyes.","Snellen chart || Eyes."],
 "CHA₂DS₂-VASc guides anticoagulation decisions.")

# ---------- valvular ----------
q("valv","A client with AFib has a mechanical heart valve. Which oral anticoagulant is indicated?",
 ["*Warfarin","Apixaban || DOACs are for nonvalvular AFib.","Rivaroxaban || DOACs are for nonvalvular AFib.","Aspirin alone || Not the lecture choice."],
 "Valvular AFib (moderate-to-severe mitral stenosis or a mechanical valve) → warfarin only.")
q("valv","Which client has NONvalvular AFib, so a DOAC is preferred?",
 ["*A client with a bioprosthetic valve","A client with a mechanical valve || Valvular.","A client with severe mitral stenosis || Valvular.","None; all AFib is valvular || Most is nonvalvular."],
 "Nonvalvular includes bioprosthetic valves and mild/moderate regurgitation.")
q("valv","What is the role of IV heparin in AFib?",
 ["*Acute, rapid, reversible control or a bridge; not long-term at home","Long-term home therapy || Not a home choice.","Rate control || It doesn't slow HR.","Rhythm conversion || It doesn't convert."],
 "Heparin is acute/bridge therapy.")

# ---------- goals ----------
q("goals","What are the three goals of AFib management? "+SATA,
 ["*Prevent clots and stroke","*Control the ventricular rate","*Control or restore the rhythm","Raise the heart rate above 100 || Not a goal."],
 "Clots: heparin, warfarin, DOACs, Watchman. Rate: metoprolol, diltiazem. Rhythm: amiodarone, ablation.")
q("goals","Which drug controls the RHYTHM (not just the rate) in AFib?",
 ["*Amiodarone","Metoprolol || Rate control.","Diltiazem || Rate control.","Apixaban || Clot prevention."],
 "Rate control doesn't convert AFib.")

# ---------- procedures ----------
q("proc","Which client is a candidate for the Watchman device?",
 ["*A client with AFib who can't take anticoagulants","A client with sinus bradycardia || Not indicated.","A client with a prolonged QT || Not indicated.","A client who needs a pacemaker || Different device."],
 "The Watchman closes off the LAA clot source; clients may stop anticoagulants about 30–60 days after.")
q("proc","What does catheter ablation do?",
 ["*Destroys small areas of heart tissue that cause abnormal signals using radiofrequency or cryoenergy","Closes the left atrial appendage || That's the Watchman.","Dissolves a clot || Not ablation.","Paces the heart || That's a pacemaker."],
 "An electrophysiologist does it in the cath lab; it isolates fibrillating impulses.")
q("proc","After a femoral-access ablation or Watchman, which nursing care applies? "+SATA,
 ["*Monitor the groin for bleeding or hematoma","*Check distal neurovascular status","*Keep prescribed bedrest","*Monitor telemetry for dysrhythmias","Ambulate right away to prevent clots || Prescribed bedrest is needed."],
 "Also assess for chest pain.")

# ---------- amiodarone ----------
q("amio","How does amiodarone work?",
 ["*Blocks potassium channels, prolonging repolarization and the QT","Blocks calcium channels only || That's diltiazem.","Blocks beta-1 receptors only || That's metoprolol.","Inhibits factor Xa || That's apixaban."],
 "It also slows sinus rate and AV conduction (prolongs PR). IV for acute, PO for long-term.")
q("amio","A client on amiodarone has a new dry cough and shortness of breath. What should the nurse suspect?",
 ["*Pulmonary toxicity (pneumonitis or fibrosis)","An expected harmless effect || Lung toxicity can be fatal.","Hypoglycemia || Not linked.","Hyperkalemia || Not linked."],
 "Report SOB, cough or fever immediately.")
q("amio","Which adverse effects are linked to amiodarone? "+SATA,
 ["*Hypo- or hyperthyroidism","*Elevated liver enzymes","*Corneal deposits and halos","*Photosensitivity and blue-gray skin","*Bradycardia and QT prolongation","Weight gain from fluid only || Not listed."],
 "Amiodarone contains iodine, which explains thyroid effects.")
q("amio","A client on warfarin starts amiodarone. What should the nurse anticipate?",
 ["*Higher INR and bleeding risk","Lower INR || Amiodarone increases warfarin's effect.","No interaction || There is one.","Lower digoxin levels || It raises digoxin too."],
 "Amiodarone increases warfarin and digoxin effects; with AV-node drugs it worsens bradycardia/block.")
q("amio","Combining amiodarone with metoprolol, diltiazem or digoxin raises the risk of:",
 ["*Worse bradycardia and heart block","Tachycardia || Opposite.","Hyperglycemia || Not listed.","Bleeding only || That's warfarin."],
 "All slow AV conduction.")

# ---------- amio teaching ----------
q("amioteach","Which baseline and periodic tests are needed for amiodarone? "+SATA,
 ["*ECG for QT and heart block","*Liver and thyroid function tests","*Pulmonary function tests and chest x-ray","*Eye exams","Amsler grid daily || Not listed for amiodarone."],
 "Continuous rhythm monitoring during IV infusion.")
q("amioteach","Which teaching is correct for amiodarone? "+SATA,
 ["*Take it at the same time daily","*Avoid excess sun and wear sunscreen","*Report vision changes, jaundice or extreme fatigue","*Don't stop it abruptly","Skip doses when the pulse feels normal || Don't stop or skip."],
 "Keep regular bloodwork and ECG follow-up.")

# ---------- heparin ----------
q("heparin","Which statement about IV heparin is correct?",
 ["*It prevents new clots and clot extension but doesn't dissolve existing clots","It dissolves the clot in the LAA || It doesn't dissolve clots.","It slows the heart rate || Not its action.","It's safe without monitoring || aPTT is monitored."],
 "Heparin boosts antithrombin → inactivates thrombin (IIa) and factor Xa.")
q("heparin","Which safety steps apply to a heparin infusion? "+SATA,
 ["*Use an infusion pump","*Independent double-check by another RN","*Baseline aPTT, PT/INR and CBC","*Repeat aPTT 6 hours after starting or any rate change","Check it only weekly || Too infrequent."],
 "Heparin is high-alert; target is usually 1.5–2 times control.")
q("heparin","On day 7 of heparin, the client's platelets drop sharply. What should the nurse do?",
 ["*Stop heparin, notify the provider and expect a non-heparin anticoagulant","Continue and recheck next week || HIT is dangerous.","Give protamine and continue heparin || Stop the heparin.","Double the heparin || Wrong direction."],
 "HIT (heparin-induced thrombocytopenia) usually appears days 5–10.")
q("heparin","What is the antidote for heparin?",
 ["*Protamine sulfate","Vitamin K || Warfarin.","Andexanet alfa || Apixaban/rivaroxaban.","Magnesium || Torsades."],
 "Protamine reverses heparin.")
q("heparin","Which teaching applies to a client on heparin? "+SATA,
 ["*Use a soft toothbrush and electric razor","*Report dark or bloody urine or stool","*Report a new headache","*Use caution with NSAIDs","Expect no blood draws || Frequent draws are expected."],
 "Also check gums, IV sites and neuro status; bleeding and fall precautions.")

# ---------- oral anticoagulants ----------
q("oral","Which lab is monitored routinely for warfarin?",
 ["*PT/INR, usually target 2–3","aPTT || Heparin.","No labs || That's the DOAC pattern.","Platelets only || HIT is a heparin concern."],
 "Warfarin has a narrow index; the target is higher for a mechanical valve.")
q("oral","What is the reversal agent for warfarin?",
 ["*Vitamin K (PCC or FFP for serious bleeding)","Protamine sulfate || Heparin.","Andexanet alfa || DOACs.","Atropine || Bradycardia."],
 "Vitamin K reverses warfarin.")
q("oral","A client on apixaban is having life-threatening bleeding. Which reversal agent is used?",
 ["*Andexanet alfa (Andexxa)","Vitamin K || Warfarin.","Protamine || Heparin.","Magnesium || Torsades."],
 "Andexanet alfa reverses factor Xa inhibitors.")
q("oral","Which teaching is specific to warfarin? "+SATA,
 ["*Keep vitamin K intake (leafy greens) consistent","*Get routine PT/INR checks","*Expect onset to take 3–5 days, possibly with heparin bridging","No lab monitoring is needed || That's DOACs."],
 "Interactions include NSAIDs, antibiotics and amiodarone.")
q("oral","What is the boxed warning for apixaban and rivaroxaban?",
 ["*Spinal or epidural hematoma with neuraxial anesthesia or spinal puncture","Liver failure in all clients || Not the boxed warning.","Blue-gray skin || Amiodarone.","Hearing loss || Not listed."],
 "The hematoma can cause long-term or permanent paralysis.")
q("oral","A client on rivaroxaban says, 'Since I don't need blood tests, there's no risk.' Best response?",
 ["*'No routine lab doesn't mean no risk; watch for bleeding and kidney function is checked.'","'Correct, it's risk-free.' || Bleeding risk remains.","'You need INR checks weekly.' || That's warfarin.","'Stop it before any dental work on your own.' || Tell providers; don't stop without guidance."],
 "DOACs aren't recommended for end-stage renal disease on dialysis.")
q("oral","Which teaching applies to warfarin, apixaban AND rivaroxaban? "+SATA,
 ["*Report unusual bleeding, bruising or dark stools","*Tell every provider and dentist about all meds and supplements","*Don't stop abruptly without guidance because of rebound clot risk","Eat no green vegetables ever || Warfarin needs consistent, not zero, vitamin K."],
 "Shared anticoagulant teaching.")

# ---------- rate control ----------
q("rate","Which statement about metoprolol and diltiazem in AFib is correct?",
 ["*Both control the ventricular rate but don't convert the rhythm","Both convert AFib to sinus || They don't.","Both are anticoagulants || They aren't.","Only metoprolol slows the heart || Both do."],
 "Metoprolol = beta-1 selective blocker; diltiazem = non-dihydropyridine calcium-channel blocker.")
q("rate","A client with diabetes takes metoprolol. Which teaching is important?",
 ["*It can mask signs of hypoglycemia; monitor glucose closely","It raises blood glucose dangerously || Not the lecture point.","It cures diabetes || No.","Skip doses when glucose is low || Don't skip without guidance."],
 "Metoprolol masks hypoglycemia signs; caution with asthma/COPD (bronchospasm).")
q("rate","Which adverse effects are specific to diltiazem? "+SATA,
 ["*Peripheral edema","*Constipation","*Headache and flushing","Masking of hypoglycemia || That's metoprolol.","Bronchospasm || That's metoprolol caution."],
 "Diltiazem also causes hypotension, bradycardia, AV block; caution in HFrEF.")
q("rate","Which teaching applies to diltiazem? "+SATA,
 ["*Avoid grapefruit juice","*Report leg or foot swelling","*Take consistently with regard to food, especially ER forms","*Don't stop abruptly","Take double if HR is high || Never self-adjust."],
 "Check HR and BP; hold and notify if below parameters; rise slowly.")
q("rate","Before giving metoprolol, the client's HR is below the ordered parameter. What should the nurse do?",
 ["*Hold it and notify the provider","Give it anyway || Could worsen bradycardia.","Give half || Not the nurse's decision.","Give it with caffeine || Not appropriate."],
 "Both drugs: abrupt stop → rebound tachycardia/HTN.")
q("rate","Which rate-control drug calls for caution in clients with asthma or COPD?",
 ["*Metoprolol","Diltiazem || Its caution is HFrEF.","Apixaban || Not a rate drug.","Heparin || Not a rate drug."],
 "Beta-1 selectivity is dose-dependent, so bronchospasm can occur.")

# ---------- flutter ----------
q("flutter","Which ECG finding is classic for atrial flutter?",
 ["*Sawtooth flutter waves with no distinct P waves","Irregularly irregular with no P waves || That's AFib.","Normal P before each QRS || Sinus.","Wide, very fast QRS || V-tach until clarified."],
 "Flutter is more organized: a reentry circuit at about 250–350/min.")
q("flutter","A client in atrial flutter has a 2:1 conduction ratio. What ventricular rate is likely?",
 ["*About 150","About 70 || That's around a 5:1 ratio.","About 300 || That's the atrial rate.","About 40 || Too slow."],
 "The AV node can't conduct every impulse; the ratio sets the ventricular rate.")
q("flutter","Why does a client with organized atrial flutter still need anticoagulation?",
 ["*The atria still don't contract effectively, so clots can form","Flutter never causes clots || It can.","It's only for rate control || Anticoagulants don't slow HR.","Because it's a ventricular rhythm || It's atrial."],
 "Prevent clots in flutter as in AFib.")
q("flutter","Which treatment is often definitive for recurrent atrial flutter?",
 ["*Catheter ablation","Watchman || Addresses LAA clots when anticoagulants can't be used.","Atropine || For bradycardia.","Magnesium || For torsades."],
 "Ablation has high success because the reentry focus is usually localized.")

# ---------- team ----------
q("team","Which team member is described as the heart's 'electrician'?",
 ["*Electrophysiologist","Interventional cardiologist || The 'plumber' for blockages and stents.","Cardiologist || The 'general contractor'.","Respiratory therapist || Oxygenation support."],
 "The electrophysiologist does ablation, cardioversion, pacemakers and ICDs.")
q("team","Which team member helps with medication access, INR lab logistics and cardiac rehab transportation?",
 ["*Case manager or social worker","Pharmacist || Doses and interactions.","Electrophysiologist || Electrical procedures.","Interventional cardiologist || Stents."],
 "The pharmacist focuses on doses, interactions and adverse-effect teaching for anticoagulants/antiarrhythmics.")
