# Week 10.3 Infection of the Digestive System — Prof. Hanikeh's PowerPoint + lesson plan.
T = "digest"
CONCEPTS = {
 "gbpatho":"Cholecystitis: patho & types (FOCUS)",
 "gbrisk":"Gallstone risk factors (4 F's)",
 "gbsx":"Cholecystitis signs & Murphy's sign (FOCUS)",
 "gbdx":"Gallbladder labs & imaging (FOCUS)",
 "ducts":"MRCP vs ERCP vs HIDA",
 "gbtx":"Cholecystitis treatment & cholecystectomy (FOCUS)",
 "gbcomp":"Gallbladder complications to escalate (FOCUS)",
 "panpatho":"Pancreatitis: autodigestion (FOCUS)",
 "panrisk":"Pancreatitis causes (FOCUS)",
 "pansx":"Acute vs chronic pancreatitis findings (FOCUS)",
 "panmon":"Pancreatitis complications to monitor (FOCUS)",
 "pandx":"Pancreatitis labs & imaging (FOCUS)",
 "pancare":"Pancreatitis care & teaching (FOCUS)",
 "creon":"Pancreatic enzymes (Creon)",
 "pcsx":"Pancreatic cancer risks & signs",
 "pcdx":"Pancreatic cancer diagnosis & treatment",
 "whipple":"Whipple procedure complications",
}
# VERSION 2 (Nov 8): every question re-worded with new scenarios/distractors.
# Classmate update (Nov 3): pancreatitis and cholecystitis are tested -> focus.
HI = ["gbpatho","gbsx","gbdx","gbtx","gbcomp","panpatho","panrisk","pansx","panmon","pandx","pancare","creon","whipple"]

SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

# ---------- cholecystitis patho (FOCUS) ----------
q("gbpatho","What does the gallbladder do?",
 ["*Stores bile made by the liver and squeezes it into the duodenum after a fatty meal","Makes insulin || Pancreas.","Makes bile || The liver makes it.","Absorbs B12 || Ileum, with intrinsic factor."],
 "Bile helps digest fats.")
q("gbpatho","A gallstone blocks the cystic duct. What happens next?",
 ["*Bile is trapped, the gallbladder swells and inflames, and it can become ischemic or infected","The pancreas digests itself || Pancreatitis.",
  "Bile flows faster || It's trapped.","Nothing; stones always pass || Calculous cholecystitis develops."],
 "Calculous cholecystitis: about 90–95% of cases.")
q("gbpatho","An ICU client with sepsis and no gallstones develops cholecystitis. What type is this?",
 ["*Acalculous cholecystitis","Calculous cholecystitis || Needs a stone.","Pancreatitis || Different organ.","Appendicitis || Different organ."],
 "Acalculous (5–10%): bile stasis, ischemia, trauma or sepsis.")
q("gbpatho","When does the gallbladder squeeze hardest, often triggering pain in cholecystitis?",
 ["*After a fatty meal","During sleep || Not the trigger.","After drinking water || Not the trigger.","During exercise || Not the trigger."],
 "That's why pain often starts after fried or fatty food.")

# ---------- risk factors ----------
q("gbrisk","Which client fits the '4 F's' of gallstone risk?",
 ["*A 43-year-old woman with obesity who has had three children","A 20-year-old male athlete || Doesn't fit.","A 12-year-old girl || Doesn't fit.","A thin 30-year-old man || Doesn't fit."],
 "Female, Fat, Fertile, Forty.")
q("gbrisk","Which gallstone risk factors can the client CHANGE? "+SATA,
 ["*Obesity","*Crash dieting (rapid weight loss)","*A high-fat, low-fiber diet","*Taking oral contraceptives","Being female || Can't change.","Native American ethnicity || Can't change."],
 "The slide also lists pregnancy as modifiable.")
q("gbrisk","Why do pregnancy and birth control pills raise gallstone risk?",
 ["*Estrogen and progesterone make the gallbladder sluggish, so bile clumps","They block the pancreatic duct || Not the reason.","They raise fiber intake || Not the reason.","They destroy intrinsic factor || Not related."],
 "Hormones slow bile movement.")

# ---------- signs (FOCUS) ----------
q("gbsx","A 41-year-old with obesity has had right upper quadrant pain for 8 hours since eating fried chicken, and it spreads to the right shoulder. What does the nurse suspect?",
 ["*Acute cholecystitis","Acute pancreatitis || Epigastric pain to the back.","Appendicitis || RLQ.","GERD || Chest burning."],
 "RUQ pain lasting more than 6 hours, often after eating.")
q("gbsx","During RUQ palpation, the client suddenly catches their breath and stops inhaling. What is this?",
 ["*A positive Murphy's sign (cholecystitis)","McBurney's point (appendicitis) || RLQ.","Cullen's sign (pancreatitis) || Bruising.","Grey Turner's sign (pancreatitis) || Flank bruising."],
 "Murphy = upper right = gallbladder.")
q("gbsx","Which findings fit acute cholecystitis? "+SATA,
 ["*RUQ pain spreading to the right shoulder","*Pain that worsens after eating","*Fever with nausea and vomiting","*Possible yellow skin","Lower left abdominal pain || Diverticulitis.","Painless jaundice with weight loss || Pancreatic cancer."],
 "Also a fast heart rate and a distended abdomen.")
q("gbsx","In the CHOLY mnemonic for cholecystitis, what does the 'L' stand for?",
 ["*Leukocytosis (high WBC)","Left-sided pain || Pain is right-sided.","Low-grade fever only || H is high fever.","Lipase || Pancreatitis."],
 "C: colicky RUQ pain · H: high fever · O: obstructed bile · L: leukocytosis · Y: yellow.")
q("gbsx","Which finding points to cholecystitis rather than appendicitis?",
 ["*A positive Murphy's sign","Tenderness at McBurney's point || Appendicitis.","Pain moving from the belly button to the RLQ || Appendicitis.","LLQ tenderness || Diverticulitis."],
 "Know both: they'll appear together as answer choices.")
q("gbsx","Which statement is correct?",
 ["*Murphy's sign = cholecystitis; McBurney's point = appendicitis","Both point to appendicitis || Murphy is gallbladder.","Both point to cholecystitis || McBurney is appendix.","Murphy = appendicitis; McBurney = cholecystitis || Reversed."],
 "Murphy = upper right. McBurney = lower right.")

# ---------- diagnosis (FOCUS) ----------
q("gbdx","Which test is done FIRST when cholecystitis is suspected?",
 ["*Abdominal ultrasound","HIDA scan || If ultrasound is unclear.","ERCP || Invasive; treats duct stones.","CT || For complications."],
 "Ultrasound: stones, a thick gallbladder wall, fluid around it.")
q("gbdx","The ultrasound is unclear. Which test does the nurse expect next?",
 ["*HIDA scan","ERCP || Not the next step.","Colonoscopy || Not related.","Chest x-ray || Not related."],
 "HIDA evaluates gallbladder function and bile flow.")
q("gbdx","The HIDA scan report says the gallbladder did not fill. What does this mean?",
 ["*Positive for acute cholecystitis (the cystic duct is blocked)","Normal || Non-filling is abnormal.","The test failed || Not the meaning.","Pancreatic cancer || Not what HIDA shows."],
 "Non-visualization = cystic duct obstruction.")
q("gbdx","Which lab results are expected with cholecystitis? "+SATA,
 ["*High WBC","*High CRP","*Slightly high AST, ALT and ALP","*High bilirubin if the common bile duct is blocked","A low WBC || WBC rises."],
 "Fever is common.")

# ---------- MRCP / ERCP / HIDA ----------
q("ducts","Which procedure can both see AND remove gallstones stuck in the ducts?",
 ["*ERCP","MRCP || Images only.","HIDA || Function only.","Ultrasound || Images only."],
 "MRCP images; ERCP can treat.")
q("ducts","Which test gives detailed images of the bile and pancreatic ducts WITHOUT a scope?",
 ["*MRCP","ERCP || Uses a scope.","HIDA || Function, not anatomy.","Whipple || A surgery."],
 "Think 'image vs treat.'")
q("ducts","Which complication should the nurse watch for after an ERCP?",
 ["*Pancreatitis","Dumping syndrome || After gastric surgery.","Pernicious anemia || Not related.","Appendicitis || Not related."],
 "Post-ERCP pancreatitis is a listed cause.")

# ---------- treatment (FOCUS) ----------
q("gbtx","A client is admitted with acute cholecystitis. Which orders does the nurse expect? "+SATA,
 ["*NPO","*IV fluids","*Pain medicine","*IV antibiotics such as ceftriaxone with metronidazole","A high-fat meal || Triggers pain."],
 "Surgery: laparoscopic cholecystectomy, usually within 48 hours.")
q("gbtx","A client is confirmed to have acute cholecystitis. What is the IMMEDIATE diet order?",
 ["*NPO","Low-fat diet || Later.","Regular diet || Not now.","Clear liquids with cream || Not appropriate."],
 "NPO rests the gallbladder.")
q("gbtx","What diet should a client follow after cholecystectomy?",
 ["*Low-fat for 4–6 weeks","High-fat to stimulate bile || Not taught.","No restrictions || Restrict fat.","Liquids only for 6 months || Not taught."],
 "The body adjusts to bile flowing straight from the liver.")
q("gbtx","After a cholecystectomy, which problems does the nurse watch for? "+SATA,
 ["*Pain","*Bleeding","*Infection","*Breathing problems","Gum overgrowth || Not related."],
 "Laparoscopic: CO2 inflation and small puncture sites. Open: right-side incision with a drain.")
q("gbtx","A client with cholecystitis is too unstable for surgery. What may be done instead?",
 ["*Percutaneous cholecystostomy (a drain into the gallbladder)","Whipple procedure || Pancreatic cancer.","Fundoplication || Hiatal hernia.","Appendectomy || Not related."],
 "Stable clients get laparoscopic surgery.")

# ---------- complications (FOCUS) ----------
q("gbcomp","A client with cholecystitis becomes confused, with a rigid abdomen and BP 86/50. What should the nurse do?",
 ["*Notify the provider immediately; suspect perforation or sepsis","Give pain medicine and recheck later || An emergency.","Start a low-fat diet || Not the priority.","Apply heat || Not indicated."],
 "Escalate: rigid abdomen, rebound, jaundice, mental status changes, fever, low BP.")
q("gbcomp","Why are lipase and amylase checked in a client with cholecystitis?",
 ["*To rule out pancreatitis","To check the kidneys || BUN/creatinine.","To check B12 || Not related.","To check clotting || Not related."],
 "A gallstone can also block the pancreatic duct.")
q("gbcomp","Which findings in a cholecystitis client need escalation? "+SATA,
 ["*New jaundice","*Rebound tenderness","*Low blood pressure","*New confusion","Mild nausea that's improving || Not a red flag."],
 "Signs of perforation, obstruction or sepsis.")

# ---------- pancreatitis patho (FOCUS) ----------
q("panpatho","A client asks what is happening in pancreatitis. What is the best answer?",
 ["*Digestive enzymes turn on inside the pancreas and start digesting it","Bile is trapped in the gallbladder || Cholecystitis.","The stomach lining erodes || PUD.","The appendix is blocked || Appendicitis."],
 "This is called autodigestion.")
q("panpatho","Which enzyme does the lecture name as digesting the pancreas itself?",
 ["*Trypsin","Pepsin || Stomach.","Lactase || Not named.","Insulin || A hormone."],
 "Enzymes and bile back up into the pancreas.")
q("panpatho","What sequence describes acute pancreatitis?",
 ["*A trigger (gallstone or alcohol) → enzymes activate early → the pancreas digests itself → inflammation, possible necrosis and infection","Infection → stones → pain || Not the sequence.",
  "Low insulin → ketones → acidosis || That's DKA.","Acid reflux → ulcer → bleed || Not pancreatitis."],
 "Can trigger a body-wide inflammatory response.")

# ---------- causes (FOCUS) ----------
q("panrisk","What are the two MOST common causes of pancreatitis?",
 ["*Gallstones and alcohol","Mumps and trauma || Less common.","Smoking and tumors || Less common.","Genetics and autoimmune disease || Less common."],
 "Gallstones block the duct; alcohol damages the cells.")
q("panrisk","A client with a triglyceride level of 1,200 mg/dL is at risk for which condition?",
 ["*Acute pancreatitis","Appendicitis || Not related.","Hiatal hernia || Not related.","Pernicious anemia || Not related."],
 "Triglycerides over 1,000 can trigger pancreatitis.")
q("panrisk","Which can trigger pancreatitis? "+SATA,
 ["*Thiazide diuretics or corticosteroids","*Valproic acid","*An ERCP","*Abdominal trauma","*Mumps","A low-fat diet || Recommended."],
 "10–20% of cases have no known cause.")
q("panrisk","A client who drinks a fifth of vodka daily and a client with gallstones are both at risk for which condition?",
 ["*Pancreatitis","Appendicitis || Not caused this way.","Diverticulitis || Not caused this way.","Gastroenteritis || Infectious."],
 "The top two causes.")

# ---------- acute vs chronic (FOCUS) ----------
q("pansx","A client has sudden, severe pain in the upper middle abdomen that bores through to the back after a night of heavy drinking. What is the likely diagnosis?",
 ["*Acute pancreatitis","Cholecystitis || RUQ to the right shoulder.","Appendicitis || RLQ.","Diverticulitis || LLQ."],
 "Also nausea, vomiting, fever, fast heart rate and possibly a rigid abdomen.")
q("pansx","A client with pancreatitis has bluish bruising around the belly button. What is this called?",
 ["*Cullen's sign","Grey Turner's sign || Flank bruising.","Murphy's sign || Cholecystitis.","McBurney's point || Appendicitis."],
 "Cullen's = belly button; Grey Turner's = flanks.")
q("pansx","A client with pancreatitis has bluish bruising on the flanks. What is this called?",
 ["*Grey Turner's sign","Cullen's sign || Around the belly button.","Murphy's sign || Cholecystitis.","Homan's sign || Not related."],
 "Both mean bleeding into the tissues.")
q("pansx","Which findings suggest CHRONIC pancreatitis? "+SATA,
 ["*Fatty, foul-smelling stools","*Weight loss","*New diabetes","*Ongoing abdominal pain","Murphy's sign || Cholecystitis."],
 "The damaged pancreas makes too few enzymes and too little insulin.")
q("pansx","Why do clients with chronic pancreatitis often develop diabetes?",
 ["*Damage to the pancreas reduces insulin production","Too much bile || Not the reason.","High fiber intake || Not the reason.","Steroids only || Not the main reason."],
 "Glucose monitoring is part of the teaching.")

# ---------- complications (FOCUS) ----------
q("panmon","A client with acute pancreatitis becomes cold and clammy with BP 82/48 and HR 128. What is happening?",
 ["*Hypovolemic shock from fluid shifting into the abdomen","Expected pain response || Shock signs.","Low blood sugar || Glucose rises.","Dumping syndrome || Not related."],
 "Escalate right away.")
q("panmon","A client with pancreatitis is suddenly short of breath with an O2 sat of 87%. What should the nurse do?",
 ["*Escalate urgently; respiratory distress is a complication","Give more pain medicine and recheck later || Not routine.","Encourage oral fluids || NPO.","Document as expected || A red flag."],
 "Pleural effusions and infiltrates can develop.")
q("panmon","Which complications should the nurse watch for in acute pancreatitis? "+SATA,
 ["*Shock","*Acute kidney injury","*Breathing trouble with pleural effusions","*Low calcium","Hyperactive bowel sounds from overeating || NPO; ileus is the concern."],
 "Low calcium can lead to clotting problems and DIC.")
q("panmon","A client with pancreatitis has a low calcium level. Which complication does the lecture link to this?",
 ["*Clotting problems and DIC","Gum overgrowth || Phenytoin.","Barrett's esophagus || GERD.","Dumping syndrome || Not related."],
 "Monitor electrolytes often.")
q("panmon","Which findings in pancreatitis need URGENT escalation? "+SATA,
 ["*Low blood pressure","*Low O2 sat","*Falling urine output","*New breathing trouble","Pain of 6/10 that is improving with IV opioids || Expected."],
 "Not routine pain management.")

# ---------- labs & imaging (FOCUS) ----------
q("pandx","Which lab results confirm acute pancreatitis?",
 ["*High lipase and amylase","Low WBC || WBC rises.","High troponin || Heart.","Low glucose || Glucose rises."],
 "Lipase is the more specific test.")
q("pandx","Which labs are HIGH in acute pancreatitis? "+SATA,
 ["*Lipase","*Amylase","*WBC","*Glucose","*Triglycerides","Calcium || Calcium is low."],
 "Also AST, ALT and bilirubin.")
q("pandx","Which imaging can be used to evaluate pancreatitis? "+SATA,
 ["*Abdominal ultrasound","*CT scan","*MRI","*ERCP","A HIDA scan only || Gallbladder function."],
 "Diagnosis combines history, exam, labs and imaging.")

# ---------- care (FOCUS) ----------
q("pancare","A client with acute pancreatitis asks for breakfast. What should the nurse say?",
 ["*You'll stay NPO for now so the pancreas can rest","A high-fat meal will give you energy || Stimulates the pancreas.","Eat whatever you like || Not yet.","Drink some juice only || NPO."],
 "Initial care: NPO, IV fluids, IV pain control, glucose control, frequent labs.")
q("pancare","Which initial orders are expected for acute pancreatitis? "+SATA,
 ["*NPO","*IV fluids and electrolytes","*IV opioids for pain","*Blood glucose monitoring","A high-fat diet || Stimulates the pancreas."],
 "Frequent labs and vital signs.")
q("pancare","When does a client with pancreatitis need an NG tube?",
 ["*For vomiting or severe abdominal swelling (ileus)","For every client || Not routine.","To give Creon || Not the purpose.","To give alcohol || Never."],
 "Surgery may be needed to remove dead, infected tissue.")
q("pancare","Which discharge statement shows correct pancreatitis teaching?",
 ["*I'll stop drinking and smoking and eat low-fat, high-protein meals","I'll have a beer now and then || Avoid alcohol.","I'll eat high-fat food to gain weight || Low-fat.","I don't need to check my sugar || Glucose monitoring is taught."],
 "Report worsening pain, fever or jaundice.")
q("pancare","Which discharge teaching is correct for pancreatitis? "+SATA,
 ["*Avoid alcohol","*Stop smoking","*Low-fat, high-protein diet","*Check blood sugar","*Report pain, fever or yellow skin","Eat a high-fat diet || Low-fat."],
 "Chronic pancreatitis needs enzyme replacement.")

# ---------- Creon ----------
q("creon","A client with chronic pancreatitis is prescribed pancrelipase (Creon). When is it taken?",
 ["*With every meal and snack","Once a day at bedtime || Not the instruction.","Only when stools are greasy || Routinely with food.","On an empty stomach || With food."],
 "These clients lack the enzymes; Creon replaces them.")
q("creon","A client can't swallow Creon capsules. What should the nurse teach?",
 ["*Open the capsule and sprinkle it on an acidic soft food like applesauce","Crush it in water || Don't crush.","Chew it || Don't chew.","Skip it || Needed with meals."],
 "Swallow whole whenever possible.")
q("creon","Which findings show Creon is working? "+SATA,
 ["*Fewer fatty stools","*Weight gain","*Less bloating","A higher lipase level || Not the measure.","More greasy stools || Not working."],
 "The dose may be adjusted if symptoms continue.")
q("creon","Which enzyme in Creon breaks down FAT?",
 ["*Lipase","Amylase || Carbohydrates.","Protease || Proteins.","Insulin || A hormone."],
 "Amylase = carbs; protease = protein.")

# ---------- pancreatic cancer ----------
q("pcsx","A 70-year-old smoker has yellow skin, dark urine and no pain. What does the nurse suspect?",
 ["*Pancreatic cancer in the head of the pancreas","Cholecystitis || Painful.","Acute pancreatitis || Very painful.","Appendicitis || RLQ pain."],
 "Painless jaundice is the classic sign.")
q("pcsx","Which are risk factors for pancreatic cancer? "+SATA,
 ["*Smoking","*Chronic pancreatitis","*Diabetes","*A diet high in red meat","*Older age","A high-fiber diet || Not a risk."],
 "Also male sex, chemical exposure and family history.")
q("pcsx","Which findings suggest pancreatic cancer? "+SATA,
 ["*Unexplained weight loss","*Dull pain that spreads to the back","*New diabetes","*Fatty stools","Murphy's sign || Cholecystitis."],
 "Usually found late.")
q("pcdx","Which tumor markers are high in pancreatic cancer? "+SATA,
 ["*CA 19-9","*CEA","BNP || Heart failure.","PSA || Prostate.","Troponin || Heart."],
 "Also amylase, lipase and alkaline phosphatase.")
q("pcdx","Which imaging best shows a pancreatic tumor?",
 ["*CT or MRI with contrast","A HIDA scan || Gallbladder.","A plain x-ray || Not the best.","An ECG || Not imaging."],
 "PET scans may also be used.")

# ---------- Whipple ----------
q("whipple","A client asks what the Whipple procedure removes. What is the answer?",
 ["*The head of the pancreas, the duodenum, the gallbladder and the bile duct","The whole stomach only || Gastrectomy.","The appendix || Appendectomy.","The colon || Not the Whipple."],
 "The remaining organs are reconnected.")
q("whipple","After a Whipple, the drain output is large and tests high in amylase. What does the nurse suspect?",
 ["*A pancreatic fistula","A bile leak || Bilious drainage.","Normal drainage || Report it.","A DVT || Not a drain finding."],
 "Watch drain amount and color.")
q("whipple","After a Whipple, the drain shows greenish-yellow bile. What does this suggest?",
 ["*A bile leak","A pancreatic fistula || High-amylase drainage.","Normal drainage || Not expected.","Delayed gastric emptying || Not a drain finding."],
 "Report unexpected drain output right away.")
q("whipple","How does the nurse prevent clots after a Whipple? "+SATA,
 ["*Early walking","*SCDs","*Anticoagulants if ordered","Strict bedrest || Raises clot risk.","Pillows under the knees all day || Not prevention."],
 "Also watch for bleeding, infection and fistula.")
q("whipple","Which Whipple complication and nursing check are matched correctly? "+SATA,
 ["*Bleeding: vitals, drain output, H&H","*Infection: temperature, WBC, wound","*Delayed gastric emptying: NPO at first, possibly an NG tube","Pancreatic fistula: check blood glucose only || Check drain amount, color and amylase."],
 "Report fever, bleeding or unexpected drain output.")
