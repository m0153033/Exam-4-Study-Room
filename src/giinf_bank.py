# Week 10.2 Gastrointestinal Infections (17 core conditions) — professor's PowerPoint.
T = "giinf"
CONCEPTS = {
 "hh":"Hiatal hernia: patho & types (FOCUS)",
 "hh2":"Hiatal hernia: signs & care (FOCUS)",
 "gerd":"GERD: cause & signs (FOCUS)",
 "gerd2":"GERD: complications & teaching (FOCUS)",
 "meds":"GI meds: PPIs & H2 blockers (FOCUS)",
 "meds2":"GI meds: sucralfate, antacids, metoclopramide (FOCUS)",
 "barrett":"Barrett's esophagus",
 "gastritis":"Gastritis: causes & types (FOCUS)",
 "gastritis2":"Gastritis: bleeding & care (FOCUS)",
 "pud":"PUD: causes & gastric vs duodenal (FOCUS)",
 "pud2":"PUD: complications & care (FOCUS)",
 "gcancer":"Gastric cancer signs (FOCUS)",
 "enteral":"Enteral nutrition",
 "tpn":"PPN / TPN",
 "dumping":"Dumping syndrome",
 "pernicious":"Pernicious anemia",
 "gastro":"Gastroenteritis",
 "append":"Appendicitis: cause & pain pattern (FOCUS)",
 "append2":"Appendicitis: nursing care & rupture (FOCUS)",
 "divert":"Diverticulitis",
 "perf":"Perforation",
 "periton":"Peritonitis",
 "sepsis":"Sepsis",
 "signs":"Murphy's vs McBurney's",
}
# VERSION 2 (Nov 8): every question re-worded with new scenarios/distractors.
# Classmate update (Nov 3): appendicitis also tested; esophageal cancer NOT tested.
# Professor: GERD, hiatal hernia, gastritis and PUD are the FOCUS conditions (in depth); the other 13 are need-to-know basics.
HI = ["hh","hh2","gerd","gerd2","meds","meds2","gastritis","gastritis2","pud","pud2","append","append2","tpn","signs","gcancer"]

SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

# ---------- hiatal hernia (FOCUS) ----------
q("hh","A client asks what a hiatal hernia is. What is the best explanation?",
 ["*Part of the stomach pushes up through the opening in the diaphragm into the chest","A pouch in the colon wall || Diverticulosis.",
  "An inflamed appendix || Appendicitis.","Changed cells in the lower esophagus || Barrett's esophagus."],
 "Two types: sliding (about 95%) and paraesophageal (rolling).")
q("hh","Which type of hiatal hernia is most common, and which is more likely to strangulate?",
 ["*Sliding is most common; paraesophageal (rolling) is more likely to strangulate","Rolling is most common; sliding strangulates || Reversed.",
  "Both are equally common || Sliding is about 95%.","Neither can strangulate || Rolling can."],
 "In a rolling hernia, the fundus rolls up beside the esophagus.")
q("hh","In a SLIDING hiatal hernia, what moves up into the chest?",
 ["*The stomach and the gastroesophageal (GE) junction","Only the fundus, beside the esophagus || Rolling hernia.","The colon || Not related.","The gallbladder || Not related."],
 "Sliding hernias are worse when lying flat.")
q("hh","Which clients are at higher risk for a hiatal hernia? "+SATA,
 ["*A pregnant client","*A client with obesity","*A client who lifts heavy boxes at work","*An older adult","A client who eats a high-fiber diet || Not a risk factor."],
 "Anything that raises abdominal pressure or weakens the diaphragm.")
q("hh","When are hiatal hernia symptoms usually worse?",
 ["*Lying flat and after big meals","Sitting upright || Upright helps.","Only in the morning || Not the pattern.","During light walking || Not the pattern."],
 "Symptoms: heartburn, regurgitation, trouble swallowing, fullness or belching.")
q("hh2","A client with a hiatal hernia likes to lie on the couch right after dinner. What should the nurse teach?",
 ["*Stay upright for 1–2 hours after eating","Lie on the left side after dinner || Stay upright.","Lie down to help digestion || Worsens reflux.","Take a walk then lie flat || Stay upright."],
 "Gravity is the first-line defense against reflux.")
q("hh2","Which interventions help a client with a hiatal hernia? "+SATA,
 ["*Small, frequent meals","*Raise the head of the bed","*Lose weight","*Avoid tight waistbands","*Avoid straining and heavy lifting","Eat one large meal at bedtime || Worsens reflux."],
 "Severe hernias may need fundoplication surgery.")
q("hh2","A client with a hiatal hernia has substernal chest pain. Why does the nurse take it seriously?",
 ["*Hernia pain can look like heart pain, so a cardiac cause must be ruled out","It always means strangulation || Not always.","It's never related to the hernia || It can be.","It means GERD only || Not the point."],
 "Rule out the heart first.")
q("hh2","What diet teaching follows a fundoplication? "+SATA,
 ["*Start with liquids and advance to soft foods","*Take small bites and chew well","*Avoid swallowing air","Drink soda to relieve bloating || Adds gas."],
 "Plus routine post-op care.")

# ---------- GERD (FOCUS) ----------
q("gerd","What is the underlying problem in GERD?",
 ["*A weak lower esophageal sphincter lets stomach contents flow back up","H. pylori in the duodenum || PUD.","No intrinsic factor || Pernicious anemia.","A blocked appendix || Appendicitis."],
 "Backflow burns the esophageal lining.")
q("gerd","A client reports a burning feeling behind the breastbone after big meals that is worse lying down. What is this?",
 ["*Heartburn (pyrosis), the classic GERD symptom","Murphy's sign || Cholecystitis.","McBurney's point pain || Appendicitis.","Dumping syndrome || After gastric surgery."],
 "Also sour regurgitation, hoarseness, chronic cough and trouble swallowing.")
q("gerd","Which findings fit GERD? "+SATA,
 ["*Heartburn","*A sour taste from regurgitation","*Chronic cough or hoarseness","*Painful or difficult swallowing","Pain in the lower right abdomen || Appendicitis."],
 "Worse after meals and when lying flat.")
q("gerd","Which are risk factors for GERD? "+SATA,
 ["*A hiatal hernia","*Obesity","*Smoking and alcohol","*Chocolate, caffeine, and fatty or spicy foods","*Pregnancy"],
 "Delayed gastric emptying also contributes.")
q("gerd2","Which complications can untreated GERD cause? "+SATA,
 ["*Barrett's esophagus","*Narrowing of the esophagus (stricture)","*Aspiration pneumonia","*Tooth enamel erosion","Pernicious anemia || Not a GERD complication."],
 "Also esophagitis and laryngitis.")
q("gerd2","Which teaching is correct for GERD? "+SATA,
 ["*Don't lie down for 2–3 hours after eating","*Raise the head of the bed about 30 degrees","*Eat small, low-fat meals","*Quit smoking and lose weight","Have a coffee after dinner || A trigger."],
 "Teach adherence; feeling better doesn't mean healed.")
q("gerd2","A client with GERD stopped their PPI because the heartburn went away. What should the nurse explain?",
 ["*Damage can continue without symptoms, so keep taking it as prescribed","That's fine once symptoms stop || Symptoms can hide damage.",
  "Take it only when it burns || Not the teaching.","PPIs only help the stomach || Not accurate."],
 "Untreated GERD can lead to strictures and Barrett's esophagus.")

# ---------- GI meds (FOCUS) ----------
q("meds","When should a client take omeprazole or pantoprazole?",
 ["*30–60 minutes before the first meal of the day","With dinner || Not the teaching.","At bedtime with a snack || Not the teaching.","1–3 hours after meals || That's antacids."],
 "A common test point.")
q("meds","A client has taken a PPI for years. Which problems should the nurse watch for? "+SATA,
 ["*Weak bones (osteoporosis)","*Low magnesium","Tardive dyskinesia || Metoclopramide.","Higher warfarin levels || Cimetidine."],
 "PPIs reduce stomach acid secretion.")
q("meds","How do PPIs work?",
 ["*They stop the stomach from secreting acid, raising the pH","They neutralize acid already there || Antacids.","They coat the ulcer || Sucralfate.","They speed stomach emptying || Metoclopramide."],
 "Pantoprazole, omeprazole: -prazole.")
q("meds","How does famotidine (Pepcid) work?",
 ["*It blocks histamine receptors so less acid is made","It blocks the proton pump || PPIs.","It neutralizes acid || Antacids.","It coats the stomach || Sucralfate."],
 "H2 blockers can be taken with or without food.")
q("meds","A client on warfarin is started on cimetidine. What should the nurse watch for?",
 ["*Bleeding, because cimetidine raises warfarin levels","Low blood sugar || Not listed.","Tardive dyskinesia || Metoclopramide.","Bone loss || PPIs."],
 "Cimetidine also raises phenytoin levels.")
q("meds2","How should sucralfate (Carafate) be taken?",
 ["*On an empty stomach before meals, apart from other medications","With meals || Empty stomach.","Mixed with antacids || Separate them.","Only at bedtime with food || Not the instruction."],
 "It forms a gel coating over the ulcer; it isn't absorbed into the body.")
q("meds2","A client on metoclopramide for 5 months has lip smacking and tongue thrusting. What does the nurse suspect?",
 ["*Tardive dyskinesia","Low magnesium || PPIs.","An expected effect || A serious adverse effect.","Dumping syndrome || Not related."],
 "Metoclopramide should not be used for more than 12 weeks.")
q("meds2","When should a client take an antacid like Mylanta?",
 ["*1–3 hours after eating, apart from other medications","30 minutes before breakfast || PPIs.","With all other pills || Blocks absorption.","Only once a week || Not the instruction."],
 "Antacids can cause diarrhea or constipation.")
q("meds2","Which drug NEUTRALIZES stomach acid that's already there?",
 ["*Aluminum hydroxide (Amphojel)","Famotidine || Reduces acid production.","Pantoprazole || Reduces acid production.","Metoclopramide || Moves food along."],
 "Antacids neutralize; H2 blockers and PPIs reduce secretion; sucralfate coats.")
q("meds2","A client takes sucralfate and three other morning pills. What should the nurse teach?",
 ["*Space the other pills apart from sucralfate, because it reduces their absorption","Take them all at once || Absorption drops.","Take sucralfate after meals || Empty stomach.","Crush sucralfate into food || Not the teaching."],
 "Sucralfate works locally.")

# ---------- Barrett's ----------
q("barrett","What happens in Barrett's esophagus?",
 ["*Long-term GERD changes the lower esophagus lining into intestinal-type cells","The esophagus becomes cancer right away || It's pre-malignant.","The stomach herniates || Hiatal hernia.","The stomach lining is inflamed || Gastritis."],
 "Raises the risk of esophageal adenocarcinoma.")
q("barrett","How is Barrett's esophagus monitored?",
 ["*Regular endoscopy with biopsy","Watching symptoms only || Not enough.","A yearly chest x-ray || Not the method.","Stool tests || Not related."],
 "Biopsy catches early dysplasia.")
q("barrett","A client with Barrett's esophagus reports new trouble swallowing. What does the nurse do?",
 ["*Report it; new dysphagia is a red flag","Reassure them it's normal heartburn || A red flag.","Suggest chewing gum || Not appropriate.","Wait until the next scope || Report now."],
 "Also report weight loss and bleeding.")
q("barrett","Which are risk factors for Barrett's esophagus? "+SATA,
 ["*Long-term, poorly controlled GERD","*Male, over age 50","*Obesity","*Smoking","A low-sodium diet || Not a risk factor."],
 "Also family history and chronic hiatal hernia.")

# ---------- gastritis (FOCUS) ----------
q("gastritis","A client takes ibuprofen daily and drinks heavily. Which condition are they at risk for?",
 ["*Gastritis","Appendicitis || Not caused this way.","Diverticulitis || Not caused this way.","Pernicious anemia || Not caused this way."],
 "Causes: NSAIDs and aspirin, alcohol, H. pylori, severe stress, bile reflux.")
q("gastritis","Which are causes of gastritis? "+SATA,
 ["*NSAIDs","*Alcohol","*H. pylori","*Severe burns or sepsis","A high-fiber diet || Not a cause."],
 "Remove the cause.")
q("gastritis","Which statement describes ACUTE gastritis?",
 ["*Sudden, caused by an irritant, and usually resolves once the irritant is removed","Long-term and H. pylori-driven || Chronic.","Always leads to cancer || Not acute.","Caused by a weak sphincter || GERD."],
 "Chronic gastritis can lead to atrophy and higher cancer risk.")
q("gastritis","Which findings are expected with gastritis? "+SATA,
 ["*Burning epigastric pain","*Nausea and vomiting","*Feeling full quickly","*Loss of appetite","Pain in the lower left abdomen || Diverticulitis."],
 "Bloody vomit or black stools mean bleeding.")
q("gastritis2","A client with gastritis vomits material that looks like coffee grounds. What does the nurse do first?",
 ["*Check vital signs and notify the provider right away","Give an antacid || Not the priority.","Offer crackers || Not with bleeding.","Recheck at the end of the shift || Act now."],
 "Coffee-ground emesis and tarry stools = GI bleeding.")
q("gastritis2","Which teaching fits gastritis? "+SATA,
 ["*Keep a food diary","*Eat a bland diet","*Avoid bedtime snacks","*Avoid alcohol, caffeine and smoking","*Lower stress","Use aspirin for the stomach pain || Remove NSAIDs."],
 "Treat H. pylori if present.")
q("gastritis2","What is the treatment plan for gastritis? "+SATA,
 ["*Stop the cause, such as NSAIDs or alcohol","*PPIs, H2 blockers or antacids","*Treat H. pylori if present","*Small, bland meals","Large, high-fat meals || Not taught."],
 "Monitor for signs of bleeding.")

# ---------- PUD (FOCUS) ----------
q("pud","A client's stomach pain gets WORSE 30–60 minutes after eating, and they've lost weight. Which ulcer is likely?",
 ["*Gastric ulcer","Duodenal ulcer || Food relieves duodenal pain.","GERD || Burning behind the breastbone.","Appendicitis || RLQ pain."],
 "Clients with gastric ulcers lose weight because eating hurts.")
q("pud","A client's stomach pain gets BETTER when they eat but returns 2–3 hours later and wakes them at night. Which ulcer is likely?",
 ["*Duodenal ulcer","Gastric ulcer || Food makes gastric pain worse.","Gastritis || Not this pattern.","Hiatal hernia || Not this pattern."],
 "Duodenal: food relieves; night pain is common.")
q("pud","What causes most peptic ulcers?",
 ["*H. pylori infection","A hiatal hernia || Not the main cause.","Low-fiber diet || Diverticulitis.","Low B12 || Not related."],
 "Also NSAIDs, smoking, alcohol and severe stress.")
q("pud","Which describes peptic ulcer disease?",
 ["*Erosion through the GI lining when acid outmatches the lining's defenses","An inflamed gallbladder || Cholecystitis.","A pouch in the colon || Diverticulosis.","Acid backflow into the esophagus || GERD."],
 "Curling's ulcers (burns) and Cushing's ulcers (head injury) are stress ulcers.")
q("pud2","A client with an ulcer suddenly has severe pain and a hard, board-like abdomen. What does the nurse suspect?",
 ["*Perforation, a surgical emergency","Needs an extra antacid || Not a med issue.","Normal ulcer pain || An emergency.","Dumping syndrome || Not related."],
 "Notify the provider immediately.")
q("pud2","Which complications of PUD should the nurse watch for? "+SATA,
 ["*Bleeding (bloody vomit or black stools)","*Perforation","*Obstruction","Barrett's esophagus || A GERD complication.","Appendicitis || Not related."],
 "Avoid NSAIDs, alcohol and smoking.")
q("pud2","A client with an ulcer asks what to take for a headache. What is the best answer?",
 ["*Avoid ibuprofen, naproxen and aspirin; ask your provider what's safe","Ibuprofen with food is fine || NSAIDs cause ulcers.","Aspirin is safest || Also damages the lining.","Naproxen at night is fine || An NSAID."],
 "NSAIDs are a major ulcer cause.")
q("pud2","How is an H. pylori ulcer treated?",
 ["*Triple or quadruple therapy plus a PPI","Surgery for every ulcer || Not first-line.","NSAIDs for pain || Cause ulcers.","Antacids alone || Don't kill H. pylori."],
 "Monitor for bleeding, perforation and obstruction.")
q("pud2","Where might peptic ulcer pain spread?",
 ["*To the back","To the right shoulder || Cholecystitis.","To the left arm || Heart.","To the lower right abdomen || Appendicitis."],
 "Burning, gnawing epigastric pain.")

# ---------- gastric cancer (FOCUS) ----------
q("gcancer","A 64-year-old has had vague indigestion for months, feels full after a few bites, and has lost 12 lb without trying. What does the nurse suspect?",
 ["*Gastric cancer","GERD || No weight loss pattern.","Appendicitis || Acute RLQ pain.","Gastroenteritis || Acute, with diarrhea."],
 "Early signs are vague, so it's often found late.")
q("gcancer","Which signs fit gastric cancer? "+SATA,
 ["*Vague indigestion","*Feeling full quickly","*Unplanned weight loss","*Anemia","*Epigastric pain"],
 "Diagnosis: endoscopy with biopsy.")
q("gcancer","Which are risk factors for gastric cancer? "+SATA,
 ["*H. pylori","*A diet of smoked, salted or preserved foods","*Smoking","*Pernicious anemia","A high-fiber diet || Not a risk factor."],
 "Also atrophic gastritis and family history.")
q("gcancer","Which test confirms gastric cancer?",
 ["*Upper endoscopy with biopsy","A stool culture || Not diagnostic.","A chest x-ray || Not diagnostic.","An abdominal exam at McBurney's point || Appendicitis."],
 "Then CT staging and treatment.")
q("gcancer","After a gastrectomy for cancer, which two problems does the nurse watch for long-term? "+SATA,
 ["*Dumping syndrome","*Vitamin B12 deficiency","Appendicitis || Not related.","GERD from a hernia || Not the focus."],
 "The cells that make intrinsic factor are removed, so B12 is lifelong.")

# ---------- enteral ----------
q("enteral","A new feeding tube has been placed. How is placement FIRST confirmed?",
 ["*X-ray","Checking the pH || For ongoing checks.","Listening for an air bolus || Not the method.","Asking the client to talk || Not a method."],
 "After that, check gastric pH and the tube markings before each use.")
q("enteral","Before giving a medication through a feeding tube, the aspirate pH is 3. What does this mean?",
 ["*The tube is likely in the stomach","The tube is in the lungs || Not likely with pH 3.","The tube is in the intestine || Intestinal pH is higher.","The tube must be replaced || pH under 5 supports placement."],
 "Gastric aspirate pH under 5 supports placement.")
q("enteral","How should a client receiving tube feedings be positioned?",
 ["*Head of bed at least 30 degrees during and for 30–60 minutes after","Flat || Aspiration risk.","On the left side flat || Not the position.","Head down || Aspiration risk."],
 "The core aspiration prevention measure.")
q("enteral","Which are complications of tube feeding? "+SATA,
 ["*Aspiration","*Diarrhea","*A clogged tube","*Bloating and high residuals","Gum overgrowth || Phenytoin."],
 "Flush before and after feeds and meds.")
q("enteral","What must a client have to receive enteral nutrition?",
 ["*A working GI tract","A central line || TPN.","A non-working gut || That's TPN.","Strict NPO || Not enteral."],
 "Used for trouble swallowing, neuro problems or poor intake.")

# ---------- PPN / TPN (professor: know the difference) ----------
q("tpn","Which statement correctly compares PPN and TPN?",
 ["*PPN: peripheral vein, short-term. TPN: central line, long-term, complete nutrition","PPN: central line; TPN: peripheral || Reversed.",
  "Both go into the stomach || That's enteral.","They're the same thing || They differ."],
 "Both bypass the GI tract.")
q("tpn","A client needs IV nutrition for 4 days and has only a peripheral IV. Which is appropriate?",
 ["*PPN","TPN || Needs a central line.","A PEG tube feeding || That's enteral, not IV.","Nothing can be given || PPN can."],
 "PPN = short-term, peripheral.")
q("tpn","A client with a bowel obstruction will need complete IV nutrition for weeks. Which is appropriate?",
 ["*TPN through a central line","PPN || Short-term only.","Tube feeding || The gut isn't working.","Clear liquids || Not complete nutrition."],
 "TPN is used when the gut can't be used.")
q("tpn","Which are true of BOTH PPN and TPN? "+SATA,
 ["*They bypass the GI tract","*They need strict aseptic technique","Both need a central line || Only TPN.","Both are long-term || PPN is short-term."],
 "Any parenteral line is an infection risk.")
q("tpn","Which statements about PPN and TPN are correct? "+SATA,
 ["*TPN goes through a central line","*PPN goes through a peripheral vein","*PPN is short-term","*TPN can provide complete nutrition long-term","TPN can run in any peripheral IV || Central line only."],
 "Know the difference.")
q("tpn","The TPN bag runs out and pharmacy needs an hour to send the next one. What is the biggest risk?",
 ["*Rebound hypoglycemia","Hyperglycemia || The opposite.","High potassium || Not the concern.","Dumping syndrome || Not related."],
 "Never stop TPN suddenly; taper it.")
q("tpn","Which nursing care fits TPN? "+SATA,
 ["*Strict aseptic technique","*Check blood glucose regularly","*Use a dedicated line","*Taper it, never stop suddenly","Push IV antibiotics through the TPN line || Dedicated line only."],
 "Complications: high or low glucose, line infection, fluid overload.")
q("tpn","A client on TPN has a fever and redness at the central line. What does the nurse suspect?",
 ["*A line infection","Low blood sugar || Not with fever and redness.","Dumping syndrome || Not related.","Fluid overload || Not with fever."],
 "TPN lines are a sepsis risk.")

# ---------- dumping ----------
q("dumping","Twenty minutes after lunch, a client who had a gastrectomy has cramping, diarrhea, sweating and a racing heart. What is this?",
 ["*Early dumping syndrome","Late dumping || 1–3 hours after eating.","Peritonitis || Rigid abdomen and fever.","Pernicious anemia || Develops slowly."],
 "Early (10–30 minutes): fluid shift into the intestine.")
q("dumping","Two hours after a meal, a client who had a gastrectomy is shaky, sweaty and confused. What is this?",
 ["*Late dumping with low blood sugar","Early dumping || Within 30 minutes.","Peritonitis || Not this picture.","A stroke || Check glucose first."],
 "Late (1–3 hours): reactive hypoglycemia.")
q("dumping","Which teaching helps prevent dumping syndrome? "+SATA,
 ["*Small, frequent meals","*Avoid sweets and simple sugars","*Separate liquids from solids by 30–45 minutes","*Lie down 20–30 minutes after eating","Drink a milkshake with lunch || Sugar plus fluid."],
 "More protein and fat helps; fiber supplements may too.")
q("dumping","Which surgeries can cause dumping syndrome? "+SATA,
 ["*Gastrectomy","*Gastric bypass","*Vagotomy or pyloroplasty","Appendectomy || Not a risk."],
 "Food empties too fast into the small intestine.")

# ---------- pernicious anemia ----------
q("pernicious","Why does pernicious anemia develop?",
 ["*Without intrinsic factor, vitamin B12 can't be absorbed","Too little iron || A different anemia.","Too much folate || Not the cause.","Bleeding ulcers || Not the cause."],
 "Causes: autoimmune, gastrectomy, atrophic gastritis.")
q("pernicious","Which findings suggest pernicious anemia? "+SATA,
 ["*A smooth, beefy red tongue","*Tingling in the hands and feet","*Trouble with balance","*Fatigue and pale skin","Lower right abdominal pain || Appendicitis."],
 "Labs: low B12, high MCV.")
q("pernicious","A client with pernicious anemia asks if eating more meat and eggs will fix it. What is the answer?",
 ["*No; you'll need lifelong B12 shots or high-dose pills, because your body can't absorb it from food","Yes, diet will fix it || No intrinsic factor.",
  "Only a short course of B12 is needed || Lifelong.","Iron pills will fix it || It's B12."],
 "Therapy is lifelong.")
q("pernicious","Why is early treatment of pernicious anemia so important?",
 ["*Nerve damage can become permanent","The tongue can rupture || Not a concern.","It causes perforation || Not related.","It causes dumping || Not related."],
 "Watch for falls from poor balance.")

# ---------- gastroenteritis ----------
q("gastro","A client with gastroenteritis has had vomiting and diarrhea for 2 days. What is the priority?",
 ["*Replace fluids and electrolytes","Give an antidiarrheal || Avoided in infection.","Start a high-fiber diet || Advance slowly.","Give a laxative || Not indicated."],
 "The fluid loss is the main danger.")
q("gastro","Which findings show dehydration? "+SATA,
 ["*Dry mouth","*Fast heart rate","*Less urine","*Poor skin turgor","A slow pulse with bounding pulses || Not dehydration."],
 "Young children and older adults are at highest risk.")
q("gastro","Which precautions are needed for infectious gastroenteritis?",
 ["*Contact precautions and hand hygiene","Airborne || Not the route.","Droplet only || Not the choice.","None || It spreads."],
 "Common causes: norovirus, rotavirus, E. coli, Salmonella, C. diff.")

# ---------- appendicitis (FOCUS) ----------
q("append","A 20-year-old's pain started around the belly button and now is sharp in the lower right abdomen. What is the likely cause?",
 ["*Appendicitis","Diverticulitis || Lower left.","Cholecystitis || Upper right.","GERD || Burning chest."],
 "Pain moves to McBurney's point.")
q("append","What usually causes appendicitis?",
 ["*A blockage of the appendix (a hard stool or swollen lymph tissue)","Pouches in the colon || Diverticulosis.","A gallstone || Cholecystitis.","Acid reflux || GERD."],
 "The blockage leads to swelling and bacterial overgrowth.")
q("append","Which findings fit appendicitis? "+SATA,
 ["*Rebound tenderness and guarding","*Low-grade fever","*Loss of appetite and nausea","*Pain at McBurney's point","Stops breathing in when the RUQ is pressed || Murphy's sign."],
 "Classic: belly button pain that moves to the RLQ.")
q("append","Which tests diagnose appendicitis?",
 ["*CT scan or ultrasound","HIDA scan || Gallbladder.","ERCP || Bile ducts.","Upper endoscopy || Esophagus and stomach."],
 "Treatment is an appendectomy.")
q("append","Which nursing actions are correct for suspected appendicitis? "+SATA,
 ["*Keep NPO","*Prepare for surgery","*Watch the pain trend","Give an enema || Can cause rupture.","Apply a heating pad || Can cause rupture."],
 "Concerns: abscess, perforation, peritonitis.")
q("append2","A client with suspected appendicitis asks for a laxative and a warm compress. What should the nurse do?",
 ["*Decline both; heat and laxatives can cause rupture","Give both || Both are risky.","Give the laxative only || Risky.","Give the compress only || Risky."],
 "Never heat, laxatives or enemas.")
q("append2","Which order should the nurse question for a client with suspected appendicitis?",
 ["*A soapsuds enema","NPO || Correct.","A CT scan || Correct.","IV fluids || Correct."],
 "Enemas raise pressure and can cause rupture.")
q("append2","A client with appendicitis says, 'My pain suddenly went from a 9 to a 1.' What does the nurse suspect?",
 ["*Rupture","It went away on its own || Sudden relief is a red flag.","The pain medicine worked || Not the concern.","Dumping syndrome || Not related."],
 "Rupture risk is highest 24–72 hours after symptoms start.")
q("append2","An hour after sudden pain relief, a client with appendicitis has a rigid abdomen and rising fever. What should the nurse do?",
 ["*Notify the provider immediately; suspect rupture with peritonitis","Give more pain medicine || Not the priority.","Encourage walking || Not appropriate.","Document as improving || Not improving."],
 "Peritonitis can progress to sepsis.")
q("append2","Why is a client with suspected appendicitis kept NPO?",
 ["*Because emergency surgery is expected","To rest the pancreas || Pancreatitis.","To prevent dumping || Not related.","NPO cures it || Surgery is the cure."],
 "Prepare for appendectomy.")

# ---------- diverticulitis ----------
q("divert","A client has lower LEFT abdominal pain, fever and a high WBC. What is likely?",
 ["*Diverticulitis","Appendicitis || Lower right.","Duodenal ulcer || Epigastric.","GERD || Chest burning."],
 "Also changes in bowel habits.")
q("divert","A client is admitted with a diverticulitis flare. Which diet does the nurse expect?",
 ["*NPO or clear liquids to rest the bowel","High fiber || After the flare.","Regular diet || Not yet.","High sugar || Not related."],
 "High fiber prevents flares, but not during one.")
q("divert","After a diverticulitis flare resolves, which diet prevents another one?",
 ["*High fiber","Low fiber || A risk factor.","High fat || Not the teaching.","No change || Fiber helps."],
 "Also avoid straining, smoking and a sedentary life.")
q("divert","Which are complications of diverticulitis? "+SATA,
 ["*Abscess","*Perforation","*Fistula","*Bowel obstruction","Pernicious anemia || Not related."],
 "Treatment: rest the bowel, IV antibiotics, pain control.")

# ---------- perforation ----------
q("perf","Which imaging finding confirms a GI perforation?",
 ["*Free air under the diaphragm on x-ray or CT","An enlarged heart || Heart failure.","A fecalith || Appendicitis cause.","A hiatal hernia || Not perforation."],
 "Perforation needs emergency surgery.")
q("perf","A client with a perforated ulcer is being prepared for surgery. Which actions are correct? "+SATA,
 ["*Notify the provider immediately","*Keep NPO","*Start IV fluids and antibiotics","*Insert an NG tube for decompression","*Check vitals often for shock","Give a PPI and recheck in 4 hours || An emergency."],
 "Signs: sudden severe pain, rigid abdomen, fever, fast heart rate, low BP.")
q("perf","Which conditions can lead to perforation? "+SATA,
 ["*Untreated peptic ulcer","*Ruptured appendix","*Diverticulitis","*Abdominal trauma","GERD alone || Not a listed cause."],
 "Delay increases mortality.")

# ---------- peritonitis ----------
q("periton","A client with peritonitis has a hard abdomen and no bowel sounds. What is happening?",
 ["*Paralytic ileus from the inflamed peritoneum; reassess and report","Normal after surgery || Not with peritonitis.","Constipation; give a laxative || Not indicated.","Improvement || Not improving."],
 "Don't just chart 'no bowel sounds.'")
q("periton","Why is peritonitis so dangerous? "+SATA,
 ["*It can quickly become sepsis","*Fluid shifts out of the vessels into the abdomen","*The bowel stops moving","It always clears up on its own || High mortality."],
 "Causes: perforation, ruptured appendix, dialysis infection.")
q("periton","Which treatments are expected for peritonitis? "+SATA,
 ["*IV antibiotics","*Large amounts of IV fluid","*NPO with an NG tube","*Surgery","A heating pad on the belly || Not a treatment."],
 "Watch for sepsis.")

# ---------- sepsis ----------
q("sepsis","A septic client has orders for blood cultures, IV antibiotics and IV fluids. Which comes FIRST?",
 ["*Blood cultures","IV antibiotics || After cultures.","Vasopressors || Fluids first.","A lactate in 6 hours || Cultures first."],
 "1-hour sepsis bundle: cultures, then antibiotics within 1 hour, then fluids.")
q("sepsis","How soon must antibiotics be given for sepsis?",
 ["*Within 1 hour","Within 6 hours || Too long.","Within 24 hours || Too long.","After culture results || Don't wait."],
 "A heavily tested time rule.")
q("sepsis","Which sign of sepsis is LATE and ominous?",
 ["*Low blood pressure","Fever || Early.","Fast heart rate || Early.","Fast breathing || Early."],
 "Septic shock = low BP despite fluids.")
q("sepsis","Which findings suggest sepsis? "+SATA,
 ["*Fever or low temperature","*Fast heart rate","*Fast breathing","*New confusion","A slow heart rate with warm, dry skin || Not the picture."],
 "Trend vitals and lactate.")
q("sepsis","Which clients are at higher risk for sepsis from a GI source? "+SATA,
 ["*A client with untreated peritonitis","*An older adult on immunosuppressants","*A client with a TPN central line","*A client whose antibiotics were delayed","A client on a high-fiber diet || Not a risk."],
 "Early recognition saves lives.")

# ---------- Murphy's vs McBurney's (professor: both will appear as choices) ----------
q("signs","The nurse presses the right upper abdomen and the client suddenly stops breathing in. What is this called, and what does it suggest?",
 ["*Murphy's sign; cholecystitis","McBurney's point; appendicitis || RLQ.","Cullen's sign; pancreatitis || Bruising.","Rebound; diverticulitis || Not this."],
 "Murphy = upper (gallbladder).")
q("signs","A client has sharp RLQ pain halfway between the belly button and the hip bone. What is this point called?",
 ["*McBurney's point (appendicitis)","Murphy's sign (cholecystitis) || RUQ.","Grey Turner's sign || Flank bruising.","Cullen's sign || Belly button bruising."],
 "McBurney = lower (appendix).")
q("signs","Which pairings are correct? "+SATA,
 ["*Murphy's sign: cholecystitis","*McBurney's point: appendicitis","Murphy's sign: appendicitis || Murphy = gallbladder.","McBurney's point: cholecystitis || McBurney = appendix."],
 "Murphy = upper right. McBurney = lower right.")
q("signs","In which quadrant is Murphy's sign checked?",
 ["*Right upper quadrant","Right lower quadrant || McBurney's.","Left lower quadrant || Diverticulitis.","Left upper quadrant || Not used."],
 "Murphy's sign = cholecystitis.")
