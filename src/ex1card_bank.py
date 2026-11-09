# Week 2.2 Cardiac Infection & Inflammation — lecture transcript, lesson plan, PowerPoint, notes, AHA endocarditis handout.
EXAM = "e1"
T = "cardinf"
CONCEPTS = {
 "risk":"Causes & general risk factors",
 "labs":"Diagnostic framework: echo, cultures, ESR & hsCRP",
 "rfpath":"Rheumatic fever: cause & findings",
 "jones":"Jones criteria & HEART mnemonic",
 "rftx":"Rheumatic fever treatment & Sore Throat Rule",
 "iepath":"Infective endocarditis: cause & risks",
 "iesigns":"Endocarditis signs: Janeway, Osler, splinters, Roth",
 "duke":"Duke criteria & blood cultures",
 "iecomp":"Endocarditis complications",
 "ietx":"Endocarditis antibiotics & surgery",
 "ienurse":"Endocarditis nursing care & prophylaxis",
 "myo":"Myocarditis: cause, findings & tests",
 "myotx":"Myocarditis treatment & nursing",
 "peri":"Pericarditis findings & ECG",
 "perimi":"Pericarditis vs MI",
 "tamp":"Effusion & cardiac tamponade",
 "constrict":"Chronic constrictive pericarditis",
 "peritx":"Pericarditis meds & procedures",
 "perinurse":"Pericarditis nursing care",
}
HI = ["iesigns","duke","iecomp","jones","peri","tamp","myotx","peritx","rftx"]

SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

# ---------- risk ----------
q("risk","Which organism type is the MOST common cause of cardiac infection?",
 ["*Bacteria","Parasites || Listed, but not the most common.","Fungi || Listed, but less common.","Viruses || Listed, but bacteria are most common."],
 "Causes: bacteria (most common), viruses, fungi, parasites and the COVID-19 vaccine.")
q("risk","Which clients are at higher risk for cardiac infection? "+SATA,
 ["*A client who injects drugs with shared needles","*A client on hemodialysis","*A client with a pacemaker","*A client with a valve replacement","A client with perfect oral hygiene and no lines || No listed risk."],
 "Other risks: congenital defects, transplant, rheumatic fever, central lines, dental procedures, piercing, untreated strep, overcrowding.")
q("risk","Which interrelated concepts are linked to cardiac infection? "+SATA,
 ["*Inflammation","*Pain","*Perfusion","*Gas exchange","Cognition || Not listed."],
 "Organism or immune response → inflammation → damaged tissue/valves → reduced perfusion.")

# ---------- labs ----------
q("labs","Which lab pattern commonly appears with cardiac infection or inflammation?",
 ["*Elevated WBC, ESR and hsCRP","Low WBC and low ESR || Opposite.","High potassium only || Not the cluster.","Low troponin and low BNP || Not the inflammation cluster."],
 "These support inflammation but must be paired with condition-specific tests.")
q("labs","Which echocardiogram best shows endocarditis vegetations?",
 ["*Transesophageal echo (TEE)","Transthoracic echo (TTE) || Noninvasive but less accurate.","Chest x-ray || Doesn't show vegetation.","Holter monitor || Records rhythm."],
 "TEE is invasive but more accurate, especially for mitral/tricuspid valves.")
q("labs","When are blood cultures drawn for suspected endocarditis?",
 ["*Before antibiotics, 2 sets from separate sites about 12 hours apart","After the first antibiotic dose || Antibiotics can make cultures falsely negative.","From one site only || Separate sites are needed.","Only if the fever is gone || Fever is a reason to culture."],
 "Draw cultures before antimicrobials.")
q("labs","An hsCRP of 4 mg/L suggests:",
 ["*A serious inflammatory condition","Normal; no inflammation || Normal is <1.0.","Low inflammation only || >3 is serious.","Dehydration || Not what hsCRP measures."],
 "hsCRP normal <1.0 mg/L; >3 mg/L = serious inflammation. ESR >20 mm/hr indicates inflammation.")

# ---------- rheumatic fever ----------
q("rfpath","A 9-year-old had an untreated sore throat 3 weeks ago and now has fever, joint pain that moves from joint to joint, and a new murmur. What is most likely?",
 ["*Rheumatic fever/carditis","Infective endocarditis || Linked to IV drug use, lines and valves, not recent strep.","Pericarditis || Pleuritic positional pain and rub.","Myocarditis || Follows a viral flu-like illness."],
 "Rheumatic fever is an immune response 2–3 weeks after group A beta-hemolytic strep pharyngitis; most common ages 5–14.")
q("rfpath","What are Aschoff bodies?",
 ["*Small myocardial nodules in rheumatic carditis that may scar","Painful finger nodules || That's Osler nodes.","Retinal hemorrhages || Roth spots.","Valve vegetations || Endocarditis."],
 "Repeated attacks → valve fibrosis → stenosis or regurgitation, sometimes decades later.")
q("rfpath","Which findings fit rheumatic fever? "+SATA,
 ["*Migratory polyarthritis","*Sydenham chorea","*Erythema marginatum","*Subcutaneous nodules","Janeway lesions || Endocarditis."],
 "Primary findings: fever, tachycardia, precordial pain, friction rub; murmur (often mitral regurgitation), prolonged PR, AFib.")
q("rfpath","Parents ask whether their child's jerky movements (Sydenham chorea) are permanent. Best response?",
 ["*'They're temporary and usually go away as the illness resolves.'","'They're permanent.' || The lecture reassures they're temporary.","'They mean a stroke happened.' || Not a stroke.","'They're from the antibiotic.' || Part of the illness."],
 "Sydenham chorea = involuntary jerky movements; temporary.")
q("rfpath","Which are risk factors for rheumatic fever? "+SATA,
 ["*Untreated or undertreated strep throat","*Overcrowding and poverty","*Poor access to antibiotics","*Genetic predisposition","Being over 70 || Most common in school-age children."],
 "Spread through oral/respiratory secretions.")

# ---------- Jones ----------
q("jones","Which criteria are used to diagnose rheumatic fever?",
 ["*Modified Jones criteria","Modified Duke criteria || Endocarditis.","Beck's triad || Tamponade.","CHA₂DS₂-VASc || AFib stroke risk."],
 "Evidence of prior strep + 2 major, or 1 major + 2 minor.")
q("jones","Which lab result is positive evidence of a recent strep infection?",
 ["*ASO titer above 200 IU","hsCRP below 1 mg/L || Normal.","Negative throat culture || Not evidence.","Low WBC || Not evidence."],
 "Throat culture and ASO (antistreptolysin O) titer show prior strep.")
q("jones","The HEART mnemonic for rheumatic fever stands for which findings? "+SATA,
 ["*Heart failure","*Enlarged heart","*Arthritis (migratory)","*Rash (erythema marginatum)","*Twitching (Sydenham chorea)","Tamponade || Not part of HEART."],
 "HEART: Heart failure, Enlarged heart, Arthritis, Rash, Twitching.")

# ---------- RF treatment ----------
q("rftx","Which antibiotic treats acute rheumatic fever, and what if the child is allergic?",
 ["*Penicillin; erythromycin if penicillin-sensitive","Vancomycin only || IE empiric therapy.","Colchicine || Pericarditis.","No antibiotics are needed || The infection must be treated."],
 "Complete the full 10-day course.")
q("rftx","What long-term prophylaxis follows rheumatic fever?",
 ["*Monthly IM penicillin G or daily oral penicillin for years, up to lifelong based on heart damage","None after the first course || Prophylaxis prevents repeat attacks.","Daily aspirin for life only || Not the prophylaxis.","Amoxicillin only before dental work || That's IE prevention."],
 "Prophylaxis lasts 5–10 years, until age 21–40, or lifelong.")
q("rftx","What is the 'Sore Throat Rule'?",
 ["*Every sore throat must be swabbed or cultured","Sore throats never need a culture || Opposite.","Use lozenges only || Not the rule.","Wait 2 weeks before seeing a provider || Delay risks heart damage."],
 "Teach the chain: throat infection → immune response → heart-valve damage.")
q("rftx","How is the acute inflammation of rheumatic carditis treated?",
 ["*High-dose aspirin or NSAID; prednisone if severe carditis or heart failure","Anticoagulants only || Not the treatment.","Diltiazem || Not used for this.","Antivirals || It's bacterial/immune."],
 "Also rest, avoid strenuous activity, gentle hydration if HF; valve repair for severe damage.")
q("rftx","Which long-term complications can follow rheumatic carditis? "+SATA,
 ["*Mitral stenosis or regurgitation","*Heart failure","*Atrial fibrillation and stroke risk","*Pulmonary hypertension","Cataracts || Not listed."],
 "Permanent valve scarring → chronic rheumatic heart disease.")

# ---------- IE ----------
q("iepath","Which is the MOST common risk factor listed for infective endocarditis?",
 ["*IV drug use","Overcrowding || A rheumatic fever risk.","Young male age || A myocarditis/pericarditis association.","Viral flu-like illness || Myocarditis."],
 "Other risks: prosthetic valve, central line, hemodialysis, pacemaker, poor dental hygiene.")
q("iepath","How does infective endocarditis damage the heart?",
 ["*Organisms stick to a damaged valve and form vegetations that destroy the valve and can embolize","It inflames the pericardial sac || Pericarditis.","It's an immune response to strep || Rheumatic fever.","It thickens the heart muscle only || Myocarditis."],
 "Usually involves mitral or tricuspid valves; organisms include Streptococcus viridans and Staphylococcus aureus.")
q("iepath","What is the hallmark presentation of infective endocarditis?",
 ["*Persistent high fever with a new or changing murmur","Sharp pain relieved by leaning forward || Pericarditis.","Jerky movements || Sydenham chorea.","Crushing pain relieved by nitroglycerin || MI."],
 "Also chills, night sweats, fatigue, anorexia, weight loss.")

# ---------- IE signs ----------
q("iesigns","A client with endocarditis has PAINFUL nodules on the finger pads. These are:",
 ["*Osler nodes","Janeway lesions || Painless spots on palms/soles.","Roth spots || Retinal.","Splinter hemorrhages || Under the nails."],
 "Osler = painful (O for 'ouch'); Janeway = painless.")
q("iesigns","Small, non-tender red spots on the palms and soles are:",
 ["*Janeway lesions","Osler nodes || Painful finger/toe pads.","Erythema marginatum || Rheumatic fever rash.","Petechiae only || Pinpoint hemorrhages."],
 "Janeway lesions = painless palms/soles.")
q("iesigns","Thin reddish-brown lines under the nail beds are:",
 ["*Splinter hemorrhages from microemboli","Roth spots || Retinal.","Osler nodes || Finger pads.","Clubbing || Not listed."],
 "Splinter hemorrhages are a sign of microemboli in IE.")
q("iesigns","What are Roth spots?",
 ["*White-centered retinal hemorrhages","Painful finger nodules || Osler.","Palm spots || Janeway.","Myocardial nodules || Aschoff bodies."],
 "Seen on eye exam in IE.")
q("iesigns","Which findings are expected in infective endocarditis? "+SATA,
 ["*Petechiae on the conjunctiva or palms","*Splinter hemorrhages","*Janeway lesions","*Osler nodes","Migratory polyarthritis || Rheumatic fever."],
 "These embolic and immune skin/eye findings point to IE.")

# ---------- Duke ----------
q("duke","Which criteria diagnose infective endocarditis?",
 ["*Modified Duke criteria","Modified Jones criteria || Rheumatic fever.","Beck's triad || Tamponade.","HEART mnemonic || Rheumatic fever."],
 "Jones = rheumatic fever; Duke = infective endocarditis.")
q("duke","What is the central diagnostic evidence for endocarditis?",
 ["*Positive blood cultures plus vegetation on echocardiogram","Elevated ASO titer || Strep/rheumatic fever.","Diffuse ST elevation || Pericarditis.","Friction rub || Pericarditis."],
 "Confirm with 2 major, 1 major + 3 minor, or 5 minor criteria.")
q("duke","Which are MINOR Duke criteria? "+SATA,
 ["*Fever above 38°C (100.4°F)","*IV drug use or an invasive line","*Vascular or embolic phenomena","*Immunologic phenomena","Positive ASO titer || Rheumatic fever."],
 "Also cultures that don't meet major criteria.")

# ---------- IE complications ----------
q("iecomp","What is the MOST common complication of infective endocarditis?",
 ["*Heart failure","Cataracts || Unrelated.","Hyperthyroidism || Not listed.","Sydenham chorea || Rheumatic fever."],
 "Left HF: fatigue, SOB, crackles. Right HF: edema, weight gain, anorexia.")
q("iecomp","A client with endocarditis suddenly has slurred speech and right arm weakness. What does the nurse suspect?",
 ["*Embolic stroke from a vegetation","Expected antibiotic effect || Not expected.","Pericarditis || Doesn't cause focal neuro deficits.","Anxiety || Ignores a stroke."],
 "Vegetations embolize; frequent neuro checks are essential.")
q("iecomp","A client with IE reports sudden abdominal pain radiating to the left shoulder. What is likely?",
 ["*Splenic infarct","Renal infarct || Flank pain.","Pulmonary embolus || Pleuritic chest pain and SOB.","Pericarditis || Chest pain relieved leaning forward."],
 "Splenic infarct pain radiates to the left shoulder.")
q("iecomp","What are the three big threats to monitor for in endocarditis? "+SATA,
 ["*Sepsis","*Heart failure","*Embolic events","Hypoglycemia || Not listed."],
 "Also renal infarct, septic aneurysm, conduction problems.")

# ---------- IE treatment ----------
q("ietx","How long is IV antibiotic therapy for infective endocarditis?",
 ["*4–6 weeks","3 days || Far too short.","10 days || That's strep throat.","1 year || Not the course."],
 "High-dose IV therapy sterilizes vegetations; narrow therapy once the organism is known.")
q("ietx","Which empiric antibiotics are listed for endocarditis? "+SATA,
 ["*Vancomycin","*Ceftriaxone","*Gentamicin","Colchicine || Pericarditis anti-inflammatory."],
 "Monitor vancomycin trough (before the 5th dose), gentamicin peak/trough and kidney function.")
q("ietx","Why is routine anticoagulation generally avoided in endocarditis?",
 ["*An embolic stroke could turn into an intracranial hemorrhage","It dissolves vegetations too fast || Not the reason.","It causes HIT in all clients || Not the reason.","It interferes with blood cultures || Not the reason."],
 "Anticoagulate only with another indication, like a prosthetic valve or AFib.")
q("ietx","Which are indications for endocarditis surgery? "+SATA,
 ["*Vegetation over 15 mm","*Severe regurgitation or pulmonary edema","*Fever or positive cultures after 7 days of correct antibiotics","*Valvular abscess","Mild fever on day 1 || Not an indication."],
 "Surgery is needed in nearly 50% of cases: vegetatectomy, valve repair/replacement, abscess drainage.")

# ---------- IE nursing ----------
q("ienurse","Which nursing actions apply to infective endocarditis? "+SATA,
 ["*Draw two culture sets from different sites before antibiotics","*Frequent neuro checks","*Sterile care of the PICC line","*Cardiac auscultation for a new murmur","Encourage contact sports to build stamina || Avoid contact sports until cleared."],
 "Evaluate: afebrile, negative cultures, stable valve, no emboli or edema.")
q("ienurse","Which teaching helps prevent infective endocarditis?",
 ["*Good oral hygiene and prophylactic antibiotics before dental procedures as prescribed","Skip dental visits || Oral care matters.","Take antibiotics only when feverish || Not the teaching.","Avoid handwashing to build immunity || Opposite."],
 "Prophylaxis (amoxicillin) is given about one hour before dental/invasive procedures.")
q("ienurse","Which findings show the IE treatment is working? "+SATA,
 ["*The client is afebrile","*Blood cultures are negative","*Valve function is stable","*No new emboli","A new murmur appears || A worsening sign."],
 "These are the lecture's evaluation outcomes.")

# ---------- myocarditis ----------
q("myo","Why is myocarditis called the 'great mimicker'?",
 ["*It can look like an MI without a coronary blockage","It mimics a cold only || It can mimic MI.","It mimics appendicitis || Not stated.","It never causes symptoms || It does."],
 "Myocarditis = inflammation of the heart muscle that may thicken and weaken it.")
q("myo","A young man had flu-like symptoms 2 weeks ago and now has chest pain, palpitations and dyspnea. Which condition fits best?",
 ["*Myocarditis","Rheumatic fever || Follows strep in children.","Infective endocarditis || Linked to IV drug use and valves.","Constrictive pericarditis || Chronic and scarring."],
 "Viral causes: coxsackie B, adenovirus, COVID-19. Young males are predisposed.")
q("myo","What is the definitive gold standard test for myocarditis?",
 ["*Endomyocardial biopsy","ASO titer || Strep.","Throat culture || Strep.","Chest x-ray || Not definitive."],
 "Cardiac MRI/echo is the noninvasive imaging standard; biopsy is reserved for severe cases.")
q("myo","Which non-infectious causes of myocarditis are listed? "+SATA,
 ["*Drug hypersensitivity (such as clozapine)","*Lupus","*Alcohol or cocaine","*Chemotherapy","Vitamin A deficiency || Not listed."],
 "Immune-mediated and toxin causes.")
q("myo","Which findings show low cardiac output from myocarditis? "+SATA,
 ["*Urine output below 30 mL/hr","*Hypotension","*S3 gallop and JVD","*Crackles","Bounding pulses and warm skin || Signs of good perfusion."],
 "Labs: elevated troponin, BNP, CRP, ESR.")

# ---------- myocarditis treatment ----------
q("myotx","Which medications should be AVOIDED in myocarditis?",
 ["*Diltiazem and verapamil","Furosemide || Used for fluid.","Lisinopril || Part of HF therapy.","Metoprolol || Part of HF therapy."],
 "Non-dihydropyridine CCBs reduce HR, pumping strength and EF, worsening HF.")
q("myotx","A client recovering from myocarditis feels better and wants to restart running. Best response?",
 ["*'Avoid strenuous activity for 3–6 months; feeling better doesn't mean the muscle has healed.'","'Start running tomorrow.' || Too soon.","'You never need restrictions.' || Restriction is key.","'Run but skip your meds.' || Not appropriate."],
 "Strict rest prevents the 'sudden crash'.")
q("myotx","What is the nurse's primary role in myocarditis?",
 ["*Prevent the 'sudden crash' with continuous telemetry and hemodynamic monitoring","Give anticoagulants to all clients || Not stated.","Teach the Sore Throat Rule || Rheumatic fever.","Draw ASO titers || Strep."],
 "Watch for SVT, V-tach, low MAP, low urine output, edema, daily weight, strict I&O.")
q("myotx","Which therapies are used for myocarditis? "+SATA,
 ["*Oxygen to keep SpO2 above 94%","*ACE inhibitor, beta blocker and diuretics","*Colchicine if the pericardium is involved","*AICD or LVAD for severe disease","Diltiazem for rate control || Avoid it."],
 "Antivirals only if a specific virus is identified early; IVIG or steroids for autoimmune forms.")

# ---------- pericarditis ----------
q("peri","A client has sharp chest pain that's worse lying flat and better sitting up and leaning forward. What is likely?",
 ["*Acute pericarditis","MI || Crushing pain relieved by nitroglycerin or rest.","Infective endocarditis || Fever and murmur.","Rheumatic fever || Migratory arthritis."],
 "Pericarditis pain is pleuritic and positional; it radiates to the left trapezius.")
q("peri","Which ECG finding is classic for acute pericarditis?",
 ["*Diffuse concave ST elevation with PR depression","Localized ST elevation || MI.","Sawtooth waves || Flutter.","Irregularly irregular rhythm || AFib."],
 "ECG is the gold standard; late T-wave inversion may follow.")
q("peri","Where and how does the nurse listen for a pericardial friction rub?",
 ["*Left lower sternal border with the diaphragm; scratchy and position-dependent","Apex with the bell; soft blowing || Not the rub description.","Over the carotid; a whoosh || That's a bruit.","Back of the lungs; wheeze || Not a rub."],
 "The rub is scratchy/grating and intermittent.")
q("peri","Which are causes or risk factors for pericarditis? "+SATA,
 ["*Recent MI (including Dressler syndrome)","*Viral infection such as coxsackie or influenza","*Kidney failure (uremia)","*Lupus or rheumatoid arthritis","*Recent heart surgery","Vitamin A deficiency || Not listed."],
 "Also idiopathic, males 20–50, TB, neoplasm, trauma.")
q("peri","What does a 'water-bottle heart' on chest x-ray suggest?",
 ["*A large pericardial effusion","Normal heart || Not normal.","Pneumonia || Not the cause.","Valve vegetation || Seen on echo, not x-ray shape."],
 "Echo shows effusion and tamponade risk.")

# ---------- pericarditis vs MI ----------
q("perimi","Which features favor pericarditis over MI? "+SATA,
 ["*Sharp, pleuritic pain","*Relief sitting up and leaning forward","*Diffuse ST elevation","*Friction rub","Crushing pressure relieved by nitroglycerin || MI."],
 "MI: crushing pain, relief with nitro/rest, localized ST elevation, S3/S4.")
q("perimi","A client with chest pain asks how the nurse knows it isn't a heart attack. Which explanation fits pericarditis?",
 ["*'Your pain changes with position and breathing, and your ECG changes are spread across many leads.'","'Heart attacks never cause chest pain.' || False.","'Your pain is relieved by nitroglycerin.' || That fits MI.","'Your ECG shows changes in only one area.' || Localized ST fits MI."],
 "Reassure and explain the difference to lower anxiety.")

# ---------- tamponade ----------
q("tamp","Which findings make up Beck's triad? "+SATA,
 ["*Hypotension","*JVD","*Muffled heart sounds","Bradycardia || Tamponade causes tachycardia.","Bounding pulses || Not part of the triad."],
 "Beck's triad = cardiac tamponade.")
q("tamp","A client with pericarditis has a BP that drops with each inspiration, muffled heart sounds and JVD. What is the priority?",
 ["*Prepare for emergency pericardiocentesis","Give an NSAID with yogurt and reassess || This is an emergency.","Start anticoagulation || Worsens bleeding into the sac.","Lay the client flat || Not the priority."],
 "Pulsus paradoxus + Beck's triad = tamponade.")
q("tamp","What is electrical alternans?",
 ["*Beat-to-beat variation in QRS size or direction seen with a large effusion or tamponade","Alternating P and T waves || Not the definition.","Normal finding || Concerning.","A pacemaker spike || Not related."],
 "Monitor for electrical alternans in pericarditis.")
q("tamp","What is the difference between pericardial effusion and tamponade?",
 ["*Effusion = fluid is present; tamponade = fluid compresses the heart and impairs filling","They're the same || Tamponade is the emergency.","Tamponade is chronic scarring || That's constrictive pericarditis.","Effusion is always an emergency || Tamponade is."],
 "Also watch tachycardia, low urine output and altered mental status.")

# ---------- constrictive ----------
q("constrict","What happens in chronic constrictive pericarditis?",
 ["*Repeated inflammation makes the pericardium thick and stiff like a corset, impairing filling","Fluid suddenly fills the sac || That's effusion/tamponade.","Valves grow vegetations || Endocarditis.","Heart muscle inflames after a virus || Myocarditis."],
 "It resembles diastolic heart failure; definitive treatment is pericardiectomy.")
q("constrict","Which findings fit constrictive pericarditis? "+SATA,
 ["*Right-sided heart failure signs","*JVD","*Hepatic engorgement","*Dependent edema","Janeway lesions || Endocarditis."],
 "Echo/CT shows a thickened pericardium.")
q("constrict","What is the definitive treatment for chronic constrictive pericarditis?",
 ["*Pericardiectomy","Pericardiocentesis || Needle drainage for tamponade.","Antibiotics for 4–6 weeks || Endocarditis.","Watchman || AFib device."],
 "Pericardiectomy removes the scarred sac so the heart can fill.")

# ---------- pericarditis treatment ----------
q("peritx","What is the first-line treatment for acute pericarditis?",
 ["*An NSAID plus colchicine","Anticoagulants || Avoid in the acute phase.","Penicillin || Rheumatic fever.","Diltiazem || Not the treatment."],
 "Prednisone if NSAIDs are contraindicated.")
q("peritx","Which teaching applies to NSAIDs for pericarditis?",
 ["*Take with food or yogurt to reduce stomach irritation","Take on an empty stomach || Raises ulcer risk.","Take with aspirin for extra effect || Avoid aspirin in pericarditis.","Stop as soon as pain eases on day 1 || Follow the prescribed course."],
 "Pain relief often begins within 48 hours.")
q("peritx","Why are anticoagulants avoided in acute pericarditis?",
 ["*Bleeding into the sac could cause tamponade","They cause a friction rub || Not the reason.","They raise the ESR || Not the reason.","They block colchicine || Not the reason."],
 "Hemorrhagic effusion can worsen into tamponade; also avoid aspirin per the nursing slide.")
q("peritx","Which preparations are needed for pericardiocentesis? "+SATA,
 ["*Code cart at the bedside","*Large-bore IV (16- or 18-gauge)","*Continuous cardiac monitoring","*Oxygen to keep SpO2 above 94%","Keep the client NPO for 3 days || Not stated."],
 "Ventricular arrhythmias can occur during the procedure.")
q("peritx","What does a pericardial window do?",
 ["*Removes part of the pericardium so fluid drains continuously","Removes the entire scarred pericardium || That's pericardiectomy.","Drains fluid once with a needle || That's pericardiocentesis.","Replaces a valve || Not related."],
 "Post-op: monitor for bleeding, infection, clots; PCA pain control; drain care.")

# ---------- pericarditis nursing ----------
q("perinurse","How should the nurse position a client with acute pericarditis for comfort?",
 ["*Upright and leaning forward, supported by pillows or an over-bed table","Flat on the back || Worsens pain.","Trendelenburg || Not appropriate.","Left side-lying flat || Not the position."],
 "Bed rest in the acute phase, then gradually increase activity.")
q("perinurse","Which assessments are priorities for a client with pericarditis? "+SATA,
 ["*Pain level, location and positional features","*Friction rub at the left sternal border","*Signs of tamponade such as pulsus paradoxus","*Electrical alternans on the monitor","Amsler grid || Eyes."],
 "Make all team members aware to avoid aspirin and anticoagulants.")
