# Week 2.3 Alterations in Male Sexual Function — lecture transcript, PowerPoint, notes.
EXAM = "e1"
T = "male"
CONCEPTS = {
 "defs":"Sexuality, sexual health & ED definitions",
 "physio":"Spark + flow: erection physiology",
 "incid":"Incidence & ED as a warning sign",
 "organic":"Organic causes",
 "psycho":"Psychogenic causes",
 "assess":"Sensitive history & assessment",
 "dx":"Diagnostic tests",
 "tx":"Treatment framework",
 "pde5":"PDE-5 inhibitors: action & timing",
 "pde5safe":"PDE-5 safety: nitrates, priapism, hearing & vision",
 "vad":"Vacuum assistive device",
 "inject":"Alprostadil injection & implants",
 "cbt":"Cognitive behavioral therapy",
 "nurse":"Nursing communication & team",
}
HI = ["pde5","pde5safe","organic","vad","dx"]

SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

# ---------- definitions ----------
q("defs","How does the lecture define erectile dysfunction?",
 ["*Persistent inability to develop and/or maintain an erection firm enough for intercourse","Ejaculation before it's desired || That's premature ejaculation.","An erection lasting over 4 hours || That's priapism.","Low sexual desire only || Not the definition."],
 "ED is persistent; one isolated episode isn't the definition.")
q("defs","Which statement about sexuality reflects the lecture?",
 ["*Sexuality has no age limit and its meaning differs from person to person","Sexuality ends after age 70 || No age limit.","Sexuality is only physical || It integrates physical, emotional and social well-being.","Nurses shouldn't discuss it || It's part of holistic care."],
 "Sexual health = physical, emotional, mental and social well-being. Use respectful, non-stigmatizing language.")
q("defs","What is priapism?",
 ["*An erection lasting more than 4 hours; a medical emergency","A normal side effect to ignore || It's an emergency.","An erection lasting 10 minutes || Not priapism.","Inability to have an erection || That's ED."],
 "Priapism needs immediate care to prevent permanent tissue damage.")

# ---------- physiology ----------
q("physio","What two things does an erection require?",
 ["*Nerve signals ('spark') and adequate blood flow ('flow')","Testosterone and estrogen only || Not the lecture framework.","Low blood pressure and high heart rate || Not the framework.","Muscle contraction only || Smooth muscle relaxes."],
 "No spark → neurologic problem. No flow → vascular/perfusion problem.")
q("physio","During arousal, what happens in the corpora cavernosa?",
 ["*The tissue relaxes, letting blood enter and engorge it","The tissue contracts to push blood out || Opposite.","Blood vessels constrict || They dilate.","Nothing changes || Relaxation is the key step."],
 "Nerve messages relax the inner tissue → blood fills the spaces → erection.")
q("physio","A client asks whether sildenafil will cause an erection without arousal. Best response?",
 ["*'No; it improves blood flow, but sexual stimulation is still needed.'","'Yes, it works automatically.' || It doesn't create arousal.","'Only if you take two.' || Never exceed the prescribed dose.","'Only with alcohol.' || Alcohol is avoided."],
 "PDE-5 inhibitors facilitate the flow response; they don't create arousal.")

# ---------- incidence ----------
q("incid","Why can ED be an early warning sign of cardiovascular disease?",
 ["*Smaller penile arteries may show atherosclerosis before the larger coronary arteries","ED causes heart disease || Not the relationship.","ED only happens in heart transplant clients || No.","It isn't linked to heart disease || It can be a sentinel marker."],
 "ED can also flag metabolic syndrome or neurologic impairment.")
q("incid","At what age range does ED incidence increase?",
 ["*Around 40–70","Only under 20 || Not the range.","Only after 90 || Not the range.","It never changes with age || It increases with age."],
 "Age brings more chronic disease and lower testosterone, but age isn't the only cause.")
q("incid","How can ED affect a client's overall care?",
 ["*It can affect confidence, relationships, quality of life and medication adherence","It has no effect beyond the bedroom || It affects well-being broadly.","It always improves adherence || It can reduce adherence.","It only affects older adults || All ages."],
 "Clients may stop antihypertensives or psychotropics because of ED side effects.")

# ---------- organic ----------
q("organic","Which are ORGANIC causes of ED? "+SATA,
 ["*Atherosclerosis and hypertension","*Diabetes","*Multiple sclerosis or spinal cord injury","*Prostatectomy or TURP","Performance anxiety || Psychogenic."],
 "Organic = vascular, neurologic, hormonal, medications, surgery/trauma, substances.")
q("organic","Which medications are listed as possible causes of ED? "+SATA,
 ["*Diuretics and beta blockers","*SSRIs","*Antipsychotics","Acetaminophen || Not listed."],
 "Antihypertensives and psychotropics are the main medication causes.")
q("organic","Which substances and lifestyle factors contribute to ED? "+SATA,
 ["*Smoking","*Alcohol","*Cocaine or marijuana","*Obesity","Regular exercise || Protective."],
 "Substances impair the spark and flow.")
q("organic","A client with diabetic neuropathy has ED. Which part of the pathway is affected?",
 ["*The nerve 'spark' (and often the vascular 'flow')","Only the psychological part || Neuropathy is organic.","Testosterone only || Not the main link.","None; diabetes doesn't affect ED || It does."],
 "Diabetes disrupts vascular and neurologic function.")

# ---------- psychogenic ----------
q("psycho","Which are PSYCHOGENIC causes of ED? "+SATA,
 ["*Anxiety or depression","*Performance anxiety","*Negative body image","*Relationship problems or stress","Hypertension || Organic."],
 "Psychogenic ED can happen even when nerves and vessels work normally.")
q("psycho","Before concluding ED is psychogenic, what must happen?",
 ["*Organic causes are ruled out","The client starts an SSRI || SSRIs can cause ED.","A penile implant is placed || Not first.","Nothing; assume it's psychological || Rule out physical causes first."],
 "Clinicians rule out physical causes before calling ED psychogenic.")

# ---------- assessment ----------
q("assess","Which questions belong in the symptom and sexual history? "+SATA,
 ["*When did the problem begin and what was happening then?","*Do you wake with morning or nighttime erections?","*Is it intermittent, global or situational?","*Is sexual desire still present?","Which sport do you play best? || Not relevant."],
 "Also ask about curvature, trauma, mental-health history and whether the concern is premature ejaculation.")
q("assess","Which physical assessments are part of an ED workup? "+SATA,
 ["*Weight/BMI and waist circumference","*Blood pressure","*Genital and vascular/neurologic exam as indicated","Visual acuity only || Not the focus."],
 "Use a holistic bio-psycho-social approach, not just a medication request.")
q("assess","Which history items are important to review for a client with ED? "+SATA,
 ["*Prior prostate or pelvic surgery or radiation","*Prescriptions, OTC drugs and substances","*Cardiovascular, endocrine and mental-health conditions","Favorite foods || Not relevant."],
 "Assess the relationship and sexual context without assumptions or stigma.")

# ---------- diagnostics ----------
q("dx","A client has 3–5 erections during sleep on a nocturnal penile tumescence test, normal labs and normal blood flow. What does this suggest?",
 ["*The physical 'machinery' works; consider a psychogenic cause","Severe vascular disease || Blood flow is normal.","Low testosterone || Labs are normal.","The test failed || 3–5 is normal."],
 "Normal nocturnal erections support a psychogenic cause after organic causes are excluded.")
q("dx","What does a penile Doppler ultrasound measure?",
 ["*Arterial blood flow after a vasoactive injection","Number of nighttime erections || That's nocturnal tumescence.","Testosterone level || That's a blood test.","Anxiety level || Not measured."],
 "Doppler measures arterial response.")
q("dx","When should serum testosterone be drawn if hypogonadism is suspected?",
 ["*In the morning, before 11 a.m.","At midnight || Not the lecture timing.","After a large meal || Not the timing.","Any time; timing never matters || Morning is preferred."],
 "Other labs: lipids, glucose or HbA1c, urine testing.")
q("dx","What is a limitation of the IIEF-5 questionnaire?",
 ["*It can't fully separate situational from global ED or reliably separate ED from premature ejaculation","It measures blood flow || It's a questionnaire.","It's the gold standard || It's an adjunct.","It requires an injection || It doesn't."],
 "The IIEF-5 is used for severity.")

# ---------- treatment ----------
q("tx","Which is the FIRST-line treatment for organic ED?",
 ["*A PDE-5 inhibitor with correct teaching","Inflatable penile implant || Used when less-invasive options fail.","Cognitive behavioral therapy || For psychogenic ED.","Vacuum device first in all clients || Used if medication is ineffective."],
 "Lifestyle and chronic-disease control come first in the framework.")
q("tx","A client's ED is from low testosterone. Which treatment fits?",
 ["*Hormone replacement as prescribed (topical, injection or urethral)","CBT only || For psychogenic.","Nitrates || Dangerous with PDE-5 and not an ED treatment.","No treatment exists || Hormone replacement is listed."],
 "Treat the physical cause.")
q("tx","Which lifestyle changes are part of ED treatment? "+SATA,
 ["*Weight loss and diet changes","*Smoking cessation","*Managing diabetes and heart health","*Limiting harmful substances","Starting daily alcohol || Alcohol impairs function."],
 "Management is usually multimodal.")

# ---------- PDE-5 ----------
q("pde5","Which drugs are PDE-5 inhibitors? "+SATA,
 ["*Sildenafil","*Tadalafil","*Vardenafil","*Avanafil","Alprostadil || An injected vasoactive drug."],
 "PDE-5 inhibitors relax penile smooth muscle to increase blood flow with stimulation.")
q("pde5","When should a client take sildenafil?",
 ["*About 1 hour before activity, avoiding large meals and alcohol","Immediately before activity with a heavy meal || Food slows it.","Three times daily || Lecture states one per day.","Only after waking up || Timing is before activity."],
 "Vardenafil and avanafil are also about 1 hour before.")
q("pde5","Which PDE-5 inhibitor can be taken daily and may last up to 36 hours?",
 ["*Tadalafil","Sildenafil || About 1 hour before activity.","Avanafil || About 1 hour before; lowest dyspepsia.","Vardenafil || About 1 hour before."],
 "Tadalafil can be daily or as required with about a 2-hour lead-in.")
q("pde5","A client says sildenafil 'didn't work' after one try. Best response?",
 ["*'It's recommended to try it on at least 6 separate occasions, with correct timing and stimulation.'","'Double the dose next time.' || Never exceed the maximum.","'It never works for anyone.' || Not true.","'Take it with nitroglycerin.' || Dangerous."],
 "Perceived failure is often an education failure.")
q("pde5","A client on sildenafil reports headache, facial flushing and nasal congestion. What should the nurse say?",
 ["*'These are expected effects from blood-vessel dilation.'","'Stop it immediately and go to the ER.' || These alone aren't emergencies.","'This means you're allergic.' || Not an allergy.","'This is priapism.' || Priapism is a prolonged erection."],
 "Expected vasodilation effects aren't a reason to stop on their own.")

# ---------- PDE-5 safety ----------
q("pde5safe","A client takes isosorbide (a nitrate) for angina and asks about tadalafil. What is the priority teaching?",
 ["*Never combine PDE-5 inhibitors with nitrates; life-threatening hypotension can occur","It's safe if taken 1 hour apart || Never combine.","Take a lower dose of both || Never combine.","It only causes a headache || The danger is severe hypotension."],
 "Also never combine with recreational 'poppers'; caution with other vasodilating antihypertensives.")
q("pde5safe","Which findings while on a PDE-5 inhibitor require emergency care? "+SATA,
 ["*Erection lasting more than 4 hours","*Sudden hearing loss","*Sudden vision loss","Mild facial flushing || Expected.","Nasal congestion || Expected."],
 "These are the three emergency warnings.")
q("pde5safe","Why is combining a PDE-5 inhibitor with poppers dangerous?",
 ["*Both cause vasodilation, leading to severe hypotension and syncope","It causes hypertension || Opposite.","It cancels the PDE-5 effect || Not the danger.","It causes hypoglycemia || Not the danger."],
 "Excessive vasodilation is life-threatening.")

# ---------- vacuum ----------
q("vad","How does a vacuum assistive device produce an erection?",
 ["*Suction draws blood into the penis; a band at the base maintains it","It injects medicine || That's alprostadil.","It's surgically implanted || That's an implant.","It stimulates nerves electrically || Not how it works."],
 "It's noninvasive.")
q("vad","What is the key safety teaching for the vacuum device?",
 ["*Remove the constriction band within 30 minutes","Leave the band on overnight || Causes ischemia.","Use it with nitrates || Not the rule.","Remove the band after 4 hours || Far too long."],
 "Longer use interrupts blood flow → ischemia and permanent injury.")

# ---------- injection & implants ----------
q("inject","Where is intracavernosal alprostadil injected?",
 ["*The penile shaft at the 10 o'clock or 2 o'clock position","The deltoid || Not the site.","The abdomen || Not the site.","The urethra || That's a suppository."],
 "It works rapidly, in about 10–15 minutes.")
q("inject","Which implant produces a permanent state of semi-erection?",
 ["*Semi-rigid (malleable) rod","Inflatable hydraulic implant || Pump-controlled.","Vacuum device || Not an implant.","Alprostadil || A medication."],
 "Inflatable = abdominal reservoir + scrotal pump, with a release valve.")
q("inject","Which statements about penile implants are correct? "+SATA,
 ["*They're surgical and irreversible","*They're used when less-invasive options are inadequate","*Teaching includes activation and release","They're first-line before trying medication || Medication comes first."],
 "Set realistic expectations.")

# ---------- CBT ----------
q("cbt","Which treatment is used for psychogenic ED once physical causes are ruled out?",
 ["*Cognitive behavioral therapy and sexual counseling","Inflatable implant || Organic, refractory ED.","Testosterone replacement || For low testosterone.","Vacuum device only || Not the psychogenic treatment."],
 "CBT changes thinking and behavior patterns.")
q("cbt","Which are parts of CBT for psychogenic ED? "+SATA,
 ["*Recognize distorted thoughts and unrealistic expectations","*Reframe thinking with a present-focused, problem-solving approach","*Build awareness, confidence and realistic expectations","Take a PDE-5 inhibitor with nitrates || Dangerous and not CBT."],
 "Several sessions may be needed.")

# ---------- nursing ----------
q("nurse","Which actions help the nurse discuss sexual function sensitively? "+SATA,
 ["*Provide privacy","*Use neutral language","*Ask permission before discussing it","*Include a partner if the client wants","Use slang to make it casual || Use respectful, non-stigmatizing language."],
 "Assess the whole person and the client's goals.")
q("nurse","A client stops his antihypertensive because of ED. What should the nurse do?",
 ["*Support adherence and discuss the side effect with the provider","Agree that stopping is fine || Unsafe for BP control.","Tell him to take double ED medication || Not appropriate.","Ignore it || Adherence matters."],
 "ED side effects can cause nonadherence to antihypertensive or psychotropic meds.")
q("nurse","Which team member addresses anxiety, depression and CBT for ED?",
 ["*Psychologist or therapist","General practitioner || Chronic-disease management.","Sexual-health specialist || Devices, surgery and specialized meds.","Pharmacist || Not listed in this lecture's team."],
 "The nurse handles sensitive assessment, teaching, safety screening, adherence and referrals.")
