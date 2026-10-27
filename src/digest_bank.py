# Week 10.3 Infection of the Digestive System — Prof. Hanikeh's PowerPoint + lesson plan.
T = "digest"
CONCEPTS = {
 "gbpatho":"Cholecystitis: patho & types",
 "gbrisk":"Gallstone risk factors (4 F's)",
 "gbsx":"Cholecystitis signs & Murphy's sign",
 "gbdx":"Gallbladder labs & imaging",
 "ducts":"MRCP vs ERCP vs HIDA",
 "gbtx":"Cholecystitis treatment & cholecystectomy",
 "gbcomp":"Gallbladder complications to escalate",
 "panpatho":"Pancreatitis: autodigestion",
 "panrisk":"Pancreatitis causes",
 "pansx":"Acute vs chronic pancreatitis findings",
 "panmon":"Pancreatitis complications to monitor",
 "pandx":"Pancreatitis labs & imaging",
 "pancare":"Pancreatitis care & teaching",
 "creon":"Pancreatic enzymes (Creon)",
 "pcsx":"Pancreatic cancer risks & signs",
 "pcdx":"Pancreatic cancer diagnosis & treatment",
 "whipple":"Whipple procedure complications",
}
HI = ["gbsx","pansx","creon","whipple","panmon"]

SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

# ---------- cholecystitis patho ----------
q("gbpatho","What is the role of bile?",
 ["*Helps digest fats in the small intestine","Breaks down carbohydrates || That's amylase.","Absorbs vitamin B12 || Needs intrinsic factor.","Neutralizes stomach acid in the esophagus || Not its role."],
 "The liver makes bile; the gallbladder stores it and contracts to release it into the duodenum after a fatty meal.")
q("gbpatho","What happens in calculous cholecystitis?",
 ["*A gallstone blocks the cystic duct → bile is trapped → inflammation and distension → ischemia and infection risk",
  "The pancreas digests itself || Pancreatitis.","No stones are present || That's acalculous.","Bile flows too freely || Bile is trapped."],
 "Calculous cholecystitis is about 90–95% of cases.")
q("gbpatho","Which client is most at risk for ACALCULOUS cholecystitis?",
 ["A healthy 42-year-old woman || Fits gallstone (calculous) risk.","*A critically ill client with sepsis or trauma",
  "A teen after a fatty meal || Not the typical picture.","A client on a low-fat diet || Not a risk factor."],
 "Acalculous (5–10%): no stones; bile stasis, ischemia, trauma or sepsis.")

# ---------- risk factors ----------
q("gbrisk","Which are the '4 F's' of gallstone risk? "+SATA,
 ["*Female","*Fat (BMI over 30)","*Fertile","*Forty",
  "Fit || Not one of the 4 F's."],
 "Estrogen and progesterone (pregnancy, oral contraceptives) make the gallbladder sluggish, so bile clumps.")
q("gbrisk","Which gallstone risk factors are MODIFIABLE? "+SATA,
 ["*Obesity","*Rapid weight loss","*High-fat, low-fiber diet","*Hormone therapy or oral contraceptives",
  "Family history of gallstones || Non-modifiable.","Native American ethnicity || Non-modifiable."],
 "Non-modifiable: female, over 40, Native American ethnicity, family history. The slide lists pregnancy under modifiable.")
q("gbrisk","Why do oral contraceptives raise gallstone risk?",
 ["*Estrogen and progesterone make the gallbladder sluggish, so bile moves less and clumps",
  "They block the pancreatic duct || Not the mechanism.","They increase fiber absorption || Not related.","They destroy intrinsic factor || Not related."],
 "Pregnancy increases risk for the same hormonal reason.")

# ---------- signs ----------
q("gbsx","During palpation of the RUQ, the client suddenly stops inhaling. What is this called?",
 ["Cullen's sign || Periumbilical bruising in pancreatitis.","*Murphy's sign","Grey Turner's sign || Flank bruising in pancreatitis.","McBurney's point || Appendicitis location."],
 "Murphy's sign = inspiratory arrest with RUQ palpation, classic for cholecystitis.")
q("gbsx","Which findings fit acute cholecystitis? "+SATA,
 ["*RUQ pain radiating to the right shoulder or mid-sternum","*Pain that worsens after eating","*Fever, nausea and vomiting","*Possible jaundice",
  "LLQ pain || Diverticulitis.","Painless jaundice with weight loss || Pancreatic cancer."],
 "RUQ pain lasting more than 6 hours. Also anorexia, distended abdomen, tachycardia, possibly a palpable gallbladder.")
q("gbsx","The CHOLY mnemonic describes cholecystitis. What does the 'Y' stand for?",
 ["*Yellow (jaundice, occasionally)","Young age || Risk is over forty.","Yawning || Not related.","Yeast infection || Not related."],
 "C: colicky RUQ pain; H: high fever; O: obstruction of bile flow; L: leukocytosis; Y: yellow.")

# ---------- diagnosis ----------
q("gbdx","What is the first-line imaging test for suspected cholecystitis?",
 ["*Ultrasound","HIDA scan || Used if ultrasound is inconclusive.","ERCP || Invasive; can treat duct stones.","CT || For complications or unclear diagnosis."],
 "Ultrasound shows gallstones, wall thickening over 3 mm and pericholecystic fluid.")
q("gbdx","On a HIDA scan, the gallbladder isn't visualized. What does this mean?",
 ["Normal gallbladder function || Non-visualization is a positive result.","*Positive for acute cholecystitis",
  "Pancreatic cancer || Not what HIDA shows.","The test failed || Not the interpretation."],
 "HIDA (cholescintigraphy) evaluates gallbladder function and bile flow; used if ultrasound is inconclusive.")
q("gbdx","Which lab findings are expected with cholecystitis? "+SATA,
 ["*Elevated WBC","*Elevated CRP","*Mildly elevated AST, ALT and ALP","*Elevated bilirubin if the obstruction reaches the common bile duct",
  "Low WBC || WBC rises with inflammation."],
 "Fever is also expected.")

# ---------- MRCP / ERCP / HIDA ----------
q("ducts","Which procedure can actually REMOVE gallstones from the ducts?",
 ["MRCP || Noninvasive imaging only.","*ERCP","HIDA scan || Evaluates function and bile flow.","Ultrasound || Imaging only."],
 "ERCP = endoscopic retrograde cholangiopancreatography: direct visualization and treatment of duct problems.")
q("ducts","Which test gives NONINVASIVE images of the biliary and pancreatic ducts?",
 ["ERCP || Endoscopic and invasive.","*MRCP","HIDA || Looks at function, not detailed duct anatomy.","Whipple || A surgery."],
 "Think 'image vs treat': MRCP images; ERCP can treat.")
q("ducts","Which complication is a known risk after ERCP?",
 ["*Pancreatitis","Dumping syndrome || After gastrectomy.","Pernicious anemia || Not related.","Appendicitis || Not related."],
 "Post-ERCP pancreatitis is listed among pancreatitis causes.")

# ---------- treatment ----------
q("gbtx","Which medical management is expected for acute cholecystitis? "+SATA,
 ["*NPO","*IV fluids","*Pain control (NSAIDs or opioids)","*Broad-spectrum antibiotics such as ceftriaxone + metronidazole",
  "High-fat diet to empty the gallbladder || Low-fat diet."],
 "Surgery: laparoscopic cholecystectomy, usually within 48 hours; percutaneous cholecystostomy if unstable.")
q("gbtx","What diet teaching follows a cholecystectomy?",
 ["High-fat diet to stimulate bile || Not taught.","*Fat-restricted diet for 4–6 weeks",
  "No restrictions || The lecture teaches restriction.","Clear liquids for 6 months || Not taught."],
 "Post-op issues: pain control, bleeding, infection, respiratory issues.")
q("gbtx","Which post-op problems should the nurse monitor after a cholecystectomy? "+SATA,
 ["*Pain","*Bleeding","*Infection","*Respiratory issues",
  "Gingival hyperplasia || Not related."],
 "Laparoscopic: abdomen inflated with CO2, small puncture sites. Open: right-side incision with a drain.")
q("gbtx","A cholecystitis client is too unstable for surgery. Which procedure might be done?",
 ["Whipple || Pancreatic cancer surgery.","*Percutaneous cholecystostomy","Fundoplication || Hiatal hernia.","Appendectomy || Not related."],
 "Stable clients usually get laparoscopic cholecystectomy within 48 hours.")

# ---------- complications ----------
q("gbcomp","A client with cholecystitis develops a rigid abdomen, rebound tenderness and confusion. What should the nurse do?",
 ["Give the scheduled pain medicine and reassess later || Signs of a surgical emergency.","*Notify the provider immediately; this could be perforation or sepsis",
  "Start a low-fat diet || Not the priority.","Apply heat || Not indicated."],
 "Watch for worsening: rigid abdomen, rebound tenderness, jaundice, mental status changes, fever, tachycardia, hypotension.")
q("gbcomp","Why does the nurse monitor amylase and lipase in a client with cholecystitis?",
 ["*To rule out pancreatitis","To check for B12 deficiency || Not related.","To check kidney function || BUN/Cr.","To check clotting || Not related."],
 "Also monitor LFTs, WBC and bilirubin.")

# ---------- pancreatitis patho ----------
q("panpatho","What is the basic mechanism of pancreatitis?",
 ["*Pancreatic enzymes activate inside the pancreas and digest it (autodigestion)","Bile is trapped in the gallbladder || Cholecystitis.",
  "Intrinsic factor is lost || Pernicious anemia.","Myelin is destroyed || MS."],
 "Trigger (gallstones, alcohol) → enzyme activation → autodigestion and inflammation → possible necrosis, infection, systemic inflammatory response.")
q("panpatho","Which enzyme does the lecture name as digesting the pancreas itself?",
 ["Pepsin || A stomach enzyme.","*Trypsin","Acetylcholinesterase || Neuro enzyme.","Lactase || Not named."],
 "The pancreatic duct becomes obstructed while enzymes are hypersecreted; enzymes and bile reflux back into the pancreas.")

# ---------- causes ----------
q("panrisk","What are the two most common causes of pancreatitis?",
 ["*Gallstones and alcohol","Mumps and trauma || Listed, but less common.","Smoking and tumors || Listed, but less common.","Genetics and autoimmunity || Listed, but less common."],
 "Gallstones block the duct; alcohol damages cells and increases enzyme secretion.")
q("panrisk","Which can trigger pancreatitis? "+SATA,
 ["*Triglycerides over 1,000 mg/dL","*Thiazide diuretics, corticosteroids, valproic acid or estrogens","*ERCP","*Abdominal trauma","*Mumps or CMV",
  "Low-fat diet || Recommended, not a cause."],
 "Idiopathic in 10–20% of cases.")

# ---------- acute vs chronic ----------
q("pansx","Which pain is classic for ACUTE pancreatitis?",
 ["*Sudden severe epigastric pain radiating to the back","RUQ pain to the right shoulder || Cholecystitis.",
  "Periumbilical pain moving to the RLQ || Appendicitis.","LLQ pain || Diverticulitis."],
 "Also nausea/vomiting, fever, tachycardia, tenderness, possible jaundice and a rigid board-like abdomen.")
q("pansx","A client with acute pancreatitis has bluish discoloration around the umbilicus. What is this called?",
 ["Grey Turner's sign || Flank discoloration.","*Cullen's sign","Murphy's sign || Cholecystitis.","Trousseau's sign || Not taught here."],
 "Cullen's = periumbilical; Grey Turner's = flank.")
q("pansx","Which findings suggest CHRONIC pancreatitis? "+SATA,
 ["*Steatorrhea (fatty stools)","*Weight loss","*Diabetes mellitus","*Persistent abdominal pain",
  "Murphy's sign || Cholecystitis.","Sudden pain relief || An appendicitis red flag."],
 "The damaged pancreas makes too few digestive enzymes and too little insulin.")
q("pansx","Why do clients with chronic pancreatitis develop diabetes?",
 ["*Pancreatic damage reduces insulin production","Too much bile || Not the mechanism.","High-fiber diet || Not the mechanism.","Steroid overuse only || Not the main reason."],
 "Blood glucose control and monitoring are part of care and teaching.")

# ---------- complications ----------
q("panmon","A client with acute pancreatitis becomes hypotensive and tachycardic with cold, clammy skin. What is happening?",
 ["*Shock from protein-rich fluid shifting into the peritoneal cavity","Expected pain response || These are shock signs.",
  "Hypoglycemia || Glucose rises in pancreatitis.","Dumping syndrome || Not related."],
 "Shock, low O2, AKI or new respiratory distress = urgent escalation, not routine pain management.")
q("panmon","Which complications should the nurse monitor for in acute pancreatitis? "+SATA,
 ["*Hypovolemic shock","*Acute kidney injury","*Respiratory distress with pleural effusions or infiltrates","*Hypocalcemia, which can lead to clotting problems and DIC",
  "Hyperactive bowel sounds from overeating || NPO; ileus is the concern."],
 "Respiratory compromise shows on ABGs as respiratory acidosis.")
q("panmon","Hypocalcemia in acute pancreatitis can lead to which complication, per the lecture?",
 ["*Coagulation problems and DIC","Gingival hyperplasia || Phenytoin.","Dumping syndrome || Not related.","Barrett's esophagus || Not related."],
 "Monitor electrolytes and labs frequently.")

# ---------- labs ----------
q("pandx","Which labs are elevated in acute pancreatitis? "+SATA,
 ["*Amylase","*Lipase","*WBC","*Glucose","*Triglycerides",
  "Calcium || Calcium is LOW (hypocalcemia)."],
 "Also elevated ALT/AST and bilirubin. ABGs may show metabolic acidosis.")
q("pandx","Which imaging may be used to evaluate pancreatitis? "+SATA,
 ["*Abdominal ultrasound","*CT scan","*MRI","*ERCP",
  "HIDA scan only || HIDA is for gallbladder function."],
 "Diagnosis is based on history, risk factors, exam, labs and imaging.")

# ---------- care ----------
q("pancare","Why is a client with acute pancreatitis kept NPO?",
 ["*To rest the pancreas","To prepare for a Whipple || Not routine.","To prevent dumping syndrome || Not related.","To raise blood glucose || Not the reason."],
 "Plus IV opioids, IV fluids and electrolytes, glucose control, labs and VS monitoring.")
q("pancare","When is an NG tube used in pancreatitis?",
 ["*For vomiting or severe distention, to decompress an ileus","For every client || Not routine.","To give pancreatic enzymes || Not the purpose.","To give alcohol withdrawal meds || Not the purpose."],
 "Surgery may be needed to resect and debride infected, necrotic pancreas.")
q("pancare","Which discharge teaching is correct for pancreatitis? "+SATA,
 ["*Avoid alcohol and smoking","*Low-fat, high-protein diet","*Monitor blood glucose","*Seek help for worsening pain, fever or jaundice",
  "High-fat diet to rebuild weight || Low-fat diet."],
 "Enzyme supplementation for chronic pancreatitis.")

# ---------- Creon ----------
q("creon","When should a client take pancreatic enzymes (Creon)?",
 ["Once daily at bedtime || Not the instruction.","*With every meal and snack",
  "Only when stools are fatty || Taken routinely with food.","On an empty stomach || Taken with food."],
 "Creon contains lipase (fats), amylase (carbohydrates) and protease (proteins).")
q("creon","A client on Creon has trouble swallowing capsules. What should the nurse teach?",
 ["Crush the capsule and mix with water || Don't crush or chew.","*Sprinkle the contents on an acidic soft food like applesauce",
  "Chew the capsule well || Don't chew.","Skip the dose || Needed with every meal."],
 "Swallow whole; sprinkling on acidic soft food is allowed if swallowing is hard.")
q("creon","Which findings show pancreatic enzyme replacement is working? "+SATA,
 ["*Less steatorrhea","*Weight gain","*Less bloating",
  "Higher lipase level || Not the effectiveness measure.","More frequent fatty stools || Shows it isn't working."],
 "Adjust dose if symptoms persist.")
q("creon","Which enzyme in Creon breaks down fats?",
 ["Amylase || Carbohydrates.","Protease || Proteins.","*Lipase","Trypsin inhibitor || Not in Creon."],
 "Creon is a pancreatic enzyme replacement therapy (PERT).")

# ---------- pancreatic cancer ----------
q("pcsx","What is the classic presenting sign of pancreatic cancer in the head of the pancreas?",
 ["Murphy's sign || Cholecystitis.","*Painless jaundice with dark urine",
  "Severe epigastric pain after a binge || Acute pancreatitis.","Bloody diarrhea || Not taught."],
 "The tumor obstructs the ducts. Clients usually seek care because of jaundice.")
q("pcsx","Which are risk factors for pancreatic cancer? "+SATA,
 ["*Smoking","*Chronic pancreatitis","*Diabetes","*High red-meat intake","*Older age and male sex",
  "High-fiber diet || Not a listed risk."],
 "Also chemical exposure and family history. It's a leading cause of cancer deaths in the U.S.")
q("pcsx","Which findings suggest pancreatic cancer? "+SATA,
 ["*Unexplained weight loss","*Dull abdominal pain radiating to the back","*New-onset diabetes","*Steatorrhea",
  "Inspiratory arrest with RUQ palpation || Murphy's sign, cholecystitis."],
 "Usually discovered late; most commonly adenocarcinoma in the head of the pancreas.")

q("pcdx","Which tumor markers are elevated in pancreatic cancer? "+SATA,
 ["*CA 19-9","*CEA",
  "BNP || Heart failure.","PSA || Prostate.","Troponin || Cardiac."],
 "Also elevated amylase, lipase and alkaline phosphatase.")
q("pcdx","What is the best imaging for visualizing a pancreatic tumor?",
 ["*CT or MRI with contrast","HIDA scan || Gallbladder function.","Plain abdominal x-ray || Not the best.","ECG || Not imaging."],
 "PET scans may also be used.")

# ---------- Whipple ----------
q("whipple","What does the Whipple procedure (pancreaticoduodenectomy) remove?",
 ["*Head of the pancreas, duodenum, gallbladder and bile duct","The whole stomach only || Gastrectomy.","The appendix || Appendectomy.","The colon || Not the Whipple."],
 "The remaining organs are reconnected so food can move through. Increasingly done robotically or laparoscopically.")
q("whipple","After a Whipple, the drain output is high and has high amylase. What should the nurse suspect?",
 ["Bile leak || Shows bilious drainage.","*Pancreatic fistula","Normal output || Report high-amylase output.","DVT || Not a drain finding."],
 "Monitor drain amount and color.")
q("whipple","Bilious drainage appears in a surgical drain after a Whipple. What does this suggest?",
 ["*Bile leak","Pancreatic fistula || High-amylase output.","Delayed gastric emptying || Managed with NPO and NG.","Expected serous drainage || Bilious isn't expected."],
 "Report unexpected drain output promptly.")
q("whipple","Which nursing measures prevent DVT/PE after a Whipple? "+SATA,
 ["*Early ambulation","*SCDs","*Anticoagulants if ordered",
  "Strict bedrest || Increases DVT risk.","Keep knees elevated on pillows all day || Not a DVT prevention measure."],
 "Priorities: complications, pain, nutrition/GI function, infection control, teaching.")
q("whipple","Match each Whipple complication to its nursing check. Which pairs are correct? "+SATA,
 ["*Hemorrhage: vitals, drain output, H&H","*Infection: temperature, WBC, wound and drain site","*Delayed gastric emptying: NPO initially, possible NG tube",
  "Pancreatic fistula: monitor blood glucose only || Monitor drain amount/color and high-amylase output."],
 "Unexpected drain output, bleeding, fever or hemodynamic changes after a Whipple → prompt evaluation.")

# ---------- Murphy's vs McBurney's (professor: both will appear as choices) ----------
q("gbsx","A client with suspected gallbladder disease is being examined. Which finding supports cholecystitis rather than appendicitis?",
 ["Tenderness at McBurney's point || That's appendicitis (RLQ).","*Positive Murphy's sign",
  "Pain moving from the umbilicus to the RLQ || Appendicitis.","LLQ tenderness || Diverticulitis."],
 "Murphy's sign: inspiratory arrest during RUQ palpation = cholecystitis.")
q("gbsx","Which statement about Murphy's sign and McBurney's point is correct?",
 ["*Murphy's sign suggests cholecystitis; McBurney's point tenderness suggests appendicitis",
  "Both suggest appendicitis || Murphy's is gallbladder.","Both suggest cholecystitis || McBurney's is appendix.",
  "Murphy's suggests appendicitis; McBurney's suggests cholecystitis || Reversed."],
 "Murphy = RUQ gallbladder. McBurney = RLQ appendix.")
