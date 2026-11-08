# Week 11.1 Glucose Regulation with Metabolic Syndrome — Prof. Mila Jones's transcript + PowerPoint (+ calorie counting chart).
# VERSION 2 (Nov 8): every question re-worded with new scenarios/distractors so answers can't be memorized. Same facts, same focus list.
T = "glucose"
CONCEPTS = {
 "norm":"Normal glucose regulation",
 "metsyn":"Metabolic syndrome criteria (FOCUS)",
 "metsx":"Metabolic syndrome findings & complications",
 "metmgmt":"Metabolic syndrome lifestyle management (FOCUS)",
 "metdrugs":"Metabolic syndrome meds: GLP-1, metformin, statins, ACE (FOCUS)",
 "barind":"Bariatric surgery: indications & procedures",
 "barcare":"Bariatric pre/post-op care & leak (FOCUS)",
 "bardc":"Bariatric discharge, dumping & supplements (FOCUS)",
 "dx":"Diagnostic tests & cutoffs (FOCUS)",
 "types":"Prediabetes, MODY & gestational diabetes",
 "t1t2":"Type 1 vs type 2 (FOCUS)",
 "monitor":"Glucose monitoring & CGM",
 "insulin":"Insulin types: onset, peak, duration",
 "insadmin":"Insulin administration, storage & sliding scale (FOCUS)",
 "drugint":"Drugs that raise or lower glucose with insulin",
 "injectables":"GLP-1 agonists & amylin mimetics (FOCUS)",
 "orals":"Oral agents: sulfonylureas to gliptins",
 "sglt2":"SGLT2 inhibitors",
 "hyper":"Hyperglycemia, dawn & Somogyi",
 "hypo":"Hypoglycemia & rule of 15 (FOCUS)",
 "dka":"DKA recognition (FOCUS)",
 "dkatx":"DKA treatment & goals (FOCUS)",
 "hhs":"HHS: signs & labs (FOCUS)",
 "hhstx":"HHS treatment & the fluid formula (FOCUS)",
 "whipple":"Whipple's triad & hypoglycemia levels (FOCUS)",
 "statin":"Statins: LFTs & rhabdomyolysis (FOCUS)",
 "leak":"Bariatric: anastomotic leak (FOCUS)",
 "dumping":"Bariatric: dumping syndrome (FOCUS)",
 "chronic":"Chronic complications",
 "sick":"Sick day rules (FOCUS)",
 "dc":"Discharge teaching & carb counting",
}
HI = ["metsyn","metmgmt","injectables","statin","leak","dumping","bardc","dka","dkatx","hhs","hhstx","hypo","whipple","t1t2","sick","insadmin","metdrugs","dx"]

SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

# ---------- normal regulation ----------
q("norm","A healthy adult's fasting glucose is 84 mg/dL. How does the nurse interpret this?",
 ["*Normal; the fasting range is 70–99 mg/dL","Prediabetes || Prediabetes starts at 100.","Hypoglycemia || Hypoglycemia is under 70.","Diabetes || Diabetes is 126 or higher on two fasting tests."],
 "Normal fasting glucose: 70–99 mg/dL.")
q("norm","A client skipped breakfast and lunch, but their glucose is still 78 mg/dL. Which hormone is keeping it up?",
 ["*Glucagon from the alpha cells, which tells the liver to release stored glucose","Insulin from the beta cells || Insulin lowers glucose.",
  "Amylin || Slows gastric emptying; it doesn't raise glucose this way.","Antidiuretic hormone || Not a glucose hormone."],
 "Insulin = the key that moves glucose into cells. Glucagon = the backup that raises it.")
q("norm","Which statements about insulin's actions are true? "+SATA,
 ["*It pushes potassium into cells along with glucose","*It stops the body from making ketones","*It helps the liver store glucose as glycogen",
  "It tells the liver to break down glycogen || That's glucagon.","It raises blood glucose between meals || That's glucagon."],
 "Insulin also builds protein and fat and blocks gluconeogenesis.")
q("norm","A student asks where the body keeps its glucose 'savings.' What is the best answer?",
 ["*In the liver, stored as glycogen","In the pancreas || The pancreas makes insulin and glucagon.","In the kidneys || Not the storage site.","In the bloodstream only || It's stored as glycogen."],
 "The pancreas makes insulin (beta cells); the liver stores glucose.")

# ---------- metabolic syndrome criteria ----------
q("metsyn","A woman has a waist of 36 inches, triglycerides of 162 mg/dL and an HDL of 46 mg/dL. Her BP is 118/76 and fasting glucose is 94. Does she have metabolic syndrome?",
 ["*Yes: waist, triglycerides and low HDL give her 3 criteria","No: her BP is normal || She only needs 3 of the 5.",
  "No: her glucose is normal || She only needs 3 of the 5.","No: HDL 46 is normal for a woman || Under 50 is low for women."],
 "Women: waist 35 inches or more and HDL under 50 count. Men: 40 inches and under 40.")
q("metsyn","Which client meets ONE metabolic syndrome criterion for waist size?",
 ["*A man with a 41-inch waist","A man with a 38-inch waist || Men need 40 inches or more.","A woman with a 33-inch waist || Women need 35 inches or more.","A woman with a 34-inch waist || Women need 35 inches or more."],
 "Large waist = central (abdominal) obesity, the main driver of insulin resistance.")
q("metsyn","Which lab value counts toward metabolic syndrome?",
 ["*Triglycerides of 155 mg/dL","Triglycerides of 120 mg/dL || Under 150 doesn't count.","Fasting glucose of 92 mg/dL || Under 100 doesn't count.","HDL of 62 mg/dL in a man || High HDL is protective."],
 "Triglycerides 150 or higher counts. Fasting glucose 100 or higher counts.")
q("metsyn","A client's BP is 128/82 and they take no BP medicine. Does this count as a metabolic syndrome criterion?",
 ["*No; the cutoff is 130/85 or higher, or taking BP medication","Yes; any BP over 120/80 counts || The cutoff is 130/85.",
  "Yes; all adults over 40 count || Not a criterion.","Only if the client is a woman || Same cutoff for both."],
 "If the client takes BP medication, the criterion counts even when the BP reading is normal.")
q("metsyn","The lecture compares metabolic syndrome to a tree. What is the 'root' that the risk factors grow from?",
 ["*Insulin resistance","Low glucagon || Not the root.","Autoimmune destruction of beta cells || That's type 1.","Thyroid disease || Not the root."],
 "The 'branches' are the risk factors: large waist, high triglycerides, low HDL, high BP and high fasting glucose.")
q("metsyn","Which set of findings is the full list of the 5 metabolic syndrome criteria?",
 ["*Large waist, high triglycerides, low HDL, high BP, high fasting glucose","High LDL, smoking, age, family history, stress || Not the 5 criteria.",
  "Obesity, A1C over 6.5, ketones, low potassium, high BUN || Not the 5 criteria.","Large waist, high HDL, low triglycerides, low BP, high glucose || HDL low and triglycerides high count."],
 "Three or more of the five = metabolic syndrome.")

# ---------- metabolic syndrome findings ----------
q("metsx","A client with metabolic syndrome asks why they feel fine. What should the nurse explain?",
 ["*Early metabolic syndrome usually has no symptoms","Symptoms always start with chest pain || Not true.",
  "If you feel fine, the lab results are wrong || Not true.","It only causes symptoms in children || Not true."],
 "As it progresses: growing waist, trouble losing weight, carb cravings, fatigue, fatty liver.")
q("metsx","Untreated metabolic syndrome raises the risk of which conditions? "+SATA,
 ["*Type 2 diabetes","*Myocardial infarction","*Stroke","*Cirrhosis from fatty liver","Type 1 diabetes || Type 1 is autoimmune."],
 "Insulin resistance, high BP and high glucose damage the heart, vessels and liver.")
q("metsx","Which client complaint fits worsening insulin resistance?",
 ["*Strong cravings for sweets and trouble losing weight","Sudden weight loss with a big appetite || Classic type 1 picture.",
  "Fruity breath || DKA.","Muscle pain on a statin || Rhabdomyolysis."],
 "Women with PCOS also have insulin resistance.")

# ---------- lifestyle ----------
q("metmgmt","A 220-lb client with metabolic syndrome asks how much weight to lose in 6 months. Which goal matches the lecture?",
 ["*About 11–22 lb (5–10% of body weight)","About 2 lb (1%) || Too little.","About 70 lb (30%) || Not the target.","No weight goal; medication is enough || Lifestyle comes first."],
 "Losing 5–10% within 6 months reduces visceral fat and insulin resistance.")
q("metmgmt","A client with metabolic syndrome asks what to try BEFORE medication. What does the nurse teach?",
 ["*Diet, exercise, weight loss and stress management","A GLP-1 agonist first || Medications come if lifestyle changes fail.",
  "Bariatric surgery first || Not first-line.","Insulin injections first || Not first-line."],
 "Lifestyle modification is the primary intervention.")
q("metmgmt","Which plan meets the lecture's exercise goal for metabolic syndrome?",
 ["*30 minutes of brisk walking 5 days a week, plus resistance training","10 minutes of walking once a week || Too little.",
  "Exercise only on weekends for 20 minutes || Too little.","No exercise until weight is lost || Exercise is part of the plan."],
 "At least 150 minutes a week of moderate exercise. Resistance training helps muscles take up glucose.")
q("metmgmt","Which meal choice fits the diet taught for metabolic syndrome?",
 ["*Grilled fish, brown rice and a large vegetable salad","Fried chicken and a large regular soda || High saturated fat and sugar.",
  "White bread with jam and juice || Simple carbs and sugary drinks.","Processed deli meats with chips || Processed foods."],
 "DASH or Mediterranean: complex carbs, high fiber, more fruits and vegetables; limit processed foods and sugary drinks.")
q("metmgmt","Which client statement shows understanding of metabolic syndrome management? "+SATA,
 ["*I'll swap soda for water","*I'll walk 30 minutes most days","*I'll try to lose 5–10% of my weight over 6 months","*I'll work on managing stress",
  "I only need to change things if my labs get worse || Lifestyle changes start now."],
 "Health promotion and prevention are the focus.")

# ---------- metabolic drugs ----------
q("metdrugs","A client just diagnosed with type 2 diabetes asks which pill they will most likely start. What does the nurse say?",
 ["*Metformin (Glucophage)","Glipizide (Glucotrol) || Second-line.","Pioglitazone (Actos) || Usually combination therapy.","Glucagon || Treats hypoglycemia."],
 "Metformin is first-line for type 2 diabetes and prediabetes.")
q("metdrugs","Where does metformin mainly work to lower blood glucose?",
 ["*The liver: it cuts how much glucose the liver puts out","The pancreas: it squeezes out more insulin || That's a sulfonylurea.",
  "The kidneys: it spills glucose into urine || That's an SGLT2 inhibitor.","The gut: it blocks carb digestion || That's acarbose."],
 "Metformin also improves insulin sensitivity and doesn't cause hypoglycemia by itself.")
q("metdrugs","A client on metformin is having a CT scan with IV contrast tomorrow. Which order should the nurse expect?",
 ["*Hold metformin for at least 48 hours after the contrast","Take a double dose before the scan || Not taught.","Keep taking it as usual || Contrast plus metformin risks lactic acidosis.","Switch to insulin permanently || Not needed."],
 "Also avoid alcohol and cimetidine. Monitor kidney function.")
q("metdrugs","A client who has taken metformin for 8 years has numbness and fatigue. Which deficiency does the nurse suspect?",
 ["*Vitamin B12","Vitamin C || Not linked to metformin.","Vitamin K || Not linked to metformin.","Potassium || Not linked to metformin."],
 "Metformin can cause B12 and folic acid malabsorption. Supplements may be needed.")
q("metdrugs","A client taking metformin went out drinking and now has muscle aches, fast breathing and confusion. What should the nurse suspect?",
 ["*Lactic acidosis","Hypoglycemia from metformin alone || Metformin alone rarely causes lows.","Normal hangover || The risk is lactic acidosis.","Dumping syndrome || Not related."],
 "Alcohol and cimetidine increase lactic acidosis risk with metformin.")
q("metdrugs","Which family history makes the nurse question a semaglutide (Ozempic) order?",
 ["*Medullary thyroid carcinoma","High cholesterol || Not a contraindication.","Type 2 diabetes || An indication.","Obesity || An indication."],
 "Also multiple endocrine neoplasia and severe GI disease such as gastroparesis.")

# ---------- statins ----------
q("statin","A client is starting atorvastatin (Lipitor). Which lab test is drawn first and then rechecked periodically?",
 ["*Liver function tests","Hemoglobin A1C || Not the statin requirement.","Serum lipase || Pancreas test.","TSH || Thyroid test."],
 "Statins require baseline and periodic LFTs.")
q("statin","A client on a statin says, 'My legs ache and feel weak, but I haven't exercised.' What does the nurse do?",
 ["*Report it right away; it could be rhabdomyolysis","Tell them it's normal soreness || Unexplained muscle pain must be reported.",
  "Suggest more exercise to stretch it out || Not the response.","Tell them to double the dose || Never."],
 "Rhabdomyolysis = muscle breakdown that can damage the kidneys.")
q("statin","Which two things does the nurse monitor for every client on a statin? "+SATA,
 ["*Liver function tests","*New, unexplained muscle pain or weakness","Daily blood glucose || Not the statin focus.","Potassium || Not the statin focus.","Fruity breath || DKA."],
 "Statins lower LDL and triglycerides and stabilize plaque.")
q("statin","Which statement by a client on simvastatin needs follow-up?",
 ["*My muscles have been sore and weak all week for no reason","I take it at the same time each day || Correct.",
  "I keep my liver test appointments || Correct.","I'm eating a low-fat diet || Correct."],
 "Unexplained muscle pain = report for possible rhabdomyolysis.")

# ---------- bariatric indications ----------
q("barind","Which client is the best candidate for bariatric surgery?",
 ["*BMI 41 who hasn't lost weight with diet and exercise","BMI 31 with no other conditions || Below criteria.",
  "BMI 34 with sleep apnea || Below the BMI 35 threshold.","BMI 38 who hasn't tried lifestyle changes yet || Conservative management must fail first."],
 "BMI 40 or more, or BMI 35 or more with a comorbidity (type 2 diabetes, high BP, high lipids, sleep apnea), after failed conservative management.")
q("barind","A client asks which bariatric surgery bypasses part of the small intestine so fewer calories are absorbed. Which one?",
 ["*Roux-en-Y gastric bypass","Sleeve gastrectomy || Restrictive only.","Adjustable gastric band || Restrictive only.","Endoscopic sleeve gastroplasty || Non-surgical and restrictive."],
 "Roux-en-Y is the gold standard: restrictive and malabsorptive, with strong diabetes remission.")
q("barind","Which bariatric procedure removes most of the stomach and cannot be reversed?",
 ["*Sleeve gastrectomy","Adjustable gastric band || Reversible.","Endoscopic sleeve gastroplasty || Non-surgical.","Roux-en-Y || Bypasses, rather than removes, most of the stomach."],
 "Sleeve: restrictive and irreversible. Staple line leaks are a risk.")
q("barind","A client wants the bariatric option with the lowest surgical risk and can accept slower weight loss. Which one fits?",
 ["*Adjustable gastric band","Duodenal switch || Complex and malabsorptive.","Roux-en-Y || Complex and permanent.","Sleeve gastrectomy || Irreversible."],
 "Band complications: slippage, erosion and port problems.")

# ---------- bariatric care ----------
q("barcare","Before bariatric surgery, which evaluations must be completed? "+SATA,
 ["*Psychological evaluation","*Nutrition consult","Cardiac catheterization for everyone || Not routine.","Colonoscopy for everyone || Not required."],
 "Also consent, accurate height and weight, and a respiratory assessment for sleep apnea.")
q("barcare","Why is a client put on a strict liquid or low-calorie diet 1–2 weeks before bariatric surgery?",
 ["*To shrink the liver so the surgeon can reach the stomach","To start dumping syndrome early || Not the reason.","To raise the potassium || Not the reason.","To test for diabetes || Not the reason."],
 "Pre-op teaching also covers the incentive spirometer, splinting and early walking.")
q("barcare","The day after bariatric surgery, the NG tube stops draining. What should the nurse do?",
 ["*Notify the surgeon; do not reposition or irrigate it","Push it in further to restart drainage || Can disrupt the staple line.",
  "Irrigate it with 60 mL of saline || Never irrigate it.","Pull it out || Not without an order."],
 "Repositioning or irrigating can damage the staple line.")
q("barcare","Which post-op orders fit a client after bariatric surgery? "+SATA,
 ["*Head of bed in semi-Fowler's","*Incentive spirometer every 1–2 hours while awake","*Walk within 4–6 hours of surgery","*SCDs while in bed","Flat in bed for 24 hours || Early walking prevents clots."],
 "Obesity is a hypercoagulable state, so clot prevention matters.")
q("barcare","The surgeon clears a bariatric client to drink. Which order is correct?",
 ["*Small sips of clear liquids, about 30 mL every hour","A full glass of water with each meal || Too much, and no fluids with meals.",
  "Protein shakes right away || The diet advances slowly.","A regular diet || Not for weeks."],
 "Clearance is often after a negative upper GI contrast study.")

# ---------- anastomotic leak ----------
q("leak","Twelve hours after a sleeve gastrectomy, a client's heart rate climbs from 88 to 124 with no clear cause. What does the nurse suspect FIRST?",
 ["*An anastomotic (staple line) leak","Normal post-op pain || Unexplained tachycardia is the earliest leak sign.","Dumping syndrome || Happens after eating.","Hypoglycemia || Not the priority concern."],
 "Unexplained tachycardia (over 120) is the earliest leak sign. Report to the surgeon immediately.")
q("leak","Which assessment finding is the nurse's top priority after bariatric surgery?",
 ["*Signs of an anastomotic leak","The client's waist size || Not a post-op priority.","A1C results || Not a post-op priority.","Readiness for solid food || Not yet."],
 "Leak signs: unexplained tachycardia, fever, tachypnea, and abdominal or left shoulder pain.")
q("leak","A client 1 day after gastric bypass reports new pain in the LEFT shoulder. Temperature is 101.2°F. What should the nurse do?",
 ["*Notify the surgeon now; this may be an anastomotic leak","Give a heating pad for the shoulder || Not the priority.",
  "Reassure the client that shoulder pain is from positioning || These are red flags.","Encourage a protein shake || Not the priority."],
 "An untreated leak can cause peritonitis: guarding and a rigid, board-like abdomen.")
q("leak","Which findings after gastric bypass point to a leak rather than dumping syndrome? "+SATA,
 ["*Fever","*Tachycardia that isn't explained by pain","*New left shoulder or back pain","Cramping right after a sugary meal || Dumping.","Diarrhea 30 minutes after eating cake || Dumping."],
 "Leak = surgical emergency. Dumping = tied to eating high-carb food.")

# ---------- dumping ----------
q("dumping","A client 6 weeks after gastric bypass ate pancakes with syrup and 30 minutes later has cramping, diarrhea and a racing heart. What is happening?",
 ["*Dumping syndrome","Anastomotic leak || A leak causes fever and shoulder pain, not a reaction to food.","Hypoglycemia from insulin || Not the pattern.","Appendicitis || Not the pattern."],
 "High-sugar food moves quickly into the small intestine and pulls fluid in.")
q("dumping","A client is having dumping syndrome right now. What should the nurse tell them to do?",
 ["*Lie down for 30 minutes","Drink a glass of juice || Sugar makes it worse.","Walk around to speed digestion || Speeds emptying.","Eat a larger meal || Makes it worse."],
 "Lying down slows gastric emptying.")
q("dumping","Which signs are typical of dumping syndrome? "+SATA,
 ["*Nausea and abdominal cramping","*Diarrhea","*Sweating and dizziness","*Fast heart rate","Fever and left shoulder pain || Leak signs."],
 "Symptoms start about 30 minutes after eating, especially high-carb food.")
q("dumping","Which meal plan helps prevent dumping syndrome?",
 ["*Six small meals a day, no sweets, and no drinking with meals","Three large meals a day with juice || Too much and too sugary.",
  "Desserts allowed if eaten slowly || Avoid high-sugar foods.","Drinking a full glass of water with each meal || No fluids with meals."],
 "No liquids 30 minutes before or 30–60 minutes after solid food.")

# ---------- bariatric discharge ----------
q("bardc","What is the correct order of the diet after bariatric surgery?",
 ["*Clear liquids, then full liquids, then pureed, then solid foods","Pureed, then clear liquids, then solids || Wrong order.",
  "Solid foods right away || Too fast.","Full liquids for life || The diet advances."],
 "Eat about 6 small meals a day, chew food to a paste, and stop at the first sign of fullness.")
q("bardc","After gastric bypass, when can a client drink fluids in relation to meals?",
 ["*Not within 30 minutes before or 30–60 minutes after solid food","With every bite to help swallowing || Flushes food through too fast.",
  "Only with meals || Not the rule.","Any time; it doesn't matter || Timing matters."],
 "This prevents dumping and stretching of the pouch.")
q("bardc","Which supplements must a client take FOR LIFE after gastric bypass? "+SATA,
 ["*Vitamin B12","*Iron","*Calcium citrate","*Vitamin D","*A multivitamin"],
 "Bypassing part of the small intestine impairs absorption of B12, folate, iron and calcium.")
q("bardc","A client asks why they need B12 shots for the rest of their life after gastric bypass. What is the reason?",
 ["*The surgery removes or bypasses the stomach cells that make intrinsic factor, which B12 needs to be absorbed","B12 prevents dumping syndrome || Not the reason.",
  "B12 keeps the staple line healing || Not the reason.","Only for the first 3 months || It's lifelong."],
 "Without B12: pernicious anemia and nerve damage.")
q("bardc","A client with diabetes says, 'After my bariatric surgery I won't have diabetes anymore.' What is the best response?",
 ["*Surgery may improve your diabetes or put it in remission, but it isn't a cure; you'll still need follow-up","You're right, it's a cure || Not a cure.",
  "Surgery makes diabetes worse || It often improves it.","You'll stop all monitoring after surgery || Follow-up continues."],
 "The client must follow the post-op bariatric diet and take supplements for life.")
q("bardc","Which call from a bariatric client after discharge needs the surgeon? "+SATA,
 ["*Temperature of 101.6°F","*Severe abdominal pain spreading to the left shoulder","*Vomiting that won't stop","*Pus draining from the incision","Losing about 1–2 lb a week || Expected."],
 "These suggest leak, infection or sepsis.")
q("bardc","Which late problems can follow gastric bypass because nutrients aren't absorbed well? "+SATA,
 ["*Pernicious anemia","*Iron-deficiency anemia","*Osteoporosis","Anastomotic leak || An early surgical complication.","Type 1 diabetes || Not a complication."],
 "Other late problems: dumping, hernias, bowel obstruction and gallstones.")

# ---------- diagnostics ----------
q("dx","A client's A1C is 6.1%. How does the nurse interpret it?",
 ["*Prediabetes","Normal || Normal is under 5.7%.","Diabetes || Diabetes is 6.5% or higher.","Well-controlled diabetes || 6.1% alone means prediabetes."],
 "Under 5.7% normal · 5.7–6.4% prediabetes · 6.5% or higher diabetes.")
q("dx","Which A1C is the LOWEST result that diagnoses diabetes?",
 ["*6.5%","5.7% || The start of prediabetes.","6.0% || Prediabetes.","7.0% || The treatment goal, not the cutoff."],
 "The A1C shows about 3 months of glucose control (the life of a red blood cell).")
q("dx","Two fasting glucose tests on different days are 131 and 138 mg/dL. What does this mean?",
 ["*Diabetes","Prediabetes || Prediabetes is 100–125.","Normal || Normal is 70–99.","Hypoglycemia || Too high."],
 "Fasting glucose 126 or higher on at least two occasions = diabetes.")
q("dx","A fasting glucose of 118 mg/dL falls in which range?",
 ["*Prediabetes (100–125)","Normal (70–99) || Too high.","Diabetes (126 or higher) || Not high enough.","Hypoglycemia || Too high."],
 "Prediabetes can be reversed with lifestyle changes.")
q("dx","What should the nurse tell a client before a fasting blood glucose test?",
 ["*Nothing to eat for at least 8 hours","Eat a normal breakfast first || Food raises the result.","Fast for 1 hour || Too short.","Drink a sugary drink first || That's the glucose tolerance test."],
 "Water is OK; food raises the result.")
q("dx","A thirsty client who urinates often has a random glucose of 240 mg/dL. How is this interpreted?",
 ["*It meets the threshold for diabetes","Normal after eating || Over 200 with symptoms is diagnostic.","Prediabetes || Too high.","Low || Too high."],
 "Random plasma glucose over 200 mg/dL plus classic symptoms = diabetes.")
q("dx","A client with severe anemia has an A1C that doesn't match their glucose logs. Why?",
 ["*Anemia can make the A1C inaccurate","The A1C only reflects the last meal || About 3 months.","The glucose meter is always wrong || Not the reason.","A1C can't be done in adults || Not true."],
 "The A1C depends on red blood cells, so anemia affects it.")
q("dx","For most adults with diabetes, what A1C goal does the ADA recommend?",
 ["*7% or below","Under 5.7% || That's the normal value.","Exactly 6.5% || That's the diagnostic cutoff.","Under 9% || Too high."],
 "An A1C over 8% suggests poor control or poor adherence.")

# ---------- types ----------
q("types","A client with prediabetes asks if they need medicine. What does the nurse explain?",
 ["*Prediabetes can often be reversed with lifestyle changes, without medication","Insulin is needed right away || Not for prediabetes.",
  "Bariatric surgery is required || Not for prediabetes.","Nothing can reverse it || It's reversible."],
 "Cut sugary drinks, control portions, eat vegetables and fish, sleep at least 8 hours.")
q("types","Which statements about MODY are correct? "+SATA,
 ["*It's caused by a gene passed down (autosomal dominant)","*It's often mistaken for type 1","*It isn't autoimmune","*Glipizide is the drug of choice","It always needs insulin from day one || Often managed with a sulfonylurea."],
 "MODY = maturity-onset diabetes of the young; onset around age 10–45.")
q("types","A pregnant client at 26 weeks is scheduled for a diabetes screen. Which test is it?",
 ["*Oral glucose tolerance test","A1C alone || Not the pregnancy screen.","Urine ketones || Not a screen.","HIDA scan || Gallbladder test."],
 "Done at 24–28 weeks: drink a glucose load, then blood draws over about 3 hours.")
q("types","A client with gestational diabetes isn't controlled with diet and exercise. Which drug should the nurse question?",
 ["*Glipizide (a sulfonylurea)","Metformin || Safest oral option in pregnancy.","Insulin || Used if needed.","None; all are safe || Sulfonylureas cross the placenta."],
 "Sulfonylureas can cause high insulin levels in the fetus.")
q("types","A client had gestational diabetes 3 years ago. What risk should the nurse teach?",
 ["*Higher risk of type 2 diabetes later","Guaranteed type 1 diabetes || Not the risk.","No future risk || Risk is higher.","Only a risk for twins || Not related."],
 "Past gestational diabetes and PCOS are non-modifiable type 2 risk factors.")

# ---------- T1 vs T2 ----------
q("t1t2","A thin 9-year-old has sudden thirst, bedwetting and weight loss, and arrives in DKA. Which type of diabetes fits?",
 ["*Type 1","Type 2 || Usually gradual, in adults with obesity.","Gestational || Only in pregnancy.","Prediabetes || Doesn't cause DKA."],
 "Type 1: autoimmune destruction of beta cells; no insulin is made; often first shows up as DKA in children.")
q("t1t2","A 58-year-old with obesity has slowly gained weight and now has tingling feet and blurred vision. Which type of diabetes fits?",
 ["*Type 2","Type 1 || Usually sudden, in thin young people.","MODY || Rare and genetic.","Gestational || Only in pregnancy."],
 "Type 2 = insulin resistance; 90–95% of cases; often lifestyle-related.")
q("t1t2","Which statement about type 1 vs. type 2 diabetes is correct?",
 ["*Type 1 makes no insulin and needs insulin for life; type 2 is insulin resistance, treated with lifestyle and metformin first",
  "Type 2 always needs insulin from diagnosis || Usually lifestyle and metformin first.","Type 1 is caused by diet || It's autoimmune.","Both are autoimmune || Only type 1."],
 "Type 2 may need insulin later as the disease progresses.")
q("t1t2","Why do clients with type 2 diabetes rarely develop ketones?",
 ["*They still make some insulin, which blocks ketone production","They don't eat fat || Not the reason.","Metformin removes ketones || Not the reason.","Their kidneys filter all ketones out || Not the reason."],
 "Type 2 clients are 'ketosis resistant,' so HHS is more common than DKA.")
q("t1t2","Which findings are seen in BOTH type 1 and type 2 diabetes? "+SATA,
 ["*Frequent urination","*Excess thirst","*Excess hunger","*Fatigue","*More infections"],
 "The 3 P's: polyuria, polydipsia, polyphagia.")
q("t1t2","Which type 2 risk factors can a client CHANGE? "+SATA,
 ["*Sedentary lifestyle","*Obesity","*Smoking","*Poor sleep","Age over 45 || Can't change.","Family history || Can't change."],
 "Chronic stress and some medications (steroids, antipsychotics) also raise risk.")
q("t1t2","Which type of diabetes is linked to each emergency?",
 ["*Type 1 → DKA; type 2 → HHS","Type 1 → HHS; type 2 → DKA || Reversed.","Both → only hypoglycemia || Not correct.","Neither has emergencies || Both do."],
 "Type 2 still makes enough insulin to prevent ketosis, but not enough to prevent extreme hyperglycemia.")

# ---------- monitoring ----------
q("monitor","A client on intensive insulin asks when to check their glucose. Which times are correct? "+SATA,
 ["*Before each meal and snack","*At bedtime","*Before driving","*Before exercise","*When they feel shaky or sweaty"],
 "Also after treating a low until it's back to normal.")
q("monitor","A client asks what their continuous glucose monitor actually reads. What is the answer?",
 ["*Glucose in the fluid under the skin (interstitial fluid)","Glucose in the urine || Not a CGM.","Venous blood glucose || Not what the sensor reads.","The A1C every hour || Not a CGM."],
 "A CGM shows trends: the direction and speed of change.")
q("monitor","Which are benefits of a continuous glucose monitor? "+SATA,
 ["*Fewer hypoglycemia episodes","*Protection overnight while sleeping","*Can lower the A1C","*Helps spot patterns","It removes the need for insulin || Not a benefit."],
 "Dexcom gives real-time alarms; FreeStyle Libre is scan-to-read.")

# ---------- insulin types ----------
q("insulin","A client needs insulin that starts working within 15 minutes to cover lunch. Which one?",
 ["*Lispro (Humalog)","NPH (Humulin N) || Starts in 2–4 hours.","Glargine (Lantus) || Long-acting.","Regular (Humulin R) || Starts in about 30 minutes."],
 "Rapid-acting: onset 5–15 minutes, peak 1–2 hours, lasts 2–4 hours.")
q("insulin","A client gets NPH at 0700. When should the nurse watch most closely for hypoglycemia?",
 ["*Late morning through early evening","Within 10 minutes || NPH starts in 2–4 hours.","Only the next day || NPH lasts 10–16 hours.","Never; NPH has no peak || NPH peaks 4–12 hours after the dose."],
 "Intermediate-acting NPH is the cloudy insulin.")
q("insulin","Which insulin gives steady background coverage for about 24 hours without a peak?",
 ["*Glargine (Lantus)","Lispro (Humalog) || Rapid-acting with a peak.","NPH || Peaks 4–12 hours.","Regular || Peaks 2–3 hours."],
 "Keep giving basal insulin on sick days.")
q("insulin","The nurse holds up an insulin vial that looks cloudy. Which insulin should it be?",
 ["*NPH","Regular || Should be clear.","Lispro || Should be clear.","Glargine || Should be clear."],
 "Clear insulin that looks cloudy should not be used.")
q("insulin","Which insulin is the ONLY one given as an IV drip for DKA?",
 ["*Regular insulin","Glargine || Never IV.","NPH || Never IV.","Degludec || Never IV."],
 "DKA: regular insulin 0.1 units/kg/hr by continuous IV infusion.")

# ---------- insulin administration ----------
q("insadmin","An unopened box of insulin pens just arrived. How should the client store them?",
 ["*In the refrigerator until opened","In the freezer || Freezing ruins insulin.","In a hot car so they stay warm || Heat ruins insulin.","On a sunny windowsill || Protect from light and heat."],
 "Once opened, insulin is good for 28 days at room temperature.")
q("insadmin","A client opened an insulin vial on March 1 and kept it at room temperature. On what date should they throw it away?",
 ["*March 29 (28 days after opening)","April 30 || Too long.","March 8 || Too short.","Only when the vial is empty || It expires after 28 days."],
 "Date the vial or pen the day it's opened.")
q("insadmin","A client always injects insulin in the same spot on their abdomen. What should the nurse teach?",
 ["*Rotate sites to prevent lipodystrophy, which makes absorption uneven","Keep using one spot so absorption is predictable || Causes lipodystrophy.",
  "Inject only into the thigh from now on || Rotate; don't use one site.","Massage the site hard after injecting || Not the teaching."],
 "Best sites: abdomen and back of the arm. Thigh is also used.")
q("insadmin","Which statements about giving insulin are correct? "+SATA,
 ["*Inject at 90 degrees (45 degrees for thin clients)","*In a client with obesity, spread the skin instead of pinching","*Rotate injection sites","*The abdomen and back of the arm are the best sites",
  "Inject through clothing to save time || Not the practice."],
 "Lipodystrophy changes insulin absorption.")
q("insadmin","The nurse is mixing regular and NPH insulin in one syringe. Which order is correct?",
 ["*Draw up the regular (clear) first, then the NPH (cloudy)","NPH first, then regular || Clear before cloudy.","Order doesn't matter || It does.","Never mix them || They can be mixed."],
 "Clear before cloudy keeps the cloudy insulin out of the clear vial.")
q("insadmin","A hospitalized client is due rapid-acting insulin before breakfast, but the tray hasn't come. What should the nurse do?",
 ["*Wait until the tray is at the bedside or the client starts eating","Give it now; the tray will come eventually || Hypoglycemia risk.",
  "Give it after the meal tomorrow || Not appropriate.","Skip it for the day || Not the action."],
 "Rapid-acting insulin works within minutes.")
q("insadmin","A client has a standing dose of lispro before meals plus a lispro correction scale. Both doses are due. How should the nurse give them?",
 ["*Add them together and give in one syringe, since it's the same insulin","Give them in two separate syringes || One syringe when it's the same insulin.",
  "Give only the correction dose || Both are due.","Give only the standing dose || Both are due."],
 "Same insulin = combine standing and correction doses in one injection.")
q("insadmin","A client's insulin-to-carb ratio is 1:15. What does this mean?",
 ["*One unit of rapid-acting insulin covers 15 g of carbohydrate","15 units cover 1 g of carbohydrate || Reversed.",
  "Take 15 units at every meal || Not what a ratio means.","Eat 15 g of carbs per unit of NPH || Not what it means."],
 "Rapid-acting insulin is given 0–15 minutes before meals.")

# ---------- drug interactions ----------
q("drugint","A client on insulin is starting prednisone. What should the nurse expect?",
 ["*Higher blood glucose, so insulin may need to go up","Lower glucose || Steroids raise glucose.","No effect || Steroids matter.","Ketones disappear || Not related."],
 "Albuterol, thiazides and thyroid hormone also raise glucose.")
q("drugint","A client on insulin had several drinks last night. When is a low most likely?",
 ["*Hours later, often overnight","Immediately || Not the usual pattern.","A week later || Not the pattern.","Never; alcohol raises glucose || It blocks the liver from releasing glucose."],
 "The liver is busy breaking down alcohol, so it doesn't release glucose.")
q("drugint","A client with diabetes takes metoprolol. Which hypoglycemia sign may be the ONLY early warning left?",
 ["*Sweating","A pounding heart || Beta blockers mask it.","Tremor || Beta blockers mask it.","Fruity breath || DKA, not hypoglycemia."],
 "Beta blockers can also worsen glucose control.")
q("drugint","Which drugs add to hypoglycemia risk in a client on insulin? "+SATA,
 ["*Sulfonylureas such as glipizide","*Meglitinides such as repaglinide","*High-dose aspirin",
  "Prednisone || Raises glucose.","Albuterol || Raises glucose."],
 "Secretagogues squeeze out more insulin.")

# ---------- GLP-1 & amylin ----------
q("injectables","Why do GLP-1 agonists rarely cause hypoglycemia on their own?",
 ["*They release insulin only when glucose is high","They contain sugar || Not true.","They block insulin || Not true.","They make the kidneys hold glucose || Not true."],
 "They also slow the stomach and cause fullness; weekly dosing for semaglutide.")
q("injectables","A client on liraglutide (Victoza) calls with severe stomach pain that goes through to the back and won't stop. What does the nurse suspect?",
 ["*Pancreatitis; stop the drug and get evaluated now","Expected nausea || Severe pain to the back is a red flag.","Gallbladder attack only || Pancreatitis must be ruled out.","Constipation || Not the concern."],
 "GLP-1s also cause severe dehydration from vomiting.")
q("injectables","What is the MOST important complication to teach a client starting a GLP-1 agonist?",
 ["*Pancreatitis: report severe abdominal pain right away","Hair thinning || Not the key complication.","Weight gain || They cause weight loss.","Dry cough || ACE inhibitors."],
 "Contraindicated with a history of medullary thyroid carcinoma.")
q("injectables","A client on semaglutide has nausea after big meals. What should the nurse teach?",
 ["*Eat smaller portions and stop when you feel full","Eat bigger meals less often || Worsens nausea.","Skip the weekly dose || Not the teaching.","Inject in the same spot each week || Rotate sites."],
 "Common side effects: nausea, vomiting, diarrhea or constipation.")
q("injectables","Which teaching is correct for pramlintide (Symlin)? "+SATA,
 ["*Inject it 30 minutes before meals","*Never mix it in the same syringe as insulin","*Watch for severe lows when used with insulin",
  "It's safe with gastroparesis || Contraindicated.","Take it even if you skip the meal || Causes hypoglycemia."],
 "Amylin mimetic: slows gastric emptying; added to insulin.")

# ---------- oral agents ----------
q("orals","A client on repaglinide (Prandin) is skipping dinner tonight. What should they do with the dose?",
 ["*Skip the dose","Take it as usual || Hypoglycemia.","Double it tomorrow || Not taught.","Take it at bedtime || Not taught."],
 "Skip a meal, skip the dose. Fast onset, short duration.")
q("orals","A client on glipizide (Glucotrol) has gained 8 lb and had two lows this week. What explains this?",
 ["*Sulfonylureas cause hypoglycemia and weight gain","Expected from metformin || Wrong drug.","Fluid retention from a TZD || Wrong drug.","Normal aging || The drug is the cause."],
 "Take 30 minutes before meals. Contraindicated in type 1 and pregnancy.")
q("orals","A client on pioglitazone (Actos) has new ankle swelling and is short of breath. Why is the nurse concerned?",
 ["*It can cause fluid retention and heart failure","It causes lactic acidosis || Metformin.","It causes pancreatitis || GLP-1s and gliptins.","It's expected weight loss || TZDs cause weight gain."],
 "TZDs are contraindicated in heart failure.")
q("orals","How should acarbose (Precose) be taken?",
 ["*With the first bite of each meal","At bedtime || Not the instruction.","On an empty stomach in the morning || Not the instruction.","Once a week || Not the instruction."],
 "Blocks carb breakdown; side effects: gas, diarrhea, abdominal pain.")
q("orals","Which history makes the nurse question an order for sitagliptin (Januvia)?",
 ["*Pancreatitis","High blood pressure || Not a contraindication.","Type 2 diabetes || An indication.","Taking metformin || Often combined."],
 "Gliptins: watch for Stevens-Johnson syndrome, angioedema and pancreatitis.")

# ---------- SGLT2 ----------
q("sglt2","A client on dapagliflozin (Farxiga) asks why they urinate more. What is the reason?",
 ["*The drug makes the kidneys spill glucose and sodium into the urine","It squeezes the pancreas || Sulfonylurea.","It slows the stomach || GLP-1.","It's a sign of overdose || Expected effect."],
 "Teach good hygiene and hydration: genital and urinary infections are common.")
q("sglt2","Which client should NOT receive an SGLT2 inhibitor? "+SATA,
 ["*A client with type 1 diabetes","*A client on dialysis","*A client with active bladder cancer","A client with heart failure || SGLT2s reduce heart failure risk.","A client with mild CKD || They slow CKD."],
 "Rare risks: euglycemic DKA, Fournier's gangrene.")
q("sglt2","When should a client take an SGLT2 inhibitor?",
 ["*In the morning, with or without food","At bedtime || Nighttime urination.","With every meal || Once daily.","Only when glucose is high || Daily."],
 "Stay hydrated.")

# ---------- hyperglycemia ----------
q("hyper","A client's glucose is 52 at 3 a.m. and 210 at 7 a.m. What is happening and what helps?",
 ["*Somogyi effect; decrease the evening insulin or add a bedtime snack","Dawn phenomenon; add insulin || The 3 a.m. reading would not be low.",
  "DKA; start an insulin drip || Not this pattern.","Normal pattern; no change || It needs a fix."],
 "Somogyi = too much insulin, an overnight low, then a rebound high.")
q("hyper","A client's glucose is 150 at 3 a.m. and 220 at 7 a.m. What is likely happening?",
 ["*Dawn phenomenon from early-morning growth hormone; insulin may be increased","Somogyi effect || The 3 a.m. reading would be low.",
  "Hypoglycemia || Not low.","Anastomotic leak || Not related."],
 "Check a 3 a.m. glucose to tell dawn from Somogyi.")
q("hyper","Which signs point to a glucose of about 250 mg/dL rather than a low? "+SATA,
 ["*Thirst","*Frequent urination","*Blurred vision","*Headache and tiredness","Shaking and sweating || Hypoglycemia."],
 "Treat with rapid-acting insulin per orders; recheck 1–2 hours later.")
q("hyper","A hospitalized client stays above 300 mg/dL despite correction doses. What should the nurse expect?",
 ["*A switch to an IV insulin infusion","Stopping all insulin || Glucose is high.","Discharge home || Not appropriate.","Sliding scale only || Avoid sliding scale alone."],
 "Basal-bolus insulin is preferred over sliding scale alone.")

# ---------- hypoglycemia ----------
q("hypo","Below what blood glucose is a client hypoglycemic?",
 ["*70 mg/dL","100 mg/dL || Upper end of normal fasting.","126 mg/dL || Diabetes cutoff.","200 mg/dL || Not low."],
 "Common causes: too much medication, too little food, or extra activity.")
q("hypo","A client is shaky and sweaty. Their glucose is 58 mg/dL, and they're awake and can swallow. What does the nurse do?",
 ["*Give 15 g of fast carbs (like 4 oz of juice) and recheck in 15 minutes","Give IV D50 || For unconscious clients.",
  "Give glucagon || For clients who can't swallow.","Give their scheduled insulin || Makes it worse."],
 "The 15-15 rule: repeat if still low, then give a snack.")
q("hypo","After treating a low with juice, the 15-minute recheck is 64 mg/dL. What's next?",
 ["*Give another 15 g of fast carbs and recheck in 15 minutes","Give insulin || Still low.","Call a code || Not indicated.","Wait an hour || Too long."],
 "Repeat the 15-15 rule until glucose is above 70, then give a snack or meal.")
q("hypo","Which choice gives about 15 g of fast-acting carbohydrate for a low?",
 ["*4 oz (1/2 cup) of orange juice","A handful of peanuts || Mostly fat and protein.","A cup of broccoli || Too little carbohydrate.","A slice of cheese || Mostly fat and protein."],
 "Other options: 1/2 cup regular soda, glucose tablets, or 1 cup of milk.")
q("hypo","A family member finds a client with diabetes unconscious at home. What should they give?",
 ["*Glucagon by injection or nasal spray, then turn the client on their side","Orange juice poured into the mouth || Aspiration risk.",
  "The client's insulin || Makes it worse.","Nothing until EMS arrives || Glucagon works fast."],
 "Teach family how to use glucagon. Recheck glucose in 15 minutes.")
q("hypo","A hospitalized client is unresponsive with a glucose of 38 mg/dL. Which treatment does the nurse anticipate?",
 ["*IV dextrose 50% (D50W)","Oral glucose gel || Can't swallow safely.","A sandwich || Can't eat.","Rapid-acting insulin || Makes it worse."],
 "Follow with a D10 infusion if the low persists. Recheck glucose.")
q("hypo","Which findings suggest a LOW glucose? "+SATA,
 ["*Shakiness","*Sweating","*Pounding heart","*Irritability","*Pale skin and dizziness","Fruity breath || DKA."],
 "Check the glucose before treating if possible.")

# ---------- Whipple's triad ----------
q("whipple","A client says they feel shaky. Their glucose is 49 mg/dL, and after juice they feel fine. Which concept does this confirm?",
 ["*Whipple's triad: low glucose, symptoms, and relief with glucose","Somogyi effect || Overnight low with rebound high.","The DKA triad || Hyperglycemia, ketones, acidosis.","Dumping syndrome || Post-meal reaction after bypass."],
 "All three parts of Whipple's triad confirm true hypoglycemia.")
q("whipple","Which three parts make up Whipple's triad?",
 ["*Low glucose + hypoglycemia symptoms + symptoms go away when glucose is given","Thirst + hunger + urination || The 3 P's of hyperglycemia.",
  "High glucose + ketones + acidosis || The DKA triad.","Fever + fast heart rate + shoulder pain || Anastomotic leak."],
 "Anxiety, migraine, TIA, hyperthyroidism and alcohol can mimic a low, so check the glucose.")
q("whipple","A client says, 'I feel like my sugar is low.' What should the nurse do FIRST if possible?",
 ["*Check the blood glucose","Give insulin || Makes a low worse.","Call a rapid response || Not first.","Give a large meal || Check and treat first."],
 "Confirm the low before treating; other conditions can mimic it.")
q("whipple","A client's glucose is 61 mg/dL. They're awake and can drink. Which level of hypoglycemia is this?",
 ["*Level 1 (54–69): treat with the 15-15 rule by mouth","Level 2 || Level 2 is under 54.","Level 3 || Level 3 includes altered consciousness.","Not hypoglycemia || Under 70 is low."],
 "Level 1: 54–69, awake. Level 2: under 54. Level 3: under 54 with altered consciousness.")
q("whipple","A client's glucose is 46 mg/dL. They respond to voice but can't swallow safely. What does the nurse give?",
 ["*Glucagon (Level 2 hypoglycemia)","Orange juice || Can't swallow safely.","Nothing; it's Level 1 || Under 54 is Level 2.","Insulin || Makes it worse."],
 "Level 3 (altered consciousness) = IV D50W.")

# ---------- DKA recognition ----------
q("dka","A teen with type 1 diabetes has deep, rapid breathing and fruity breath. Glucose is 460 and urine ketones are large. What is the likely problem?",
 ["*DKA","HHS || Little or no ketones.","Hypoglycemia || Glucose is high.","Dumping syndrome || Not related."],
 "DKA triad: high glucose, ketones, metabolic acidosis.")
q("dka","Which glucose cutoffs separate DKA from HHS?",
 ["*DKA usually over 250; HHS over 600","DKA over 600; HHS over 250 || Reversed.","Both over 126 || That's the diabetes cutoff.","Both over 180 || Mild hyperglycemia."],
 "DKA is often 300–500. HHS is often over 1,000.")
q("dka","What is the deep, rapid breathing pattern in DKA called, and why does it happen?",
 ["*Kussmaul respirations, to blow off acid","Cheyne-Stokes, from a stroke || Not DKA.","Biot's breathing, from pain || Not DKA.","Bradypnea, from too much insulin || Not DKA."],
 "The body is trying to fix metabolic acidosis.")
q("dka","Which lab results fit DKA? "+SATA,
 ["*pH under 7.3","*Bicarbonate under 15","*Ketones in the blood","*Anion gap over 12","Glucose 1,100 with no ketones || HHS."],
 "Potassium is often high at first, then drops when insulin starts.")
q("dka","A client in DKA has a potassium of 5.6 mEq/L before treatment. What should the nurse expect once insulin starts?",
 ["*The potassium will drop, so it must be watched closely","It will keep rising || Insulin moves potassium into cells.",
  "It won't change || It changes a lot.","It doesn't matter || Low potassium causes arrhythmias."],
 "Goal potassium during treatment: 4–5 mEq/L.")
q("dka","Which DKA complications can be life-threatening? "+SATA,
 ["*Cerebral edema","*Dysrhythmias","*Shock","*Coma","Gum overgrowth || Not related."],
 "DKA is often the first sign of type 1 in children.")

# ---------- DKA treatment ----------
q("dkatx","A client in DKA has a BP of 84/50. What does the nurse give FIRST?",
 ["*0.9% normal saline, 1–2 L quickly","An IV insulin bolus || No bolus; fluids first.","Sodium bicarbonate || Only if pH is under 6.9.","D5W || Dextrose comes later."],
 "Then 250–500 mL/hr depending on hydration.")
q("dkatx","Which list correctly describes DKA treatment?",
 ["*IV fluids, a regular insulin drip, and potassium replacement","Oral fluids and a snack || Not for DKA.",
  "An insulin bolus only || Fluids come first; no bolus.","Glucagon and D50 || Glucose is high."],
 "Regular insulin 0.1 units/kg/hr, no initial bolus.")
q("dkatx","The potassium is 3.0 mEq/L, and an insulin drip is ordered for DKA. What should the nurse do?",
 ["*Hold the insulin, notify the provider, and replace potassium first","Start the insulin as ordered || Insulin would drop potassium further.",
  "Double the insulin rate || Dangerous.","Give potassium after the first hour of insulin || Replace first."],
 "Hold insulin if potassium is under 3.3 mEq/L.")
q("dkatx","During DKA treatment the glucose falls to 230 mg/dL, but the client is still acidotic. What does the nurse expect?",
 ["*Add dextrose to the IV fluids and keep the insulin running","Stop the insulin || Never stop unless ordered; acidosis isn't fixed.",
  "Give an insulin bolus || Not indicated.","Give glucagon || Glucose isn't low."],
 "Dextrose prevents a low while insulin keeps clearing ketones.")
q("dkatx","How fast should glucose come down during DKA treatment?",
 ["*About 50–70 mg/dL per hour","As fast as possible || Risk of cerebral edema.","200 mg/dL per hour || Too fast.","10 mg/dL per day || Too slow."],
 "Steady, not sudden.")
q("dkatx","Which nursing actions apply to a client on an insulin drip for DKA? "+SATA,
 ["*Check glucose every 1–2 hours","*Neuro checks for cerebral edema","*Strict I&O","*Cardiac monitoring","Turn off the insulin once glucose looks normal || Never without an order."],
 "Also electrolytes every 2–4 hours and seizure precautions.")
q("dkatx","Which results show DKA has resolved so the client can switch to subcutaneous insulin? "+SATA,
 ["*pH over 7.30","*Bicarbonate over 18","*Anion gap under 12","*Glucose under 200","Kussmaul breathing still present || Should be gone."],
 "Also stable vital signs and urine output of 30–50 mL/hr.")
q("dkatx","How are DKA fluid boluses given to a child compared with an adult?",
 ["*More slowly, over 30–60 minutes","Faster || Children are given fluids more slowly.","Not at all || Fluids are needed.","Dextrose only || Isotonic saline is used."],
 "Rapid shifts in children can cause cerebral edema.")

# ---------- HHS ----------
q("hhs","An 80-year-old with type 2 diabetes has been confused for 3 days. Glucose is 1,050, sodium 152 and urine ketones are negative. What is the likely problem?",
 ["*HHS","DKA || Ketones would be present.","Hypoglycemia || Glucose is high.","Stroke only || The labs point to HHS."],
 "HHS: glucose over 600, high osmolality, profound dehydration, little or no ketosis.")
q("hhs","Which findings are expected in HHS? "+SATA,
 ["*Glucose over 600 mg/dL","*Serum osmolality over 320","*Severe dehydration","*Confusion or other mental status changes","Fruity breath and Kussmaul breathing || Notably absent."],
 "Labs: sodium over 145, high BUN/creatinine, bicarbonate over 15, high hematocrit (hemoconcentration).")
q("hhs","Why does a client in HHS NOT have fruity breath or Kussmaul breathing?",
 ["*There's little or no ketosis and no significant acidosis","Because glucose is low || Glucose is very high.",
  "Because they're too dehydrated to breathe fast || Not the reason.","Because HHS only happens in type 1 || Mostly type 2."],
 "Type 2 clients still make some insulin, enough to prevent ketosis.")
q("hhs","How does HHS compare with DKA? "+SATA,
 ["*HHS develops more slowly, over days to weeks","*HHS has a higher death rate","*HHS is more common in type 2","*HHS glucose is usually higher","HHS has more ketones || Fewer."],
 "Typical fluid deficit in HHS is 8–12 L.")

# ---------- HHS treatment ----------
q("hhstx","What is the FIRST priority in treating HHS?",
 ["*IV fluids","Insulin drip || May not even be needed.","Sodium bicarbonate || No significant acidosis.","Glucagon || Glucose is high."],
 "Normal saline 1–2 L in the first hour, then 100–200 mL/hr based on heart status.")
q("hhstx","Which formula estimates the fluid (free water) deficit in HHS?",
 ["*0.6 × weight (kg) × [(serum Na⁺ ÷ 140) − 1]","0.1 × weight (kg) || That's the insulin drip dose (units/kg/hr).",
  "Weight (kg) × 30 || A daily fluid estimate.","Glucose ÷ 18 || Not the formula."],
 "Know the formula. Typical deficit: 8–12 L.")
q("hhstx","In the HHS fluid-deficit formula, which number is multiplied by the client's weight in kg?",
 ["*0.6","0.1 || That's the insulin drip dose per kg.","140 || The sodium is divided by 140.","1.5 || Not in the formula."],
 "0.6 × weight (kg) × [(serum Na⁺ ÷ 140) − 1].")
q("hhstx","The serum sodium in the HHS fluid formula is divided by which number?",
 ["*140","100 || Not the number.","0.6 || That multiplies the weight.","600 || The HHS glucose cutoff."],
 "Then subtract 1, and multiply by 0.6 × weight (kg).")
q("hhstx","The estimated HHS fluid deficit is 10 L. How is it replaced?",
 ["*Half over the first 12 hours, the other half over the next 36 hours","All 10 L in the first 2 hours || Too fast; cerebral edema.",
  "Evenly over 4 hours || Too fast.","By mouth as tolerated || IV is needed."],
 "Watch older adults for fluid overload and pulmonary edema.")
q("hhstx","During HHS treatment, when does the nurse expect the IV fluid to change from 0.9% to 0.45% saline?",
 ["*When glucose drops below 300 or the client is stable, per the provider","Immediately on arrival || Start with 0.9%.",
  "When glucose is over 600 || That's the starting point.","Never || The slide says to switch."],
 "Assess for cerebral edema and pulmonary edema throughout.")
q("hhstx","Why is glucose lowered slowly (50–70 mg/dL per hour) in HHS?",
 ["*To prevent cerebral edema","To save insulin || Not the reason.","To let ketones clear first || HHS has few ketones.","Because fast drops raise potassium || Not the reason."],
 "Reduce the insulin drip when glucose is under 300, or stop it under 250 after provider evaluation.")
q("hhstx","During HHS treatment, what potassium level is the goal?",
 ["*4–5 mEq/L","2–3 mEq/L || Too low.","6–7 mEq/L || Too high.","Potassium doesn't need monitoring || Watch for arrhythmias."],
 "Also replace phosphate if severely low and correct magnesium.")
q("hhstx","Which events can trigger HHS? "+SATA,
 ["*Pneumonia or a UTI","*Starting steroids or diuretics","*Stopping diabetes medications","*MI or stroke","Daily walking || Not a trigger."],
 "Teach sick day rules and hydration.")
q("hhstx","Which nursing care fits a client being treated for HHS? "+SATA,
 ["*Neuro checks every 1–2 hours","*Seizure precautions","*Strict I&O","*Daily weights","Ambulate right away || Bed rest until stable."],
 "Also DVT and fall prevention.")

# ---------- chronic complications ----------
q("chronic","Which diabetes complications are MICROvascular? "+SATA,
 ["*Retinopathy","*Nephropathy","*Neuropathy","Heart attack || Macrovascular.","Stroke || Macrovascular."],
 "The kidney is the first organ affected by diabetes.")
q("chronic","A client with long-standing diabetes gets dizzy when standing and feels full after a few bites. Which complication explains this?",
 ["*Autonomic neuropathy","Retinopathy || Affects the eyes.","Nephropathy || Affects the kidneys.","Hypoglycemia || Not the explanation."],
 "Autonomic neuropathy can also cause silent MI.")
q("chronic","Which routine care does every client with diabetes need? "+SATA,
 ["*A yearly eye exam","*Daily foot checks and proper shoes","*Provider visits every 3–6 months","An eye exam only if vision changes || Yearly regardless."],
 "Neuropathy plus poor blood flow leads to foot ulcers.")

# ---------- sick day ----------
q("sick","A client with type 2 diabetes on insulin has a stomach virus and asks, 'Should I skip my insulin?' What is the answer?",
 ["*No; keep taking insulin, because illness raises glucose","Yes, until you can eat || Risks DKA or HHS.",
  "Take half every other day || Not the rule.","Only if your sugar is over 400 || Too late."],
 "Check glucose often and stay hydrated.")
q("sick","Which sick day rules should the nurse teach? "+SATA,
 ["*Keep taking insulin","*Drink 8–12 oz of sugar-free fluid every hour while awake","*Check glucose about every 4 hours","*Use sugar-free cough medicine","Stop all diabetes medicines until better || Don't stop without the provider."],
 "Use soft or liquid carbs if solid food isn't tolerated.")
q("sick","When should a sick client with diabetes go to the emergency department? "+SATA,
 ["*Vomiting for more than 6 hours","*Glucose that stays over 240","*Ketones in the urine","*Fruity breath or confusion","A mild sore throat || Not an emergency."],
 "These signal DKA risk.")

# ---------- discharge ----------
q("dc","Which discharge teaching is important for a client newly on insulin? "+SATA,
 ["*Wear a medical alert bracelet","*Carry a fast-acting sugar snack","*How to store and dispose of insulin","*How to use a glucagon pen","Skip meals to lose weight || Hypoglycemia risk."],
 "Involve family and community resources.")
q("dc","A client with diabetes gets a small blister on the heel from new shoes. What should the nurse teach?",
 ["*Check feet daily and report any wound that isn't healing","Pop it and ignore it || Small wounds can become ulcers.",
  "Soak the foot in hot water || Burns from poor sensation.","Go barefoot to let it breathe || Wear proper shoes."],
 "Neuropathy hides pain, so look at the feet every day.")
q("dc","About how many calories per kg per day does the carb counting slide recommend?",
 ["*25–30 kcal/kg/day (varies with activity)","10–15 kcal/kg/day || Too low.","50–60 kcal/kg/day || Too high.","There's no target || There is."],
 "Carbs: about 45–60 g per meal and 15–30 g per snack.")
