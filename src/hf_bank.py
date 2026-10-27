# Week 9.3 Cardiomyopathy / Heart Failure — built only from the professor's transcript + slides.
# Option syntax: "*text" = correct; "text || why it's wrong" = distractor with its note.
T = "hf"
CONCEPTS = {
 "co":"Cardiac output, preload, afterload & EF",
 "targets":"What each drug class targets",
 "causes":"Causes, risk factors & triggers",
 "comp":"Compensation & remodeling",
 "sysdia":"Systolic (HFrEF) vs diastolic (HFpEF)",
 "lr":"Left- vs right-sided signs",
 "nyha":"NYHA classes",
 "bnp":"BNP",
 "imaging":"Echo, TEE, chest x-ray & ECG",
 "labs":"Labs: K, Na, Mg, BUN/Cr, LFTs, TSH, ABG",
 "hemo":"MAP & CVP",
 "assess":"Priority assessment & lung sounds",
 "weight":"Daily weights & early decompensation",
 "edjvd":"Edema & JVD assessment",
 "pillars":"The four pillars",
 "loop":"Loop diuretics (furosemide)",
 "spiro":"Spironolactone",
 "ace":"ACE inhibitors",
 "arb":"ARBs",
 "arni":"ARNI: sacubitril/valsartan",
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
HI = ["lr","weight","ape","check","dig","arni","hcm","loop"]

SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r):
    Q.append((c, stem, opts, r))

# ---------------- cardiac output ----------------
q("co","Stroke volume depends on three factors. Which description matches afterload?",
 ["How full the ventricle is at the end of diastole || That's preload.",
  "*The resistance the ventricle pushes against to eject blood",
  "How strong the heart muscle squeezes || That's contractility.",
  "The number of beats per minute || That's heart rate, which multiplies stroke volume to give cardiac output."],
 "Afterload = resistance the ventricle pushes against. High blood pressure means high afterload. Preload = filling; contractility = squeeze.")
q("co","What ejection fraction range does this course use as normal?",
 ["40–50% || 40% or less is the HFrEF cutoff, not normal.",
  "*55–70%",
  "70–90% || Too high for the lecture's normal range.",
  "25–40% || That range describes reduced EF (systolic failure)."],
 "The professor uses the American Heart Association's 55–70% (Pearson lists 50–70%). EF = percent of LV blood ejected per beat.")
q("co","In early heart failure, why is tachycardia often one of the first signs?",
 ["Beta receptors become blocked || That's what a beta blocker does; it slows the rate.",
  "*Stroke volume drops, so the body speeds up the heart rate to keep cardiac output up",
  "Preload falls to zero || Preload rises in heart failure from fluid retention.",
  "The ejection fraction rises || EF falls or stays the same; it doesn't rise to cause tachycardia."],
 "CO = HR × SV. When the squeeze bottle puts out less per beat, the body squeezes more often.")
q("co","A client with long-standing hypertension has a high afterload. What happens to stroke volume?",
 ["It rises because the ventricle fills more || Afterload is resistance to ejection, not filling.",
  "*It falls because the ventricle pushes against more resistance, so less blood gets out",
  "It doesn't change; only preload affects stroke volume || Stroke volume depends on preload, afterload and contractility.",
  "It rises because contractility doubles || Contractility doesn't automatically double to overcome resistance."],
 "More resistance = less squeeze gets out. Hypertension and a narrow aortic valve both raise afterload.")

# ---------------- drug targets ----------------
q("targets","Which drug class's main goal is lowering preload?",
 ["*Loop diuretics",
  "ACE inhibitors || Lecture groups ACE inhibitors under lowering afterload.",
  "Digoxin || Digoxin increases contractility.",
  "Beta blockers || Beta blockers slow the heart rate and workload."],
 "Lower preload: diuretics, nitrates, SGLT2 inhibitors. Lower afterload: ACE/ARB/ARNI, hydralazine. Increase contractility: digoxin, dobutamine, milrinone. Slow rate: beta blockers.")
q("targets","Which medications increase contractility? "+SATA,
 ["*Digoxin","*Dobutamine","*Milrinone",
  "Hydralazine || Hydralazine dilates arteries and lowers afterload.",
  "Furosemide || Furosemide lowers preload."],
 "Positive inotropes (digoxin, IV dobutamine and milrinone) strengthen the squeeze.")
q("targets","A drug that dilates vessels to lower afterload is started. Which side effect should the nurse anticipate?",
 ["Hyperglycemia || Not a predicted effect of vasodilation.",
  "*Low blood pressure with dizziness",
  "Bradycardia from increased contractility || Vasodilators don't increase contractility; reflex tachycardia is more likely.",
  "Weight gain from fluid retention || Lowering afterload doesn't cause fluid retention."],
 "Know what a drug does to preload, afterload or contractility and you can predict its side effects: dilating vessels drops the BP.")

# ---------------- causes ----------------
q("causes","What is the most common cause of heart failure overall?",
 ["Hyperthyroidism || A sudden-extra-demand cause, not the most common.",
  "*Coronary artery disease and myocardial infarction",
  "Valve disorders || A cause, but not the most common.",
  "Sepsis || A sudden-extra-demand trigger, not the most common cause."],
 "Damaged heart muscle from CAD/MI is the most common cause. Hypertension is the main 'worked too hard, too long' cause.")
q("causes","A client with stable heart failure is admitted decompensated. Which history findings are common exacerbation triggers? "+SATA,
 ["*Stopped taking furosemide because of frequent urination","*Took ibuprofen daily for back pain","*New-onset atrial fibrillation",
  "*Ate salty takeout most nights",
  "Walked 20 minutes daily || Regular paced activity is recommended, not a trigger."],
 "Triggers: skipping meds, too much sodium or fluid, NSAIDs, infection, uncontrolled BP, new A-fib.")
q("causes","Which are listed risk factors for heart failure? "+SATA,
 ["*Sleep apnea","*Cocaine use","*Age 65 or older","*Prior myocardial infarction",
  "Regular aerobic exercise || Activity isn't a risk factor; paced walking is part of HF care.",
  "Low-normal blood pressure || Hypertension, not low-normal BP, is the risk factor."],
 "Risk factors: CAD, hypertension, diabetes, obesity, smoking, alcohol and cocaine, sleep apnea, age 65+, prior MI.")

# ---------------- compensation ----------------
q("comp","Why do the body's compensation mechanisms eventually worsen heart failure?",
 ["They lower preload too much || They raise preload.",
  "*Fluid retention and vasoconstriction raise preload, afterload and oxygen demand, so the heart weakens further",
  "They permanently stop the heart rate from rising || SNS activation speeds the heart up.",
  "They cause the kidneys to excrete too much sodium || RAAS makes the kidneys hold sodium and water."],
 "SNS speed-up, RAAS salt/water retention and hypertrophy help short term, but more to pump and more to push against makes the heart bigger and weaker; the cycle repeats.")
q("comp","Which drugs help heart failure patients live longer by blocking the body's 'fixes'? "+SATA,
 ["*Beta blockers","*ACE inhibitors","*Spironolactone",
  "Furosemide || Treats symptoms; it doesn't block the compensation that damages the heart.",
  "Digoxin || Treats symptoms; no survival benefit."],
 "Beta blockers calm the SNS speed-up; ACE inhibitors, ARBs and spironolactone block RAAS/aldosterone salt and water retention.")
q("comp","What does 'remodeling' mean in heart failure?",
 ["The heart repairing itself back to normal size || Remodeling is harmful change, not repair.",
  "*Changes in the heart's size, shape and structure (bigger ventricle, thin or stiff walls, scar) that make it pump less efficiently",
  "Surgical replacement of a valve || That's valve surgery, not remodeling.",
  "Medication changes when the class worsens || Not what remodeling means."],
 "Remodeling = the heart changing shape in a bad way after damage or strain. Spironolactone and ACE inhibitors slow it.")

# ---------------- systolic vs diastolic ----------------
q("sysdia","An echocardiogram shows EF 25% with a large dilated left ventricle. Which type of heart failure is this?",
 ["Diastolic (HFpEF) || HFpEF has EF 50%+ with a thick stiff ventricle.",
  "*Systolic heart failure with reduced EF (HFrEF)",
  "Hypertrophic cardiomyopathy || HCM has a thick septum and normal-to-high EF.",
  "Restrictive cardiomyopathy || RCM has rigid walls and normal EF."],
 "Systolic/HFrEF: can't squeeze, EF 40% or less, dilated thin walls, often after MI or dilated cardiomyopathy; S3.")
q("sysdia","Which findings fit diastolic heart failure (HFpEF)? "+SATA,
 ["*EF of 60%","*Thick, stiff ventricle with a small chamber","*S4 heart sound","*Long-standing hypertension",
  "S3 heart sound || S3 goes with systolic failure.",
  "Dilated ventricle with thin walls || That describes systolic failure."],
 "HFpEF: can't relax and fill. EF 50%+, thick stiff ventricle, S4. Causes: HTN, aging, diabetes, obesity, HCM.")
q("sysdia","For which type of heart failure do the 'four pillar' medications lower the risk of death?",
 ["*Systolic heart failure (HFrEF)",
  "Diastolic heart failure (HFpEF) || HFpEF care focuses on BP, HR and fluid; SGLT2 inhibitors help.",
  "Right-sided failure from COPD only || Not the lecture's indication.",
  "Restrictive cardiomyopathy only || Not the lecture's indication."],
 "The four pillars (ARNI/ACE/ARB, beta blocker, aldosterone antagonist, SGLT2 inhibitor) are guideline therapy for HFrEF.")
q("sysdia","Which heart sound is associated with systolic heart failure?",
 ["S1 || A normal heart sound.","S2 || A normal heart sound.","*S3",
  "S4 || S4 goes with diastolic failure and HCM."],
 "S3 = systolic (dilated) failure. S4 = diastolic (stiff) failure.")

# ---------------- left vs right ----------------
q("lr","Which findings point to LEFT-sided heart failure? "+SATA,
 ["*Orthopnea","*Crackles","*Paroxysmal nocturnal dyspnea","*Pink, frothy sputum",
  "Jugular vein distension || Right-sided (systemic congestion).",
  "Ascites || Right-sided (liver/abdominal congestion)."],
 "Left = lungs: dyspnea, orthopnea, PND, crackles, tachypnea, cough; pink frothy sputum = pulmonary edema.")
q("lr","Which findings point to RIGHT-sided heart failure? "+SATA,
 ["*Jugular vein distension","*Dependent edema","*Hepatomegaly with RUQ pain","*Nausea and anorexia","*Nocturia",
  "Crackles at the bases || Lung findings point left."],
 "Right = body: JVD, hepatojugular reflux, dependent (sacral if bedbound) edema, weight gain, hepatomegaly, ascites, nausea, nocturia.")
q("lr","What is the most common cause of right-sided heart failure?",
 ["Pulmonary embolism || A cause, but not the most common.",
  "*Left-sided heart failure",
  "COPD (cor pulmonale) || A cause, but not the most common.",
  "Hyperthyroidism || Not listed as a right-sided cause."],
 "Most right-sided failure follows left-sided failure. Others: pulmonary HTN, COPD, MI, PE.")
q("lr","A client used to sleep on 2 pillows and now sleeps sitting up in a recliner. What does this suggest?",
 ["Improving heart failure || Needing to sit more upright is worse, not better.",
  "*Worsening left-sided heart failure (orthopnea)",
  "Right-sided failure only || Orthopnea is a lung (left-sided) symptom.",
  "A normal age-related change || Not normal; it should be reported."],
 "Ask how many pillows and document the number. More pillows or needing a recliner = worsening orthopnea.")
q("lr","Which findings reflect LOW cardiac output? "+SATA,
 ["*Fatigue and activity intolerance","*New restlessness or confusion","*Oliguria","*Cool, pale skin",
  "Bounding pulses || Low output gives weak pulses and tachycardia.",
  "Warm, flushed skin || Low output gives cool, pale skin."],
 "Low output: fatigue, restlessness, confusion, oliguria, cool pale skin, tachycardia.")
q("lr","On assessment a heart failure client has edema, an enlarged liver and JVD. Which side is failing?",
 ["Left || Lung findings point left.",
  "*Right",
  "Neither; these are kidney findings || These are systemic venous congestion findings.",
  "It can't be determined || Edema, liver signs and JVD point right."],
 "Lung findings point left; edema, liver symptoms and JVD point right. Many chronic patients have both.")

# ---------------- NYHA ----------------
q("nyha","A client with heart failure has symptoms even at rest. Which NYHA class is this?",
 ["Class I || No limitation.","Class II || Symptoms with ordinary activity.",
  "Class III || Comfortable at rest; less-than-ordinary activity causes symptoms.","*Class IV"],
 "The professor says don't memorize every class, but know that symptoms at rest = severe (Class IV). Care builds from lifestyle to meds, devices, transplant, hospice.")
q("nyha","Which treatment focus matches NYHA Class IV?",
 ["Lifestyle changes and low sodium only || Class I focus.",
  "*Transplant, VAD, IV inotropes, or palliative or hospice care",
  "Adding an ACE inhibitor to a beta blocker || Class II focus.",
  "No treatment needed || Class IV is the most severe."],
 "Focus of care advances with each class; Class IV may need transplant, VAD, IV inotropes, or palliative/hospice care. Clients can move up or down classes.")

# ---------------- BNP ----------------
q("bnp","What does a BNP level reflect?",
 ["Damage to the kidneys || That's BUN/creatinine.",
  "*How stretched and overloaded the ventricles are",
  "Liver congestion || That's LFTs.",
  "Thyroid function || That's TSH."],
 "Ventricles release BNP when stretched by volume or pressure. Higher = more stretch.")
q("bnp","A client with COPD and heart failure arrives short of breath. BNP is 60 pg/mL. What does this suggest?",
 ["*Heart failure is unlikely to be the cause; look at the lungs",
  "Severe heart failure || Severe HF would show a much higher BNP.",
  "The diuretic is working || There's no earlier value to trend against.",
  "The lab is wrong because BNP is always over 100 || BNP under 100 is a normal finding."],
 "BNP under 100 pg/mL makes heart failure unlikely. If it were 1,500, the heart would likely be the problem.")
q("bnp","A client's BNP was 1,500 on admission and 500 after three days of IV diuretics. How should the nurse interpret this?",
 ["Heart failure is now cured || BNP supports, but doesn't make or rule out, the diagnosis alone.",
  "*Treatment is working; the ventricles are less stretched",
  "The client is dehydrated || Falling BNP shows less stretch, not dehydration.",
  "BNP can't be compared between days || The professor says to trend BNP, not react to one number."],
 "Trend BNP over the stay. It supports the HF diagnosis but doesn't make it alone.")

# ---------------- imaging ----------------
q("imaging","Which test is the gold standard for diagnosing heart failure and shows the ejection fraction?",
 ["Chest x-ray || Shows cardiomegaly, congestion and effusion, but not EF.",
  "*Echocardiogram",
  "ECG || No single ECG finding diagnoses heart failure.",
  "BNP || Supports, but doesn't make, the diagnosis."],
 "Echo: noninvasive ultrasound, no radiation or special prep. Shows EF, chamber size, wall thickness and motion, and valves.")
q("imaging","A client returns from a transesophageal echocardiogram (TEE). Which action is the priority before giving anything by mouth?",
 ["Offer warm tea for the sore throat || Nothing by mouth until the gag reflex returns.",
  "*Confirm the gag reflex has returned",
  "Remove the IV || IV access stays while recovering from sedation.",
  "Have the client lie flat for 6 hours || Not part of TEE recovery."],
 "The throat is numbed and the client is sedated. NPO until the gag reflex returns to prevent aspiration (classic NCLEX point).")
q("imaging","After a TEE, which findings should the nurse report right away? "+SATA,
 ["*Severe throat pain","*Trouble swallowing","*Bleeding","*Severe chest pain",
  "Mild sore throat || Expected after the procedure."],
 "A mild sore throat is expected. Severe throat or chest pain, trouble swallowing, or bleeding may mean esophageal injury.")
q("imaging","Which nursing care applies BEFORE a TEE? "+SATA,
 ["*NPO about 6 hours","*Signed consent","*IV access","*Remove dentures",
  "Full bowel prep || Not required for a TEE."],
 "Before: NPO (~6 hr), consent, IV access, remove dentures. After: VS, sedation level, gag reflex before food or drink.")
q("imaging","What is the main role of the ECG in heart failure?",
 ["It diagnoses heart failure by itself || No single ECG finding diagnoses HF.",
  "*It finds causes and complications like an old MI, ischemia or atrial fibrillation",
  "It measures the ejection fraction || The echo shows EF.",
  "It measures fluid in the lungs || The chest x-ray shows congestion."],
 "A-fib is common in HF: the ventricle loses the atrial kick, and rapid A-fib cuts filling time and can tip a stable client into failure.")
q("imaging","On day 3 of IV diuretics, the chest x-ray shows less pulmonary congestion than on admission. What does this mean?",
 ["*The diuretics are working",
  "Pneumonia is developing || Less congestion is an improvement.",
  "The heart is getting larger || The finding is about congestion, not heart size.",
  "The x-ray can't be compared || Like BNP, the chest x-ray is useful to trend."],
 "Chest x-ray looks for cardiomegaly, congestion and pleural effusion, and rules out other causes like pneumonia.")

# ---------------- labs ----------------
q("labs","A heart failure client's serum sodium falls a little each day. What may this indicate?",
 ["Dehydration from too little fluid || Dilutional hyponatremia comes from holding too much fluid.",
  "*Fluid retention diluting the sodium, a possible sign of advancing heart failure",
  "Too much salt in the diet || That would tend to raise sodium.",
  "Improving kidney function || Not what a falling sodium suggests."],
 "Normal Na 135–145. Low sodium in HF is usually dilutional; a falling trend can signal advancing HF.")
q("labs","Creatinine is rising in a client receiving IV furosemide. What could this mean? "+SATA,
 ["*The heart is worsening and not perfusing the kidneys","*The client has been over-diuresed and dried out",
  "The diuretic is improving kidney perfusion || Rising creatinine means worse perfusion.",
  "Potassium is too high || Creatinine reflects kidney function, not potassium."],
 "Heart and kidneys are tightly linked. Rising creatinine = poor perfusion from a failing heart, or too much diuresis.")
q("labs","Acute pulmonary edema: ABGs first show respiratory alkalosis, then CO2 starts rising. What does the rising CO2 mean?",
 ["The client is improving || Rising CO2 in distress is a bad sign.",
  "*The client is tiring out and may need BiPAP or intubation",
  "The diuretic is working || Not related to the CO2 trend.",
  "Metabolic acidosis from diarrhea || It's a respiratory pattern."],
 "Hypoxic, fast breathing blows off CO2 (alkalosis). When the client tires, CO2 rises (acidosis), a sign of respiratory failure.")
q("labs","Why is TSH ordered in a heart failure workup?",
 ["To check for liver congestion || That's LFTs.",
  "*Thyroid problems can mimic or cause heart failure, and they're treatable",
  "To measure ventricular stretch || That's BNP.",
  "To dose furosemide || Kidney function guides dosing."],
 "Hyperthyroid speeds the HR and can trigger A-fib; hypothyroid slows and weakens the heart and causes fluid retention.")
q("labs","Why does a low albumin worsen edema in heart failure?",
 ["*Albumin holds fluid inside the vessels; when it's low, fluid leaks into the tissues",
  "Albumin causes the kidneys to retain sodium || That's aldosterone.",
  "Low albumin raises BNP || Not the mechanism taught.",
  "Low albumin slows the heart rate || Not related."],
 "LFTs (AST, ALT, bilirubin) rise when right-sided failure congests the liver and usually come down with diuresis.")

# ---------------- MAP / CVP ----------------
q("hemo","A client's BP is 84/48 mmHg. What is the MAP, and what should the nurse do?",
 ["*60 mmHg; report it, since organs aren't adequately perfused",
  "60 mmHg; this is normal, keep monitoring || A MAP under 65 is inadequate.",
  "66 mmHg; this is adequate || (84 + 48 + 48) ÷ 3 = 60.",
  "84 mmHg; this is normal || MAP isn't the systolic value."],
 "MAP = (SBP + 2 × DBP) ÷ 3. At least 65 perfuses the brain, kidneys and heart; normal about 70–100. Signs of poor perfusion: low urine, confusion, cool skin.")
q("hemo","A client has CVP 14, JVD and 3+ edema. Which order should the nurse expect?",
 ["IV fluid bolus || A high CVP means too much volume.",
  "*A diuretic such as furosemide",
  "Hold all medications || Fluid overload needs treatment.",
  "Lie the client flat || Doesn't treat overload and worsens breathing."],
 "High CVP = too much volume or a right ventricle that can't keep up (fluid overload or right-sided HF). Focus on the direction, not the number.")
q("hemo","What does a LOW central venous pressure suggest?",
 ["Right-sided heart failure || That raises CVP.",
  "*Not enough volume: dehydration, bleeding, or over-diuresis",
  "Fluid overload || That raises CVP.",
  "Cardiac tamponade || Not the low-CVP picture taught."],
 "Low CVP = not enough volume. Report both very high and very low values, especially with a falling BP.")

# ---------------- priority assessment ----------------
q("assess","Which lung finding is the most concerning in a heart failure client?",
 ["Fine crackles at the bases that are unchanged || A classic HF finding; watch how high they go.",
  "Diminished sounds at the bases || Often a pleural effusion.",
  "*Gurgling or rhonchi with pink, frothy sputum",
  "Wheezing that started today || Can be fluid in the airway walls, but less urgent than gurgling with pink frothy sputum."],
 "Gurgling/rhonchi with pink frothy sputum = severe pulmonary edema, an emergency.")
q("assess","How can the nurse tell fluid crackles apart from secretions?",
 ["Fluid crackles are only heard on expiration || They're usually fine and heard on inspiration.",
  "*Fluid crackles don't clear with coughing",
  "Fluid crackles are only at the apices || They start at the bases.",
  "Fluid crackles improve with a bronchodilator || Fluid has to come out with diuresis."],
 "Crackles usually start at the bases; rising to mid-lung or throughout means fluid is building.")
q("assess","A heart failure client is wheezing. Which statement is accurate?",
 ["A bronchodilator will fix it || In HF wheezing, fluid narrows the airway; it has to come out.",
  "*Fluid in the airway walls narrows the airway; removing fluid stops the wheeze",
  "Wheezing rules out heart failure || Fluid can cause wheezing in HF.",
  "Wheezing means a pleural effusion || Effusion causes diminished sounds."],
 "Fluid in the airway walls can cause wheezing; diuresis, not a bronchodilator, resolves it.")
q("assess","Which urine output should the nurse report for a heart failure client?",
 ["45 mL/hr || Above the reportable threshold.","60 mL/hr || Above the reportable threshold.",
  "*25 mL/hr","35 mL/hr || Above the reportable threshold."],
 "Strict I&O. Report urine output under 30 mL/hr.")
q("assess","Which questions belong in the priority history for a heart failure client? "+SATA,
 ["*How far can you walk before you get short of breath?","*How many pillows do you sleep with?",
  "*Are you taking your medicines as prescribed?","*Do you take NSAIDs like ibuprofen?",
  "How many hours of TV do you watch? || Not a priority HF assessment question."],
 "Also ask about weight change, appetite or nausea, and salt and fluid intake.")

# ---------------- daily weight ----------------
q("weight","What is the most accurate measure of a heart failure client's fluid status?",
 ["Intake and output || Important, but the professor says daily weight may be even more accurate.",
  "*Daily weight","Edema grade || Subjective and varies between facilities.","BNP || Measures ventricular stretch, not total fluid."],
 "1 kg = 1 L of fluid.")
q("weight","Which instructions for daily weights are correct? "+SATA,
 ["*Same time each morning","*After voiding, before breakfast","*Same scale and same clothing",
  "After breakfast so readings are consistent || Weigh before breakfast.",
  "Any scale is fine as long as it's digital || Use the same scale."],
 "Consistency is what makes the trend accurate.")
q("weight","Which weight change should a heart failure client report to the provider?",
 ["1 lb in a week || Not reportable.","*3 lb in one day",
  "2 lb in a month || Not reportable.","4 lb in a week || Report 5 lb in a week."],
 "Report a gain of 2–3 lb in 24 hours or 5 lb in a week.")
q("weight","Which findings are early signs of decompensation? "+SATA,
 ["*Weight up","*Needing more pillows to sleep","*New crackles","*New confusion","*Less urine",
  "Lower BNP than last week || A falling BNP shows improvement."],
 "Early decompensation: weight up, more pillows, new crackles, new confusion, less urine (under 30 mL/hr).")
q("weight","A client's weight is up 2.5 lb since yesterday, with new crackles at the bases. What is the priority action?",
 ["Recheck the weight in one week || A 2–3 lb gain in 24 hours is reportable now.",
  "*Report to the provider; these are signs of decompensation",
  "Encourage more fluids || The client is retaining fluid.",
  "Document only || New crackles plus weight gain need to be reported."],
 "New crackles can appear before the client feels short of breath; that's why the nurse listens every assessment.")

# ---------------- edema & JVD ----------------
q("edjvd","Where should the nurse assess for edema in a bedbound client?",
 ["The ankles || Fluid follows gravity; in bed the lowest point is the sacrum.",
  "*The sacrum","The face || Not the dependent area.","The hands || Not the dependent area."],
 "Ambulatory: feet, ankles, lower legs. Bedbound: sacrum.")
q("edjvd","Only the client's left leg is swollen. What should the nurse consider?",
 ["Typical heart failure edema || HF edema is bilateral and systemic.",
  "*Something other than heart failure, such as a DVT",
  "Right-sided failure only || Still causes both legs to swell.",
  "Nothing; one-sided edema is normal || One-sided edema needs follow-up."],
 "Compare both sides: bilateral = systemic like HF; one leg = possibly DVT.")
q("edjvd","How should the nurse position a client to assess jugular vein distension?",
 ["Flat in bed || Almost anyone's neck veins look full when flat.",
  "*Semi-Fowler's, head of bed 30–45°",
  "High Fowler's at 90° || Not the lecture's position.",
  "Trendelenburg || Not used."],
 "Look above the collarbone with the HOB at 30–45°.")
q("edjvd","Which statements about JVD are accurate? "+SATA,
 ["*It usually means too much pressure on the right side: fluid overload or right-sided HF",
  "*New or worsening JVD suggests the client is retaining fluid and decompensating",
  "*It can also occur with kidney failure fluid overload, cardiac tamponade or tension pneumothorax",
  "It tells you exactly how severe the heart failure is || It doesn't show severity.",
  "It only occurs in heart failure || JVD isn't specific to HF."],
 "Treat new or worsening JVD like rising weight or new crackles: report it.")
q("edjvd","A client with leg edema is sitting in a chair. Their legs are elevated, and they now have crackles and more shortness of breath. What should the nurse do?",
 ["Raise the legs higher || Elevation sends more fluid back toward the heart and lungs.",
  "*Watch breathing closely and lower the legs; elevation returns fluid to the heart and lungs",
  "Lie the client flat || Worsens breathing.",
  "No change is needed || Breathing changes need action."],
 "Elevating legs helps edema but sends fluid back to the heart. In acute pulmonary edema, sit up and dangle the legs.")
q("edjvd","How is pitting edema graded?",
 ["*1+ to 4+, by the depth of the dent and how long it takes to rebound",
  "By the circumference of the ankle only || Not the pitting scale.",
  "Mild/moderate/severe by color || Not the pitting scale.",
  "By the weight change || Weight is a separate measure."],
 "Press about 5 seconds over a bony area. 1+ = shallow and gone almost right away; 4+ = deep, lasting 1–2 minutes. Scales vary, so document what you saw.")

# ---------------- four pillars ----------------
q("pillars","Which are the 'four pillars' for HFrEF? "+SATA,
 ["*ARNI (or ACE inhibitor/ARB)","*Beta blocker","*Aldosterone antagonist","*SGLT2 inhibitor",
  "Loop diuretic || Relieves symptoms but doesn't lengthen life.",
  "Digoxin || Relieves symptoms but doesn't lengthen life."],
 "The four pillars lower death and hospitalization. Diuretics and digoxin treat symptoms only.")
q("pillars","A client asks why they still take furosemide if it isn't one of the four pillars. Best response?",
 ["\"It protects your heart muscle from scarring.\" || That's spironolactone.",
  "*\"It relieves fluid and symptoms, but it doesn't lengthen life the way the four pillars do.\"",
  "\"It's a pillar; the list is wrong.\" || Diuretics aren't pillars.",
  "\"It raises your potassium.\" || Furosemide lowers potassium."],
 "Diuretics and digoxin treat symptoms but don't lengthen life.")

# ---------------- loop diuretics ----------------
q("loop","Before giving IV furosemide, which assessments are priorities? "+SATA,
 ["*Blood pressure","*Potassium level","*Daily weight and I&O","*Lung sounds",
  "Blood glucose only || Not the priority check for furosemide."],
 "Check BP and K+ before giving. Hold and notify for K+ under 3.5, low BP, or dehydration.")
q("loop","What is the correct rate for IV push furosemide?",
 ["Rapid push over 10 seconds || Rapid push risks ototoxicity.",
  "*Slowly, over 1–2 minutes (per 20 mg)",
  "Over 30 minutes by gravity || Not the lecture's IV push rate.",
  "Never IV; only by mouth || It's given IV in the hospital."],
 "Push slowly so a big dose doesn't hit the inner ear all at once, causing ringing or muffled hearing.")
q("loop","A client on IV furosemide reports ringing in the ears. What is the likely cause?",
 ["Hyperkalemia || Furosemide lowers potassium.",
  "*Ototoxicity from a rapid push or high dose",
  "Expected therapeutic effect || Ringing is an adverse effect to report.",
  "Angioedema || That's swelling of lips, tongue or airway with ACE/ARNI."],
 "Ototoxicity: rapid IV push or high doses shift the inner-ear fluid balance. Push slowly and ask about ringing.")
q("loop","A client's potassium is 3.2 mEq/L and IV furosemide is due. What should the nurse do?",
 ["Give it and recheck in the morning || Furosemide will lower K+ further.",
  "*Hold and notify the provider",
  "Give double the potassium supplement and the dose || The nurse doesn't change orders.",
  "Give it faster so it works sooner || Speed doesn't fix low potassium."],
 "Hold and notify for K+ under 3.5. Low K+ also raises digoxin toxicity risk.")
q("loop","Which teaching is correct for oral furosemide?",
 ["Take it at bedtime || It peaks in 1–2 hours; at night the client will be up urinating.",
  "*Take it in the morning (a second dose early afternoon)",
  "Avoid all potassium-rich foods || Eat potassium-rich foods unless told otherwise.",
  "Stand up quickly to avoid dizziness || Rise slowly."],
 "Also teach: rise slowly; report cramps, weakness, palpitations or ringing in the ears.")
q("loop","Which findings suggest a client has been over-diuresed? "+SATA,
 ["*Rising BUN and creatinine","*Falling urine output","*Low BP with dizziness on standing","*Weight dropping too fast",
  "New crackles || Crackles suggest too much fluid."],
 "Furosemide rarely damages the kidney directly; pulling off too much fluid too fast leaves too little volume to perfuse the kidneys. Report before the next dose.")
q("loop","Which findings show IV furosemide was effective? "+SATA,
 ["*Urine output increased","*Weight went down","*Crackles decreased","*Needs fewer pillows",
  "Potassium went down || That's an adverse effect, not effectiveness."],
 "Also: easier breathing and less edema.")

# ---------------- spironolactone ----------------
q("spiro","Which teaching is most important for a client starting spironolactone?",
 ["Use a salt substitute instead of table salt || Most salt substitutes are potassium chloride, which can cause dangerous hyperkalemia.",
  "*Avoid salt substitutes and potassium supplements",
  "Eat extra bananas and potatoes || Limit potassium-rich foods.",
  "Take it with a potassium supplement || Spironolactone keeps potassium."],
 "Spironolactone is potassium-sparing: Na+ and water out, K+ kept, the reverse of furosemide.")
q("spiro","Spironolactone is due. K+ is 5.4 mEq/L. What should the nurse do?",
 ["Give it; potassium is normal || Normal K+ is 3.5–5.0.",
  "*Hold it and notify the provider",
  "Give it with furosemide to lower the potassium || The nurse doesn't make that decision.",
  "Give half the dose || Not the nurse's call."],
 "Hold and notify for K+ above 5.0 or rising creatinine.")
q("spiro","A client on spironolactone and lisinopril shows tall, narrow, pointed T waves on telemetry. What should the nurse suspect?",
 ["Hypokalemia || Low K+ doesn't cause peaked T waves.",
  "*Hyperkalemia",
  "Digoxin toxicity || Presents with GI, vision, bradycardia and block.",
  "Hypomagnesemia || Not the classic peaked-T finding."],
 "Additive hyperkalemia: spironolactone plus ACE/ARB/ARNI. Signs: weakness, fatigue, numbness, tingling, dysrhythmias, peaked T waves.")
q("spiro","Why is spironolactone one of the four pillars even though it's a weak diuretic?",
 ["It removes the most fluid of any diuretic || It's weak alone and is usually paired with a loop diuretic.",
  "*Blocking aldosterone slows scarring and stiffening of the heart, so clients live longer",
  "It raises the ejection fraction immediately || Not the mechanism taught.",
  "It increases contractility || That's digoxin or inotropes."],
 "Aldosterone also causes cardiac fibrosis and remodeling; blocking it improves survival in HFrEF.")
q("spiro","Which side effects of spironolactone should the nurse teach the client to report? "+SATA,
 ["*Breast enlargement or tenderness","*Weakness or tingling","*Irregular heartbeat",
  "Ringing in the ears || That's furosemide ototoxicity.",
  "Dry cough || That's ACE inhibitors."],
 "Hormonal effects include gynecomastia, breast tenderness, menstrual changes and erectile dysfunction.")

# ---------------- ACE inhibitors ----------------
q("ace","A client on lisinopril for 2 years has swelling of the lips and tongue. What is the nurse's priority?",
 ["Reassure them; angioedema only happens in the first week || It can happen even after years on the drug.",
  "*Treat it as an emergency and protect the airway",
  "Give the next dose with an antihistamine || Stop the drug; this is an emergency.",
  "Switch them to sacubitril/valsartan today || The ARNI also carries angioedema risk."],
 "Angioedema (lips, tongue, airway) is an emergency. Teach: facial swelling or trouble breathing = call 911.")
q("ace","A client on enalapril has a persistent dry cough. What does the nurse anticipate?",
 ["Stopping all heart failure medications || Not needed.",
  "*Reporting it; the provider may switch to an ARB",
  "Adding an ARB to the ACE inhibitor || Never combine an ACE inhibitor with an ARB.",
  "A cough suppressant and no other change || Report it; an ARB doesn't cause the bradykinin cough."],
 "ACE inhibitors cause bradykinin buildup and the dry cough. ARBs give the same benefits without it.")
q("ace","Which are true about ACE inhibitors? "+SATA,
 ["*Names end in -pril","*They can cause hyperkalemia and rising creatinine","*They are contraindicated in pregnancy",
  "*Monitor closely about 2 hours after the first dose for hypotension",
  "They should be combined with an ARB for better effect || Never give with an ARB or ARNI."],
 "They block conversion of angiotensin I to II: vasodilation, less aldosterone. Lower afterload and preload; improve survival.")
q("ace","Which teaching is correct for a client starting lisinopril? "+SATA,
 ["*Change positions slowly; lie down if dizzy","*Avoid potassium supplements, salt substitutes and NSAIDs",
  "*Report a cough that won't go away",
  "Stop it on your own if a cough starts || Report a persistent cough; the provider may switch to an ARB.",
  "Use a salt substitute to lower sodium || Salt substitutes contain potassium."],
 "Hold and notify: SBP below parameter, K+ above 5.0, rising creatinine, any angioedema.")

# ---------------- ARBs ----------------
q("arb","Which medication is an ARB?",
 ["Lisinopril || ACE inhibitor (-pril).","*Losartan","Carvedilol || Beta blocker (-lol).","Spironolactone || Aldosterone antagonist."],
 "ARBs end in -sartan: losartan, valsartan, candesartan.")
q("arb","A client takes sacubitril/valsartan (Entresto). The provider also orders valsartan. What should the nurse do?",
 ["Give both; they work differently || Valsartan is already half of Entresto.",
  "*Question the order; the client would be getting valsartan twice",
  "Give valsartan only in the morning || Still a duplicate.",
  "Hold Entresto instead || The nurse clarifies the order with the provider."],
 "Never give valsartan with sacubitril/valsartan, and never combine an ARB with an ACE inhibitor.")
q("arb","Why don't ARBs cause the dry cough that ACE inhibitors do?",
 ["They are given at lower doses || Not the reason.",
  "*They block angiotensin II at the receptor without bradykinin buildup",
  "They aren't absorbed in the lungs || Not the reason.",
  "They raise potassium instead || They can raise potassium, but that's not why there's no cough."],
 "Same benefits as an ACE inhibitor, no bradykinin cough. Still monitor BP, K+ and BUN/Cr; contraindicated in pregnancy.")
q("arb","Which teaching applies to a woman of childbearing age starting losartan?",
 ["*Use birth control and report a pregnancy",
  "It's preferred in pregnancy || ARBs are contraindicated in pregnancy.",
  "Take potassium supplements daily || Avoid potassium supplements.",
  "Stop it if you feel dizzy when standing || Change positions slowly; don't stop without the provider."],
 "ACE inhibitors, ARBs and ARNI are all contraindicated in pregnancy.")

# ---------------- ARNI ----------------
q("arni","A client is switching from lisinopril to sacubitril/valsartan. How long must they be off the ACE inhibitor before the first dose?",
 ["12 hours || Too short.","24 hours || Too short.","*At least 36 hours","No wait is needed || Overlap causes angioedema risk."],
 "Both drugs block bradykinin breakdown, so overlapping them causes a real angioedema risk.")
q("arni","A client says, \"I took my lisinopril this morning.\" Sacubitril/valsartan is ordered for this evening. What should the nurse do?",
 ["Give it; the evening is far enough apart || Less than 36 hours after an ACE inhibitor.",
  "*Hold it and call the provider",
  "Give half the dose || Not the nurse's call, and still unsafe.",
  "Give it with an antihistamine || Doesn't remove the angioedema risk."],
 "Use nursing judgment: hold and notify. ACE to ARNI requires at least 36 hours.")
q("arni","In which client is sacubitril/valsartan contraindicated? "+SATA,
 ["*A client with a history of angioedema","*A pregnant client","*A client who took enalapril 10 hours ago",
  "A client with HFrEF and an EF of 30% || This is the main indication."],
 "Sacubitril/valsartan (Entresto) is preferred over ACE inhibitors and ARBs for HFrEF.")
q("arni","How does sacubitril/valsartan work?",
 ["*Valsartan blocks angiotensin II; sacubitril blocks neprilysin so natriuretic peptides last longer",
  "It increases intracellular calcium to strengthen contraction || That's digoxin.",
  "It blocks sodium and chloride in the loop of Henle || That's furosemide.",
  "It blocks beta receptors to slow the rate || That's a beta blocker."],
 "More vasodilation and more Na+/water excretion. The professor says the nursing care matters more than the patho.")
q("arni","Before each dose of sacubitril/valsartan, what should the nurse check?",
 ["*Blood pressure",
  "Apical pulse for a full minute only || That's digoxin.",
  "Blood glucose || Not the key check.",
  "Hearing || That's furosemide."],
 "Check BP before each dose; monitor K+ and BUN/Cr. Hold for SBP below parameter (often under 90–100), K+ above 5.0, rising creatinine or angioedema.")

# ---------------- beta blockers ----------------
q("bb","Which beta blockers are proven for HFrEF? "+SATA,
 ["*Carvedilol","*Metoprolol succinate","*Bisoprolol",
  "Propranolol || Not one of the three proven for HFrEF.",
  "Losartan || ARB, not a beta blocker."],
 "Only these three are proven. They slow the HR, lower BP and O2 demand, and allow more filling time; EF can improve over time.")
q("bb","A client asks to stop metoprolol succinate because they feel fine. What should the nurse teach?",
 ["Stopping is fine if the BP is normal || Never stop a beta blocker abruptly.",
  "*Never stop it abruptly; talk with the provider",
  "Cut the dose in half on your own || Changes go through the provider.",
  "Switch to digoxin || Not interchangeable."],
 "Nursing Priorities Review: never stop a beta blocker abruptly. Check apical HR and BP; hold for HR under 60 or SBP below parameter.")

# ---------------- SGLT2 ----------------
q("sglt2","A client without diabetes is prescribed empagliflozin (Jardiance) for heart failure and wants to stop it. Best response?",
 ["\"You're right; it's only for diabetes.\" || It's used for HF with or without diabetes.",
  "*\"It helps your heart and kidneys whether or not you have diabetes.\"",
  "\"Take it only when your sugar is high.\" || It's taken as prescribed for HF.",
  "\"It replaces your furosemide.\" || Not what's taught."],
 "SGLT2 inhibitors (-gliflozin) spill sodium and glucose into the urine: mild diuresis, lower preload. Used for HFrEF and HFpEF.")
q("sglt2","A client on dapagliflozin has nausea, vomiting and abdominal pain, with a glucose of 140 mg/dL. What should the nurse suspect?",
 ["Gastroenteritis only; glucose is normal || Normal glucose doesn't rule out ketoacidosis with SGLT2s.",
  "*Euglycemic DKA",
  "Hypoglycemia || Glucose is 140.",
  "Digoxin toxicity || Not on digoxin, and glucose matters here."],
 "Euglycemic DKA: ketoacidosis with near-normal glucose. Hold and notify.")
q("sglt2","Which teaching is correct for an SGLT2 inhibitor? "+SATA,
 ["*Genital hygiene; report itching, burning or discharge","*Report genital pain, redness or swelling with fever right away",
  "*Sick days: call the provider if vomiting or unable to eat or drink",
  "Double the dose on sick days || Usually held when NPO or acutely ill.",
  "It's only for clients with diabetes || Used with or without diabetes."],
 "Side effects: genital yeast infections, UTIs, frequent urination, volume depletion. Rare: Fournier's gangrene. Usually held ~3 days before surgery (per order).")

# ---------------- digoxin ----------------
q("dig","Before giving digoxin to an adult, the apical pulse is 56. What should the nurse do?",
 ["Give it; 56 is close enough || Adult hold parameter is under 60.",
  "*Hold it and notify the provider",
  "Recheck the radial pulse for 15 seconds || Take an apical pulse for a full minute.",
  "Give half the dose || Not the nurse's call."],
 "Apical pulse for 1 full minute. Hold if under 60 (adult), under 90 (infant), under 70 (child).")
q("dig","Which findings are signs of digoxin toxicity? "+SATA,
 ["*Anorexia, nausea and vomiting","*Blurred vision or yellow-green halos","*Confusion or weakness","*Bradycardia or heart block",
  "Ringing in the ears || That's furosemide ototoxicity."],
 "Early toxicity is GI. Therapeutic level 0.5–2 ng/mL (Pearson). Antidote: digoxin immune Fab.")
q("dig","Which lab finding most increases the risk of digoxin toxicity?",
 ["*Potassium 3.1 mEq/L",
  "Sodium 140 mEq/L || Normal.","Magnesium 2.0 mg/dL || Normal; low Mg is the risk.",
  "Potassium 4.5 mEq/L || Normal."],
 "Hypokalemia is the most common risk (loop diuretics lower K+). Also low Mg, renal impairment and older age.")
q("dig","What is the antidote for digoxin toxicity?",
 ["Protamine sulfate || That reverses heparin.","Naloxone || That reverses opioids.",
  "*Digoxin immune Fab (DigiFab)","Vitamin K || That reverses warfarin."],
 "Also teach: take pulse daily, hold if under 60 and call; never double a missed dose; report appetite loss, nausea or vision changes.")
q("dig","A client's digoxin level is 2.6 ng/mL. What should the nurse do?",
 ["Give the dose; the level is therapeutic || Therapeutic is 0.5–2 ng/mL.",
  "*Hold the dose and notify the provider",
  "Give the dose with potassium || Hold first.",
  "Recheck the level in a week || Above 2 needs action now."],
 "Hold and notify: HR below parameter, K+ under 3.5, level above 2 ng/mL, or toxicity signs.")
q("dig","Digoxin is ordered for an infant. Below what apical heart rate should the nurse hold it?",
 ["60 || The adult parameter.","70 || The child parameter.","*90","110 || Not a lecture parameter."],
 "Hold if under 60 (adult), under 70 (child), under 90 (infant).")

# ---------------- vasodilators & inotropes ----------------
q("vasoino","A client on isosorbide dinitrate says he took sildenafil last night. What should the nurse do?",
 ["Give the nitrate as scheduled || Nitrates with PDE-5 inhibitors can cause severe hypotension.",
  "*Hold the nitrate and notify the provider",
  "Give the nitrate lying flat || Still contraindicated.",
  "Give half the dose || Not the nurse's call."],
 "Nitrates are contraindicated with PDE-5 inhibitors (sildenafil, tadalafil). Teach: no erectile dysfunction drugs.")
q("vasoino","Which statements about IV dobutamine or milrinone are correct? "+SATA,
 ["*Continuous infusion on a pump, titrated","*Continuous telemetry with frequent BP, HR and urine output",
  "*Don't stop abruptly; it needs to be weaned","*Check the site for extravasation; a central line is preferred",
  "They are long-term oral home medications || They're short-term IV drugs (or a bridge in Class IV)."],
 "IV inotropes increase contractility for acute decompensated HF or low output; monitor for hypotension.")
q("vasoino","Which teaching applies to hydralazine/isosorbide dinitrate?",
 ["*Headache usually eases within a few weeks; change positions slowly",
  "Expect bradycardia || Reflex tachycardia is the side effect.",
  "Safe to use with tadalafil || Contraindicated with PDE-5 inhibitors.",
  "It raises blood pressure || It lowers BP."],
 "Side effects: headache, flushing, dizziness, reflex tachycardia. Hydralazine can cause a lupus-like syndrome. Avoid in HCM.")

# ---------------- check, hold, call ----------------
q("check","Which medications can RAISE potassium? "+SATA,
 ["*Lisinopril","*Losartan","*Sacubitril/valsartan","*Spironolactone",
  "Furosemide || Furosemide lowers potassium."],
 "Low K+: loop diuretics (and low K+ makes digoxin toxic). High K+: ACE inhibitors, ARBs, ARNI, aldosterone antagonists.")
q("check","Which medication–hold parameter pair is correct?",
 ["Beta blocker: HR under 80 || Hold for HR under 60.",
  "Spironolactone: K+ under 3.5 || Spironolactone is held for K+ over 5.0.",
  "*Furosemide: K+ under 3.5 mEq/L",
  "ACE inhibitor: K+ under 3.5 || ACE inhibitors are held for K+ over 5.0."],
 "Loop diuretics: K+ under 3.5, hypotension, dehydration. Spironolactone and ACE/ARB/ARNI: K+ over 5.0, rising creatinine.")
q("check","A heart failure client is on furosemide and digoxin. Morning K+ is 3.3, apical HR 72. What should the nurse do first?",
 ["Give both medications as scheduled || Low K+ plus digoxin = toxicity risk; furosemide lowers K+ further.",
  "*Hold and notify the provider about the low potassium before giving them",
  "Give digoxin and hold furosemide only || Low K+ makes digoxin toxic too; notify first.",
  "Give a salt substitute to raise potassium || Not the nurse's call."],
 "Check before you give: digoxin (apical HR × 1 min, K+, level) and loop diuretics (BP, K+, weight, I&O).")
q("check","Which pre-administration checks are correct? "+SATA,
 ["*Digoxin: apical pulse for 1 full minute","*Spironolactone: potassium and creatinine",
  "*Nitrates: ask about sildenafil or tadalafil use","*SGLT2 inhibitor: volume status and acute illness or NPO",
  "Beta blocker: hearing test || Check apical HR and BP."],
 "Use the Check, Hold and Call table to know what to look at before each med.")

# ---------------- acute pulmonary edema ----------------
q("ape","A heart failure client becomes restless and tachypneic, with crackles throughout and pink, frothy sputum. What is the FIRST action?",
 ["Leave to get the furosemide from the pharmacy || Stay with the client.",
  "*Stay with the client and call a rapid response",
  "Lie the client flat to rest || Worsens the congestion.",
  "Elevate the legs on pillows || Increases venous return to the lungs."],
 "Acute pulmonary edema is an emergency. Priority order starts with staying and calling for help.")
q("ape","Which positioning is correct for acute pulmonary edema?",
 ["Supine with legs elevated || Sends more fluid to the lungs.",
  "*High Fowler's with legs dangling",
  "Trendelenburg || Worsens congestion.",
  "Left side-lying flat || Not the lecture's position."],
 "Sitting up with legs dangling reduces venous return and gets fluid away from the lungs.")
q("ape","Which interventions are expected for acute pulmonary edema? "+SATA,
 ["*High-flow oxygen or non-rebreather; prepare for BiPAP","*IV furosemide as ordered","*Nitroglycerin as ordered if BP allows",
  "*Stay calm and explain, since anxiety raises O2 demand",
  "IV fluid bolus || Adds to the fluid overload."],
 "Then monitor SpO2, lung sounds, VS, urine output and K+.")
q("ape","Which findings are LATE signs of acute pulmonary edema? "+SATA,
 ["*Pink, frothy sputum","*Cool, clammy, cyanotic skin","*SpO2 falling despite oxygen","*Confusion and hypotension",
  "Anxiety and restlessness || Early sign.",
  "Worsening dyspnea with cough || Early sign."],
 "Early: anxiety, restlessness, tachypnea, dyspnea, cough, crackles, tachycardia.")

# ---------------- nursing management & discharge ----------------
q("dc","What sodium intake does this lecture teach for heart failure?",
 ["Less than 500 mg/day || Not the lecture's value.","*1.5–2 g/day","4–5 g/day || Too high.","No limit if on a diuretic || Sodium is still limited."],
 "Read labels for sodium; no salt substitutes on ACE/ARB/ARNI/spironolactone.")
q("dc","A client on a fluid restriction asks what counts toward the limit. Which items count? "+SATA,
 ["*Ice chips","*Broth","*Coffee",
  "Plain bread || Not a fluid."],
 "Ice chips, broth and other liquids all count toward the fluid restriction.")
q("dc","Which in-hospital care is correct for heart failure? "+SATA,
 ["*Cluster care; rest between activities","*Stool softeners to avoid Valsalva","*Six small meals a day",
  "*Progressive activity; avoid prolonged bedrest",
  "Strict bedrest until discharge || Avoid prolonged bedrest."],
 "Also: HOB up, oxygen as ordered, meds on time after checking parameters, daily weight, strict I&O, lung sounds.")
q("dc","Which client statement shows a need for MORE teaching?",
 ["\"I'll weigh myself every morning after I urinate.\" || Correct.",
  "*\"I'll take ibuprofen for my arthritis pain.\"",
  "\"I'll call if I gain 3 pounds in a day.\" || Correct.",
  "\"I'll take my medicines even when I feel well.\" || Correct."],
 "No NSAIDs or OTC cold medicines without checking with the provider. NSAIDs are a common exacerbation trigger.")
q("dc","Which symptoms should a heart failure client be taught to call 911 for? "+SATA,
 ["*Chest pain","*Severe shortness of breath","*Pink, frothy sputum","*Fainting",
  "A 3-lb weight gain in a day || Call the provider, not 911.",
  "Needing one more pillow || Call the provider."],
 "Call the provider: weight gain, more SOB or pillows, swelling, cough, dizziness. Use teach-back; follow up within 7 days.")

# ---------------- advanced HF ----------------
q("adv","A client with an ICD received one shock and now feels fine. What should they do?",
 ["Call 911 immediately || That's for more than one shock or feeling unwell.",
  "*Call the provider",
  "Ignore it; this is expected daily || Shocks should be reported.",
  "Place a magnet over the device || Keep magnets away."],
 "ICD: shocks VT/VF, usually for EF 35% or less. One shock and fine: call the provider. More than one, or unwell: call 911. Carry the ID card.")
q("adv","A client with an LVAD has no palpable pulse but is alert with stable vital signs. What should the nurse understand?",
 ["Start CPR immediately || The continuous-flow pump may leave no palpable pulse.",
  "*An LVAD may cause no palpable pulse",
  "The LVAD has failed || Alert and stable suggests it's working.",
  "Give digoxin || Not indicated."],
 "LVAD pumps blood from the LV to the aorta (bridge or destination therapy). Clients are anticoagulated and at risk of driveline infection.")
q("adv","A heart transplant recipient asks why their heart rate is 100 at rest and slow to rise with exercise. Best response?",
 ["\"You're rejecting the heart.\" || A denervated heart normally behaves this way.",
  "*\"The new heart isn't connected to the nerves, so it rests faster and needs a longer warm-up.\"",
  "\"Your beta blocker dose is too high.\" || Not the cause.",
  "\"You need a pacemaker.\" || Not indicated by this finding."],
 "Denervated heart: resting HR 90–110, slow to rise with exercise. Lifelong immunosuppression: infection and rejection risk.")
q("adv","Which end-of-life topics should be discussed with clients with advanced heart failure? "+SATA,
 ["*Advance directives and palliative care, early","*ICD deactivation","*Hospice when appropriate",
  "*Dyspnea relief such as positioning, a fan, and opioids or diuretics as ordered",
  "Avoid discussing prognosis so the client stays hopeful || Chronic HF is ultimately terminal; discuss early."],
 "Chronic heart failure is ultimately terminal.")

# ---------------- lifespan ----------------
q("life","Which findings suggest heart failure in an infant? "+SATA,
 ["*Sweating or tiring with feeds","*Poor weight gain","*Tachypnea","*Fewer wet diapers",
  "Rapid weight gain from overfeeding || Poor weight gain is the finding."],
 "In children HF is usually from congenital defects. Care: cluster care; small, frequent, high-calorie feeds.")
q("life","A client at 2 months postpartum reports new orthopnea and ankle edema. What should the nurse do?",
 ["Reassure her it's normal postpartum swelling || Don't dismiss dyspnea, orthopnea or edema.",
  "*Report it; peripartum cardiomyopathy can occur from the last trimester to 6 months postpartum",
  "Start lisinopril || Not the nurse's order, and ACE inhibitors are avoided in pregnancy.",
  "Increase her fluid intake || Doesn't address possible HF."],
 "Pregnancy raises CO by 30–50%, so HF can decompensate. ACE/ARB/ARNI are contraindicated; beta blockers, loop diuretics and digoxin can be used.")
q("life","How may heart failure present in an older adult? "+SATA,
 ["*Fatigue","*Confusion","*Poor appetite",
  "Always with classic chest pain || Older adults often present atypically.",
  "Lower risk of digoxin toxicity || Older adults have higher digoxin toxicity risk."],
 "Most HF is in people 65+. Watch polypharmacy and falls (diuretics, orthostasis, nocturia). Adapt teaching for hearing, vision and memory.")

# ---------------- cardiomyopathy ----------------
q("cm","Which cardiomyopathy has big, thin, weak chambers with a low ejection fraction?",
 ["Hypertrophic || Thick septum, normal or high EF.","*Dilated","Restrictive || Rigid walls, normal EF."],
 "DCM is the most common type. Causes: idiopathic, alcohol, cocaine, chemo, pregnancy, some inherited. Findings: HF signs, S3, dysrhythmias, mural thrombi and emboli.")
q("cm","A young athlete has exertional syncope, angina and a loud S4. Which type of cardiomyopathy is most likely?",
 ["Dilated || Big weak chambers with an S3.","*Hypertrophic","Restrictive || More common in older adults; right-sided signs.","Diastolic HF from aging || Not in a young athlete."],
 "HCM is usually inherited; it can cause sudden death in young athletes.")
q("cm","Which statements describe restrictive cardiomyopathy? "+SATA,
 ["*Rigid walls can't fill","*EF is normal","*Causes include amyloidosis, radiation and fibrosis","*Right-sided HF signs and fatigue",
  "Needs aggressive diuresis || Diuresis must be cautious."],
 "Management: treat HF symptoms with cautious diuresis.")
q("cm","Which teaching applies to ALL types of cardiomyopathy? "+SATA,
 ["*Screen first-degree relatives","*Family learns CPR","*No competitive sports for children with cardiomyopathy",
  "Only affected adults need follow-up || Relatives should be screened."],
 "These family and safety points apply across DCM, HCM and RCM.")
q("cm","Which management fits dilated cardiomyopathy? "+SATA,
 ["*Guideline-directed HF medications","*Anticoagulants (mural thrombi and emboli)","*ICD","*LVAD or transplant",
  "Septal myectomy || That's for HCM."],
 "DCM is managed like HFrEF, plus anticoagulation and devices as indicated.")

# ---------------- HCM safety ----------------
q("hcm","Why does dehydration make hypertrophic cardiomyopathy worse?",
 ["It raises the ejection fraction too high || Not the mechanism.",
  "*A less-full ventricle lets the thick septum block outflow more",
  "It causes hyperkalemia || Not the mechanism taught.",
  "It increases preload || Dehydration lowers preload."],
 "More volume and more filling time = less obstruction.")
q("hcm","Which should be AVOIDED in a client with hypertrophic cardiomyopathy? "+SATA,
 ["*Nitrates and other vasodilators","*Digoxin and other positive inotropes","*Aggressive diuresis","*Hot tubs, saunas and alcohol",
  "Beta blockers || These help: they slow the rate so the ventricle fills."],
 "Also avoid strenuous exercise or competitive sports, sudden standing, and Valsalva.")
q("hcm","Which medications help a client with hypertrophic cardiomyopathy? "+SATA,
 ["*Beta blockers","*Verapamil","*Diltiazem",
  "Nitroglycerin || Vasodilators worsen obstruction.",
  "Digoxin || Inotropes worsen obstruction."],
 "Slowing the rate lets the ventricle fill. Also: keep hydrated, sit or lie down at the first sign of dizziness, ICD for those at risk of sudden death.")
q("hcm","A client with HCM feels dizzy after standing up quickly. What should the nurse teach?",
 ["Stand up faster next time || Sudden standing worsens obstruction.",
  "*Sit or lie down at the first sign of dizziness, and stay hydrated",
  "Take a nitroglycerin || Worsens obstruction.",
  "Bear down to raise blood pressure || Valsalva worsens obstruction."],
 "HCM needs filling, not dehydration.")
