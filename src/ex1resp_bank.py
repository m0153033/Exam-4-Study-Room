# Week 1.2 Pharmacology: The Respiratory System — PowerPoint, notes, slide deck, mind map, poster.
EXAM = "e1"
T = "resp"
CONCEPTS = {
 "anat":"Upper vs lower airway & disorders",
 "copd":"Asthma vs COPD",
 "mast":"Mast cells & the messengers they release",
 "ns":"Nervous system framework",
 "symp":"Sympathetic vs parasympathetic",
 "predict":"Predicting whole-body drug effects",
 "beta2":"Beta-2 agonists: albuterol vs salmeterol",
 "anticho":"Anticholinergics: ipratropium & umeclidinium",
 "theo":"Methylxanthines: theophylline",
 "gluco":"Glucocorticoids",
 "mastmed":"Cromolyn & montelukast",
 "antihist":"Antihistamines: diphenhydramine vs cetirizine",
 "phenyl":"Nasal sympathomimetic: phenylephrine",
 "cough":"Matching cough medicine to cough type",
 "nursing":"Nursing assessment & teaching",
}
HI = ["beta2","anticho","gluco","cough","predict","symp","theo"]

SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

# ---------- anatomy ----------
q("anat","Which structures belong to the LOWER respiratory tract? "+SATA,
 ["*Bronchi","*Bronchioles","*Alveoli","Sinuses || Upper tract.","Pharynx || Upper tract."],
 "Upper: nose, sinuses, pharynx, larynx, trachea. Lower: lungs, bronchi, bronchioles, alveoli.")
q("anat","Which disorders affect the UPPER respiratory tract? "+SATA,
 ["*Hay fever","*Rhinitis","*Cold and flu","Asthma || Lower tract.","COPD || Lower tract."],
 "Upper: hay fever, rhinitis, cold/flu. Lower: asthma, COPD.")
q("anat","Why does the location of a respiratory problem matter for medication choice?",
 ["*Location affects how the drug is delivered and how urgent it is","All respiratory drugs work the same everywhere || Different drugs target different areas.","Only the lower tract can be treated || Rhinitis is treated too.","Location only matters for antibiotics || It matters for all categories."],
 "Upper-tract rhinitis often uses nasal/topical treatment; lower-tract drugs are inhaled or systemic to reach bronchioles and alveoli.")
q("anat","Which findings are expected with rhinitis? "+SATA,
 ["*Runny or stuffy nose","*Sneezing","*Itchy, watery eyes","*Cough","Alveolar damage || That's emphysema."],
 "Rhinitis = inflammation of the nasal lining from allergies or infection; usually temporary.")

# ---------- asthma vs COPD ----------
q("copd","Which statement correctly compares asthma and COPD?",
 ["*Asthma airway obstruction is reversible; COPD is progressive and irreversible","Both are fully reversible || COPD isn't.","Both are upper-airway diseases || Both are lower-airway.","COPD is reversible; asthma is not || Reversed."],
 "Asthma = chronic inflammation and narrowing of bronchial tubes, reversible. COPD = progressive, irreversible.")
q("copd","In COPD, which description matches emphysema?",
 ["*Damage to the alveoli","Damage to the airways || That's chronic bronchitis.","Inflammation of the nasal lining || That's rhinitis.","Clouding of the lens || That's a cataract."],
 "COPD makes exhalation difficult: emphysema = alveolar damage; chronic bronchitis = airway damage.")
q("copd","Which findings are shared by asthma and COPD? "+SATA,
 ["*Wheezing","*Cough","*Dyspnea","*Chest tightness","Watery, itchy eyes || That's rhinitis."],
 "Both show wheezing, cough, difficulty breathing, mucus and chest tightness.")

# ---------- mast cells ----------
q("mast","The professor asks: when you see mucus production and inflammation, which cell should you think of?",
 ["*Mast cells","Red blood cells || Carry oxygen.","Platelets || Clotting.","Osteoblasts || Bone formation."],
 "Mast cells respond to allergens (noninfectious) or antigens (infectious).")
q("mast","Which chemical messengers do triggered mast cells release? "+SATA,
 ["*Histamine","*Leukotrienes","*Prostaglandins","Insulin || Not a mast-cell messenger.","Acetylcholine || A neurotransmitter, not a mast-cell messenger."],
 "Histamine, leukotrienes and prostaglandins → inflammation, edema, mucus → narrowed airway.")
q("mast","What are the two medication goals for inflamed, narrowed airways?",
 ["*Reduce inflammation and help the airway dilate","Increase mucus and constrict the airway || The opposite.","Raise heart rate and blood pressure || Not the goals.","Kill all bacteria || Not the stated goals."],
 "Goals: reduce inflammation + facilitate dilation.")

# ---------- nervous system ----------
q("ns","Which nervous system controls involuntary functions such as HR, BP and RR?",
 ["*Autonomic nervous system","Somatic nervous system || Voluntary actions like walking and talking.","Central nervous system only || CNS is the brain and spinal cord.","None; they're voluntary || They're involuntary."],
 "The PNS divides into autonomic (involuntary) and somatic (voluntary). Autonomic divides into sympathetic and parasympathetic.")
q("ns","What is the difference between an agonist and an antagonist?",
 ["*An agonist binds a receptor and causes a response; an antagonist binds and blocks a response","An agonist blocks; an antagonist activates || Reversed.","Both always cause the same response || They have opposite effects.","Neither binds receptors || Both bind receptors."],
 "Agonist = activates. Antagonist = blocks.")
q("ns","Walking, talking and reacting are controlled by which system?",
 ["*Somatic nervous system","Autonomic nervous system || Involuntary functions.","Parasympathetic nervous system || Rest and digest.","Sympathetic nervous system || Fight or flight."],
 "Somatic = voluntary.")

# ---------- symp vs parasymp ----------
q("symp","Which effects come from SYMPATHETIC (adrenergic) stimulation of the airway?",
 ["*Bronchodilation and decreased secretions","Bronchoconstriction and increased secretions || That's parasympathetic.","No airway effect || The airway responds.","Bronchoconstriction and decreased HR || Parasympathetic."],
 "Sympathetic = fight or flight = adrenergic: bronchodilation, ↓ secretions, ↑ HR.")
q("symp","Which receptor language matches the parasympathetic system?",
 ["*Cholinergic","Adrenergic || Sympathetic.","Alpha only || Adrenergic.","Beta-2 only || Adrenergic."],
 "Parasympathetic = rest and digest = cholinergic. Drugs that stimulate it are parasympathomimetics.")
q("symp","Adrenergic drugs are also called:",
 ["*Sympathomimetics","Parasympathomimetics || Those are cholinergics.","Anticholinergics || Those block cholinergic receptors.","Antihistamines || A different class."],
 "Adrenergics = sympathomimetics; cholinergics = parasympathomimetics. Blockers: alpha and beta blockers; anticholinergics.")
q("symp","Parasympathetic stimulation causes which airway changes? "+SATA,
 ["*Bronchoconstriction","*Increased secretions","Bronchodilation || Sympathetic.","Decreased secretions || Sympathetic."],
 "Parasympathetic/cholinergic: bronchoconstriction, ↑ secretions, ↓ HR.")

# ---------- predicting effects ----------
q("predict","A client receives an anticholinergic drug. Which effects should the nurse expect? "+SATA,
 ["*Pupil dilation","*Increased HR","*Decreased peristalsis","*Urinary retention","Increased secretions || Anticholinergics dry secretions."],
 "Anticholinergic: pupil and bronchial dilation, ↓ secretions, ↑ HR, ↓ peristalsis, bladder relaxes + sphincter contracts → retention.")
q("predict","Which effects are expected from cholinergic stimulation? "+SATA,
 ["*Pupil constriction","*Decreased HR","*Increased peristalsis","*Increased secretions","Urinary retention || Cholinergics relax the sphincter, causing urination."],
 "Cholinergic: constriction of pupils and bronchi, ↑ secretions, ↓ HR, ↑ peristalsis, bladder contracts + sphincter relaxes.")
q("predict","How does adrenergic stimulation raise blood pressure?",
 ["*Vasoconstriction","Vasodilation || That lowers BP (adrenergic blockers).","Increased peristalsis || A GI effect.","Increased secretions || Not a BP effect."],
 "Adrenergic stimulation: ↑ HR, ↑ BP via vasoconstriction, ↓ peristalsis.")
q("predict","Which effects match an ADRENERGIC BLOCKER per the slide? "+SATA,
 ["*Decreased HR","*Decreased BP through vasodilation","*Bronchial constriction","Bronchodilation || That's adrenergic stimulation.","Pupil dilation || Blockers constrict the pupil."],
 "Adrenergic blocker: pupil and bronchial constriction, ↑ secretions, ↓ HR, ↓ BP via vasodilation.")

# ---------- beta-2 agonists ----------
q("beta2","A client with asthma is wheezing and short of breath right now. Which inhaler is the rescue medicine?",
 ["*Albuterol (SABA)","Salmeterol (LABA) || Not fast enough for rescue.","Fluticasone || A glucocorticoid for inflammation, not rescue.","Montelukast || A leukotriene modifier for prevention."],
 "Albuterol = short-acting beta-2 agonist for acute symptoms.")
q("beta2","A client asks to use salmeterol during an acute asthma attack. What is the best response?",
 ["*Salmeterol is for scheduled maintenance; use albuterol for an attack","That's fine; it works within seconds || It's long-acting, not rescue.","Use salmeterol with a double dose || Never for rescue.","Stop all inhalers during an attack || Rescue is needed."],
 "LABAs are never used alone for acute attacks; they're fixed daily maintenance in COPD or persistent asthma.")
q("beta2","After albuterol, a client says their heart is racing and they feel shaky. How should the nurse interpret this?",
 ["*Expected adrenergic effects; monitor HR","An allergic reaction; give epinephrine || Not anaphylaxis.","Proof the drug didn't work || Unrelated to effectiveness.","A sign of hypoglycemia || Not linked here."],
 "Beta-2 agonists stimulate the sympathetic system: ↑ HR, tremors, nervousness. Monitor for tachycardia/palpitations.")
q("beta2","Which findings show salmeterol is working? "+SATA,
 ["*Clearer lung sounds over time","*Less need for the rescue inhaler","*Long-term airway stability","Immediate relief within seconds of an attack || That's the rescue drug."],
 "Evaluate LABA by long-term stability and less rescue use; evaluate SABA by improved breath sounds and less wheezing.")
q("beta2","Where are beta-2 receptors found?",
 ["*Smooth muscle such as the lungs","Only in the heart || Beta-1 is the heart.","In the eyelids || Not stated.","In bone || Not stated."],
 "Desired beta-2 effects: bronchodilation, vasodilation, decreased secretions.")

# ---------- anticholinergics ----------
q("anticho","How do inhaled anticholinergics such as ipratropium open the airway?",
 ["*They block acetylcholine, which causes bronchoconstriction and mucus","They stimulate beta-2 receptors || That's albuterol.","They block phosphodiesterase || That's theophylline.","They suppress leukotrienes || That's montelukast."],
 "Blocking the parasympathetic response → bronchodilation and decreased secretions.")
q("anticho","Which client needs the nurse to use CAUTION with an anticholinergic inhaler?",
 ["*A client with glaucoma","A client with diarrhea || Slowed peristalsis isn't a danger here.","A client with frequent urination || Not the concern.","A client with a slow heart rate || Not the listed caution."],
 "Anticholinergics dilate the pupil and can obstruct drainage → ↑ IOP. They also cause urinary retention.")
q("anticho","Which is the LONG-acting anticholinergic prototype?",
 ["*Umeclidinium","Ipratropium || Short-acting.","Albuterol || A SABA.","Cromolyn || A mast-cell stabilizer."],
 "Ipratropium = short-acting; umeclidinium = long-acting.")
q("anticho","A client on ipratropium reports trouble starting urination. Why?",
 ["*Anticholinergics relax the bladder and contract the sphincter","The drug causes kidney failure || Not stated.","It's unrelated to the medication || It's an expected anticholinergic effect.","It increases bladder contraction || Opposite."],
 "Urinary retention is a key anticholinergic adverse effect.")

# ---------- theophylline ----------
q("theo","How does theophylline cause bronchodilation?",
 ["*It blocks phosphodiesterase, so more cAMP stays to relax smooth muscle","It stimulates phosphodiesterase || It blocks it.","It blocks acetylcholine || That's an anticholinergic.","It prevents histamine release || That's cromolyn."],
 "Phosphodiesterase breaks down cAMP → constriction. Blocking it keeps cAMP → dilation.")
q("theo","Which teaching is specific to theophylline?",
 ["*Limit caffeine","Take with grapefruit juice || Not stated.","Increase chocolate for energy || Chocolate contains methylxanthines too.","Avoid all fluids || Not stated."],
 "Methylxanthines are naturally in caffeine and chocolate; limit caffeine.")
q("theo","A client on theophylline can't sleep and feels nervous. What explains this?",
 ["*Theophylline is a CNS stimulant","It's a sedating antihistamine || Opposite effect.","It causes hypoglycemia || Not stated.","It's a glucocorticoid side effect || Different class."],
 "CNS stimulation → enhanced neuron excitability, insomnia, nervousness.")

# ---------- glucocorticoids ----------
q("gluco","A client on long-term prednisone wants to stop it suddenly. What is the priority teaching?",
 ["*Don't stop abruptly; it must be tapered to prevent adrenal crisis","It's safe to stop any time || Abrupt stop can cause adrenal crisis.","Double the dose for a day, then stop || Never.","Switch to cetirizine || Not a substitute."],
 "Glucocorticoids suppress the adrenal gland's own production; it needs time to recover.")
q("gluco","For a client on long-term glucocorticoids, what should the nurse monitor? "+SATA,
 ["*Blood glucose","*Signs of infection","*Muscle wasting","*Bone demineralization","*Fluid retention and weight gain","Weight loss || Weight gain is expected, not loss."],
 "Hyperglycemia, immunosuppression, muscle wasting, bone loss, fluid retention/weight gain.")
q("gluco","How do glucocorticoids reduce airway inflammation?",
 ["*They prevent release of leukotrienes, prostaglandins and histamine and decrease capillary permeability","They block acetylcholine || Anticholinergic.","They stimulate beta-2 receptors || Beta agonist.","They thin mucus || Mucolytic."],
 "They mimic cortisol; therapeutic result = less inflammation and edema.")
q("gluco","Which drugs are glucocorticoid prototypes in this lecture? "+SATA,
 ["*Prednisone","*Fluticasone","*Beclomethasone","Montelukast || Leukotriene modifier.","Guaifenesin || Expectorant."],
 "Prednisone, fluticasone, beclomethasone; used short- and long-term.")
q("gluco","Why is a client on long-term prednisone at higher risk of infection?",
 ["*Glucocorticoids suppress the immune system","They raise white cells too high || Not the mechanism.","They cause bronchoconstriction || They reduce inflammation.","They dry secretions || Not the reason."],
 "Immunosuppression is a key long-term concern.")

# ---------- cromolyn & montelukast ----------
q("mastmed","How does cromolyn work?",
 ["*It stabilizes mast cells, preventing release of leukotrienes and histamine","It suppresses leukotrienes only || That's montelukast.","It blocks phosphodiesterase || Theophylline.","It stimulates beta-2 receptors || Albuterol."],
 "Mast-cell stabilizer → less inflammation and edema.")
q("mastmed","Which drug is a leukotriene modifier?",
 ["*Montelukast","Cromolyn || Mast-cell stabilizer.","Ipratropium || Anticholinergic.","Cetirizine || Antihistamine."],
 "Montelukast suppresses leukotrienes → less inflammation/edema.")
q("mastmed","What is the key difference between cromolyn and montelukast?",
 ["*Cromolyn prevents leukotriene AND histamine release; montelukast suppresses leukotrienes","Cromolyn is a rescue inhaler || Neither is rescue.","Montelukast is an antibiotic || It isn't.","They're the same drug || Different classes."],
 "Both decrease inflammation and edema by different routes.")

# ---------- antihistamines ----------
q("antihist","A client takes diphenhydramine for allergies. Which adverse effects should the nurse expect? "+SATA,
 ["*Drowsiness","*Dry mouth","*Urinary retention","*Constipation","Insomnia and jitters || Those fit stimulants like theophylline."],
 "First-generation antihistamines cross the blood-brain barrier and have anticholinergic properties.")
q("antihist","Why does cetirizine cause less drowsiness than diphenhydramine?",
 ["*Cetirizine doesn't cross the blood-brain barrier","Cetirizine is a stimulant || It's an antihistamine.","Cetirizine blocks acetylcholine more || Not the reason.","They cause equal drowsiness || Cetirizine is non-sedating."],
 "2nd generation = non-sedating; doesn't cross the BBB.")
q("antihist","An older adult with an enlarged prostate wants something for hay fever. Which antihistamine concern is highest?",
 ["*Diphenhydramine can cause urinary retention","Cetirizine causes hypertension || Not listed.","Diphenhydramine causes diarrhea || It causes constipation.","Antihistamines increase urination || Opposite."],
 "Diphenhydramine's anticholinergic properties cause retention.")

# ---------- phenylephrine ----------
q("phenyl","How does phenylephrine relieve nasal congestion?",
 ["*It stimulates adrenergic receptors, causing vasoconstriction in the nasal passages","It blocks histamine || That's an antihistamine.","It thins mucus || That's a mucolytic.","It suppresses cough || That's an antitussive."],
 "Phenylephrine = nasal sympathomimetic.")
q("phenyl","Which client should use phenylephrine with caution?",
 ["*A client with hypertension or cardiac disease","A client with a dry cough || Not a phenylephrine concern.","A client with allergic conjunctivitis || Not the listed caution.","A healthy teen || No listed caution."],
 "Vasoconstriction can worsen cardiac disease or HTN.")

# ---------- cough ----------
q("cough","A client has a dry, hacking cough keeping them awake. Which drug class fits?",
 ["*Antitussive, such as dextromethorphan","Expectorant, such as guaifenesin || For productive cough.","Mucolytic, such as acetylcysteine || For productive cough.","Leukotriene modifier || Not a cough drug."],
 "Dry cough → suppress it (antitussive: opioid codeine or non-opioid dextromethorphan).")
q("cough","A client has a productive cough with thick mucus. Which medications fit? "+SATA,
 ["*Guaifenesin","*Acetylcysteine","Codeine || Suppresses a dry cough.","Dextromethorphan || Suppresses a dry cough."],
 "Productive → move or thin mucus: expectorant (guaifenesin) or mucolytic (acetylcysteine).")
q("cough","Which cough medicine is an OPIOID antitussive?",
 ["*Codeine","Dextromethorphan || Non-opioid antitussive.","Guaifenesin || Expectorant.","Acetylcysteine || Mucolytic."],
 "Codeine = opioid; dextromethorphan = non-opioid.")
q("cough","Match the prototype: guaifenesin is a(n):",
 ["*Expectorant","Mucolytic || That's acetylcysteine.","Antitussive || That's codeine or dextromethorphan.","Antihistamine || That's diphenhydramine or cetirizine."],
 "Guaifenesin = expectorant for productive cough.")

# ---------- nursing ----------
q("nursing","Which nursing assessments apply to clients on respiratory drugs? "+SATA,
 ["*Lung sounds and wheezing","*Heart rate for tachycardia","*Urinary retention and bowel sounds","*Pupils and eye pressure concerns","Hearing acuity || Not listed."],
 "Assess gas exchange, HR, secretions, eyes, elimination and technique.")
q("nursing","Why does the nurse check the client's inhaler technique?",
 ["*To be sure the drug reaches the bronchioles, not just the back of the throat","To count the puffs left || Not the main reason.","To check the expiration date || Not the main reason.","It isn't needed for inhalers || Technique matters."],
 "Teach purpose, timing, rescue vs maintenance, technique, expected effects and safety.")
q("nursing","Which two safety rules does the lecture stress? "+SATA,
 ["*Don't use a LABA alone for acute rescue","*Don't stop glucocorticoids abruptly","Always double the albuterol dose || Not a rule.","Take antihistamines before driving || Diphenhydramine causes drowsiness."],
 "These are the two major safety rules in the quick-recall list.")
