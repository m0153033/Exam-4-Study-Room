# Week 10.1 Pharmacology: The Neurological System Part 1
# Sources: professor's PowerPoint (mechanisms, emphasis) + assigned ATI Pharmacology Made Easy tables (drug specifics).
T = "neuro"
CONCEPTS = {
 "nt":"Neurotransmitters, receptors & enzymes",
 "act":"Agonists, antagonists & enzyme inhibitors",
 "baclofen":"Baclofen (centrally acting)",
 "dantrolene":"Dantrolene & malignant hyperthermia",
 "szpatho":"Seizure pathophysiology & 3 treatment approaches",
 "phenytoin":"Phenytoin",
 "carbamaz":"Carbamazepine",
 "valproic":"Valproic acid",
 "oxcarb":"Oxcarbazepine",
 "local":"Local anesthesia: lidocaine",
 "general":"General anesthesia & sedation",
 "stim":"CNS stimulants for ADHD & narcolepsy",
 "modafinil":"Modafinil",
 "pdpatho":"Parkinson's: dopamine & the blood-brain barrier",
 "levodopa":"Levodopa/carbidopa",
 "pramipexole":"Pramipexole",
 "selegiline":"Selegiline, MAO-B & tyramine",
 "adpatho":"Alzheimer's disease & treatment goals",
 "donepezil":"Donepezil",
 "memantine":"Memantine",
 "ms":"Multiple sclerosis & interferon beta",
 "migraine":"Migraine & sumatriptan",
}
# Professor's slides drill these (matching activities, teaching prompts)
HI = ["phenytoin","carbamaz","valproic","stim","levodopa","ms","migraine"]

SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

# ---------- neurotransmitters ----------
q("nt","Which neurotransmitters are INHIBITORY (calming)? "+SATA,
 ["*GABA","*Glycine","*Serotonin",
  "Glutamate || Excitatory: the main one driving neurons to fire.",
  "Norepinephrine || Excitatory: fight-or-flight."],
 "Inhibitory decreases the chance a neuron fires. Excitatory: glutamate, epinephrine, norepinephrine, dopamine, acetylcholine, histamine.")
q("nt","Which neurotransmitter acts as the brain's 'brake pedal'?",
 ["Glutamate || The main excitatory neurotransmitter.","Dopamine || Coordinates smooth voluntary movement; reward.",
  "*GABA","Norepinephrine || Fight-or-flight."],
 "GABA produces a calming effect. Many seizure and anesthesia drugs work by increasing GABA.")
q("nt","Which enzyme breaks down acetylcholine?",
 ["Monoamine oxidase A || Breaks down serotonin, epinephrine and norepinephrine.",
  "Monoamine oxidase B || Breaks down dopamine and serotonin.",
  "*Acetylcholinesterase","Carbidopa || Carbidopa is a drug, not the enzyme."],
 "Enzymes end in -ase and break down or clean up neurotransmitters.")
q("nt","Which pairing of neurotransmitter and role is correct?",
 ["*Dopamine: coordinates smooth, voluntary movement",
  "GABA: fight-or-flight || That's norepinephrine.",
  "Glutamate: calming || Glutamate is excitatory (learning and memory).",
  "Acetylcholine: the body's natural pain reliever || That's endorphins."],
 "Acetylcholine triggers muscle contraction (PNS) and regulates attention, learning and memory (CNS). Endorphins are the body's natural pain relievers.")
q("nt","Which receptors receive epinephrine and norepinephrine?",
 ["Cholinergic || Receive acetylcholine.","*Adrenergic","NMDA || Glutamate receptors (memantine's target).","Dopaminergic || Receive dopamine."],
 "Receptors on neurons respond to specific neurotransmitters.")

# ---------- agonist / antagonist ----------
q("act","A medication binds to a receptor and mimics the natural neurotransmitter. What is it called?",
 ["Antagonist || Suppresses (blocks) the neurotransmitter's action.","*Agonist",
  "Enzyme inhibitor || Prevents breakdown of the neurotransmitter.","Precursor || A building block, like levodopa."],
 "Medications can stimulate (agonists), suppress (antagonists), or inhibit the enzyme that breaks a neurotransmitter down.")
q("act","Which drug works by inhibiting the enzyme that breaks down a neurotransmitter? "+SATA,
 ["*Donepezil","*Selegiline",
  "Memantine || An NMDA receptor antagonist.","Pramipexole || A dopamine receptor agonist.","Baclofen || A GABA agonist."],
 "Donepezil blocks acetylcholinesterase; selegiline blocks MAO-B (which breaks down dopamine).")
q("act","Memantine blocks NMDA glutamate receptors. Which category is it?",
 ["Agonist || Agonists stimulate.","*Antagonist","Enzyme inhibitor || It acts on the receptor, not an enzyme.","Dopamine precursor || Not related."],
 "Memantine is an NMDA receptor antagonist: it decreases excessive glutamate signaling.")

# ---------- baclofen ----------
q("baclofen","How does baclofen relieve muscle spasms?",
 ["Inhibits calcium release in the muscle fiber || That's dantrolene (peripheral).",
  "*Mimics GABA in the CNS and indirectly inhibits acetylcholine",
  "Blocks sodium influx into nerves || That's lidocaine.",
  "Increases dopamine in the brain || That's levodopa."],
 "Baclofen is a centrally acting muscle relaxant (prototype) for spasms of MS, spinal cord injury and cerebral palsy.")
q("baclofen","A client on oral baclofen wants to stop it today. What should the nurse teach?",
 ["Stopping abruptly is safe after 2 weeks || Don't stop abruptly.",
  "*Don't stop abruptly; taper over 1 to 2 weeks to prevent withdrawal",
  "Stop it if you get drowsy || Drowsiness decreases with time; avoid driving instead.",
  "Double the dose before stopping || Not taught."],
 "Oral withdrawal: psychosis, seizures. Intrathecal withdrawal: fever, confusion, rigidity, and can be fatal.")
q("baclofen","Which adverse effects should the nurse monitor for with baclofen? "+SATA,
 ["*Drowsiness and dizziness","*Constipation","*Urinary retention","*Weakness and fatigue early in therapy",
  "Gingival hyperplasia || That's phenytoin."],
 "Start low and go slow. Give oral doses with food or milk; increase fluids and fiber.")
q("baclofen","What teaching applies to both centrally and peripherally acting muscle relaxants?",
 ["*Start low and go slow; expect drowsiness",
  "Take at bedtime only || Not the shared teaching point.",
  "Eat a high-protein diet || That interferes with levodopa.",
  "Avoid sunlight || That's carbamazepine/oxcarbazepine."],
 "The professor's slide: 'Start low and go slow' and 'Drowsiness.' Avoid driving and CNS depressants like alcohol.")

# ---------- dantrolene ----------
q("dantrolene","Which medication is given IV to treat malignant hyperthermia?",
 ["Baclofen || Centrally acting; not used for malignant hyperthermia.","*Dantrolene",
  "Lidocaine || A local anesthetic.","Midazolam || A sedative."],
 "Malignant hyperthermia = calcium overload in skeletal muscle. Dantrolene inhibits calcium release in the muscle fiber.")
q("dantrolene","What is malignant hyperthermia?",
 ["A CNS infection causing high fever || Not the definition taught.",
  "*A pharmacogenetic skeletal-muscle disorder caused by calcium overload in muscle fibers",
  "Heat stroke from exercise || Not the definition taught.",
  "A reaction to sumatriptan || Not related."],
 "Peripheral (muscle) problem → peripherally acting dantrolene. Oral dantrolene can be given 1–2 days preop for prophylaxis.")
q("dantrolene","Which lab should the nurse monitor for a client on dantrolene?",
 ["Ammonia || That's valproic acid.","*Liver function tests","Sodium || That's oxcarbazepine.","Phenytoin level || Not related."],
 "Dantrolene can cause liver toxicity. Teach: report abdominal pain or jaundice. Contraindicated in liver disease.")
q("dantrolene","Which teaching is correct for oral dantrolene? "+SATA,
 ["*Report muscle weakness","*Avoid alcohol and other CNS depressants","*Report diarrhea","*Report jaundice or abdominal pain",
  "Take with a high-protein meal || That's a levodopa interaction."],
 "Assess muscle strength frequently. Estrogen use raises the liver toxicity risk in women over 35.")

# ---------- seizure patho ----------
q("szpatho","According to the lecture, what imbalance causes seizures?",
 ["Too little glutamate and too much GABA || Reversed.",
  "*Too much glutamate, too little GABA, and rising cellular sodium",
  "Too much dopamine || That's not the seizure model taught.",
  "Too little acetylcholine || That's the Alzheimer's model."],
 "Seizures = abnormal, excessive, synchronous electrical discharges from excitation/inhibition imbalances and sodium imbalances.")
q("szpatho","Which are the three ways seizure medications work, per the lecture? "+SATA,
 ["*Decrease available glutamic acid","*Increase available GABA","*Inhibit sodium influx into the cell",
  "Increase dopamine || Parkinson's approach.","Block calcium release in muscle || Dantrolene's approach."],
 "Prototypes: oxcarbazepine (less glutamate); valproic acid (more GABA); hydantoins, carbamazepine, valproic acid and oxcarbazepine (block sodium influx).")
q("szpatho","During depolarization, what moves into the nerve cell?",
 ["Potassium || Not the ion described in the lecture.","*Sodium","Calcium || Calcium matters in muscle contraction.","Chloride || Not the ion described."],
 "Resting cell is negative inside; sodium (+) rushes in to depolarize and create an action potential, then moves back out (repolarization).")

# ---------- phenytoin ----------
q("phenytoin","Which side effect is unique to phenytoin?",
 ["*Gingival hyperplasia","Increased ammonia || Valproic acid.","Bone marrow suppression || Carbamazepine.","Hyponatremia || Oxcarbazepine (especially with diuretics)."],
 "Phenytoin (hydantoin) causes overgrowth of gum tissue.")
q("phenytoin","Which nursing care is specific to phenytoin?",
 ["Monitor WBC count || Carbamazepine.","Monitor for hepatitis or pancreatitis || Valproic acid.",
  "*Regular dental checkups, soft toothbrush, gum massage and flossing","Last dose by noon || Selegiline."],
 "Matches the professor's slide: hydantoins → regular dental checkups.")
q("phenytoin","A client's phenytoin level is 32 mcg/mL. How should the nurse interpret this?",
 ["Therapeutic || Therapeutic range is 10–20 mcg/mL.",
  "*Toxic; notify the provider",
  "Too low; give an extra dose || The level is high.",
  "Normal for IV dosing || Range is the same."],
 "Narrow therapeutic range 10–20 mcg/mL; levels over 30 can be toxic.")
q("phenytoin","Which teaching is correct for phenytoin? "+SATA,
 ["*Don't stop it abruptly","*Report a rash","*Don't drive if drowsy","*It can decrease the effectiveness of oral contraceptives",
  "Mix IV phenytoin with dextrose || IV phenytoin is incompatible with dextrose."],
 "Discontinue if rash occurs (SJS risk). Give with meals. Inject IV slowly; monitor VS for dysrhythmias and hypotension.")
q("phenytoin","During IV phenytoin, what should the nurse monitor?",
 ["*Vital signs and cardiac rhythm, for dysrhythmias and hypotension",
  "Blood glucose only || Not the IV priority.",
  "Urine color || Darkened urine is levodopa.",
  "Gag reflex || Not related."],
 "Inject slowly with the correct dilution; it's incompatible with dextrose and many other drugs.")

# ---------- carbamazepine ----------
q("carbamaz","Which side effect is the main concern with carbamazepine, per the lecture's matching activity?",
 ["Gingival hyperplasia || Phenytoin.","*Bone marrow suppression","Increased ammonia || Valproic acid.","Darkened urine || Levodopa."],
 "Carbamazepine → monitor WBC/CBC throughout therapy; withhold for low counts.")
q("carbamaz","A client on carbamazepine should report which findings? "+SATA,
 ["*Fever","*Sore throat","*Easy bruising","*A rash",
  "Gum overgrowth || Phenytoin."],
 "Fever, sore throat and bruising suggest low blood counts. Severe rash/SJS can occur.")
q("carbamaz","Which teaching is correct for carbamazepine? "+SATA,
 ["*Use sunscreen and protect from the sun","*Avoid grapefruit juice","*It may make oral contraceptives less effective",
  "*Swallow sustained-release forms whole",
  "It's safe in pregnancy || It's teratogenic."],
 "Grapefruit juice raises carbamazepine levels. Give much of the daily dose at bedtime to limit daytime side effects.")
q("carbamaz","Before starting carbamazepine, a client of Asian descent may be tested for what?",
 ["Phenytoin level || Not related.","*The HLA-B*1502 gene, which raises the risk of severe skin reactions",
  "Ammonia level || Valproic acid.","Tyramine sensitivity || Not related."],
 "Severe skin reactions (SJS, epidermal necrolysis) are a major concern with carbamazepine.")

# ---------- valproic acid ----------
q("valproic","Which nursing care is specific to valproic acid?",
 ["Regular dental checkups || Phenytoin.","*Monitor for hepatitis and pancreatitis","Monitor WBC count || Carbamazepine.","Monitor sodium || Oxcarbazepine."],
 "Matches the professor's slide. Liver toxicity may be fatal; monitor LFTs before and during therapy.")
q("valproic","A client on valproic acid is vomiting and newly confused with a decreased level of consciousness. What should the nurse suspect?",
 ["*Hyperammonemia","Hyponatremia from diuretics || That's oxcarbazepine.","Gingival hyperplasia || Phenytoin.","Serotonin syndrome || Not the valproic acid concern."],
 "Valproic acid raises ammonia. Monitor blood ammonia; report vomiting, confusion, or decreased LOC.")
q("valproic","Which findings should a client on valproic acid report? "+SATA,
 ["*Abdominal pain with nausea and vomiting","*Jaundice","*Bruising or bleeding","*Confusion or drowsiness",
  "Darkened sweat || Levodopa."],
 "Pancreatitis (abdominal pain, N/V), liver toxicity (jaundice, anorexia), low platelets (bruising, bleeding), hyperammonemia (confusion).")
q("valproic","A client on valproic acid plans a pregnancy. What does the nurse know?",
 ["It's the safest seizure medicine in pregnancy || It's teratogenic.",
  "*It can cause neural tube defects; the client should contact the provider, and folic acid is given",
  "Stop it abruptly once pregnant || Never stop seizure medicines abruptly; contact the provider.",
  "It only matters in the third trimester || Neural tube defects occur early."],
 "Contraindicated: pregnancy, liver disorders, thrombocytopenia.")
q("valproic","Which labs should the nurse monitor for valproic acid? "+SATA,
 ["*Platelet count and bleeding time","*Liver function tests","*Ammonia level","*Serum amylase if symptoms occur",
  "Phenytoin level only || Valproic acid raises phenytoin levels, but that isn't its own monitoring."],
 "Give with food and use enteric-coated forms to reduce GI upset.")

# ---------- oxcarbazepine ----------
q("oxcarb","A client on oxcarbazepine and a diuretic is confused with a headache. Which lab should the nurse check first?",
 ["Ammonia || Valproic acid.","*Sodium","Phenytoin level || Not related.","Glucose || Not the oxcarbazepine concern."],
 "Oxcarbazepine can cause hyponatremia, especially with diuretics. Monitor Na and WBC.")
q("oxcarb","Which teaching is correct for oxcarbazepine? "+SATA,
 ["*Use additional birth control if taking oral contraceptives","*Limit sun exposure and wear protective clothing","*Report a rash",
  "It's fine for clients allergic to carbamazepine || Contraindicated with carbamazepine allergy."],
 "Adverse effects include dizziness, ataxia, vision changes, SJS, leukopenia and hyponatremia. Start low and increase gradually.")
q("oxcarb","Oxcarbazepine is the lecture's prototype for which seizure approach?",
 ["Increasing GABA || Valproic acid is the prototype.","*Decreasing available glutamic acid (and also blocking sodium influx)",
  "Increasing dopamine || Not a seizure approach.","Blocking calcium in muscle || Dantrolene."],
 "Oxcarbazepine is a second/third-generation ASM.")

# ---------- local anesthesia ----------
q("local","How does lidocaine produce local anesthesia?",
 ["*Blocks the influx of sodium into nerves",
  "Increases GABA || General anesthesia agents do this.",
  "Depresses the entire CNS || General anesthesia.",
  "Blocks dopamine receptors || Not related."],
 "No sodium in = no action potential = no pain signal locally.")
q("local","Why is lidocaine with epinephrine avoided in fingers, toes and the nose?",
 ["It wears off too quickly there || Epinephrine prolongs anesthesia.",
  "*Vasoconstriction can cause gangrene in end-artery sites",
  "It causes gingival hyperplasia || Phenytoin.",
  "It causes hyperammonemia || Valproic acid."],
 "Epinephrine increases the duration of anesthesia but can cut off blood flow in end-artery sites.")
q("local","A client has spinal anesthesia with lidocaine and becomes hypotensive. What should the nurse do first?",
 ["Raise the head of the bed || Lower the head of the bed.","*Lower the head of the bed",
  "Give naloxone || Reverses opioids, not lidocaine.","Encourage oral fluids only || Not the first action."],
 "If hypotension continues, prepare to give ephedrine or phenylephrine. Monitor for CNS effects and respiratory status.")
q("local","Which findings suggest lidocaine CNS toxicity? "+SATA,
 ["*Dizziness and restlessness","*Tremors","*Confusion and paresthesia","*Seizures",
  "Gum overgrowth || Phenytoin."],
 "CNS stimulation can be followed by depression (respiratory arrest). Don't apply topical lidocaine to broken skin.")

# ---------- general anesthesia ----------
q("general","How do general anesthesia agents such as barbiturates, benzodiazepines and opioids work, per the lecture?",
 ["Block sodium influx at one nerve || That's local anesthesia.",
  "*Depress the CNS and increase GABA",
  "Increase dopamine || Not the mechanism.","Inhibit acetylcholinesterase || Not the mechanism."],
 "Used for anesthesia induction or conscious sedation.")
q("general","A client receives midazolam for an endoscopy and can't remember the procedure. What should the nurse explain?",
 ["A stroke occurred || Amnesia is an expected effect.","*Memory loss is an expected effect of the medication",
  "The client was under general anesthesia || Midazolam gives conscious sedation.","Naloxone will restore memory || Not used for this."],
 "Midazolam: inject IV bolus slowly and wait at least 2 minutes before a second dose. Watch for respiratory or cardiac arrest.")
q("general","During procedural sedation with fentanyl, what must be at the bedside?",
 ["Flumazenil only || Fentanyl is an opioid.","*Naloxone and resuscitation equipment",
  "Dantrolene only || For malignant hyperthermia.","Vitamin K || Not related."],
 "Fentanyl adverse effects: sedation, nausea, respiratory and circulatory depression.")
q("general","What is the PRIORITY assessment during and after conscious sedation?",
 ["Pain score || Important, but not the top priority.",
  "*Airway and respiratory status",
  "Bowel sounds || Not the priority.",
  "Urine color || Not the priority."],
 "Barbiturates (methohexital), benzodiazepines (midazolam) and opioids (fentanyl) can all cause respiratory depression; additive CNS depressants raise the risk.")
q("general","Which statements about methohexital are correct? "+SATA,
 ["*It's a short-acting barbiturate for rapid induction","*It can cause respiratory depression or apnea","*It's given IV only",
  "*Prevent intra-arterial injection and extravasation",
  "It can be given safely with midazolam to deepen sedation || Considered duplicate therapy; prolongs anesthesia."],
 "Monitor respiratory status and vital signs before, during and after.")

# ---------- stimulants ----------
q("stim","How do CNS stimulants such as methylphenidate treat ADHD?",
 ["Block reuptake of serotonin only || Not the mechanism taught.",
  "*Increase dopamine and norepinephrine in the brain",
  "Increase GABA || Calming, not stimulating.","Block dopamine receptors || That would worsen focus."],
 "Restores neurotransmitter balance; provides energy, focus, alertness. High potential for misuse.")
q("stim","Which adverse effects should the nurse assess for with a CNS stimulant? "+SATA,
 ["*Increased BP and heart rate","*Insomnia","*Nervousness","*Poor appetite and weight loss",
  "Bradycardia || Stimulants raise the heart rate."],
 "Also palpitations. In children, monitor height and weight; medication holidays may prevent growth suppression.")
q("stim","Which teaching applies to a CNS stimulant? "+SATA,
 ["*Take it in the morning (last dose of methylphenidate by 4 p.m.)","*Avoid caffeine","*Don't stop abruptly; taper",
  "*Tolerance and misuse can develop",
  "Take it at bedtime for best absorption || Causes insomnia."],
 "Matches the professor's slide. Also monitor appetite/weight and report palpitations or hypertension.")
q("stim","A parent says their child's methylphenidate makes him skip lunch. What should the nurse suggest?",
 ["Stop the medication || Don't stop without the provider.",
  "*Plan the largest meals for when appetite is greatest, and monitor weight and height",
  "Give it at bedtime || Causes insomnia.","Add caffeine to boost appetite || Avoid caffeine."],
 "Report anorexia and weight loss to the provider.")
q("stim","A client stops methylphenidate suddenly. What should the nurse monitor for?",
 ["Gingival hyperplasia || Phenytoin.","*Depression and fatigue (withdrawal)","Hyperammonemia || Valproic acid.","Malignant hyperthermia || Not related."],
 "Taper when discontinuing.")
q("stim","Which conditions are contraindications for methylphenidate? "+SATA,
 ["*Use of an MAOI within 2 weeks","*Glaucoma","*Motor tics or Tourette's","*History of substance use disorder",
  "Narcolepsy || Narcolepsy is an indication for CNS stimulants."],
 "Also cardiac dysrhythmias, structural defects, psychosis, mania and children under 6.")
q("stim","Which instruction is correct for a methylphenidate transdermal patch?",
 ["Apply at bedtime || Apply in the morning.","*Apply in the morning, wear no more than 9 hours, and use a new site daily",
  "Apply over a rash to absorb faster || Don't apply on rash or inflamed skin.","Leave on for 24 hours || Maximum 9 hours."],
 "Sustained-release oral forms must be swallowed whole.")

# ---------- modafinil ----------
q("modafinil","How does modafinil differ from CNS stimulants, per the lecture?",
 ["It has a higher potential for misuse || Lower potential for misuse.",
  "*It blocks norepinephrine reuptake, promotes wakefulness, and has low misuse potential",
  "It increases GABA || Not its mechanism.","It's only for children || Used for shift workers and adults."],
 "Modafinil is a non-CNS stimulant, frequently prescribed for shift workers.")
q("modafinil","A woman on oral contraceptives starts modafinil. What teaching is essential?",
 ["No change is needed || It decreases contraceptive effectiveness.",
  "*Use a backup method (such as condoms) during use and for 30 days after stopping",
  "Take it at bedtime || Take in the morning or 1 hour before work.","Double the contraceptive dose || Not taught."],
 "Modafinil is contraindicated in pregnancy and valvular heart disease.")
q("modafinil","When should a shift worker take modafinil?",
 ["At bedtime || Promotes wakefulness.","*1 hour before work","Only on days off || Not taught.","With the evening meal || Not tied to a meal."],
 "For narcolepsy and sleep apnea, give in the morning.")
q("modafinil","Which findings should a client on modafinil report? "+SATA,
 ["*Palpitations or chest pain","*A rash","*Headache, nervousness or dizziness",
  "Darkened urine || Levodopa.","Gum overgrowth || Phenytoin."],
 "Rash includes Stevens-Johnson syndrome; discontinue modafinil. Monitor vital signs for tachycardia and hypertension.")

# ---------- Parkinson's patho ----------
q("pdpatho","What causes the tremors, rigidity and slow movement of Parkinson's disease?",
 ["Too much dopamine || Dopamine is lost.",
  "*Loss of dopamine-producing neurons, leaving more acetylcholine than dopamine",
  "Destruction of myelin || That's MS.","Amyloid plaques || Alzheimer's."],
 "Muscle function needs a dopamine/acetylcholine balance; dopamine inhibits motor movement while acetylcholine stimulates it.")
q("pdpatho","True or false: Parkinson's is treated by giving dopamine itself.",
 ["True; dopamine replaces what's lost || Extrinsic dopamine can't cross the BBB.",
  "*False; dopamine can't cross the blood-brain barrier, so its precursor levodopa is given"],
 "Levodopa crosses the BBB and converts to dopamine in the brain.")
q("pdpatho","Why is carbidopa combined with levodopa?",
 ["It increases levodopa's conversion in the bloodstream || It prevents that conversion.",
  "*It stops levodopa from converting to dopamine before it reaches the brain",
  "It blocks MAO-B || That's selegiline.","It stimulates dopamine receptors directly || That's pramipexole."],
 "Without carbidopa, levodopa converts to dopamine in the blood, and dopamine can't get into the brain.")
q("pdpatho","Which are the three ways to support dopamine in Parkinson's? "+SATA,
 ["*Give the precursor levodopa (with carbidopa)","*Mimic dopamine with a receptor agonist (pramipexole)",
  "*Block the enzyme that breaks dopamine down (selegiline)",
  "Give IV dopamine || Can't cross the BBB.","Give an acetylcholinesterase inhibitor || That's Alzheimer's."],
 "Make more, mimic it, or prevent its breakdown.")

# ---------- levodopa ----------
q("levodopa","A client on levodopa/carbidopa notices dark urine and sweat. What should the nurse say?",
 ["Stop the medication now || Expected and harmless.","*This is an expected effect of the medication",
  "It's a sign of liver failure || Not with this drug.","Go to the emergency department || Not needed."],
 "Warn clients ahead of time that urine and sweat may darken.")
q("levodopa","Which teaching is correct for levodopa/carbidopa? "+SATA,
 ["*Avoid high-protein meals around doses","*Move slowly to sitting and standing","*Report dyskinesias",
  "*Full response can take up to 6 months",
  "Take vitamin B6 supplements || B6 decreases its action."],
 "High protein decreases absorption. Orthostatic hypotension raises fall risk.")
q("levodopa","A client's Parkinson's symptoms return a couple of hours before each dose. What may help?",
 ["*Giving doses 4 times a day instead of 3, or switching to controlled-release",
  "Stopping the medication || Not appropriate.",
  "A high-protein snack with each dose || Decreases absorption.",
  "Adding vitamin B6 || Decreases levodopa action."],
 "On-off episodes and wearing off: report to the provider. Adding a dopamine agonist, COMT inhibitor or MAO-B inhibitor may also help.")
q("levodopa","Which drug is contraindicated within 2 weeks of levodopa/carbidopa because it can cause a hypertensive crisis?",
 ["Amantadine || Used to decrease dyskinesias.","*An MAOI antidepressant",
  "Pramipexole || Added to help on-off.","Acetaminophen || Not an interaction."],
 "Also contraindicated: angle-closure glaucoma, history of melanoma, psychosis.")

# ---------- pramipexole ----------
q("pramipexole","Which adverse effect of pramipexole poses the biggest safety risk while driving?",
 ["Darkened urine || Levodopa.","*Sudden 'sleep attacks'","Gingival hyperplasia || Phenytoin.","Hyperammonemia || Valproic acid."],
 "Avoid driving or activities needing alertness if drowsy. Avoid alcohol and CNS depressants.")
q("pramipexole","How does pramipexole work?",
 ["*Directly stimulates dopamine receptors, mimicking dopamine",
  "Converts to dopamine in the brain || That's levodopa.","Blocks MAO-B || That's selegiline.","Blocks NMDA receptors || That's memantine."],
 "Direct-acting dopamine receptor agonist; also used for restless leg syndrome.")
q("pramipexole","When should pramipexole be taken for restless leg syndrome?",
 ["In the morning || Not for RLS.","*2–3 hours before bedtime","At noon || Not the instruction.","Only during symptoms || Taken on schedule."],
 "When stopping, taper slowly over 1 week. When increasing, allow 5–7 days between increases.")
q("pramipexole","Which adverse effects should the nurse monitor for with pramipexole? "+SATA,
 ["*Nausea","*Orthostatic hypotension","*Dyskinesias","*Muscle weakness",
  "Bradycardia from cholinesterase inhibition || That's donepezil."],
 "Nausea can lessen over time; take with food if it occurs.")

# ---------- selegiline ----------
q("selegiline","How does selegiline help in Parkinson's disease?",
 ["*Blocks MAO-B, the enzyme that breaks down dopamine in the brain",
  "Mimics GABA || Baclofen.","Is converted into dopamine || Levodopa.","Blocks acetylcholine breakdown || Donepezil."],
 "Given with levodopa/carbidopa so the levodopa dose can be reduced.")
q("selegiline","When should a client take the last dose of selegiline each day?",
 ["At bedtime || It causes insomnia.","*By noon","With the evening meal || Too late.","Any time || Timing matters for sleep."],
 "Give before the morning meal; with the ODT form, nothing to eat or drink 5 minutes before or after.")
q("selegiline","Why must clients on MAO inhibitors be careful with aged cheese and fermented meats?",
 ["They cause hypoglycemia || Not the concern.",
  "*They contain tyramine, which can build up and cause a hypertensive crisis",
  "They block levodopa absorption || That's high protein.","They cause gingival hyperplasia || Phenytoin."],
 "MAOIs also inhibit the enzyme that metabolizes tyramine. Selegiline is less likely to cause this than other MAOIs, but foods should still be reviewed.")
q("selegiline","Which drugs interact dangerously with selegiline? "+SATA,
 ["*Meperidine","*SSRI or tricyclic antidepressants","*St. John's wort or ephedra",
  "Acetaminophen || Not a listed interaction."],
 "Meperidine and other opioids, MAOIs, TCAs or SSRIs can cause high fever, hypertension and rigidity. Clients should check with the provider before any new medication.")

# ---------- Alzheimer's ----------
q("adpatho","Which brain changes characterize Alzheimer's disease? "+SATA,
 ["*Amyloid plaques","*Neurofibrillary tangles","*Brain shrinkage","*Low acetylcholine and high glutamate",
  "Destroyed myelin sheath || That's MS."],
 "Cause unknown; progressive and ultimately fatal. The goal is symptom management.")
q("adpatho","A client prescribed memantine asks what the medication will do. Which statement should the nurse include?",
 ["\"Your disease will keep improving the longer you take it.\" || The disease is progressive.",
  "*\"It will slow the decline of your thinking and physical function.\"",
  "\"It will reverse the damage to your brain cells.\" || Can't reverse degeneration.",
  "\"It will dissolve the calcium plaques.\" || Doesn't dissolve plaques."],
 "From the professor's slide: Alzheimer's can be slowed and symptoms managed, but it is ultimately fatal.")
q("adpatho","What are the two medication approaches for Alzheimer's disease? "+SATA,
 ["*Increase acetylcholine with a cholinesterase inhibitor (donepezil)","*Decrease glutamate with an NMDA receptor antagonist (memantine)",
  "Increase dopamine with levodopa || Parkinson's.","Suppress the immune system with interferon || MS."],
 "Excess glutamate causes calcium dysregulation, which leads to plaque formation and cell damage.")

# ---------- donepezil ----------
q("donepezil","Which adverse effect of donepezil should the nurse monitor by checking the heart rate?",
 ["Tachycardia || Donepezil slows the heart.","*Bradycardia","Hypertensive crisis || MAOIs.","Gingival hyperplasia || Phenytoin."],
 "Report temporary loss of consciousness. Keep the client safe from falls if dizzy.")
q("donepezil","When is donepezil usually given?",
 ["In the morning on an empty stomach || Not the ATI instruction.","*At bedtime, with food to reduce GI effects",
  "By noon || Selegiline.","Only as needed || Daily."],
 "Monitor weight; report vomiting, severe diarrhea or weight loss.")
q("donepezil","A client on donepezil takes daily ibuprofen. What should the nurse monitor for?",
 ["*GI bleeding: dark stools or coffee-ground emesis",
  "Hyponatremia || Oxcarbazepine.","Malignant hyperthermia || Not related.","Sleep attacks || Pramipexole."],
 "NSAIDs increase the GI bleeding risk with donepezil; GI bleeding is a contraindication.")
q("donepezil","Which medication decreases the effect of donepezil?",
 ["*Antihistamines (anticholinergics)","Acetaminophen || Not listed.","Folic acid || Not listed.","Furosemide || Not listed."],
 "Anticholinergics work against a drug that increases acetylcholine.")

# ---------- memantine ----------
q("memantine","How does memantine work?",
 ["Increases acetylcholine || Donepezil.",
  "*Blocks NMDA receptors, decreasing calcium influx into neurons",
  "Increases dopamine || Levodopa.","Suppresses leukocytes || MS drugs."],
 "Less calcium influx inhibits plaque formation and brain cell damage. Used for moderate to severe Alzheimer's.")
q("memantine","Which adverse effects of memantine should the caregiver report? "+SATA,
 ["*Dizziness","*Headache","*Increased confusion",
  "Darkened urine || Levodopa.","Gum overgrowth || Phenytoin."],
 "Keep the client safe if dizzy. Renal failure is a contraindication.")
q("memantine","Which interaction raises memantine to toxic levels?",
 ["*Antacids like sodium bicarbonate that increase urine pH","Grapefruit juice || Carbamazepine.",
  "High-protein meals || Levodopa.","Aged cheese || MAOIs."],
 "Memantine can be given with or without food.")

# ---------- MS ----------
q("ms","What is multiple sclerosis?",
 ["*An autoimmune disease in which leukocytes destroy CNS myelin, with remissions and exacerbations",
  "A loss of dopamine-producing neurons || Parkinson's.",
  "Amyloid plaques and tangles || Alzheimer's.","A calcium overload in muscle || Malignant hyperthermia."],
 "Deficits: muscle weakness, tingling and numbness, impaired vision, incontinence, cognitive impairment.")
q("ms","What is the difference between immunomodulators and immunosuppressants?",
 ["They're the same || The lecture distinguishes them.",
  "*Immunomodulators normalize the immune response; immunosuppressants suppress it",
  "Immunomodulators increase leukocyte damage || Both inhibit damaging leukocyte effects.",
  "Immunosuppressants only treat migraines || Not related."],
 "Both work by inhibiting the damaging effects of leukocytes. Prototypes: interferon beta-1a and beta-1b.")
q("ms","A client on interferon beta reports easy bruising, fatigue and frequent infections. What should the nurse suspect?",
 ["Expected flu-like symptoms || Those are fever and aches.","*Myelosuppression (bone marrow suppression)",
  "Hyperammonemia || Valproic acid.","Malignant hyperthermia || Not related."],
 "Anemia → fatigue, dyspnea. Neutropenia → infection risk. Thrombocytopenia → bleeding risk.")
q("ms","Which should the nurse monitor for a client on interferon beta? "+SATA,
 ["*CBC: platelets, RBC, WBC","*Liver function tests","*Temperature","*Injection sites",
  "Phenytoin level || Not related."],
 "The professor's slide also lists ammonia. Hepatotoxicity: jaundice, anorexia, abdominal tenderness.")
q("ms","Match the blood count problem to its risk: neutropenia causes an increased risk for what?",
 ["Bleeding || Thrombocytopenia.","*Infection","Dyspnea || Anemia.","Hypertension || Not related."],
 "Anemia → dyspnea and fatigue; thrombocytopenia → bleeding.")
q("ms","Which teaching is correct for interferon beta? "+SATA,
 ["*Premedicate with acetaminophen for flu-like symptoms","*Rotate injection sites","*Cool compress before, warm moist compress after injection",
  "*Report easy bruising, bleeding or fatigue",
  "Flu-like symptoms will get worse over time || They decrease with prolonged treatment."],
 "Beta-1a: IM weekly or SUBQ 3 times a week, late in the day, 48 hours apart. Beta-1b: SUBQ every other day.")

# ---------- migraine ----------
q("migraine","What is the goal of migraine treatment, per the lecture?",
 ["Dilate the blood vessels || Migraine already involves dilation.",
  "*Constrict and reduce inflammation of the blood vessels",
  "Increase GABA || Not the lecture's goal.","Block dopamine || Not the lecture's goal."],
 "Migraine pathophysiology: dilation and inflammation of blood vessels. Sumatriptan activates serotonin receptors to constrict them.")
q("migraine","A client takes sumatriptan and reports chest tightness spreading to the jaw that doesn't go away. What should the nurse do?",
 ["Reassure them it's an expected side effect || Persistent chest pressure can mean coronary vasospasm.",
  "*Treat it as possible angina from coronary vasospasm and notify the provider at once",
  "Give a second dose || Don't repeat with chest symptoms.","Have them lie flat and sleep || Delays needed care."],
 "Vasoconstriction in the heart = angina = ischemia. Teach: notify the provider at once for chest, back, jaw or throat tightness that doesn't resolve.")
q("migraine","In which clients is sumatriptan contraindicated? "+SATA,
 ["*Coronary artery disease or previous MI","*Severe hypertension","*Peripheral vascular disease","*History of stroke",
  "Tension headache only || Not a listed contraindication."],
 "Also contraindicated: an MAOI within 2 weeks or another triptan within 24 hours.")
q("migraine","A client took oral sumatriptan 2 hours ago with no relief. What is correct?",
 ["*They may repeat one oral dose; maximum 200 mg in 24 hours",
  "They may take another dose every 30 minutes || Not the ATI instruction.",
  "They should take ergotamine now || Avoid ergotamine within 24 hours.","Sumatriptan can't be repeated || One repeat is allowed after 2 hours."],
 "SUBQ: repeat once after 1 hour if no relief, no more than 2 doses in 24 hours. Nasal: may repeat after 2 hours.")
q("migraine","What is sumatriptan used for?",
 ["*Relieving an existing migraine or cluster headache",
  "Daily migraine prevention || It's for acute attacks.","Seizure prevention || Not its use.","Muscle spasm || Not its use."],
 "Valproic acid is an example of a drug that can prevent migraines.")
q("migraine","Which drug combination with sumatriptan can cause serotonin syndrome?",
 ["*Other serotonin agonists or St. John's wort","Acetaminophen || Not a listed interaction.","Folic acid || Not listed.","Antacids || Memantine interaction."],
 "MAOIs within 2 weeks can cause sumatriptan toxicity.")
