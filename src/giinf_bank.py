# Week 10.2 Gastrointestinal Infections (17 core conditions) — professor's PowerPoint.
T = "giinf"
CONCEPTS = {
 "hh":"Hiatal hernia",
 "gerd":"GERD",
 "meds":"GI meds: H2 blockers, PPIs, sucralfate, antacids, metoclopramide",
 "barrett":"Barrett's esophagus",
 "ecancer":"Esophageal cancer",
 "gastritis":"Gastritis",
 "pud":"Peptic ulcer disease",
 "gcancer":"Gastric cancer",
 "enteral":"Enteral nutrition",
 "tpn":"PPN / TPN",
 "dumping":"Dumping syndrome",
 "pernicious":"Pernicious anemia",
 "gastro":"Gastroenteritis",
 "append":"Appendicitis",
 "divert":"Diverticulitis",
 "perf":"Perforation",
 "periton":"Peritonitis",
 "sepsis":"Sepsis",
 "signs":"Murphy's vs McBurney's",
}
HI = ["meds","pud","append","sepsis","dumping","tpn","perf","enteral","signs"]

SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

# ---------- hiatal hernia ----------
q("hh","What is a hiatal hernia?",
 ["*A portion of the stomach protrudes up through the diaphragm's esophageal hiatus into the chest",
  "An outpouching of the colon wall || That's diverticulosis.",
  "Inflammation of the appendix || Appendicitis.",
  "Replacement of esophageal cells with intestinal-type cells || Barrett's esophagus."],
 "Two types: sliding (~95%, worse when supine) and paraesophageal/rolling (higher strangulation risk).")
q("hh","Which type of hiatal hernia has the higher risk of strangulation?",
 ["Sliding || Most common (~95%), but lower strangulation risk.","*Paraesophageal (rolling)",
  "Both carry equal risk || The lecture contrasts them.","Neither can strangulate || Rolling hernias can."],
 "In a rolling hernia the fundus rolls up beside the esophagus while the GE junction stays put.")
q("hh","Which teaching is the first-line defense for a client with a hiatal hernia?",
 ["Lie down for 1 hour after eating || Avoid the recumbent position after meals.",
  "*Stay upright 1–2 hours after eating",
  "Eat 3 large meals a day || Small, frequent meals.",
  "Wear a snug waistband for support || Avoid tight clothing."],
 "NCLEX alert: avoid the recumbent position after meals; gravity is the first-line defense against reflux.")
q("hh","Which are risk factors for hiatal hernia? "+SATA,
 ["*Obesity","*Pregnancy","*Chronic coughing or heavy lifting","*Aging",
  "High-fiber diet || Not a listed risk factor."],
 "Anything raising intra-abdominal pressure or weakening the diaphragm.")
q("hh","After a fundoplication for a severe hiatal hernia, which diet teaching is correct? "+SATA,
 ["*Start with liquids, then advance to a soft diet","*Take small bites and chew well","*Reduce air swallowing",
  "Drink carbonated beverages to relieve bloating || Increases gas and air."],
 "Plus routine post-op care.")

# ---------- GERD ----------
q("gerd","What causes GERD?",
 ["*An incompetent lower esophageal sphincter lets gastric contents back up",
  "H. pylori in the duodenum || A major PUD cause.",
  "Loss of intrinsic factor || Pernicious anemia.","Fecalith obstruction || Appendicitis."],
 "Backflow irritates the esophageal mucosa.")
q("gerd","Which complications can result from untreated GERD? "+SATA,
 ["*Barrett's esophagus","*Esophageal stricture","*Aspiration pneumonia","*Dental erosion and chronic cough",
  "Pernicious anemia || Linked to gastrectomy and atrophic gastritis."],
 "Also esophagitis, laryngitis.")
q("gerd","Which teaching is correct for GERD? "+SATA,
 ["*Avoid lying down 2–3 hours after eating","*Elevate the head of the bed 30°","*Small, low-fat meals",
  "*Stop smoking and lose weight",
  "Have chocolate or coffee after meals to aid digestion || Caffeine and chocolate are triggers."],
 "Teach adherence; symptoms can mask ongoing damage.")
q("gerd","What is the classic symptom of GERD?",
 ["*Heartburn (pyrosis)","RLQ pain || Appendicitis.","Beefy red tongue || Pernicious anemia.","LLQ pain || Diverticulitis."],
 "Also regurgitation of sour material, dysphagia, chronic cough, hoarseness. Worse after meals and when supine.")

# ---------- meds ----------
q("meds","When should a client take pantoprazole for best effect?",
 ["At bedtime || Not the teaching point.","*30–60 minutes before the first meal of the day",
  "With every meal || Not the teaching point.","1–3 hours after eating || That's antacids."],
 "NCLEX alert: PPIs work best 30–60 minutes before the first meal; a common test point.")
q("meds","Which long-term effects are associated with PPIs? "+SATA,
 ["*Osteoporosis","*Hypomagnesemia",
  "Tardive dyskinesia || Metoclopramide.","Increased phenytoin levels || H2 blockers (cimetidine)."],
 "PPIs inhibit gastric secretions, raising pH.")
q("meds","Which teaching is correct for sucralfate?",
 ["Take with meals || Take on an empty stomach before meals.",
  "*Take on an empty stomach before meals; it can decrease absorption of other medications",
  "It's absorbed systemically to block acid || It forms a local gel coating; not systemic.",
  "Take it with antacids at the same time || Can decrease absorption of other meds."],
 "Sucralfate is a gastric protectant.")
q("meds","A client on metoclopramide for 4 months develops lip smacking and tongue movements. What should the nurse suspect?",
 ["Expected effect || A serious adverse effect.","*Tardive dyskinesia",
  "Hypomagnesemia || PPI.","Dumping syndrome || Not related."],
 "Metoclopramide (prokinetic) increases gastric peristalsis; not to be used longer than 12 weeks.")
q("meds","A client on warfarin starts cimetidine. What should the nurse monitor for?",
 ["*Increased anticoagulant effect (bleeding)","Hypoglycemia || Not listed.","Tardive dyskinesia || Metoclopramide.","Osteoporosis || Long-term PPIs."],
 "H2 blockers increase levels of anticoagulants and phenytoin. They can be taken with or without food.")
q("meds","When should antacids such as Mylanta be taken?",
 ["30–60 minutes before the first meal || PPIs.","*1–3 hours after eating, separated from other medications",
  "With other medications to help absorption || They inhibit absorption of other meds.","Only at bedtime || Not the instruction."],
 "Antacids neutralize acid; assess for diarrhea or constipation.")
q("meds","Match the drug to its action: which neutralizes gastric acid?",
 ["Famotidine || Blocks histamine receptors to decrease secretion.","Pantoprazole || Inhibits gastric secretions.",
  "*Aluminum hydroxide (Amphojel), Mylanta, Tums","Metoclopramide || Increases peristalsis."],
 "Antacids neutralize; H2 blockers and PPIs decrease secretion; sucralfate coats; metoclopramide moves things along.")

# ---------- Barrett's ----------
q("barrett","What is Barrett's esophagus?",
 ["*Metaplasia from chronic GERD: normal squamous cells of the distal esophagus are replaced by intestinal-type cells",
  "A cancer of the upper esophagus || Pre-malignant, not cancer.",
  "A stomach hernia || Hiatal hernia.","Gastric inflammation || Gastritis."],
 "Considered pre-malignant; raises the risk of esophageal adenocarcinoma.")
q("barrett","How is Barrett's esophagus followed?",
 ["Monitoring symptoms only || Barrett's itself doesn't cause new symptoms.",
  "*Surveillance endoscopy with biopsy",
  "Yearly chest x-ray || Not the method.","Stool cultures || Not related."],
 "NCLEX alert: surveillance biopsy, not symptom monitoring alone, catches early dysplasia.")
q("barrett","Which new finding in a client with Barrett's esophagus is a red flag?",
 ["Mild heartburn || Common with chronic GERD.","*New dysphagia",
  "Taking a PPI daily || Recommended therapy.","Weight loss with diet || Planned weight loss is encouraged."],
 "Also teach warning signs: weight loss and GI bleeding.")
q("barrett","Which are risk factors for Barrett's esophagus? "+SATA,
 ["*Long-standing, poorly controlled GERD","*Male sex, age over 50","*Obesity and smoking","*Family history",
  "Low-sodium diet || Not a listed risk factor."],
 "Also chronic hiatal hernia.")

# ---------- esophageal cancer ----------
q("ecancer","Which esophageal cancer type is linked to GERD and Barrett's and is most common in the U.S.?",
 ["*Adenocarcinoma, lower third of the esophagus","Squamous cell, upper/mid esophagus || Linked to alcohol and tobacco.",
  "Gastric adenocarcinoma || That's stomach cancer.","Melanoma || Not discussed."],
 "Squamous cell: upper/mid esophagus, alcohol and tobacco.")
q("ecancer","A client with esophageal cancer now has trouble swallowing liquids as well as solids. What should the nurse do?",
 ["Document it as expected || A change that must be reported.",
  "*Report it immediately; it signals worsening obstruction and changes aspiration risk",
  "Encourage thicker solid foods || Worsens risk.","Give a laxative || Not related."],
 "NCLEX alert: dysphagia progressing from solids to liquids = worsening luminal obstruction.")
q("ecancer","Which nursing priorities apply to esophageal cancer? "+SATA,
 ["*Nutrition support (liquid, semi-soft, or enteral feeding)","*Aspiration precautions and swallowing checks",
  "*Prepare for esophagectomy, chemo or radiation","*Psychosocial support and palliative discussions",
  "High-fiber raw vegetables to clear the obstruction || Not a nursing priority."],
 "Often asymptomatic until advanced; unintentional weight loss is common.")

# ---------- gastritis ----------
q("gastritis","A client with gastritis has coffee-ground emesis. What should the nurse do first?",
 ["Give an antacid || Not the priority.","*Assess vital signs and notify the provider immediately",
  "Encourage a bland snack || Not with bleeding.","Document and reassess at shift change || A red flag needs action now."],
 "NCLEX alert: coffee-ground emesis or tarry stools = bleeding red flag.")
q("gastritis","Which are causes of gastritis? "+SATA,
 ["*NSAIDs and aspirin","*Alcohol","*H. pylori","*Severe physiologic stress such as burns or sepsis",
  "High-fiber diet || Not a listed cause."],
 "Also bile reflux.")
q("gastritis","How does chronic gastritis differ from acute gastritis?",
 ["*Chronic is often H. pylori-driven and can progress to atrophy and higher cancer risk",
  "Chronic resolves once the irritant is removed || That describes acute.",
  "Chronic is always caused by NSAIDs || Acute is irritant-driven.","There's no difference || The lecture contrasts them."],
 "Acute: sudden, from irritants, self-limiting.")
q("gastritis","Which lifestyle teaching is correct for gastritis? "+SATA,
 ["*Keep a food journal","*Bland diet","*Avoid bedtime snacks","*Avoid alcohol, caffeine and smoking","*Reduce stress",
  "Take ibuprofen for the epigastric pain || Remove NSAIDs."],
 "Remove the causative agent; PPIs/H2 blockers/antacids; H. pylori eradication if positive.")

# ---------- PUD ----------
q("pud","Which finding points to a DUODENAL ulcer rather than a gastric ulcer?",
 ["Pain worsens after eating with weight loss || Gastric ulcer.",
  "*Pain is relieved by food and recurs 2–3 hours later, often at night",
  "Pain 30–60 minutes after eating || Gastric ulcer.","Beefy red tongue || Pernicious anemia."],
 "Gastric = pain with food. Duodenal = food relieves, then pain returns 2–3 hours later and at night.")
q("pud","A client with peptic ulcer disease suddenly has severe pain and a rigid, board-like abdomen. What should the nurse suspect?",
 ["Needing the PPI dose earlier || Not a medication-timing issue.","*Perforation, a surgical emergency",
  "Dumping syndrome || Post-gastrectomy.","Normal ulcer pain || Board-like abdomen is an emergency."],
 "NCLEX alert: sudden board-like abdomen in PUD = perforation.")
q("pud","What causes the majority of peptic ulcers?",
 ["*H. pylori infection","Hiatal hernia || Not the main cause.","Low-fiber diet || Diverticulitis.","Vitamin B12 deficiency || Not related."],
 "Also chronic NSAIDs, smoking, alcohol, physiologic stress (Curling's and Cushing's ulcers).")
q("pud","Which complications of peptic ulcer disease should the nurse monitor for? "+SATA,
 ["*Hemorrhage (hematemesis, melena)","*Perforation","*Obstruction",
  "Barrett's esophagus || A GERD complication.","Pernicious anemia || Not listed."],
 "Treatment: H. pylori triple/quad therapy, PPIs; avoid NSAIDs, alcohol and smoking.")
q("pud","A client with PUD asks what to take for a headache. Best response?",
 ["\"Ibuprofen is fine with food.\" || NSAIDs are a major ulcer cause.","*\"Avoid NSAIDs like ibuprofen and aspirin; ask your provider what's safe.\"",
  "\"Aspirin is safest.\" || Aspirin also damages the mucosa.","\"Take naproxen at bedtime.\" || An NSAID."],
 "Teach to avoid NSAIDs, alcohol and smoking.")

# ---------- gastric cancer ----------
q("gcancer","Why does a client need lifelong vitamin B12 monitoring after a gastrectomy?",
 ["The surgery damages the ileum || The stomach was removed, not the ileum.",
  "*The cells that make intrinsic factor were removed, so B12 can't be absorbed",
  "B12 causes dumping syndrome || Not related.","Chemotherapy destroys B12 || Not the reason."],
 "NCLEX alert: any post-gastrectomy client needs lifelong B12 monitoring.")
q("gcancer","Which are risk factors for gastric cancer? "+SATA,
 ["*H. pylori infection","*Diet high in smoked, salted or preserved foods","*Smoking","*Pernicious anemia or chronic atrophic gastritis",
  "High-fiber diet || Protective for diverticular disease, not a risk factor."],
 "Also family history. Often silent until advanced.")
q("gcancer","After a gastrectomy, what should the nurse watch for?",
 ["*Dumping syndrome","Appendicitis || Not related.","GERD from a hiatal hernia || Not the post-op focus.","Hyperkalemia || Not discussed."],
 "Also small, frequent meals; nutrition and emotional support; wound and drain care.")
q("gcancer","How is gastric cancer diagnosed?",
 ["*Upper endoscopy (gastroscopy) with biopsy","Stool culture || Not diagnostic.","McBurney's point exam || Appendicitis.","Chest x-ray alone || Not diagnostic."],
 "Then CT staging, gastrectomy, and chemo/radiation, targeted therapy or immunotherapy.")

# ---------- enteral ----------
q("enteral","What is the gold standard for confirming INITIAL feeding tube placement?",
 ["Gastric pH || Used for ongoing checks.","*X-ray",
  "Auscultating an air bolus || Not the lecture's method.","Client can talk || Not a confirmation method."],
 "Then check gastric pH (<5) and note the external markings before every feeding or medication.")
q("enteral","Before each tube feeding, which gastric aspirate pH supports correct placement?",
 ["*Under 5","7.4 || Not gastric.","Over 8 || Not gastric.","Exactly 10 || Not gastric."],
 "Reassess placement before every feeding and medication.")
q("enteral","What is the core aspiration-prevention measure for enteral feedings?",
 ["Lie flat during feeds || Raises aspiration risk.","*HOB at least 30° (30–45°) during and 30–60 minutes after feeding",
  "Give feeds only at night || Not the core measure.","Feed faster to finish sooner || Not the core measure."],
 "NCLEX alert from the slide.")
q("enteral","Which are complications of enteral feeding? "+SATA,
 ["*Aspiration","*Diarrhea","*Tube clogging","*Abdominal distention and high residuals",
  "Gingival hyperplasia || Phenytoin."],
 "Flush before and after feeds and meds; monitor for aspiration (cough, falling SpO2); check glucose per policy.")
q("enteral","What does enteral nutrition require?",
 ["*An intact, functioning GI tract","A central line || TPN.","A nonfunctional gut || That's when parenteral nutrition is used.","NPO with nothing in the GI tract || Not enteral."],
 "Used for dysphagia, neuro impairment, ventilation, or inadequate oral intake.")

# ---------- TPN ----------
q("tpn","A client's TPN bag runs out and the new bag isn't ready. What is the main risk?",
 ["Hyperglycemia || The risk is the opposite.","*Rebound hypoglycemia",
  "Hyperkalemia || Not the lecture's concern.","Dumping syndrome || Not related."],
 "NCLEX alert: never stop TPN abruptly; taper. The body has adapted to the high glucose.")
q("tpn","Which nursing care applies to TPN? "+SATA,
 ["*Strict aseptic technique","*Monitor blood glucose regularly","*Dedicated line; no other meds through it","*Taper; never stop abruptly",
  "Give antibiotics through the TPN line to save an IV site || Dedicated line."],
 "Complications: hyper/hypoglycemia, catheter infection, fluid overload, electrolyte imbalance.")
q("tpn","How does PPN differ from TPN?",
 ["*PPN is peripheral and short-term; TPN uses a central line and is long-term, complete nutrition",
  "PPN goes into the stomach || That's enteral.","They're identical || The lecture contrasts them.","TPN is peripheral || TPN is central."],
 "Parenteral nutrition bypasses the GI tract; used for obstruction, severe malabsorption, prolonged ileus, short bowel.")
q("tpn","A client on TPN has fever and redness at the central line site. What does the nurse suspect?",
 ["*Catheter-related infection","Rebound hypoglycemia || Presents with low glucose.","Dumping syndrome || Not related.","Fluid overload || Not with fever and redness."],
 "TPN lines are a sepsis risk; strict aseptic technique always.")

# ---------- dumping ----------
q("dumping","Which intervention is most tested for dumping syndrome?",
 ["Drink fluids with every meal || Speeds emptying.","*Separate liquids from solids by 30–45 minutes",
  "Eat 3 large high-sugar meals || Worsens it.","Walk right after eating || Lie down instead."],
 "NCLEX alert: separating liquids from meals slows gastric emptying.")
q("dumping","Which teaching helps prevent dumping syndrome? "+SATA,
 ["*Small, frequent meals","*Avoid simple sugars and concentrated sweets","*Lie down 20–30 minutes after eating","*Increase protein and fat",
  "Drink a milkshake with lunch || Concentrated sugar plus liquid with a meal."],
 "Fiber supplements (psyllium) may also help.")
q("dumping","Two hours after eating, a post-gastrectomy client is shaky, sweaty and confused. What is happening?",
 ["Early dumping from a fluid shift || Early happens in 10–30 minutes.",
  "*Late dumping with reactive hypoglycemia",
  "Peritonitis || Would show a rigid abdomen and fever.","Pernicious anemia || Develops slowly."],
 "Early (10–30 min): fluid shift; tachycardia, diaphoresis, cramping, diarrhea. Late (1–3 hrs): reactive hypoglycemia.")
q("dumping","Which surgeries put a client at risk for dumping syndrome? "+SATA,
 ["*Gastrectomy","*Gastric bypass (bariatric) surgery","*Vagotomy or pyloroplasty",
  "Appendectomy || Not a listed risk."],
 "Rapid emptying of hyperosmolar contents into the small intestine.")

# ---------- pernicious anemia ----------
q("pernicious","What causes pernicious anemia?",
 ["Iron deficiency || A different anemia.","*Lack of intrinsic factor, so B12 can't be absorbed in the ileum",
  "Folate excess || Not the cause.","Blood loss from ulcers || Not the cause."],
 "Megaloblastic anemia. Causes: autoimmune destruction of parietal cells, gastrectomy, atrophic gastritis.")
q("pernicious","Which findings suggest pernicious anemia? "+SATA,
 ["*Bright red, beefy, smooth tongue","*Paresthesias","*Ataxia and balance problems","*Fatigue and pallor",
  "RLQ pain || Appendicitis."],
 "Labs: low B12, elevated MCV, intrinsic factor/parietal cell antibodies.")
q("pernicious","A client with pernicious anemia asks if eating more B12-rich foods will cure it. Best response?",
 ["\"Yes, diet alone will fix it.\" || Without intrinsic factor, dietary B12 isn't absorbed.",
  "*\"You'll need lifelong B12 injections (or high-dose oral); diet alone can't correct it.\"",
  "\"You only need a short course of B12.\" || Therapy is lifelong.","\"An iron supplement will cure it.\" || It's B12, not iron."],
 "Teach that therapy is lifelong.")
q("pernicious","Why does early treatment of pernicious anemia matter so much?",
 ["*Neurologic damage can become irreversible if treatment is delayed",
  "The tongue can rupture || Not a concern.","It causes perforation || Not related.","It leads to dumping syndrome || Not related."],
 "NCLEX alert: early recognition matters more than the anemia itself. Monitor fall risk from ataxia.")

# ---------- gastroenteritis ----------
q("gastro","What is the PRIORITY intervention for gastroenteritis?",
 ["Give an antidiarrheal || Avoided in suspected infectious causes.","*Rehydration with fluids and electrolytes",
  "Start a high-fiber diet || Advance diet slowly.","Give a laxative || Not indicated."],
 "Fluid and electrolyte loss is the primary danger, not the infection itself.")
q("gastro","Which findings suggest dehydration in gastroenteritis? "+SATA,
 ["*Dry mucous membranes","*Tachycardia","*Decreased urine output","*Poor skin turgor",
  "Bradycardia with bounding pulses || Not dehydration findings."],
 "Monitor I&O, daily weights, skin turgor. Young children and older adults are at highest risk.")
q("gastro","Which precautions are needed for a client with infectious gastroenteritis?",
 ["Airborne || Not the route.","*Contact precautions and strict hand hygiene","Droplet only || Not the lecture's choice.","None needed || It spreads."],
 "Causes: norovirus and rotavirus (most common viral), E. coli, Salmonella, C. difficile.")

# ---------- appendicitis ----------
q("append","Which pain pattern is classic for appendicitis?",
 ["*Starts vague around the umbilicus, then moves to the RLQ (McBurney's point)",
  "LLQ pain with fever || Diverticulitis.","Epigastric pain relieved by food || Duodenal ulcer.","Burning chest pain when lying flat || GERD/hiatal hernia."],
 "Also rebound tenderness, guarding, low-grade fever, anorexia, nausea.")
q("append","A client with suspected appendicitis asks for a heating pad and a laxative. What should the nurse do?",
 ["Provide both for comfort || Both can cause rupture.","*Decline both; heat and laxatives or enemas can precipitate rupture",
  "Give the laxative only || Laxatives can cause rupture.","Give the heating pad only || Heat can cause rupture."],
 "NCLEX alert: never apply heat or give laxatives/enemas for suspected appendicitis.")
q("append","A client with appendicitis suddenly reports that the pain is gone. What should the nurse suspect?",
 ["The appendicitis resolved || Sudden relief is a red flag.","*Rupture",
  "The analgesic worked || Not the concern taught.","Dumping syndrome || Not related."],
 "Assess the pain trend. Untreated cases risk rupture within 24–72 hours.")
q("append","Which nursing actions are correct for suspected appendicitis? "+SATA,
 ["*Keep NPO","*Prepare for emergent appendectomy","*Assess the pain trend",
  "Give an enema to clear the bowel || Can precipitate rupture.","Apply heat to the RLQ || Can precipitate rupture."],
 "Diagnosis: CT or abdominal ultrasound. Concerns: abscess, perforation, peritonitis.")

# ---------- diverticulitis ----------
q("divert","Which finding is most common in diverticulitis?",
 ["RLQ pain at McBurney's point || Appendicitis.","*LLQ abdominal pain",
  "Pain relieved by food || Duodenal ulcer.","Heartburn when lying flat || GERD."],
 "Also fever, leukocytosis, bowel habit changes, sometimes a tender mass.")
q("divert","A client is admitted with an acute diverticulitis flare. Which diet order does the nurse expect?",
 ["High-fiber diet || That's for after the attack resolves.","*NPO or clear liquids to rest the bowel",
  "Regular diet || Not during a flare.","High-sugar diet || Not related."],
 "NCLEX alert: high fiber protects between attacks, but the bowel is rested during a flare. Timing of diet teaching matters.")
q("divert","After diverticulitis resolves, which teaching prevents recurrence?",
 ["*A high-fiber diet","Strict low-fiber diet || Low fiber is a risk factor.","Stay sedentary || A risk factor.","Strain with bowel movements || A risk factor."],
 "Risk factors: low-fiber diet, aging, obesity, sedentary life, smoking, straining.")
q("divert","Which are complications of diverticulitis? "+SATA,
 ["*Abscess","*Perforation and peritonitis","*Fistula","*Bowel obstruction or stricture",
  "Pernicious anemia || Not related."],
 "Acute management: NPO/clear liquids, IV antibiotics, pain control, monitor for perforation.")

# ---------- perforation ----------
q("perf","What is the hallmark imaging finding of GI perforation?",
 ["*Free air on x-ray or CT","Cardiomegaly || Heart failure.","Pleural effusion only || Not the hallmark.","A fecalith || Appendicitis cause."],
 "Perforation requires emergent surgical repair; delay increases mortality.")
q("perf","Which nursing actions apply to a perforated ulcer? "+SATA,
 ["*Notify the provider now","*Keep NPO and prepare for emergent surgery","*IV fluids, broad-spectrum antibiotics and NG decompression",
  "*Frequent vital signs to watch for shock",
  "Give the PPI and reassess in 4 hours || Not routine pain; it's a surgical emergency."],
 "Signs: sudden severe diffuse pain, rigid board-like abdomen, rebound tenderness, fever, tachycardia, hypotension → shock.")
q("perf","Which conditions can lead to perforation? "+SATA,
 ["*Untreated peptic ulcer disease","*Ruptured appendicitis","*Diverticulitis","*Trauma",
  "Barrett's esophagus surveillance || Not a listed cause."],
 "Also severe gastritis or ischemia.")

# ---------- peritonitis ----------
q("periton","A client with peritonitis has a rigid abdomen and absent bowel sounds. What should the nurse do?",
 ["Chart 'no output' and recheck tomorrow || Reassess, don't just chart.",
  "*Recognize paralytic ileus from peritoneal inflammation, reassess and report",
  "Give a laxative || Not indicated.","Encourage a regular diet || Keep NPO."],
 "NCLEX alert: absent bowel sounds + rigid abdomen = paralytic ileus.")
q("periton","Why is peritonitis so dangerous? "+SATA,
 ["*It can rapidly progress to sepsis and septic shock","*Fluid shifts into the peritoneal space (third-spacing)","*Bowel motility decreases (paralytic ileus)",
  "It always resolves without treatment || High mortality without prompt treatment."],
 "Causes: perforation, ruptured appendix or diverticulum, peritoneal dialysis infection, post-surgical contamination.")
q("periton","Which treatments are expected for peritonitis? "+SATA,
 ["*IV broad-spectrum antibiotics","*Aggressive fluid resuscitation","*NPO with NG tube decompression","*Surgery",
  "Heating pad to the abdomen || Not a treatment."],
 "Monitor closely for progression to sepsis.")

# ---------- sepsis ----------
q("sepsis","A client with suspected sepsis from a perforated bowel has orders for blood cultures, IV antibiotics and IV fluids. What comes first?",
 ["*Draw blood cultures","Give the antibiotics || Cultures come before antibiotics.","Start vasopressors || Fluids first; vasopressors PRN.","Check the lactate in 6 hours || Monitor lactate, but cultures first."],
 "1-hour sepsis bundle: cultures, then antibiotics (within 1 hour), then fluids.")
q("sepsis","Within what time should broad-spectrum antibiotics be given for sepsis?",
 ["6 hours || Too long.","*1 hour","24 hours || Too long.","Only after culture results || Don't wait for results."],
 "One of the most heavily tested time-sensitive protocols.")
q("sepsis","Which sign of sepsis is a LATE, ominous sign?",
 ["Fever || Early.","Tachycardia || Early.","*Hypotension","Tachypnea || Early."],
 "Septic shock = sepsis + persistent hypotension despite fluids.")
q("sepsis","Which findings suggest sepsis? "+SATA,
 ["*Fever or hypothermia","*Tachycardia","*Tachypnea","*Altered mental status",
  "Bradycardia with warm, dry skin || Not the lecture's sepsis picture."],
 "Progression: infection → SIRS → sepsis → septic shock. Trend vitals and lactate.")
q("sepsis","Which are risk factors for sepsis from a GI source? "+SATA,
 ["*Untreated peritonitis, perforation or abscess","*Immunosuppression and older age","*Indwelling lines such as TPN or central lines","*Delayed antibiotics",
  "A high-fiber diet || Not a risk factor."],
 "Early recognition dramatically improves survival.")

# ---------- PPN vs TPN (professor: know the difference) ----------
q("tpn","A client needs IV nutrition for 3 days while recovering, and has only a peripheral IV. Which is appropriate?",
 ["*PPN","TPN || TPN requires a central line and is for long-term, complete nutrition.","Enteral feeding through a PEG || The question asks about IV nutrition.","Neither can be given IV || Both PPN and TPN are IV."],
 "PPN = peripheral line, short-term. TPN = central line, long-term, complete nutrition.")
q("tpn","A client with short bowel syndrome needs complete nutrition for months. Which is appropriate?",
 ["PPN || Short-term and peripheral only.","*TPN through a central line","Enteral feeding || Requires a functioning GI tract.","Clear liquids by mouth || Not complete nutrition."],
 "Parenteral nutrition is used when the gut is nonfunctional: obstruction, severe malabsorption, prolonged ileus, short bowel syndrome.")
q("tpn","Which statements correctly compare PPN and TPN? "+SATA,
 ["*PPN is given through a peripheral vein","*TPN is given through a central line","*PPN is for short-term use","*TPN provides long-term, complete nutrition",
  "PPN goes into the stomach through a tube || That's enteral nutrition.","TPN can be given through any peripheral IV || TPN needs a central line."],
 "Both bypass the GI tract entirely and need strict aseptic technique.")
q("tpn","Which statement is true of BOTH PPN and TPN?",
 ["*They bypass the GI tract and require strict aseptic technique","Both require a central line || Only TPN.",
  "Both are for long-term nutrition || PPN is short-term.","Both require a functioning gut || That's enteral nutrition."],
 "High infection risk with any parenteral line.")

# ---------- Murphy's vs McBurney's (professor: both will appear as choices) ----------
q("signs","A client has periumbilical pain that has moved to the right lower quadrant, with rebound tenderness. Which finding is the nurse assessing?",
 ["Murphy's sign || That's inspiratory arrest with RUQ palpation, for cholecystitis.","*McBurney's point tenderness",
  "Cullen's sign || Periumbilical bruising in pancreatitis.","Grey Turner's sign || Flank bruising in pancreatitis."],
 "McBurney's point = RLQ = appendicitis. Murphy's sign = RUQ = cholecystitis.")
q("signs","During right upper quadrant palpation, a client suddenly stops breathing in. Which condition does this suggest?",
 ["Appendicitis || That's McBurney's point in the RLQ.","*Cholecystitis","Diverticulitis || LLQ pain.","Peptic ulcer disease || Epigastric pain."],
 "Murphy's sign = inspiratory arrest with RUQ palpation.")
q("signs","Match the sign to its condition. Which pairings are correct? "+SATA,
 ["*Murphy's sign: cholecystitis","*McBurney's point: appendicitis",
  "Murphy's sign: appendicitis || Murphy's = gallbladder (RUQ).","McBurney's point: cholecystitis || McBurney's = appendix (RLQ)."],
 "Memory tip: Murphy = upper (gallbladder, RUQ); McBurney = lower (appendix, RLQ).")
q("signs","Where is McBurney's point?",
 ["Right upper quadrant || That's where Murphy's sign is checked.","*Right lower quadrant","Left lower quadrant || Diverticulitis pain.","Epigastric area || Pancreatitis and ulcer pain."],
 "Appendicitis pain starts periumbilical, then migrates to McBurney's point.")
