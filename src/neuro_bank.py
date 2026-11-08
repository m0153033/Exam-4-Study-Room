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
# VERSION 2 (Nov 8): every question re-worded with new scenarios/distractors.
# Professor's slides drill these (matching activities, teaching prompts)
# Student review #2 (Nov 4): seizures focus on phenytoin.
HI = ["phenytoin","carbamaz","valproic","stim","levodopa","ms","migraine"]

SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

# ---------- neurotransmitters ----------
q("nt","Which neurotransmitters CALM the nervous system (inhibitory)? "+SATA,
 ["*GABA","*Glycine","*Serotonin","Glutamate || Excitatory.","Epinephrine || Excitatory."],
 "Excitatory: glutamate, epinephrine, norepinephrine, dopamine, acetylcholine, histamine.")
q("nt","Which neurotransmitter is the main 'gas pedal' that makes neurons fire?",
 ["*Glutamate","GABA || The brake pedal.","Glycine || Inhibitory.","Serotonin || Inhibitory."],
 "Too much glutamate and too little GABA can lead to seizures.")
q("nt","Many seizure and anesthesia drugs work by increasing which calming neurotransmitter?",
 ["*GABA","Glutamate || Excitatory.","Dopamine || Movement and reward.","Histamine || Excitatory."],
 "GABA is the brain's brake pedal.")
q("nt","Which enzyme breaks down acetylcholine?",
 ["*Acetylcholinesterase","MAO-B || Breaks down dopamine.","MAO-A || Breaks down serotonin and norepinephrine.","Carbidopa || A drug, not an enzyme."],
 "Enzymes end in -ase.")
q("nt","Which neurotransmitter and role are matched correctly?",
 ["*Acetylcholine: muscle contraction and memory","Dopamine: fight-or-flight || Norepinephrine.","GABA: excites neurons || It calms them.","Endorphins: smooth movement || Dopamine."],
 "Endorphins are the body's natural pain relievers.")
q("nt","Epinephrine and norepinephrine bind to which receptors?",
 ["*Adrenergic","Cholinergic || Acetylcholine.","NMDA || Glutamate.","Dopaminergic || Dopamine."],
 "Each receptor responds to specific neurotransmitters.")

# ---------- agonists & antagonists ----------
q("act","Pramipexole binds to dopamine receptors and acts like dopamine. What type of drug is this?",
 ["*Agonist","Antagonist || Blocks.","Enzyme inhibitor || Stops breakdown.","Precursor || A building block."],
 "Agonists mimic; antagonists block.")
q("act","Which drugs work by blocking an ENZYME that breaks down a neurotransmitter? "+SATA,
 ["*Donepezil","*Selegiline","Memantine || Receptor antagonist.","Baclofen || GABA agonist.","Pramipexole || Dopamine agonist."],
 "Donepezil blocks acetylcholinesterase; selegiline blocks MAO-B.")
q("act","Memantine blocks glutamate at NMDA receptors. Which type of drug is it?",
 ["*Antagonist","Agonist || Stimulates.","Enzyme inhibitor || Acts on a receptor.","Precursor || Not related."],
 "It calms excessive glutamate signaling.")

# ---------- baclofen ----------
q("baclofen","A client with MS has painful muscle spasms. Baclofen is ordered. How does it work?",
 ["*It acts like GABA in the brain and spinal cord to calm the signals","It stops calcium release inside the muscle || Dantrolene.","It blocks sodium in nerves || Lidocaine.","It raises dopamine || Levodopa."],
 "Centrally acting muscle relaxant.")
q("baclofen","A client wants to stop baclofen today because it makes them sleepy. What should the nurse teach?",
 ["*Don't stop suddenly; it must be tapered over 1–2 weeks","Stop it today; drowsiness is dangerous || Withdrawal risk.","Double the dose first || Not taught.","Stop if you feel better || Taper."],
 "Intrathecal withdrawal can be fatal.")
q("baclofen","Which side effects of baclofen should the nurse watch for? "+SATA,
 ["*Drowsiness","*Constipation","*Urinary retention","*Weakness early in therapy","Gum overgrowth || Phenytoin."],
 "Give with food; increase fluids and fiber.")
q("baclofen","What advice applies to ALL muscle relaxants in this lecture?",
 ["*Start low, go slow, and expect drowsiness","Take only at bedtime || Not the shared teaching.","Avoid the sun || Carbamazepine.","Eat high-protein meals || Not related."],
 "Avoid driving and alcohol.")

# ---------- dantrolene ----------
q("dantrolene","During surgery, a client's temperature spikes and muscles become rigid (malignant hyperthermia). Which drug is given IV?",
 ["*Dantrolene","Baclofen || Not for malignant hyperthermia.","Midazolam || A sedative.","Lidocaine || A local anesthetic."],
 "Dantrolene stops calcium release in the muscle fiber.")
q("dantrolene","What causes malignant hyperthermia?",
 ["*Too much calcium inside skeletal muscle fibers (an inherited reaction)","A brain infection || Not the cause.","Heat stroke || Not the cause.","Too much dopamine || Not the cause."],
 "Peripheral (muscle) problem → peripherally acting dantrolene.")
q("dantrolene","Which lab is monitored for a client on dantrolene?",
 ["*Liver function tests","Ammonia || Valproic acid.","Sodium || Oxcarbazepine.","Drug level || Phenytoin."],
 "Dantrolene can damage the liver.")
q("dantrolene","Which findings should a client on oral dantrolene report? "+SATA,
 ["*Muscle weakness","*Diarrhea","*Yellow skin or eyes","*Abdominal pain","Darkened urine || Levodopa (harmless)."],
 "Avoid alcohol and other CNS depressants.")

# ---------- seizure patho ----------
q("szpatho","Which imbalance causes seizures, per the lecture?",
 ["*Too much glutamate, too little GABA, and too much sodium entering the cell","Too much GABA || Reversed.","Too much dopamine || Not the seizure model.","Too little acetylcholine || Alzheimer's."],
 "Seizures are abnormal, excessive electrical discharges.")
q("szpatho","What are the three ways seizure medications work? "+SATA,
 ["*Lower glutamate","*Raise GABA","*Block sodium from entering the cell","Raise dopamine || Parkinson's.","Block calcium in muscle || Dantrolene."],
 "Oxcarbazepine lowers glutamate; valproic acid raises GABA; several block sodium.")
q("szpatho","Which ion rushes INTO the nerve cell to start an action potential?",
 ["*Sodium","Potassium || Not the ion described.","Calcium || Muscle contraction.","Chloride || Not described."],
 "Blocking sodium entry stops the signal.")

# ---------- phenytoin (FOCUS) ----------
q("phenytoin","A client has taken phenytoin (Dilantin) for a year. During mouth care the nurse sees swollen, overgrown gums. What is this?",
 ["*Gingival hyperplasia, a side effect of phenytoin","High ammonia || Valproic acid.","Bone marrow suppression || Carbamazepine.","Low sodium || Oxcarbazepine."],
 "Unique to phenytoin.")
q("phenytoin","Which teaching is specific to phenytoin?",
 ["*Regular dental visits, a soft toothbrush and good flossing","Check WBCs often || Carbamazepine.","Watch for pancreatitis || Valproic acid.","Take the last dose by noon || Selegiline."],
 "Hydantoins → dental care.")
q("phenytoin","What is the therapeutic range for phenytoin?",
 ["*10–20 mcg/mL","0.5–2 ng/mL || Digoxin.","50–100 mcg/mL || Too high.","1–5 mcg/mL || Too low."],
 "A narrow range; over 30 can be toxic.")
q("phenytoin","A phenytoin level is 28 mcg/mL. What should the nurse do?",
 ["*Notify the provider; it's above the therapeutic range","Give an extra dose || Too high.","No action; it's therapeutic || Range is 10–20.","Recheck next month || Act now."],
 "Phenytoin has a narrow therapeutic range.")
q("phenytoin","A phenytoin level is 7 mcg/mL. How is this interpreted?",
 ["*Below the therapeutic range (10–20)","Therapeutic || Too low.","Toxic || Too low.","Normal for IV || Same range."],
 "A low level raises seizure risk; notify the provider.")
q("phenytoin","IV phenytoin is ordered. The client's IV has D5W running. What should the nurse do?",
 ["*Don't mix phenytoin with dextrose; use a compatible setup","Push it into the D5W line || Incompatible.","Mix it in a D5W bag || Incompatible.","Give it IM instead || Not the answer."],
 "Phenytoin is incompatible with dextrose.")
q("phenytoin","During an IV phenytoin infusion, what does the nurse monitor?",
 ["*Heart rhythm and BP, for dysrhythmias and low BP","Blood glucose only || Not the priority.","Urine color || Levodopa.","The gag reflex || Not related."],
 "Inject slowly.")
q("phenytoin","Which teaching is correct for phenytoin? "+SATA,
 ["*Never stop it suddenly","*Report any rash","*Don't drive if drowsy","*It can make birth control pills less effective","Mix it with dextrose for IV use || Incompatible."],
 "Stop for rash (Stevens-Johnson risk) only with provider direction.")
q("phenytoin","A client on phenytoin says, 'My seizures stopped, so I'll quit taking it.' What is the best response?",
 ["*Don't stop it suddenly; that can cause seizures. Talk with your provider","That's fine if you feel well || Never stop abruptly.","Cut the dose in half yourself || Provider decides.","Take it only when you feel an aura || Daily."],
 "Keep the level steady.")

# ---------- carbamazepine ----------
q("carbamaz","What is the main lab concern with carbamazepine (Tegretol)?",
 ["*Bone marrow suppression; monitor the CBC and WBC","Liver failure only || Valproic acid.","Low sodium only || Oxcarbazepine.","High ammonia || Valproic acid."],
 "Hold for low counts.")
q("carbamaz","A client on carbamazepine has a fever, sore throat and bruises. Why is this concerning?",
 ["*These suggest low blood counts from bone marrow suppression","They're expected side effects || Report them.","They mean high ammonia || Valproic acid.","They mean low sodium || Oxcarbazepine."],
 "Also report rash (Stevens-Johnson).")
q("carbamaz","Which teaching is correct for carbamazepine? "+SATA,
 ["*Avoid grapefruit juice","*Use sunscreen","*Use backup birth control","*Swallow extended-release tablets whole","It's safe in pregnancy || Teratogenic."],
 "Grapefruit juice raises the drug level.")
q("carbamaz","Before starting carbamazepine, a client of Asian descent may be tested for which gene?",
 ["*HLA-B*1502","BRCA1 || Not related.","APOE || Not related.","CYP2D6 only || Not the lecture's test."],
 "The gene raises the risk of severe skin reactions.")

# ---------- valproic acid ----------
q("valproic","Which nursing monitoring is specific to valproic acid (Depakene)?",
 ["*Liver and pancreas problems (hepatitis and pancreatitis)","Dental care || Phenytoin.","WBC count || Carbamazepine.","Sodium || Oxcarbazepine."],
 "Liver toxicity can be fatal.")
q("valproic","A client on valproic acid is vomiting, confused and hard to wake. Which lab should the nurse check?",
 ["*Ammonia","Sodium || Oxcarbazepine.","Phenytoin level || Not related.","Glucose only || Not the valproic acid concern."],
 "Valproic acid can raise ammonia.")
q("valproic","Which findings should a client on valproic acid report? "+SATA,
 ["*Belly pain with nausea and vomiting","*Yellow skin","*Easy bruising","*Confusion","Dark sweat || Levodopa."],
 "Pancreatitis, liver damage, low platelets, high ammonia.")
q("valproic","A client on valproic acid wants to get pregnant. What should the nurse teach?",
 ["*It can cause neural tube defects; talk to the provider, and folic acid is given","It's the safest seizure drug in pregnancy || Teratogenic.","Stop it when pregnant || Never stop abruptly.","It only matters late in pregnancy || Early risk."],
 "Contraindicated in pregnancy and liver disease.")
q("valproic","Which labs are monitored for valproic acid? "+SATA,
 ["*Platelets","*Liver function tests","*Ammonia","*Amylase if symptoms occur","Only the phenytoin level || Not its own monitoring."],
 "Give with food to reduce GI upset.")

# ---------- oxcarbazepine ----------
q("oxcarb","A client takes oxcarbazepine (Trileptal) and a diuretic. They're confused with a headache. Which lab is checked first?",
 ["*Sodium","Ammonia || Valproic acid.","Glucose || Not the concern.","Phenytoin level || Not related."],
 "Oxcarbazepine can cause low sodium, especially with diuretics.")
q("oxcarb","Which teaching is correct for oxcarbazepine? "+SATA,
 ["*Use backup birth control","*Limit sun exposure","*Report a rash","It's safe with a carbamazepine allergy || Contraindicated."],
 "Monitor sodium and WBC.")
q("oxcarb","Oxcarbazepine is the lecture's example for which seizure approach?",
 ["*Lowering glutamate (it also blocks sodium)","Raising GABA || Valproic acid.","Raising dopamine || Not a seizure approach.","Blocking muscle calcium || Dantrolene."],
 "A second/third-generation antiseizure drug.")
q("carbamaz","Which seizure drug and key side effect are matched correctly? "+SATA,
 ["*Phenytoin: gum overgrowth","*Carbamazepine: bone marrow suppression","*Valproic acid: liver damage, pancreatitis, high ammonia","*Oxcarbazepine: low sodium","Phenytoin: low sodium || Oxcarbazepine."],
 "Know each drug's signature problem.")

# ---------- local anesthesia ----------
q("local","How does lidocaine numb an area?",
 ["*It blocks sodium from entering the nerves","It raises GABA || General anesthesia.","It depresses the whole brain || General anesthesia.","It blocks dopamine || Not related."],
 "No sodium in = no pain signal.")
q("local","Why is lidocaine with epinephrine NOT used on fingers, toes or the nose?",
 ["*Epinephrine squeezes the blood vessels and can cut off blood flow (gangrene)","It wears off too fast || Epinephrine makes it last longer.","It causes gum overgrowth || Phenytoin.","It raises ammonia || Valproic acid."],
 "End-artery sites.")
q("local","After spinal anesthesia with lidocaine, a client's BP drops. What should the nurse do first?",
 ["*Lower the head of the bed","Raise the head of the bed || Lower it.","Give naloxone || Reverses opioids.","Encourage oral fluids only || Not first."],
 "If it continues, prepare to give ephedrine or phenylephrine.")
q("local","Which findings suggest lidocaine toxicity? "+SATA,
 ["*Restlessness and dizziness","*Tremors","*Confusion and tingling","*Seizures","Gum overgrowth || Phenytoin."],
 "Stimulation can be followed by respiratory depression.")

# ---------- general anesthesia & sedation ----------
q("general","How do barbiturates, benzodiazepines and opioids produce general anesthesia or sedation?",
 ["*They depress the CNS and increase GABA","They block sodium at one nerve || Local anesthesia.","They raise dopamine || Not the mechanism.","They block acetylcholinesterase || Not the mechanism."],
 "Used for induction or conscious sedation.")
q("general","After a colonoscopy with midazolam (Versed), a client can't remember the procedure. What should the nurse say?",
 ["*Memory loss is an expected effect of the medicine","You may have had a stroke || Expected.","You were fully asleep with general anesthesia || Conscious sedation.","Naloxone will bring the memory back || Not used for this."],
 "Push midazolam slowly and wait 2 minutes before another dose.")
q("general","During procedural sedation with fentanyl, what must be ready at the bedside?",
 ["*Naloxone and resuscitation equipment","Flumazenil only || Fentanyl is an opioid.","Dantrolene only || Malignant hyperthermia.","Vitamin K || Not related."],
 "Fentanyl can depress breathing.")
q("general","What is the PRIORITY assessment during conscious sedation?",
 ["*Airway and breathing","Pain score || Important, not the priority.","Bowel sounds || Not the priority.","Urine color || Not the priority."],
 "All of these sedatives can cause respiratory depression.")
q("general","Which statements about methohexital (Brevital) are correct? "+SATA,
 ["*It's a short-acting barbiturate for fast induction","*It can stop breathing (apnea)","*It's given IV only","*Prevent it from leaking out of the vein","Give it with midazolam to deepen sedation || Duplicate therapy."],
 "Monitor breathing before, during and after.")

# ---------- stimulants (FOCUS) ----------
q("stim","How does methylphenidate (Ritalin) help ADHD?",
 ["*It increases dopamine and norepinephrine in the brain","It increases GABA || Calming.","It blocks dopamine || Would worsen focus.","It blocks serotonin only || Not the mechanism."],
 "High misuse potential.")
q("stim","Which side effects should the nurse watch for with a CNS stimulant? "+SATA,
 ["*Higher blood pressure and heart rate","*Trouble sleeping","*Nervousness","*Poor appetite and weight loss","A slow heart rate || Stimulants raise it."],
 "Monitor height and weight in children.")
q("stim","When should a child take the last daily dose of methylphenidate?",
 ["*By 4 p.m.","At bedtime || Causes insomnia.","With dinner || Too late.","Any time || Timing matters."],
 "Avoid caffeine.")
q("stim","Which teaching applies to CNS stimulants? "+SATA,
 ["*Take them in the morning","*Avoid caffeine","*Don't stop suddenly; taper","*Tolerance and misuse can happen","Take them at bedtime || Insomnia."],
 "Report palpitations or high BP.")
q("stim","A parent says their son skips lunch since starting methylphenidate. What should the nurse suggest?",
 ["*Serve bigger meals when he's hungriest, and track height and weight","Stop the drug || Provider decides.","Give it at bedtime || Insomnia.","Add coffee || Avoid caffeine."],
 "Medication holidays may help growth.")
q("stim","A teen stops methylphenidate suddenly. What should the nurse watch for?",
 ["*Depression and extreme tiredness (withdrawal)","Gum overgrowth || Phenytoin.","High ammonia || Valproic acid.","Malignant hyperthermia || Not related."],
 "Taper when stopping.")
q("stim","Which conditions make methylphenidate unsafe? "+SATA,
 ["*Taking an MAOI in the last 2 weeks","*Glaucoma","*Tourette's or motor tics","*A history of substance misuse","Narcolepsy || An indication."],
 "Also heart rhythm problems and children under 6.")
q("stim","How is a methylphenidate patch used?",
 ["*Apply in the morning, remove after no more than 9 hours, and use a new site daily","Apply at bedtime || Morning.","Wear it 24 hours || Max 9 hours.","Apply over a rash || Use healthy skin."],
 "Swallow extended-release pills whole.")

# ---------- modafinil ----------
q("modafinil","How is modafinil (Provigil) different from methylphenidate?",
 ["*It promotes wakefulness by blocking norepinephrine reuptake and has low misuse potential","It has higher misuse potential || Lower.","It increases GABA || Not its action.","It's only for children || Adults and shift workers."],
 "A non-CNS stimulant.")
q("modafinil","A woman on birth control pills starts modafinil. What should she be taught?",
 ["*Use a backup method during use and for 30 days after stopping","No change is needed || It lowers effectiveness.","Take it at bedtime || Morning.","Double the pill dose || Not taught."],
 "Contraindicated in pregnancy.")
q("modafinil","A night-shift nurse is prescribed modafinil. When should it be taken?",
 ["*1 hour before the shift starts","At bedtime || Promotes wakefulness.","Only on days off || Not taught.","With the last meal || Not tied to meals."],
 "For narcolepsy and sleep apnea: in the morning.")
q("modafinil","Which findings should a client on modafinil report? "+SATA,
 ["*Chest pain or palpitations","*A rash","*Headache or nervousness","Dark urine || Levodopa.","Gum overgrowth || Phenytoin."],
 "A rash can be Stevens-Johnson syndrome.")

# ---------- Parkinson's ----------
q("pdpatho","What causes the symptoms of Parkinson's disease?",
 ["*Loss of dopamine neurons, leaving more acetylcholine than dopamine","Too much dopamine || Lost.","Myelin destruction || MS.","Plaques and tangles || Alzheimer's."],
 "Movement needs a balance of dopamine and acetylcholine.")
q("pdpatho","Why isn't dopamine itself given for Parkinson's disease?",
 ["*It can't cross the blood-brain barrier","It works too fast || Not the reason.","It causes seizures || Not the reason.","It's too expensive || Not the reason."],
 "Levodopa crosses and becomes dopamine in the brain.")
q("pdpatho","Why is carbidopa added to levodopa?",
 ["*It keeps levodopa from turning into dopamine before it reaches the brain","It speeds conversion in the blood || Opposite.","It blocks MAO-B || Selegiline.","It mimics dopamine || Pramipexole."],
 "More levodopa reaches the brain.")
q("pdpatho","Which are the three ways to boost dopamine in Parkinson's? "+SATA,
 ["*Give levodopa (with carbidopa)","*Mimic dopamine with pramipexole","*Block dopamine breakdown with selegiline","Give IV dopamine || Can't cross.","Give donepezil || Alzheimer's."],
 "Make it, mimic it, or protect it.")

# ---------- levodopa (FOCUS) ----------
q("levodopa","A client on levodopa/carbidopa (Sinemet) is worried their urine and sweat look dark. What should the nurse say?",
 ["*This is expected and harmless","Stop the drug now || Expected.","It's liver failure || Not with this drug.","Go to the ED || Not needed."],
 "Warn clients ahead of time.")
q("levodopa","A client on levodopa/carbidopa eats a large steak with every dose. What should the nurse teach?",
 ["*High-protein meals reduce absorption; avoid them around doses","Protein helps it work || Reduces absorption.","Take it with milk || Not the teaching.","Take B6 with it || B6 reduces its effect."],
 "Full response can take up to 6 months.")
q("levodopa","Which teaching is correct for levodopa/carbidopa? "+SATA,
 ["*Avoid high-protein meals around doses","*Rise slowly to prevent falls","*Report jerky, uncontrolled movements","*Full effect may take months","Take vitamin B6 supplements || Reduces action."],
 "Orthostatic hypotension raises fall risk.")
q("levodopa","A client's tremor returns a few hours before each dose. What may help?",
 ["*More frequent doses or a controlled-release form","Stopping the drug || Not appropriate.","A protein shake with each dose || Reduces absorption.","Vitamin B6 || Reduces action."],
 "Report 'wearing off' to the provider.")
q("levodopa","Which drug must NOT be taken within 2 weeks of levodopa/carbidopa?",
 ["*An MAOI antidepressant (hypertensive crisis)","Amantadine || Used for dyskinesias.","Pramipexole || Often added.","Acetaminophen || No interaction."],
 "Also contraindicated with angle-closure glaucoma and history of melanoma.")

# ---------- pramipexole ----------
q("pramipexole","A client on pramipexole (Mirapex) suddenly fell asleep while driving. What is this?",
 ["*A 'sleep attack,' a known side effect","Dark urine || Levodopa.","Gum overgrowth || Phenytoin.","High ammonia || Valproic acid."],
 "Avoid driving if drowsy.")
q("pramipexole","How does pramipexole work?",
 ["*It directly stimulates dopamine receptors","It becomes dopamine in the brain || Levodopa.","It blocks MAO-B || Selegiline.","It blocks NMDA || Memantine."],
 "Also used for restless legs.")
q("pramipexole","When is pramipexole taken for restless legs syndrome?",
 ["*2–3 hours before bedtime","In the morning || Not for RLS.","At noon || Not the instruction.","Only during symptoms || On schedule."],
 "Taper slowly over a week when stopping.")
q("pramipexole","Which side effects of pramipexole should the nurse watch for? "+SATA,
 ["*Nausea","*Dizziness when standing","*Uncontrolled movements","*Muscle weakness","A slow heart rate || Donepezil."],
 "Take with food if nauseated.")

# ---------- selegiline ----------
q("selegiline","How does selegiline (Eldepryl) help Parkinson's disease?",
 ["*It blocks MAO-B, so dopamine isn't broken down","It acts like GABA || Baclofen.","It turns into dopamine || Levodopa.","It blocks acetylcholine breakdown || Donepezil."],
 "Lets the levodopa dose be lowered.")
q("selegiline","When should a client take the last daily dose of selegiline?",
 ["*By noon","At bedtime || Insomnia.","With dinner || Too late.","Any time || Timing matters."],
 "Take before breakfast.")
q("selegiline","A client on selegiline asks why to be careful with aged cheese and salami. What is the answer?",
 ["*They contain tyramine, which can build up and cause a dangerous BP spike","They lower blood sugar || Not the concern.","They block levodopa || That's protein.","They cause gum overgrowth || Phenytoin."],
 "Selegiline is less likely than other MAOIs to do this, but foods should be reviewed.")
q("selegiline","Which drugs interact dangerously with selegiline? "+SATA,
 ["*Meperidine","*SSRIs","*Tricyclic antidepressants","*St. John's wort","Acetaminophen || No listed interaction."],
 "Check with the provider before any new medicine.")

# ---------- Alzheimer's ----------
q("adpatho","Which brain changes are seen in Alzheimer's disease? "+SATA,
 ["*Amyloid plaques","*Tangles","*Brain shrinkage","*Low acetylcholine and high glutamate","Myelin destruction || MS."],
 "Progressive and ultimately fatal.")
q("adpatho","A family asks what donepezil will do for their mother's Alzheimer's. What is the best answer?",
 ["*It can slow the decline, but it won't cure or reverse the disease","It will reverse the brain damage || Can't reverse.","It will cure it || No cure.","It dissolves plaques || Doesn't."],
 "The goal is managing symptoms.")
q("adpatho","Which are the two medication approaches for Alzheimer's? "+SATA,
 ["*Raise acetylcholine (donepezil)","*Block excess glutamate (memantine)","Raise dopamine (levodopa) || Parkinson's.","Suppress the immune system (interferon) || MS."],
 "Excess glutamate lets too much calcium into neurons.")

# ---------- donepezil ----------
q("donepezil","Before giving donepezil (Aricept), what does the nurse check because the drug can slow the heart?",
 ["*Heart rate","Blood glucose || Not the concern.","Hearing || Furosemide.","Sodium || Oxcarbazepine."],
 "Bradycardia; report fainting.")
q("donepezil","When is donepezil usually given?",
 ["*At bedtime with food","In the morning on an empty stomach || Not the instruction.","By noon || Selegiline.","Only as needed || Daily."],
 "Report vomiting, diarrhea or weight loss.")
q("donepezil","A client on donepezil also takes daily naproxen. What should the nurse watch for?",
 ["*GI bleeding: black stools or coffee-ground vomit","Low sodium || Oxcarbazepine.","Sleep attacks || Pramipexole.","Malignant hyperthermia || Not related."],
 "NSAIDs add to the bleeding risk.")
q("donepezil","Which drug class works AGAINST donepezil?",
 ["*Antihistamines (anticholinergics)","Acetaminophen || No interaction.","Folic acid || No interaction.","Loop diuretics || Not listed."],
 "Anticholinergics block acetylcholine.")

# ---------- memantine ----------
q("memantine","How does memantine (Namenda) work?",
 ["*It blocks NMDA receptors so less calcium enters neurons","It raises acetylcholine || Donepezil.","It raises dopamine || Levodopa.","It suppresses white cells || MS."],
 "Used for moderate to severe Alzheimer's.")
q("memantine","Which side effects of memantine should a caregiver report? "+SATA,
 ["*Dizziness","*Headache","*More confusion","Dark urine || Levodopa.","Gum overgrowth || Phenytoin."],
 "Contraindicated in kidney failure.")
q("memantine","Which over-the-counter product can push memantine to toxic levels?",
 ["*Antacids like sodium bicarbonate (they raise urine pH)","Grapefruit juice || Carbamazepine.","Aged cheese || MAOIs.","Protein shakes || Levodopa."],
 "Memantine can be taken with or without food.")

# ---------- MS (FOCUS) ----------
q("ms","What happens in multiple sclerosis?",
 ["*White blood cells attack and destroy myelin in the CNS, with flare-ups and remissions","Dopamine neurons die || Parkinson's.","Plaques and tangles form || Alzheimer's.","Calcium overloads the muscles || Malignant hyperthermia."],
 "Signs: weakness, numbness, vision problems, incontinence, cognitive changes.")
q("ms","What is the difference between immunomodulators and immunosuppressants for MS?",
 ["*Immunomodulators normalize the immune response; immunosuppressants suppress it","They're the same || They differ.","Immunomodulators make the attack worse || Both reduce damage.","Immunosuppressants treat migraines || Not related."],
 "Prototype: interferon beta.")
q("ms","A client on interferon beta-1a (Avonex) has aches and a fever after each injection. What should the nurse teach?",
 ["*Take acetaminophen beforehand; flu-like symptoms usually lessen over time","Stop the drug || Expected effect.","These will get worse over time || They lessen.","Take it in the morning only || Late-day dosing helps."],
 "Rotate injection sites.")
q("ms","A client on interferon beta bruises easily, is very tired and keeps getting infections. What does the nurse suspect?",
 ["*Bone marrow suppression","Normal flu-like effects || Different signs.","High ammonia || Valproic acid.","Malignant hyperthermia || Not related."],
 "Monitor the CBC.")
q("ms","Which should be monitored for a client on interferon beta? "+SATA,
 ["*CBC","*Liver function tests","*Temperature","*Injection sites","Phenytoin level || Not related."],
 "Liver damage: yellow skin, poor appetite, belly tenderness.")
q("ms","A client on interferon beta has a low neutrophil count. What is the biggest risk?",
 ["*Infection","Bleeding || Low platelets.","Shortness of breath || Anemia.","High BP || Not related."],
 "Anemia → fatigue; low platelets → bleeding.")
q("ms","Which teaching is correct for interferon beta injections? "+SATA,
 ["*Rotate sites","*Cool compress before the shot, warm compress after","*Report bruising, bleeding or extreme tiredness","*Take acetaminophen beforehand","Symptoms will worsen over time || They improve."],
 "Beta-1a: IM weekly or SubQ 3 times a week.")

# ---------- migraine (FOCUS) ----------
q("migraine","What is the goal of migraine medication?",
 ["*Constrict the swollen, inflamed blood vessels","Dilate the vessels || Already dilated.","Raise GABA || Not the goal.","Block dopamine || Not the goal."],
 "Sumatriptan activates serotonin receptors to constrict vessels.")
q("migraine","After sumatriptan (Imitrex), a client has chest and jaw tightness that won't go away. What should the nurse do?",
 ["*Notify the provider at once; this may be angina from coronary spasm","Reassure them it's normal || Persistent tightness is a red flag.","Give another dose || Not with chest symptoms.","Have them sleep it off || Delays care."],
 "Teach: report chest, back, jaw or throat tightness.")
q("migraine","Which clients should NOT take sumatriptan? "+SATA,
 ["*A client with coronary artery disease","*A client with a past stroke","*A client with severe high BP","*A client with peripheral vascular disease","A client with tension headaches only || Not a listed contraindication."],
 "Also no MAOI within 2 weeks or another triptan within 24 hours.")
q("migraine","A client took oral sumatriptan 2 hours ago and still has a migraine. What is correct?",
 ["*One more oral dose may be taken; maximum 200 mg in 24 hours","Take a dose every 30 minutes || Not the instruction.","Take ergotamine now || Avoid within 24 hours.","It can't be repeated || Once after 2 hours."],
 "SubQ: may repeat once after 1 hour.")
q("migraine","What is sumatriptan used for?",
 ["*Stopping a migraine or cluster headache that has started","Preventing migraines daily || For acute attacks.","Preventing seizures || Not its use.","Muscle spasms || Not its use."],
 "Valproic acid can prevent migraines.")
q("migraine","Taking sumatriptan with which products can cause serotonin syndrome?",
 ["*Other serotonin drugs or St. John's wort","Acetaminophen || No interaction.","Folic acid || No interaction.","Antacids || Memantine."],
 "MAOIs within 2 weeks can cause sumatriptan toxicity.")
