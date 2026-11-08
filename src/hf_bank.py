# Week 9.3 Cardiomyopathy / Heart Failure — built only from the professor's transcript + slides.
# VERSION 2 (Nov 8): every question re-worded with new scenarios/distractors.
# Option syntax: "*text" = correct; "text || why it's wrong" = distractor with its note.
T = "hf"
CONCEPTS = {
 "co":"Cardiac output, preload, afterload & EF",
 "targets":"What each drug class targets",
 "causes":"Causes, risk factors & triggers",
 "comp":"Compensation & remodeling",
 "sysdia":"Systolic (HFrEF) vs diastolic (HFpEF)",
 "lr":"Left- vs right-sided signs (FOCUS)",
 "nyha":"NYHA classes",
 "bnp":"BNP (FOCUS)",
 "imaging":"Echo, TEE, chest x-ray & ECG",
 "labs":"Labs: K, Na, Mg, BUN/Cr, LFTs, TSH, ABG",
 "hemo":"MAP & CVP",
 "assess":"Priority assessment & lung sounds (FOCUS)",
 "weight":"Daily weights & early decompensation",
 "edjvd":"Edema & JVD assessment",
 "pillars":"The four pillars",
 "loop":"Loop diuretics (furosemide) (FOCUS)",
 "spiro":"Spironolactone",
 "ace":"ACE inhibitors",
 "arb":"ARBs",
 "arni":"ARNI: sacubitril/valsartan (FOCUS)",
 "bb":"Beta blockers",
 "sglt2":"SGLT2 inhibitors",
 "dig":"Digoxin",
 "vasoino":"Vasodilators & IV inotropes",
 "check":"Check, hold & call",
 "ape":"Acute pulmonary edema",
 "dc":"Nursing management & discharge teaching",
 "adv":"ICD, LVAD, pacing, transplant, end of life",
 "life":"Across the lifespan",
 "cm":"Cardiomyopathy types",
 "hcm":"Hypertrophic cardiomyopathy safety",
}
# Nursing Priorities Review slide = professor emphasis -> two questions per full game
# Student review #2 (Nov 4): left vs right, BNP, priority assessment, Entresto switch, furosemide.
HI = ["lr","weight","ape","check","dig","arni","hcm","loop","bnp","assess"]

SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r):
    Q.append((c, stem, opts, r))

# ---------------- cardiac output ----------------
q("co","A client with severe aortic stenosis has a heart that must push against a narrow valve. Which part of stroke volume is raised?",
 ["*Afterload","Preload || Filling volume.","Contractility || Squeeze strength.","Heart rate || Not part of stroke volume."],
 "Afterload = resistance to ejection. High BP and aortic stenosis raise it.")
q("co","Which term describes how full the ventricle is at the end of diastole?",
 ["*Preload","Afterload || Resistance to ejection.","Contractility || Squeeze strength.","Ejection fraction || Percent ejected."],
 "Diuretics and nitrates lower preload.")
q("co","An echo shows an EF of 62%. How does the nurse interpret this?",
 ["*Normal (55–70%)","Reduced; systolic heart failure || 40% or less is reduced.","Too high; hyperdynamic || Within normal.","Mildly reduced || Within normal."],
 "EF = the percent of left ventricle blood pushed out with each beat.")
q("co","Why is a fast heart rate often an early sign of heart failure?",
 ["*Less blood goes out per beat, so the heart beats faster to keep cardiac output up","The heart is getting stronger || It's weaker.",
  "Preload drops to zero || Preload rises.","The EF rises || EF falls or stays the same."],
 "Cardiac output = heart rate × stroke volume.")
q("co","Uncontrolled high blood pressure raises afterload. What happens to the blood ejected with each beat?",
 ["*It drops, because the ventricle pushes against more resistance","It rises, because the ventricle fills more || Afterload isn't filling.",
  "It doesn't change || Afterload affects stroke volume.","It doubles || Not true."],
 "More resistance = less blood gets out.")

# ---------------- drug targets ----------------
q("targets","A drug is given to remove extra fluid and lower PRELOAD. Which class is it?",
 ["*A loop diuretic such as furosemide","An ACE inhibitor || Mainly lowers afterload.","Digoxin || Increases contractility.","A beta blocker || Slows heart rate."],
 "Preload: diuretics, nitrates, SGLT2s. Afterload: ACE/ARB/ARNI, hydralazine. Contractility: digoxin, dobutamine, milrinone.")
q("targets","Which drugs make the heart squeeze HARDER? "+SATA,
 ["*Digoxin","*Dobutamine","*Milrinone","Hydralazine || Lowers afterload.","Carvedilol || Slows the heart."],
 "Positive inotropes strengthen contraction.")
q("targets","A client starts a drug that opens up the arteries to lower afterload. Which side effect should the nurse expect?",
 ["*Dizziness from low blood pressure","Weight gain || Not expected.","High blood sugar || Not expected.","Slow heart rate from stronger contraction || Reflex fast heart rate is more likely."],
 "Know what a drug does, and you can predict its side effects.")

# ---------------- causes ----------------
q("causes","Which is the MOST common cause of heart failure?",
 ["*Coronary artery disease and heart attack","Thyroid disease || Less common.","Sepsis || A trigger, not the most common cause.","Valve disease || Less common."],
 "Hypertension is the main 'worked too hard for too long' cause.")
q("causes","A client with stable heart failure is admitted with fluid overload. Which history clues explain it? "+SATA,
 ["*Stopped furosemide because of frequent bathroom trips","*Takes naproxen for knee pain","*Ate fast food most days this week","*New atrial fibrillation",
  "Walks 20 minutes a day || Recommended activity."],
 "Triggers: missed meds, salt or fluid excess, NSAIDs, infection, uncontrolled BP, new A-fib.")
q("causes","Which are risk factors for heart failure? "+SATA,
 ["*Obstructive sleep apnea","*Diabetes","*Cocaine use","*Previous heart attack","Regular exercise || Not a risk factor."],
 "Also hypertension, obesity, smoking, alcohol and age 65+.")

# ---------------- compensation ----------------
q("comp","The body's 'fixes' for heart failure eventually make it worse. Why?",
 ["*Holding salt and water and tightening vessels add more volume and resistance for a weak heart","They lower blood pressure too much || They raise it.",
  "They slow the heart too much || The heart speeds up.","They make the kidneys lose too much sodium || The kidneys hold sodium."],
 "SNS and RAAS help short term but strain the heart long term.")
q("comp","Which medications block the harmful 'fixes' and help clients live longer? "+SATA,
 ["*Carvedilol","*Lisinopril","*Spironolactone","Furosemide || Symptoms only.","Digoxin || Symptoms only."],
 "Beta blockers calm the SNS; ACE/ARB and spironolactone block RAAS.")
q("comp","A client asks what 'remodeling' of the heart means. What is the best answer?",
 ["*The heart changing size and shape in a harmful way, so it pumps worse","The heart healing back to normal || Remodeling is harmful.",
  "Replacing a valve || That's surgery.","Adjusting the medication list || Not what it means."],
 "ACE inhibitors and spironolactone slow remodeling.")

# ---------------- systolic vs diastolic ----------------
q("sysdia","An echo shows a big, thin-walled left ventricle with an EF of 30%. Which type of heart failure?",
 ["*Systolic (HFrEF)","Diastolic (HFpEF) || EF would be 50% or more.","Hypertrophic cardiomyopathy || Thick septum.","Restrictive cardiomyopathy || Rigid walls, normal EF."],
 "HFrEF: can't squeeze; EF 40% or less; S3.")
q("sysdia","An older client with long-standing high BP has an EF of 58% but stiff, thick ventricle walls. Which type of heart failure?",
 ["*Diastolic (HFpEF)","Systolic (HFrEF) || EF would be 40% or less.","Dilated cardiomyopathy || Thin, weak walls.","No heart failure || The stiff ventricle can't fill."],
 "HFpEF: can't relax and fill; EF 50% or more; S4.")
q("sysdia","Which heart sound goes with each type of heart failure?",
 ["*S3 with systolic; S4 with diastolic","S4 with systolic; S3 with diastolic || Reversed.","S1 with both || S1 is normal.","No extra sounds in heart failure || S3 and S4 are clues."],
 "S3 = dilated, weak ventricle. S4 = stiff ventricle.")
q("sysdia","The 'four pillar' medications improve survival in which type of heart failure?",
 ["*HFrEF (reduced EF)","HFpEF (preserved EF) || Care focuses on BP, HR and fluid.","Only restrictive cardiomyopathy || Not the indication.","Only right-sided failure || Not the indication."],
 "SGLT2 inhibitors help both types.")

# ---------------- left vs right (FOCUS) ----------------
q("lr","A heart failure client has crackles, a cough and must sleep sitting up. Which side is failing?",
 ["*Left","Right || Right-sided signs are in the body: JVD, edema.","Neither || These are heart failure signs.","Both equally || The lung signs point left."],
 "Left = Lungs.")
q("lr","A heart failure client has JVD, swollen ankles, a big liver and a 4-lb weight gain. Which side is failing?",
 ["*Right","Left || Left signs are in the lungs.","Neither || These are heart failure signs.","Can't tell || These are classic right-sided signs."],
 "Right = rest of the body.")
q("lr","Which findings are LEFT-sided? "+SATA,
 ["*Crackles","*Orthopnea","*Waking at night short of breath","*Pink, frothy sputum","Ascites || Right-sided.","JVD || Right-sided."],
 "Pink frothy sputum = pulmonary edema.")
q("lr","Which findings are RIGHT-sided? "+SATA,
 ["*JVD","*Dependent edema","*Weight gain","*Enlarged liver and RUQ discomfort","*Nausea and poor appetite","Crackles || Left-sided."],
 "Bedbound clients get sacral edema.")
q("lr","What usually causes right-sided heart failure?",
 ["*Left-sided heart failure","A blood clot in the leg || Not the most common cause.","COPD || A cause, but not the most common.","Hypothyroidism || Not listed."],
 "Others: pulmonary hypertension, COPD, MI, PE.")
q("lr","Last month a client slept on 1 pillow; now they need 3. What does this mean?",
 ["*Worsening left-sided heart failure","Getting better || More pillows = worse.","Right-sided failure only || Orthopnea is a lung sign.","Normal aging || Report it."],
 "Document the number of pillows.")
q("lr","Which findings show LOW cardiac output? "+SATA,
 ["*New confusion","*Cool, pale skin","*Low urine output","*Fatigue","Warm, flushed skin || Not low output."],
 "Also restlessness and a fast heart rate.")

# ---------------- NYHA ----------------
q("nyha","A client with heart failure is short of breath while sitting in a chair at rest. Which NYHA class?",
 ["*Class IV","Class I || No limits.","Class II || Symptoms with ordinary activity.","Class III || Comfortable at rest."],
 "Symptoms at rest = the most severe class.")
q("nyha","Which care fits NYHA Class IV heart failure?",
 ["*Transplant, LVAD, IV inotropes, or palliative or hospice care","Lifestyle changes only || Class I.","No treatment || Class IV is severe.","Adding one new pill only || Not the Class IV focus."],
 "Clients can move up or down classes.")

# ---------------- BNP (FOCUS) ----------------
q("bnp","Why does the BNP rise in heart failure?",
 ["*The stretched, overloaded ventricles release it","The kidneys are failing || That's BUN/creatinine.","The liver is congested || That's LFTs.","The thyroid is overactive || That's TSH."],
 "Higher BNP = more stretch.")
q("bnp","A short-of-breath client with COPD has a BNP of 70 pg/mL. What does this suggest?",
 ["*Heart failure is unlikely; the lungs are the likely cause","Severe heart failure || BNP would be much higher.","The lab is wrong || Under 100 is normal.","The diuretic is working || No earlier value to compare."],
 "BNP under 100 makes heart failure unlikely.")
q("bnp","A client's BNP drops from 1,800 to 600 over 4 days of IV furosemide. What does this mean?",
 ["*Treatment is working; the ventricles are less stretched","Heart failure is cured || BNP doesn't diagnose or rule out alone.",
  "The client is dehydrated || A falling BNP means less stretch.","BNP can't be trended || It should be trended."],
 "Trend BNP; don't react to one number.")
q("bnp","Which lab result best supports a diagnosis of heart failure?",
 ["*A high BNP","A high A1C || Diabetes.","A high lipase || Pancreas.","A low TSH || Thyroid."],
 "BNP supports but doesn't make the diagnosis alone; the echo is the gold standard.")

# ---------------- imaging ----------------
q("imaging","Which test is the gold standard for diagnosing heart failure because it shows the EF?",
 ["*Echocardiogram","Chest x-ray || Shows congestion, not EF.","ECG || Can't diagnose HF alone.","BNP || Supports the diagnosis only."],
 "Echo: noninvasive ultrasound with no radiation.")
q("imaging","A client is back from a TEE and asks for a drink of water. What should the nurse do first?",
 ["*Check that the gag reflex has returned","Give small sips right away || Aspiration risk.","Give warm tea for the sore throat || Gag reflex first.","Wait 24 hours || Only until the gag reflex returns."],
 "The throat is numbed and the client is sedated.")
q("imaging","After a TEE, which findings should be reported? "+SATA,
 ["*Severe throat pain","*Trouble swallowing","*Bleeding","*Chest pain","A mild sore throat || Expected."],
 "These may mean esophageal injury.")
q("imaging","Which preparation is needed before a TEE? "+SATA,
 ["*NPO about 6 hours","*Signed consent","*IV access","*Dentures removed","A bowel prep || Not needed."],
 "After: vitals, sedation level, gag reflex.")
q("imaging","What does an ECG add to a heart failure workup?",
 ["*It finds causes and complications such as an old MI or atrial fibrillation","It diagnoses heart failure alone || No single ECG finding does.",
  "It shows the EF || The echo shows EF.","It measures lung fluid || The chest x-ray does."],
 "Fast A-fib cuts filling time and can tip a stable client into failure.")
q("imaging","A chest x-ray on day 4 shows less congestion than on admission. What does this suggest?",
 ["*The diuretics are working","Pneumonia is starting || Less congestion is better.","The heart is enlarging || Not what the finding shows.","X-rays can't be compared || They can be trended."],
 "X-ray shows heart size, congestion and effusions.")

# ---------------- labs ----------------
q("labs","A heart failure client's sodium drifts down each day: 136, 133, 130. What does this suggest?",
 ["*Extra fluid is diluting the sodium; heart failure may be advancing","Too much salt intake || Would raise sodium.","Dehydration || Usually dilutional.","Better kidney function || Not the meaning."],
 "Normal sodium is 135–145.")
q("labs","A client on IV furosemide has a rising creatinine. What are possible causes? "+SATA,
 ["*Too much fluid was removed, so the kidneys aren't perfused","*The failing heart isn't perfusing the kidneys","The kidneys are improving || Rising creatinine = worse.","High potassium || Not what creatinine measures."],
 "The heart and kidneys are tightly linked.")
q("labs","A client in acute pulmonary edema has a CO2 that was low and is now climbing. What does this mean?",
 ["*The client is tiring and may need BiPAP or intubation","The client is improving || A bad sign.","The diuretic is working || Not related.","It's from diarrhea || Respiratory pattern."],
 "Fast breathing first blows off CO2; tiring makes CO2 rise.")
q("labs","Why is a TSH checked in heart failure?",
 ["*Thyroid disease can cause or mimic heart failure and is treatable","To check the liver || LFTs.","To measure stretch || BNP.","To dose digoxin || Not the reason."],
 "Hyperthyroid can trigger A-fib; hypothyroid weakens the heart.")
q("labs","A heart failure client has a low albumin. Why does their edema get worse?",
 ["*Albumin keeps fluid in the vessels; without it, fluid leaks into the tissues","Albumin makes the kidneys hold salt || Aldosterone does that.",
  "Low albumin speeds the heart || Not related.","Low albumin raises BNP || Not the mechanism."],
 "Liver congestion from right-sided failure raises LFTs.")

# ---------------- MAP & CVP ----------------
q("hemo","A client's MAP is 58 mmHg. What should the nurse do?",
 ["*Report it; a MAP under 65 doesn't perfuse the organs","Nothing; it's normal || Normal is about 70–100.","Give a diuretic || Would drop the BP further.","Recheck tomorrow || Needs action now."],
 "Poor perfusion signs: low urine output, confusion, cool skin.")
q("hemo","A client's CVP is high, with JVD and 3+ edema. Which order fits?",
 ["*A diuretic","A fluid bolus || Too much volume already.","Lying flat || Worsens breathing.","Hold all meds || Overload needs treatment."],
 "High CVP = too much volume or a right ventricle that can't keep up.")
q("hemo","A client has a LOW CVP after aggressive diuresis. What does this suggest?",
 ["*Not enough volume (over-diuresis)","Fluid overload || That raises CVP.","Right-sided failure || That raises CVP.","Normal after diuresis || Report a low CVP with falling BP."],
 "Also low from bleeding or dehydration.")

# ---------------- priority assessment (FOCUS) ----------------
q("assess","A heart failure client is newly confused and their O2 sat is 87%. What is the priority?",
 ["*Treat it as urgent: raise the head of the bed, give oxygen, assess and notify the provider","Reorient and recheck at the next round || A red flag.",
  "Give a sedative || Hides hypoxia.","Encourage fluids || Fluid is restricted."],
 "New confusion and a low O2 sat = poor perfusion or worsening congestion.")
q("assess","Which lung finding in a heart failure client is an emergency?",
 ["*Gurgling breath sounds with pink, frothy sputum","Fine crackles at the bases that haven't changed || Watch the trend.","Diminished sounds at one base || Often a pleural effusion.","Clear lungs || Normal."],
 "Severe pulmonary edema.")
q("assess","The nurse hears crackles in a heart failure client and asks them to cough. The crackles don't change. What does this suggest?",
 ["*Fluid in the lungs, not secretions","Secretions that need suctioning || Secretions clear with coughing.","Normal lungs || Crackles aren't normal.","A pneumothorax || Not the finding."],
 "Crackles start at the bases and move up as fluid builds.")
q("assess","A heart failure client is wheezing. What will fix it?",
 ["*Removing fluid with diuretics","A bronchodilator || Fluid is narrowing the airway.","More IV fluids || Worsens it.","Lying flat || Worsens it."],
 "Fluid in the airway walls causes wheezing.")
q("assess","Which hourly urine output should the nurse report in a heart failure client?",
 ["*22 mL/hr","40 mL/hr || Above 30.","55 mL/hr || Above 30.","35 mL/hr || Above 30."],
 "Report urine output under 30 mL/hr.")
q("assess","Which questions should the nurse ask a heart failure client? "+SATA,
 ["*How many pillows do you sleep on?","*How far can you walk before getting short of breath?","*Are you taking your medicines?","*Do you use ibuprofen or naproxen?","What's your favorite color? || Not relevant."],
 "Also weight changes, appetite and salt and fluid intake.")

# ---------------- daily weight ----------------
q("weight","Which is the BEST way to track a heart failure client's fluid status?",
 ["*Daily weight","Edema grade || Subjective.","BNP || Measures stretch.","How thirsty they feel || Not reliable."],
 "1 kg = 1 L of fluid.")
q("weight","How should a client weigh themselves at home? "+SATA,
 ["*Every morning at the same time","*After urinating, before breakfast","*On the same scale in similar clothes","After dinner || Before breakfast.","Any scale nearby || Same scale."],
 "Consistency makes the trend accurate.")
q("weight","Which weight change should a heart failure client report?",
 ["*2.5 lb overnight","1 lb in a week || Not reportable.","3 lb over a month || Not reportable.","4 lb in a week || Report 5 lb in a week."],
 "Report 2–3 lb in 24 hours or 5 lb in a week.")
q("weight","Which findings are EARLY signs that heart failure is getting worse? "+SATA,
 ["*Weight gain","*Needing more pillows","*New crackles","*New confusion","*Less urine","A falling BNP || Improvement."],
 "New crackles can come before the client feels short of breath.")
q("weight","A client gained 3 lb since yesterday and has new crackles. What should the nurse do?",
 ["*Report it now; these are signs of decompensation","Recheck the weight next week || Report now.","Give extra fluids || Worsens it.","Document only || Must report."],
 "Listen to lung sounds at every assessment.")

# ---------------- edema & JVD ----------------
q("edjvd","Where does the nurse check for edema in a client who has been in bed for 3 days?",
 ["*The sacrum","The ankles || In bed, fluid moves to the sacrum.","The face || Not dependent.","The hands || Not dependent."],
 "Fluid follows gravity.")
q("edjvd","Only the right calf is swollen in a heart failure client. What should the nurse think of?",
 ["*Something other than heart failure, such as a DVT","Typical heart failure edema || HF edema is on both sides.","Right-sided failure || Still both legs.","Normal || Needs follow-up."],
 "Always compare both sides.")
q("edjvd","How is the client positioned to check for JVD?",
 ["*Head of bed at 30–45 degrees","Flat || Neck veins look full in almost everyone.","Sitting straight up at 90 degrees || Not the position.","Head down || Not used."],
 "Look above the collarbone.")
q("edjvd","Which statements about JVD are correct? "+SATA,
 ["*It usually means too much pressure on the right side","*New or worse JVD suggests fluid retention","*It can also happen with kidney failure or tamponade","It shows exactly how bad the heart failure is || It doesn't show severity.","It only happens in heart failure || Not specific."],
 "Report new or worsening JVD.")
q("edjvd","A client with swollen legs has them up on a footstool and is now more short of breath with crackles. What should the nurse do?",
 ["*Lower the legs and watch breathing; elevation sends fluid back to the lungs","Raise the legs higher || Worsens it.","Lay the client flat || Worsens breathing.","Nothing || Breathing changes need action."],
 "In acute pulmonary edema: sit up, legs dangling.")
q("edjvd","A dent stays deep in the shin for over a minute after pressing. How is this graded?",
 ["*4+ pitting edema","1+ || Shallow and gone right away.","2+ || Not this deep or long.","No edema || Pitting is edema."],
 "Scales vary by facility, so document what you see.")

# ---------------- four pillars ----------------
q("pillars","Which drugs are the 'four pillars' for HFrEF? "+SATA,
 ["*An ARNI (or ACE inhibitor or ARB)","*A beta blocker","*An aldosterone antagonist","*An SGLT2 inhibitor","Furosemide || Symptoms only.","Digoxin || Symptoms only."],
 "The four pillars lower death and hospitalization.")
q("pillars","A client asks why they take furosemide if it isn't a 'pillar.' What is the best answer?",
 ["*It removes fluid and eases symptoms, but it doesn't make you live longer","It protects the heart from scarring || That's spironolactone.",
  "It is a pillar || It isn't.","It raises potassium || It lowers it."],
 "Diuretics and digoxin treat symptoms only.")

# ---------------- loop diuretics (FOCUS) ----------------
q("loop","IV furosemide is due. Which checks come first? "+SATA,
 ["*Blood pressure","*Potassium","*Weight and I&O","*Lung sounds","Blood glucose only || Not the key check."],
 "Hold and notify for potassium under 3.5, low BP or dehydration.")
q("loop","How fast is IV push furosemide given?",
 ["*Slowly, over 1–2 minutes per 20 mg","As fast as possible || Ototoxicity.","Over 2 hours || Not an IV push.","It's never given IV || It is."],
 "A fast push can cause ringing in the ears.")
q("loop","After an IV furosemide push, the client says their ears are ringing. What is the likely cause?",
 ["*Ototoxicity from pushing too fast or a high dose","High potassium || Furosemide lowers it.","An expected effect || Report it.","Angioedema || ACE inhibitors."],
 "Push slowly and ask about hearing.")
q("loop","Morning potassium is 3.1 mEq/L and furosemide is due. What should the nurse do?",
 ["*Hold it and notify the provider","Give it and recheck tomorrow || Will drop potassium further.","Give it faster || Not related.","Double the potassium pill on your own || Not the nurse's call."],
 "Low potassium also makes digoxin toxic.")
q("loop","When should a client take oral furosemide at home?",
 ["*In the morning","At bedtime || Up all night urinating.","Only when swollen || Take as prescribed.","With a salt substitute || Not the teaching."],
 "Rise slowly. Report cramps, weakness or ringing in the ears.")
q("loop","Furosemide is given for LEFT-sided heart failure. Which finding shows it's working?",
 ["*More urine and fewer crackles","Weight going up || Should go down.","More crackles || Worse.","Potassium rising || Furosemide lowers it."],
 "Left = lungs, so clearer lungs show it's working.")
q("loop","Furosemide is given for RIGHT-sided heart failure. Which finding shows it's working?",
 ["*Less leg swelling and a lower weight","New JVD || Worse.","Less urine || Not working.","More edema || Worse."],
 "Right = body, so less edema shows it's working.")
q("loop","Which findings suggest TOO MUCH fluid was removed? "+SATA,
 ["*Rising BUN and creatinine","*Less urine","*Dizziness when standing","*Weight dropping too fast","New crackles || Too much fluid, not too little."],
 "Report before the next dose.")
q("loop","Which findings show IV furosemide worked? "+SATA,
 ["*More urine output","*Lower weight","*Fewer crackles","*Needs fewer pillows","A lower potassium || A side effect, not effectiveness."],
 "Also easier breathing and less edema.")

# ---------------- spironolactone ----------------
q("spiro","A client on spironolactone says they use 'NoSalt' at meals. What should the nurse teach?",
 ["*Stop; salt substitutes are potassium and can raise it dangerously","That's a great choice || Potassium risk.",
  "Use it only at dinner || Still unsafe.","Add bananas too || Limit potassium."],
 "Spironolactone keeps potassium in the body.")
q("spiro","Spironolactone is due. Potassium is 5.5 mEq/L. What should the nurse do?",
 ["*Hold it and notify the provider","Give it; that's normal || Normal is 3.5–5.0.","Give half || Not the nurse's call.","Give it with a banana || Not appropriate."],
 "Hold for potassium over 5.0 or rising creatinine.")
q("spiro","A client on lisinopril and spironolactone has peaked T waves. What does the nurse suspect?",
 ["*High potassium","Low potassium || Not peaked T waves.","Digoxin toxicity || Different signs.","Low magnesium || Not the classic sign."],
 "Both drugs raise potassium.")
q("spiro","Spironolactone is a weak diuretic. Why is it still a 'pillar'?",
 ["*Blocking aldosterone slows heart scarring and helps clients live longer","It removes the most fluid || It's weak.",
  "It strengthens the squeeze || That's digoxin.","It raises the EF right away || Not the reason."],
 "Usually paired with a loop diuretic.")
q("spiro","Which side effects of spironolactone should a client report? "+SATA,
 ["*Breast tenderness or enlargement","*Weakness or tingling","*An irregular heartbeat","A dry cough || ACE inhibitors.","Ringing in the ears || Furosemide."],
 "Also menstrual changes.")

# ---------------- ACE inhibitors ----------------
q("ace","A client who has taken lisinopril for 5 years wakes up with a swollen tongue. What should the nurse do?",
 ["*Treat it as an emergency and protect the airway","Give the next dose with Benadryl || Stop the drug.","Reassure them it only happens in the first week || It can happen any time.","Switch to Entresto today || Also angioedema risk."],
 "Teach: facial swelling or trouble breathing = call 911.")
q("ace","A client on enalapril has had a dry, tickly cough for weeks. What does the nurse expect?",
 ["*The provider may switch them to an ARB","Add an ARB to the ACE inhibitor || Never combine.","Stop all heart meds || Not needed.","Cough syrup only || Report it."],
 "ACE inhibitors cause a bradykinin cough; ARBs don't.")
q("ace","Which statements about ACE inhibitors are true? "+SATA,
 ["*Their names end in -pril","*They can raise potassium","*They aren't used in pregnancy","*Watch for low BP after the first dose","Combine with an ARB for best results || Never combine."],
 "They lower afterload and preload and improve survival.")
q("ace","Which teaching fits a client starting lisinopril? "+SATA,
 ["*Get up slowly","*Avoid salt substitutes and potassium pills","*Avoid NSAIDs","*Report a cough that won't go away","Stop it yourself if you cough || Report it instead."],
 "Hold for low BP, potassium over 5.0, rising creatinine or angioedema.")

# ---------------- ARBs ----------------
q("arb","Which drug is an ARB?",
 ["*Valsartan","Enalapril || ACE inhibitor.","Metoprolol || Beta blocker.","Furosemide || Loop diuretic."],
 "ARBs end in -sartan.")
q("arb","A client on Entresto also has a new order for valsartan. What should the nurse do?",
 ["*Question the order; valsartan is already in Entresto","Give both || Duplicate.","Give valsartan at night || Still duplicate.","Hold Entresto on your own || Clarify with the provider."],
 "Never give an ARB with Entresto or an ACE inhibitor.")
q("arb","Why is losartan given to a client who couldn't tolerate an ACE inhibitor cough?",
 ["*ARBs don't cause bradykinin buildup, so there's no cough","ARBs are weaker || Not the reason.","ARBs aren't absorbed in the lungs || Not the reason.","ARBs lower potassium || They can raise it."],
 "Same benefits, no cough.")
q("arb","What should a woman of childbearing age taking losartan be taught?",
 ["*Use birth control and report a pregnancy","It's the preferred drug in pregnancy || Contraindicated.","Take potassium pills daily || Avoid them.","Stop it if dizzy || Don't stop without the provider."],
 "ACE inhibitors, ARBs and ARNI are all avoided in pregnancy.")

# ---------------- ARNI (FOCUS) ----------------
q("arni","A client's last dose of lisinopril was Monday at 0800. What is the EARLIEST time sacubitril/valsartan (Entresto) can be started?",
 ["*Tuesday at 2000 (36 hours later)","Monday at 2000 || Only 12 hours.","Tuesday at 0800 || Only 24 hours.","Right away || Must wait 36 hours."],
 "Both drugs block bradykinin breakdown, so overlap risks angioedema.")
q("arni","A client says, 'I took my enalapril at breakfast.' Entresto is due at dinner. What should the nurse do?",
 ["*Hold the Entresto and notify the provider","Give it; dinner is far enough apart || Less than 36 hours.","Give half the dose || Still unsafe.","Give it with an antihistamine || Doesn't prevent angioedema."],
 "ACE inhibitor to Entresto requires a 36-hour gap.")
q("arni","A client switching from losartan (an ARB) to Entresto asks if they need to wait 36 hours. What is correct?",
 ["*No; the 36-hour wait is only after an ACE inhibitor, but the ARB is stopped (never given together)","Yes, 36 hours after any blood pressure pill || Only ACE inhibitors.",
  "Take both together for a week || Never combine an ARB with Entresto.","Wait 7 days || Not the rule."],
 "Entresto already contains valsartan, an ARB.")
q("arni","Which clients should NOT receive Entresto? "+SATA,
 ["*A client with past angioedema","*A pregnant client","*A client who took lisinopril 8 hours ago","A client with HFrEF and an EF of 30% || The main indication."],
 "Entresto is preferred over ACE inhibitors and ARBs for HFrEF.")
q("arni","What should the nurse check before each dose of Entresto?",
 ["*Blood pressure","Apical pulse for a full minute only || Digoxin.","Hearing || Furosemide.","Blood glucose || Not the key check."],
 "Also potassium and creatinine. Hold for low BP, potassium over 5.0 or angioedema.")
q("arni","Combining Entresto with an ACE inhibitor is dangerous because of which complication?",
 ["*Angioedema","Hypoglycemia || Not the risk.","Ototoxicity || Furosemide.","Rhabdomyolysis || Statins."],
 "Swelling of the lips, tongue or airway is an emergency.")

# ---------------- beta blockers ----------------
q("bb","Which beta blockers are proven to help HFrEF? "+SATA,
 ["*Carvedilol","*Metoprolol succinate","*Bisoprolol","Propranolol || Not one of the three.","Atenolol || Not one of the three."],
 "They slow the heart so it fills better; EF can improve over time.")
q("bb","A client feels great and wants to stop carvedilol. What should the nurse teach?",
 ["*Never stop it suddenly; talk with the provider","It's fine to stop if BP is normal || Never stop abruptly.","Cut it in half yourself || Provider decides.","Switch to digoxin || Not the same."],
 "Stopping suddenly can cause a rebound fast heart rate and high BP.")
q("bb","The apical pulse is 54 before metoprolol succinate. What should the nurse do?",
 ["*Hold it and notify the provider","Give it || Hold for HR under 60.","Give half || Not the nurse's call.","Give it with coffee || Not appropriate."],
 "Check apical HR and BP before every dose.")

# ---------------- SGLT2 ----------------
q("sglt2","A heart failure client without diabetes asks why they take empagliflozin (Jardiance). What does the nurse say?",
 ["*It helps the heart and kidneys whether or not you have diabetes","It's only for diabetes, so stop it || Not true.","Take it only when your sugar is high || Take as prescribed.","It replaces your furosemide || Not true."],
 "It spills sodium and glucose into the urine, lowering preload.")
q("sglt2","A client on dapagliflozin has vomiting and belly pain. Glucose is 150. What should the nurse suspect?",
 ["*Euglycemic DKA","Simple stomach flu; glucose is fine || Normal glucose doesn't rule it out.","Low blood sugar || Glucose is 150.","Digoxin toxicity || Not on digoxin."],
 "Hold the drug and notify the provider.")
q("sglt2","Which teaching fits an SGLT2 inhibitor? "+SATA,
 ["*Keep the genital area clean; report itching or discharge","*Report genital pain or swelling with fever right away","*Call the provider if you're vomiting or can't eat or drink","Double the dose when sick || Usually held."],
 "Rare: Fournier's gangrene.")

# ---------------- digoxin (FOCUS) ----------------
q("dig","An adult's apical pulse is 57 before digoxin. What does the nurse do?",
 ["*Hold it and notify the provider","Give it || Hold for under 60.","Check the radial pulse for 15 seconds instead || Apical for 1 full minute.","Give half || Not the nurse's call."],
 "Hold under 60 (adult), 70 (child), 90 (infant).")
q("dig","A child is due digoxin. Below what apical pulse should it be held?",
 ["*70","60 || Adult.","90 || Infant.","100 || Not a parameter."],
 "Count the apical pulse for 1 full minute.")
q("dig","Which early sign of digoxin toxicity should the nurse watch for?",
 ["*Loss of appetite and nausea","Ringing in the ears || Furosemide.","A dry cough || ACE inhibitors.","High blood sugar || Not digoxin."],
 "Later: yellow-green halos, confusion, slow heart rate, heart block.")
q("dig","Which signs suggest digoxin toxicity? "+SATA,
 ["*Nausea and vomiting","*Yellow-green halos around lights","*Confusion","*A slow heart rate","Peaked T waves || High potassium."],
 "Therapeutic level: 0.5–2 ng/mL.")
q("dig","A client on digoxin and furosemide has a potassium of 3.0. Why is this dangerous?",
 ["*Low potassium makes digoxin toxicity more likely","Low potassium blocks digoxin from working || Opposite.","It isn't dangerous || It is.","It causes angioedema || Not related."],
 "Also low magnesium, kidney problems and older age raise the risk.")
q("dig","A digoxin level comes back at 2.4 ng/mL. What should the nurse do?",
 ["*Hold the dose and notify the provider","Give it; it's therapeutic || Over 2 is high.","Give it with potassium || Hold first.","Recheck next month || Act now."],
 "Antidote: digoxin immune Fab (DigiFab).")
q("dig","Which medication reverses digoxin toxicity?",
 ["*Digoxin immune Fab (DigiFab)","Naloxone || Opioids.","Vitamin K || Warfarin.","Protamine || Heparin."],
 "Teach: never double a missed dose; check pulse daily.")

# ---------------- vasodilators & inotropes ----------------
q("vasoino","A client on isosorbide dinitrate asks if he can take tadalafil (Cialis). What is the answer?",
 ["*No; together they can drop the BP dangerously","Yes, any time || Contraindicated.","Yes, if taken 1 hour apart || Still unsafe.","Yes, at half dose || Still unsafe."],
 "No erectile dysfunction drugs with nitrates.")
q("vasoino","Which statements about IV dobutamine and milrinone are correct? "+SATA,
 ["*Run on a pump and titrated","*Need telemetry and frequent BP and urine checks","*Must be weaned, not stopped suddenly","*A central line is preferred","They're taken by mouth at home || IV and short-term."],
 "Watch for low BP and dysrhythmias.")
q("vasoino","A client starting hydralazine/isosorbide dinitrate (BiDil) has a headache. What should the nurse teach?",
 ["*It usually eases within a few weeks; rise slowly","Stop the drug || Not without the provider.","It means the BP is too high || It lowers BP.","Expect a slow heart rate || A fast rate is more likely."],
 "Hydralazine can cause a lupus-like syndrome.")

# ---------------- check, hold, call ----------------
q("check","Which drugs can cause HIGH potassium? "+SATA,
 ["*Lisinopril","*Losartan","*Entresto","*Spironolactone","Furosemide || Lowers potassium."],
 "Furosemide lowers potassium, which makes digoxin more toxic.")
q("check","Which drug and hold parameter are matched correctly?",
 ["*Furosemide: hold for potassium under 3.5","Spironolactone: hold for potassium under 3.5 || Held for over 5.0.","Beta blocker: hold for HR under 80 || Under 60.","Lisinopril: hold for potassium under 3.5 || Held for over 5.0."],
 "Use the check, hold and call table.")
q("check","A client takes furosemide and digoxin. Potassium is 3.2 and HR is 70. What should the nurse do first?",
 ["*Hold both and notify the provider about the low potassium","Give both || Toxicity risk.","Give digoxin only || Low potassium makes digoxin toxic too.","Give a salt substitute || Not the nurse's call."],
 "Check before you give.")
q("check","Which pre-dose checks are matched correctly? "+SATA,
 ["*Digoxin: apical pulse for 1 full minute","*Spironolactone: potassium and creatinine","*Nitrates: ask about sildenafil or tadalafil","*Entresto: blood pressure","Beta blocker: hearing || Apical HR and BP."],
 "Know what to check before each drug.")

# ---------------- acute pulmonary edema ----------------
q("ape","A heart failure client is suddenly gasping, with crackles everywhere and pink, frothy sputum. What should the nurse do FIRST?",
 ["*Stay with the client and call for help (rapid response)","Leave to get IV furosemide || Stay with them.","Lay them flat || Worsens it.","Raise the legs || Sends more fluid to the lungs."],
 "Acute pulmonary edema is an emergency.")
q("ape","How should a client in acute pulmonary edema be positioned?",
 ["*Sitting upright with legs dangling","Flat with legs up || Worsens it.","Head down || Worsens it.","Flat on the left side || Not the position."],
 "Dangling the legs keeps fluid away from the lungs.")
q("ape","Which treatments are expected for acute pulmonary edema? "+SATA,
 ["*High-flow oxygen; prepare for BiPAP","*IV furosemide","*Nitroglycerin if BP allows","*A calm voice and explanations","An IV fluid bolus || Adds fluid."],
 "Then monitor SpO2, lung sounds, vitals, urine and potassium.")
q("ape","Which are LATE signs of acute pulmonary edema? "+SATA,
 ["*Pink, frothy sputum","*Blue, cool, clammy skin","*O2 sat dropping despite oxygen","*Confusion and low BP","Restlessness and anxiety || Early.","A new cough || Early."],
 "Early signs: anxiety, fast breathing, cough, crackles.")

# ---------------- nursing management & discharge ----------------
q("dc","How much sodium per day does the lecture recommend for heart failure?",
 ["*1.5–2 g","Under 500 mg || Not the lecture's value.","4–5 g || Too much.","No limit || Sodium is limited."],
 "Read labels.")
q("dc","A client on a fluid restriction asks what counts as fluid. Which items count? "+SATA,
 ["*Ice chips","*Soup broth","*Gelatin","*Coffee","Toast || Not a fluid."],
 "Anything liquid at room temperature counts.")
q("dc","Which hospital care fits a heart failure client? "+SATA,
 ["*Space out activities with rest","*Give stool softeners to avoid straining","*Offer small, frequent meals","*Slowly increase activity","Keep on strict bedrest || Avoid long bedrest."],
 "Also HOB up, oxygen, daily weights and strict I&O.")
q("dc","Which client statement means more teaching is needed?",
 ["*I'll take Advil for my headaches","I'll weigh myself every morning || Correct.","I'll call if I gain 3 pounds in a day || Correct.","I'll keep taking my pills when I feel good || Correct."],
 "NSAIDs make the body hold fluid and are a common trigger.")
q("dc","When should a heart failure client call 911? "+SATA,
 ["*Chest pain","*Severe shortness of breath","*Pink, frothy sputum","*Fainting","A 3-lb weight gain || Call the provider.","Needing one more pillow || Call the provider."],
 "Follow up within 7 days of discharge.")
q("dc","Which teaching fits a heart failure client with fluid overload? "+SATA,
 ["*Stay within the fluid limit","*Keep sodium to 1.5–2 g a day","*Weigh daily","*Track what goes in and comes out","Drink extra water to flush the kidneys || Fluid is restricted."],
 "Report weight gain, more pillows, new crackles or confusion.")

# ---------------- advanced HF ----------------
q("adv","A client's ICD fires once. They feel fine afterward. What should they do?",
 ["*Call the provider","Call 911 || For more than one shock or feeling unwell.","Ignore it || Report it.","Hold a magnet over it || Keep magnets away."],
 "More than one shock or feeling unwell = call 911.")
q("adv","A client with an LVAD has no palpable pulse but is talking and has stable vitals. What does the nurse understand?",
 ["*An LVAD often leaves no palpable pulse","Start CPR || Not needed if alert.","The LVAD has failed || Alert and stable = working.","Give digoxin || Not indicated."],
 "LVAD clients are on anticoagulants and at risk for driveline infection.")
q("adv","A heart transplant client's resting heart rate is 105. Why?",
 ["*The new heart isn't connected to the nerves, so it rests faster","They're rejecting the heart || Normal for a denervated heart.","Too much beta blocker || Not the cause.","They need a pacemaker || Not indicated."],
 "They also need a longer warm-up for exercise.")
q("adv","Which end-of-life topics should be discussed early in advanced heart failure? "+SATA,
 ["*Advance directives","*Palliative care","*Turning off the ICD","*Hospice when appropriate","Avoid talking about prognosis || Discuss early."],
 "Chronic heart failure is ultimately terminal.")

# ---------------- lifespan ----------------
q("life","Which signs suggest heart failure in a baby? "+SATA,
 ["*Sweating during feeds","*Poor weight gain","*Fast breathing","*Fewer wet diapers","Gaining weight quickly from overfeeding || Not the sign."],
 "Usually from congenital heart defects.")
q("life","A woman 3 months after delivery has new swollen ankles and can't breathe lying flat. What should the nurse do?",
 ["*Report it; peripartum cardiomyopathy can occur up to 6 months after delivery","Tell her it's normal swelling || Don't dismiss it.","Encourage more fluids || Not appropriate.","Start lisinopril || Not the nurse's order."],
 "ACE inhibitors, ARBs and ARNI are avoided in pregnancy.")
q("life","How might heart failure show up in an older adult? "+SATA,
 ["*Fatigue","*Confusion","*Poor appetite","Always with crushing chest pain || Often atypical.","Lower digoxin toxicity risk || Higher risk."],
 "Watch for falls from diuretics and dizziness.")

# ---------------- cardiomyopathy ----------------
q("cm","Which cardiomyopathy has large, thin, weak chambers and a low EF?",
 ["*Dilated","Hypertrophic || Thick septum.","Restrictive || Rigid walls, normal EF.","None || Dilated fits."],
 "The most common type; causes include alcohol, cocaine, chemo and pregnancy.")
q("cm","A 17-year-old basketball player faints during practice and has a loud S4. Which cardiomyopathy is most likely?",
 ["*Hypertrophic","Dilated || S3, older adults.","Restrictive || Older adults.","Peripartum || Pregnancy."],
 "HCM is usually inherited and can cause sudden death in young athletes.")
q("cm","Which describe restrictive cardiomyopathy? "+SATA,
 ["*Stiff walls that can't fill","*A normal EF","*Can be caused by amyloidosis or radiation","*Right-sided heart failure signs","Needs aggressive diuresis || Diurese cautiously."],
 "Treat symptoms with cautious diuresis.")
q("cm","Which teaching applies to every type of cardiomyopathy? "+SATA,
 ["*Screen first-degree relatives","*Family should learn CPR","*No competitive sports for affected children","Only the client needs follow-up || Screen relatives."],
 "These family and safety points apply to all types.")
q("cm","Which care fits dilated cardiomyopathy? "+SATA,
 ["*Heart failure medications","*Anticoagulants","*An ICD","*An LVAD or transplant","Septal myectomy || For HCM."],
 "Managed like HFrEF.")

# ---------------- HCM safety (FOCUS) ----------------
q("hcm","A client with hypertrophic cardiomyopathy is dehydrated. Why is this dangerous?",
 ["*A less-full ventricle lets the thick septum block blood flow out more","It raises the EF || Not the mechanism.","It raises potassium || Not the mechanism.","It raises preload || Dehydration lowers preload."],
 "HCM needs filling.")
q("hcm","Which should a client with hypertrophic cardiomyopathy AVOID? "+SATA,
 ["*Nitroglycerin","*Digoxin","*Hot tubs and saunas","*Heavy diuresis","Beta blockers || These help."],
 "Also avoid alcohol, competitive sports, sudden standing and straining.")
q("hcm","Which medications help hypertrophic cardiomyopathy? "+SATA,
 ["*Beta blockers","*Verapamil","*Diltiazem","Nitrates || Worsen obstruction.","Digoxin || Worsens obstruction."],
 "Slowing the heart lets the ventricle fill.")
q("hcm","A client with HCM gets lightheaded after jumping out of bed. What should the nurse teach?",
 ["*Sit or lie down at the first sign of dizziness and stay hydrated","Get up faster || Worsens it.","Take nitroglycerin || Worsens it.","Hold your breath and bear down || Valsalva worsens it."],
 "An ICD may be placed for clients at risk of sudden death.")
