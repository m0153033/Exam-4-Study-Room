# Week 11.1 Glucose Regulation with Metabolic Syndrome — Prof. Mila Jones's transcript + PowerPoint (+ calorie counting chart).
T = "glucose"
CONCEPTS = {
 "norm":"Normal glucose regulation",
 "metsyn":"Metabolic syndrome criteria",
 "metsx":"Metabolic syndrome findings & complications",
 "metmgmt":"Metabolic syndrome lifestyle management",
 "metdrugs":"Metabolic syndrome meds: GLP-1, metformin, statins, ACE",
 "barind":"Bariatric surgery: indications & procedures",
 "barcare":"Bariatric pre/post-op care & leak",
 "bardc":"Bariatric discharge, dumping & supplements",
 "dx":"Diagnostic tests & cutoffs",
 "types":"Prediabetes, MODY & gestational diabetes",
 "t1t2":"Type 1 vs type 2",
 "monitor":"Glucose monitoring & CGM",
 "insulin":"Insulin types: onset, peak, duration",
 "insadmin":"Insulin administration, storage & sliding scale",
 "drugint":"Drugs that raise or lower glucose with insulin",
 "injectables":"GLP-1 agonists & amylin mimetics",
 "orals":"Oral agents: sulfonylureas to gliptins",
 "sglt2":"SGLT2 inhibitors",
 "hyper":"Hyperglycemia, dawn & Somogyi",
 "hypo":"Hypoglycemia & rule of 15",
 "dka":"DKA recognition",
 "dkatx":"DKA treatment & goals",
 "hhs":"HHS",
 "chronic":"Chronic complications",
 "sick":"Sick day rules",
 "dc":"Discharge teaching & carb counting",
}
HI = ["hypo","dka","dkatx","hhs","insulin","insadmin","orals","sick","dx","hyper"]

SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

# ---------- normal regulation ----------
q("norm","What is the normal fasting blood glucose for a healthy adult, per the lecture?",
 ["*70–99 mg/dL","100–125 mg/dL || Prediabetes.","126–180 mg/dL || Diabetes range.","50–69 mg/dL || Hypoglycemia."],
 "The body keeps fasting glucose tightly in 70–99 mg/dL.")
q("norm","Which hormone is released by alpha cells when blood glucose is low?",
 ["Insulin || Released by beta cells when glucose is high.","*Glucagon","Amylin || Not the backup hormone described.","Cortisol || Not the pancreatic hormone described."],
 "Glucagon signals the liver to release stored glucose (glycogen). Insulin is the 'key' that lets glucose into cells.")
q("norm","Which effects does insulin have? "+SATA,
 ["*Moves glucose into cells","*Promotes glycogen storage in the liver","*Moves potassium into cells","*Inhibits ketone production",
  "Breaks down glycogen into glucose || Glucagon's effect; insulin inhibits glycogenolysis."],
 "Insulin also enhances protein and fat synthesis and inhibits gluconeogenesis.")

# ---------- metabolic syndrome criteria ----------
q("metsyn","How many criteria are needed to diagnose metabolic syndrome?",
 ["1 || Not enough; 3 or more are needed.","2 || Not enough; 3 or more are needed.","*3 or more","All 5 || Only 3 or more are required."],
 "Criteria: BP ≥130/85 (or on meds), low HDL, triglycerides ≥150, fasting glucose ≥100 (or on meds), large waist.")
q("metsyn","Which findings count toward metabolic syndrome? "+SATA,
 ["*BP 134/88 mmHg","*Triglycerides 180 mg/dL","*Fasting glucose 108 mg/dL","*Waist 37 inches in a woman",
  "Waist 38 inches in a man || Men need 40 inches or more.","HDL 70 mg/dL || High HDL is protective; LOW HDL counts."],
 "Waist: 40+ inches men, 35+ inches women.")
q("metsyn","What does the lecture call the common denominator of metabolic syndrome and type 2 diabetes?",
 ["*Insulin resistance","Autoimmune beta-cell destruction || Type 1 diabetes.","Low glucagon || Not the common link.","Hypothyroidism || Not discussed as the link."],
 "Central (abdominal) adiposity is the primary driver of insulin resistance.")

# ---------- metabolic syndrome findings ----------
q("metsx","Which findings may appear as metabolic syndrome progresses? "+SATA,
 ["*Increasing waistline","*Difficulty losing weight","*Cravings for carbs and sweets","*Sleep disturbances and fatigue","*Nonalcoholic fatty liver disease",
  "Weight loss with increased appetite || More typical of type 1 diabetes."],
 "Early on there are usually no symptoms. Women with PCOS also have insulin resistance.")
q("metsx","Which are complications of metabolic syndrome? "+SATA,
 ["*Type 2 diabetes","*Atherosclerosis with angina or MI","*Stroke","*Heart failure","*Fatty liver progressing to cirrhosis"],
 "Insulin resistance, high BP and hyperglycemia all damage the heart and vessels.")

# ---------- lifestyle ----------
q("metmgmt","How much weight loss within 6 months helps reverse metabolic syndrome?",
 ["1–2% || Too little.","*5–10% of baseline","25–30% || Not the lecture's target.","Any amount only after surgery || Lifestyle comes first."],
 "Reduces visceral fat and insulin resistance.")
q("metmgmt","Which lifestyle recommendations does the lecture give for metabolic syndrome? "+SATA,
 ["*DASH or Mediterranean diet with complex carbs and high fiber","*At least 150 minutes of moderate exercise a week","*Resistance training","*Stress management",
  "Sugary drinks in moderation daily || Limit sugary beverages."],
 "Resistance training helps muscles take up more glucose.")

# ---------- metabolic drugs ----------
q("metdrugs","A client starting semaglutide asks how to avoid severe nausea. Best teaching?",
 ["*Eat smaller portions and stop eating as soon as you feel full",
  "Eat a large meal before the injection || Worsens nausea.","Skip doses when nauseated || Not the teaching.","Inject it into the same spot each week || Rotate sites."],
 "GLP-1s slow gastric emptying and increase satiety. Rotate sites: abdomen, thigh, upper arm.")
q("metdrugs","A client on liraglutide has severe persistent abdominal pain radiating to the back. What should the nurse suspect?",
 ["Expected GI upset || Severe pain radiating to the back isn't expected.","*Acute pancreatitis",
  "Hypoglycemia || Doesn't present this way.","Dumping syndrome || Not related."],
 "Teach clients to report severe, unremitting abdominal pain immediately. GLP-1s can also cause severe dehydration from vomiting.")
q("metdrugs","Which history is a contraindication to GLP-1 agonists?",
 ["*Personal or family history of medullary thyroid carcinoma","Hypertension || Not a contraindication.","Obesity || An indication.","Type 2 diabetes || An indication."],
 "Also multiple endocrine neoplasia and severe GI disease (gastroparesis).")
q("metdrugs","A client on metformin is scheduled for a CT with IV contrast. What should the nurse anticipate?",
 ["Double the metformin the night before || Not taught.","*Hold metformin for at least 48 hours after the contrast study",
  "No change is needed || Contrast can cause lactic acidosis.","Give it with the contrast || Not taught."],
 "Also avoid alcohol and cimetidine (lactic acidosis risk). Take with meals; monitor renal function.")
q("metdrugs","A client on atorvastatin reports unexplained muscle pain and weakness. What is the concern?",
 ["Expected soreness from exercise || Must be reported.","*Rhabdomyolysis","Lactic acidosis || Metformin.","Angioedema || ACE inhibitors."],
 "Statins require baseline and periodic LFTs.")

# ---------- bariatric indications ----------
q("barind","Which client meets bariatric surgery criteria?",
 ["BMI 32 with no health problems || Below criteria.",
  "*BMI 37 with type 2 diabetes, after failed conservative management",
  "BMI 30 with sleep apnea || Below the BMI 35 threshold.","BMI 33 who hasn't tried lifestyle changes || Below criteria and no failed conservative management."],
 "BMI ≥35 + 1 comorbidity (T2DM, HTN, HLD, OSA), or BMI ≥40 regardless, plus failed conservative management.")
q("barind","Which procedure is malabsorptive and bypasses part of the small intestine?",
 ["Sleeve gastrectomy || Restrictive only.","Adjustable gastric banding || Restrictive only.",
  "*Roux-en-Y gastric bypass","Endoscopic sleeve gastroplasty || Non-surgical, restrictive."],
 "Roux-en-Y is the gold standard with excellent diabetes remission and weight loss (60–80% excess weight).")
q("barind","Which bariatric procedure is reversible with the lowest surgical risk, but the slowest weight loss?",
 ["*Adjustable gastric banding","Roux-en-Y || Complex and permanent.","Sleeve gastrectomy || Irreversible.","Duodenal switch || Complex and malabsorptive."],
 "Complications include band slippage, erosion and port problems.")
q("barind","Why do bypass clients need lifelong vitamin supplements?",
 ["*Bypassing part of the small intestine impairs absorption of B12, folate, iron and calcium",
  "The stomach makes more acid || Not the reason.","The pancreas stops working || Not the reason.","Only for the first year after surgery || It's lifelong."],
 "Permanence, lifelong supplements and strict behavior change are the major disadvantages.")

# ---------- bariatric care ----------
q("barcare","After a gastric bypass, what is the EARLIEST sign of an anastomotic leak?",
 ["Hypotension || Later sign.","*Unexplained tachycardia (HR over 120)","Bradycardia || Not the sign.","Weight gain || Not related."],
 "Also tachypnea, fever, and progressive left shoulder or back pain. Report to the surgeon immediately.")
q("barcare","Which post-op care is correct after bariatric surgery? "+SATA,
 ["*Semi-Fowler's position","*Incentive spirometer every 1–2 hours while awake","*Ambulate 4–6 hours after surgery, then 3–4 times a day","*SCDs while in bed",
  "Reposition the NG tube if it isn't draining || Never reposition or irrigate it; it can disrupt staple lines."],
 "Obesity is a hypercoagulable state; DVT prevention matters.")
q("barcare","When the surgeon clears a bariatric client to drink, how should fluids start?",
 ["Full glass of water with each meal || Too much, and no fluids with meals.","*Small sips of clear liquids, about 30 mL every hour",
  "Protein shakes on day 1 || Diet progresses slowly.","Regular diet || Not until weeks later."],
 "Clearance is often after a negative upper GI contrast study.")
q("barcare","Which pre-op teaching applies to bariatric surgery? "+SATA,
 ["*Strict liquid or low-calorie diet 1–2 weeks before, to shrink the liver","*How to use an incentive spirometer","*Splint the incision with a pillow when coughing","*Expect to walk within hours of surgery",
  "No need for a psychological evaluation || Psychological clearance is mandatory."],
 "Also verify consent and clearance, accurate height and weight, a respiratory assessment (OSA), and CHG prep in skin folds.")

# ---------- bariatric discharge ----------
q("bardc","Which diet progression is correct after bariatric surgery?",
 ["*Clear liquids → full liquids → pureed → solid foods over several weeks","Solid foods right away || Too fast.",
  "Full liquids for life || Diet advances.","Pureed → clear → solid || Wrong order."],
 "Eat 6 small meals a day, chew to a paste and stop at the first feeling of fullness.")
q("bardc","What is the 'crucial rule' about fluids after bariatric surgery?",
 ["Drink with every bite || Pushes food through too fast.","*No liquids 30 minutes before and 30–60 minutes after solid food",
  "Only drink at bedtime || Not the rule.","Carbonated drinks only || Not the rule."],
 "Prevents premature flushing of food into the intestine (dumping) and pouch stretching.")
q("bardc","A post-bypass client feels dizzy, sweaty and crampy with palpitations soon after eating. What should the nurse teach?",
 ["Drink a large glass of juice || Sugar worsens dumping.","*Lie down for 30 minutes and avoid high-sugar, high-fat, processed carbs",
  "Walk briskly after meals || Not the teaching.","Eat bigger meals less often || Small meals."],
 "Early dumping syndrome: high-carb contents move rapidly into the small intestine and draw in fluid.")
q("bardc","When should a bariatric client call the surgeon? "+SATA,
 ["*Fever over 101°F (38.3°C)","*Severe abdominal pain radiating to the left shoulder","*Persistent nausea and vomiting","*Redness or purulent drainage at the incision",
  "Losing about 1–2 lb a week || Expected."],
 "Signs of leak, infection and sepsis.")
q("bardc","Which late complications can occur after bariatric surgery? "+SATA,
 ["*Iron-deficiency and pernicious anemia","*Osteoporosis from poor vitamin D and calcium absorption","*Internal or incisional hernias and bowel obstruction","*Gallstones",
  "Type 1 diabetes || Not a complication."],
 "Also marginal ulcers and band slippage or stenosis.")

# ---------- diagnostics ----------
q("dx","Which A1C result diagnoses diabetes?",
 ["5.5% || Normal.","6.0% || Prediabetes (5.7–6.4%).","*6.8%","5.7% || The bottom of the prediabetes range."],
 "A1C ≥6.5% = diabetes. Normal under 5.7%. It reflects the average glucose over ~120 days (RBC lifespan).")
q("dx","Which fasting glucose result falls in the prediabetes range?",
 ["92 mg/dL || Normal.","*112 mg/dL","130 mg/dL || Diabetes range (≥126, confirmed twice).","68 mg/dL || Low."],
 "Prediabetes: fasting 100–125 mg/dL; 2-hour OGTT 140–199; A1C 5.7–6.4%.")
q("dx","What must a client do for an accurate fasting blood glucose?",
 ["*Fast for 8 hours","Fast for 2 hours || Too short.","Eat a high-carb meal first || That's a different test.","Nothing; timing doesn't matter || Eating raises the result."],
 "A fasting result ≥126 mg/dL on at least two occasions = diabetes.")
q("dx","A random plasma glucose of 250 mg/dL with polyuria and polydipsia means what?",
 ["Normal after a meal || Over 200 with symptoms is diagnostic.","*It meets the threshold for diabetes",
  "Prediabetes || Too high.","Hypoglycemia || Too high."],
 "Random plasma glucose over 200 mg/dL with classic symptoms is diagnostic.")
q("dx","Which limitation of the A1C test does the lecture point out?",
 ["*It's affected by anemia","It's affected by the last meal || That limits fasting glucose.","It only shows the last 24 hours || About 120 days.","It can't diagnose diabetes || It's the gold standard."],
 "A1C over 8% = poorly controlled diabetes or poor adherence.")
q("dx","What is the ADA's recommended A1C goal for most clients with diabetes?",
 ["Under 5.7% || The normal value, not the treatment goal.","*7% or below","Under 9% || Too high.","Exactly 6.5% || The diagnostic threshold."],
 "Also pre-meal glucose 70–130 mg/dL and post-meal peak at 180 mg/dL.")

# ---------- types ----------
q("types","How is prediabetes usually managed?",
 ["*Lifestyle changes; it can be reversed without medication","Insulin right away || Not needed.","Sulfonylureas || Not first-line here.","Bariatric surgery || Not for prediabetes."],
 "Cut sugary drinks, vegetable and fish diet, portion control, at least 8 hours of sleep. Darkened skin on the neck, armpit or groin may appear.")
q("types","Which statements describe MODY? "+SATA,
 ["*A genetic, autosomal dominant mutation","*Onset around age 10–45","*Often misdiagnosed as type 1","*Not autoimmune, with preserved beta-cell function",
  "Always requires insulin from diagnosis || Often no treatment; sulfonylureas are the drug of choice."],
 "Glipizide is the drug of choice; insulin if sulfonylureas don't control it.")
q("types","Which test screens for gestational diabetes in the second trimester?",
 ["*Oral glucose tolerance test","A1C only || Not the standard pregnancy test.","Serum ketones || Not a screen.","HIDA scan || Not related."],
 "Done at 24–28 weeks; the client drinks a glucose load and blood is drawn over about 3 hours.")
q("types","If diet and exercise don't control gestational diabetes, which medication is NOT used?",
 ["Metformin || The safest oral agent in pregnancy.","Insulin || Used if metformin isn't enough.",
  "*Sulfonylureas such as glipizide","None; all are safe || Sulfonylureas are contraindicated."],
 "Sulfonylureas cross the placenta and can cause fetal hyperinsulinemia.")
q("types","A woman with past gestational diabetes asks about her future risk. What should the nurse say?",
 ["*Gestational diabetes increases her risk for type 2 diabetes later",
  "It always turns into type 1 || Not the risk.","It has no future impact || Risk increases.","It only affects future pregnancies || It raises T2DM risk overall."],
 "History of gestational diabetes or PCOS is a non-modifiable type 2 risk factor.")

# ---------- T1 vs T2 ----------
q("t1t2","Which findings point to type 1 rather than type 2 diabetes? "+SATA,
 ["*Thin child or young adult","*Sudden onset","*Absolute insulin deficiency","*Nocturnal enuresis","*Prone to ketosis",
  "Gradual onset in an adult with obesity || Type 2."],
 "Type 1: autoimmune destruction of beta cells; often first presents as DKA in children.")
q("t1t2","Why are clients with type 2 diabetes 'ketosis resistant'?",
 ["*They still produce some insulin","They don't eat carbohydrates || Not the reason.","Their kidneys excrete ketones instantly || Not the reason.","They take metformin || Not the reason."],
 "Type 2: insulin resistance with relative deficiency; 90–95% of cases.")
q("t1t2","Which symptoms are common to BOTH type 1 and type 2 diabetes? "+SATA,
 ["*Polyuria","*Polydipsia","*Polyphagia","*Fatigue and weakness","*Higher infection risk"],
 "Type 2 infections are often recurring urogenital ones.")
q("t1t2","Which are MODIFIABLE risk factors for type 2 diabetes? "+SATA,
 ["*Obesity","*Sedentary lifestyle","*Smoking","*Chronic stress","*Sleep apnea or insomnia",
  "Family history || Non-modifiable.","Age over 45 || Non-modifiable."],
 "Medications such as corticosteroids, antipsychotics and some diuretics also raise risk.")

# ---------- monitoring ----------
q("monitor","When should a client on intensive insulin therapy check blood glucose? "+SATA,
 ["*Before meals and snacks","*At bedtime","*Before exercising","*Before driving","*When hypoglycemia symptoms occur"],
 "Also periodically after meals, and after treating a low until normal.")
q("monitor","What does a continuous glucose monitor (CGM) measure?",
 ["Venous blood glucose || Not what the sensor reads.","*Glucose in the interstitial fluid via a subcutaneous sensor",
  "Urine glucose || Not a CGM.","A1C daily || Not a CGM."],
 "CGM shows trends with direction and rate of change.")
q("monitor","Which benefits of CGM does the lecture list? "+SATA,
 ["*Lowers A1C by 0.5–1% with consistent use","*30–40% fewer hypoglycemic episodes","*Overnight monitoring and sleep protection","*Pattern recognition",
  "Eliminates the need for insulin || Not a benefit."],
 "FreeStyle Libre is scan-to-read without continuous alarms; Dexcom gives real-time alarms.")

# ---------- insulin types ----------
q("insulin","Which insulin has an onset of 5–15 minutes and is used for mealtime coverage?",
 ["*Lispro (Humalog)","Regular (Humulin R) || Onset 30 minutes.","NPH || Onset 2–4 hours.","Glargine (Lantus) || Long-acting, no peak."],
 "Rapid-acting (lispro, aspart, glulisine): peak 1–2 hours, duration 2–4 hours.")
q("insulin","Which insulin has no pronounced peak and provides steady basal coverage?",
 ["Lispro || Rapid-acting, peaks 1–2 hours.","NPH || Peaks 4–12 hours.","*Glargine (Lantus)","Regular || Peaks 2–3 hours."],
 "Glargine/detemir: onset 2–4 hours, duration 20–24 hours. Degludec (ultra-long): over 42 hours.")
q("insulin","A client got NPH at 7 a.m. When is the greatest risk of hypoglycemia?",
 ["7:15 a.m. || Too early; NPH onset is 2–4 hours.","*Between about 11 a.m. and 7 p.m.","Next morning || Duration 10–16 hours.","There's no peak || Glargine has no peak; NPH does."],
 "NPH (intermediate) peaks 4–12 hours after the dose.")
q("insulin","Which insulin is cloudy?",
 ["Lispro || Clear.","Regular || Clear.","*NPH","Glargine || Clear."],
 "Don't use short-acting insulin if it's cloudy.")
q("insulin","Which insulin does the lecture list for the IV infusion in DKA?",
 ["NPH || Not given IV.","Glargine || Not given IV.","*Regular insulin","Degludec || Not given IV."],
 "DKA: regular insulin 0.1 units/kg/hr IV continuous infusion.")

# ---------- insulin administration ----------
q("insadmin","When should the nurse give pre-meal rapid-acting insulin in the hospital?",
 ["An hour before the tray arrives || Hypoglycemia risk if the meal is late.","*When the tray is at the bedside or after the first bite",
  "After the meal is finished || Too late for mealtime coverage.","At bedtime || Not mealtime insulin."],
 "Monitor for hypoglycemia, especially in active adolescents.")
q("insadmin","Lispro 10 units is ordered before meals plus a lispro sliding scale. Pre-breakfast glucose is 180 mg/dL, and the scale gives 4 units for that range. What should the nurse give?",
 ["10 units in one syringe and 4 units in another || Use one syringe when possible.","*14 units of lispro in one syringe",
  "4 units only || The standing dose is also due.","10 units only || The sliding scale dose is also due."],
 "Same insulin: add the standing dose and the correction dose and draw them in one syringe.")
q("insadmin","When mixing regular and NPH insulin, which is drawn up first?",
 ["NPH (cloudy) || Draw clear first.","*Regular (clear)","Either one || Order matters.","They should never be mixed || They can be, per manufacturer."],
 "Clear before cloudy, so the cloudy insulin doesn't contaminate the clear vial.")
q("insadmin","How long can an opened insulin vial stay at room temperature (up to 77°F)?",
 ["7 days || Too short.","*28 days","6 months || Too long.","Until the printed expiration date || That's for unopened, refrigerated vials."],
 "Unopened: refrigerate at 36–46°F. Protect from light; use a cool bag with ice packs when traveling.")
q("insadmin","Which insulin injection practices are correct? "+SATA,
 ["*Rotate sites to prevent lipodystrophy","*90-degree angle (45 for thin clients)","*Don't pinch in obese clients; spread the skin instead","*Best sites are the abdomen and back of the arm",
  "Use the same spot each time for consistent absorption || Causes lipodystrophy."],
 "Lipodystrophy affects insulin absorption.")
q("insadmin","A client's insulin-to-carb ratio is 1:10. How many units of rapid-acting insulin cover a 60-gram carb meal?",
 ["4 units || 60 ÷ 10 = 6.","*6 units","10 units || That's the ratio, not the dose.","60 units || Not how the ratio works."],
 "1:10 = 1 unit per 10 grams of carbohydrate. Rapid-acting insulin is given 0–15 minutes before meals.")

# ---------- drug interactions ----------
q("drugint","A client on insulin drinks alcohol all evening. When is hypoglycemia most likely?",
 ["Within 5 minutes || Not the pattern.","*Delayed, often overnight (6–24 hours later)","Only the next week || Not the pattern.","Never; alcohol raises glucose || It suppresses liver glucose release."],
 "The liver is busy breaking down alcohol and doesn't release glucose.")
q("drugint","Which medications can RAISE blood glucose in a client on insulin? "+SATA,
 ["*Prednisone","*Albuterol","*Thiazide diuretics","*Thyroid hormone",
  "Sulfonylureas || These increase hypoglycemia risk."],
 "Review the medication profile; notify the provider so insulin doses can be adjusted.")
q("drugint","How do beta blockers affect a client with diabetes?",
 ["*They can worsen glucose control and hide early warning signs of hypoglycemia (except sweating)",
  "They cure insulin resistance || Not true.","They have no effect || They matter.","They cause lactic acidosis || Metformin."],
 "Sweating may be the only early warning sign left.")
q("drugint","Which drugs increase hypoglycemia risk when given with insulin? "+SATA,
 ["*High-dose aspirin (salicylates)","*Thiazolidinediones at high doses","*Sulfonylureas","*Meglitinides",
  "Glucocorticoids || These raise glucose."],
 "Sensitizers make cells respond more; secretagogues squeeze more insulin out.")

# ---------- GLP-1 & amylin ----------
q("injectables","How do GLP-1 agonists such as semaglutide lower glucose with a LOW risk of hypoglycemia?",
 ["*They stimulate insulin release only when glucose is elevated","They block all glucose absorption || Not the mechanism.",
  "They replace insulin entirely || Not the mechanism.","They make the kidneys excrete glucose || SGLT2."],
 "They also suppress glucagon, slow gastric emptying, promote satiety; 5–15% weight loss; weekly dosing.")
q("injectables","Which teaching is correct for pramlintide (Symlin)? "+SATA,
 ["*Give SC 30 minutes before meals","*Don't mix it in the same syringe as insulin","*Watch for severe hypoglycemia with insulin",
  "It's safe with gastroparesis || Contraindicated with gastroparesis.","Take it whether or not you eat || Skipping the meal causes hypoglycemia."],
 "Amylin mimetic: slows gastric emptying, suppresses postprandial glucagon; peaks in 20 minutes.")
q("injectables","Which side effects are common with GLP-1 agonists? "+SATA,
 ["*Nausea and vomiting","*Diarrhea or constipation","*Injection site reactions","*Possible gallbladder disease",
  "Lactic acidosis || Metformin."],
 "Rare: pancreatitis, which needs urgent management.")

# ---------- oral agents ----------
q("orals","What is the first-line oral medication for type 2 diabetes?",
 ["Glipizide || Second-line.","*Metformin","Pioglitazone || Usually combination therapy.","Acarbose || Not first-line."],
 "Metformin blocks liver glucose production and doesn't cause hypoglycemia alone. It may cause weight loss or keep weight steady.")
q("orals","A client on metformin reports muscle aches, confusion and fatigue after drinking heavily. What should the nurse suspect?",
 ["*Lactic acidosis","Hypoglycemia || Metformin alone doesn't cause it.","Expected effects || Not expected.","Rhabdomyolysis from statins || The scenario points to metformin."],
 "Avoid alcohol and cimetidine. Metformin can also cause B12 and folic acid malabsorption.")
q("orals","A client takes repaglinide (a meglitinide) and plans to skip lunch. What should the nurse teach?",
 ["*Skip the dose if you skip the meal","Take it anyway || Causes hypoglycemia.","Double it at dinner || Not taught.","Take it at bedtime || Not taught."],
 "Meglitinides: take 30 minutes before meals, up to 3–4 times a day; fast onset, short duration.")
q("orals","Which side effects are associated with sulfonylureas such as glipizide? "+SATA,
 ["*Hypoglycemia","*Weight gain","*Increased cardiovascular risk",
  "Fluid retention leading to heart failure || TZDs.","Flatulence || AGIs."],
 "Contraindicated in type 1, pregnancy and lactation. Take 30 minutes before meals; swallow whole.")
q("orals","A client on pioglitazone (a TZD) has new ankle edema and shortness of breath. What is the concern?",
 ["*Fluid retention leading to heart failure","Lactic acidosis || Metformin.","Expected weight loss || TZDs cause weight gain.","Pancreatitis || Gliptins/GLP-1s."],
 "TZDs also raise triglycerides and bladder cancer risk; contraindicated in heart failure.")
q("orals","When should acarbose (an alpha-glucosidase inhibitor) be taken?",
 ["*With the first bite of each meal","At bedtime || Not the instruction.","30 minutes before meals || Not the instruction.","Once weekly || Not the instruction."],
 "Blocks the enzyme that breaks down carbs; side effects: flatulence, diarrhea, abdominal pain. Avoid in IBD and cirrhosis.")
q("orals","Which adverse effects are associated with gliptins such as sitagliptin (Januvia)? "+SATA,
 ["*Stevens-Johnson syndrome","*Angioedema","*Pancreatitis","*Upper respiratory infection",
  "Severe hypoglycemia alone || Gliptins don't cause hypoglycemia."],
 "Can be combined with metformin. Contraindicated with a history of pancreatitis or severe renal impairment.")

# ---------- SGLT2 ----------
q("sglt2","How do SGLT2 inhibitors such as dapagliflozin lower glucose?",
 ["*They increase urinary glucose excretion","They squeeze more insulin out of the pancreas || Sulfonylureas.",
  "They slow gastric emptying || GLP-1.","They block carb digestion || AGIs."],
 "They also reduce HF/CV events, slow CKD, raise HDL and lower triglycerides.")
q("sglt2","Which are contraindications to SGLT2 inhibitors? "+SATA,
 ["*Type 1 diabetes","*Severe renal impairment or dialysis","*Active bladder cancer",
  "Heart failure || SGLT2s reduce HF risk.","Chronic kidney disease (mild) || They slow CKD progression."],
 "Side effects: hypotension, genital and urinary infections, euglycemic DKA, Fournier's gangrene (rare).")
q("sglt2","When should an SGLT2 inhibitor be taken?",
 ["*Every morning, with or without food","At bedtime || Causes nighttime urination.","With each meal || Not the instruction.","Only when glucose is high || Daily."],
 "Combine with diet and exercise; stay hydrated.")

# ---------- hyperglycemia ----------
q("hyper","A client's 3 a.m. glucose is LOW and the morning glucose is high. What is this?",
 ["Dawn phenomenon || 3 a.m. glucose would be normal or high.","*Somogyi phenomenon","DKA || Not this pattern.","HHS || Not this pattern."],
 "Somogyi = too much insulin → overnight low → rebound high. Decrease insulin or add a bedtime snack.")
q("hyper","A client's 3 a.m. glucose is normal or high, and the morning glucose is high. What is the likely cause and action?",
 ["*Dawn phenomenon; add insulin","Somogyi phenomenon; decrease insulin || Somogyi has a low 3 a.m. reading.",
  "Hypoglycemia; give juice || Glucose isn't low.","Normal; no change || A pattern to correct."],
 "Dawn = natural growth hormone surge in the early morning.")
q("hyper","Which are early signs of hyperglycemia (180–300 mg/dL)? "+SATA,
 ["*Polyuria","*Polydipsia","*Blurred vision","*Headache and fatigue",
  "Shakiness and sweating || Hypoglycemia."],
 "Treatment: rapid-acting insulin per orders; recheck 1–2 hours after dosing.")
q("hyper","A hospitalized client's glucose stays above 300 mg/dL despite appropriate correction doses. What should the nurse anticipate?",
 ["*Escalation to IV insulin infusion","Stopping insulin || Glucose is high.","Discharge || Not appropriate.","Sliding scale alone || Avoid sliding scale alone."],
 "Use basal-bolus correctional insulin rather than sliding scale alone.")

# ---------- hypoglycemia ----------
q("hypo","What blood glucose level defines hypoglycemia?",
 ["Under 100 mg/dL || Normal fasting is 70–99.","*Under 70 mg/dL","Under 126 mg/dL || Diabetes threshold.","Under 180 mg/dL || Not hypoglycemia."],
 "Causes: medication, too little food, or too much activity.")
q("hypo","An alert client's glucose is 62 mg/dL and they can swallow. What should the nurse do?",
 ["*Give 15 g of fast carbs, wait 15 minutes, recheck","Give IV D50 immediately || For unresponsive clients.",
  "Give glucagon IM || For clients who can't take oral carbs.","Give rapid-acting insulin || Worsens the low."],
 "Rule of 15: repeat if still low. Level 1 (54–70) = awake and able to take PO carbs.")
q("hypo","A client with diabetes is found unresponsive with a glucose of 40 mg/dL in the hospital. What is the priority treatment?",
 ["Orange juice by mouth || Aspiration risk.","*IV dextrose 50%, then D10 infusion if persistent",
  "Hold the next meal || Not a treatment.","Give insulin || Worsens it."],
 "Level 3: altered LOC, can't swallow. Recheck glucose after treatment.")
q("hypo","After a family member gives glucagon to an unconscious client at home, what should they do next?",
 ["*Turn the client on their side to prevent aspiration","Give water by mouth || Aspiration risk.","Lay the client flat on their back || Aspiration risk.","Give insulin || Worsens the low."],
 "Glucagon comes as IM/SC injection or nasal spray; teach significant others how to give it.")
q("hypo","Which are signs of hypoglycemia? "+SATA,
 ["*Shakiness and tremors","*Sweating","*Palpitations","*Irritability","*Dizziness and pallor",
  "Fruity breath || DKA."],
 "Check the glucose first: anxiety, migraine, TIA, hyperthyroidism and alcohol intoxication can mimic hypoglycemia.")
q("hypo","Which items provide about 15 g of carbohydrate? "+SATA,
 ["*1/2 cup of fruit juice","*1 slice of bread","*1 small apple",
  "1 cup of broccoli || Non-starchy vegetables have ~5 g per 1/2 cup.","2 tablespoons of peanut butter || Mainly fat and protein."],
 "Carb standard: 1 serving = 15 g. Also 1/2 cup oatmeal or rice, 1 cup milk.")

# ---------- DKA recognition ----------
q("dka","Which findings are expected in DKA? "+SATA,
 ["*Fruity breath","*Kussmaul respirations","*Glucose 300–500 mg/dL","*pH under 7.3","*Ketones in the blood and urine",
  "Glucose over 1,000 with no ketones || HHS."],
 "Diagnostic triad: hyperglycemia, ketonemia (>3 mmol/L), metabolic acidosis (pH <7.3, bicarb <15).")
q("dka","Which type of diabetes most commonly develops DKA?",
 ["*Type 1","Type 2 || More often HHS.","Prediabetes || Not typical.","MODY || Not typical."],
 "Type 1 clients produce no insulin, so fat breaks down into ketones. DKA is often the first sign in children.")
q("dka","What happens to the anion gap in DKA?",
 ["It falls below 8 || It rises.","*It rises above 12","It stays normal || It rises.","It can't be measured || It's calculated."],
 "Normal 8–12 mEq/L; can be very high in severe DKA.")
q("dka","What happens to serum potassium in DKA?",
 ["*It's often high at first, then drops once insulin moves it into cells","It's always low from the start || Often high initially.",
  "It never changes || Changes are a major danger.","It drops only if the client eats bananas || Not related."],
 "Also low sodium and phosphate; elevated BUN/creatinine and WBC.")
q("dka","Which complications of untreated DKA are life-threatening? "+SATA,
 ["*Cerebral edema","*Cardiac dysrhythmias","*Shock and coma",
  "Gingival hyperplasia || Not related."],
 "Mortality rate 2–5%.")

# ---------- DKA treatment ----------
q("dkatx","A client with DKA is hypotensive. Which intervention comes FIRST?",
 ["IV insulin bolus || Don't bolus insulin initially.","*IV 0.9% normal saline, 1–2 L rapidly",
  "Sodium bicarbonate || Only if pH <6.9 (controversial).","Subcutaneous lispro || Not for DKA."],
 "Fluid resuscitation: 15–20 mL/kg/hr initially, then 250–500 mL/hr.")
q("dkatx","Before starting an insulin infusion for DKA, the potassium is 3.1 mEq/L. What should the nurse do?",
 ["Start the infusion as ordered || Insulin drives K+ into cells and could cause arrhythmias.","*Hold insulin and notify the provider; replace potassium first",
  "Give insulin at double the rate || Dangerous.","Start insulin and recheck K+ in 4 hours || Insulin first would drop K+ further."],
 "Hold insulin if K+ is under 3.3 mEq/L. Goal K+ 4–5 mEq/L.")
q("dkatx","What is the target rate of glucose decline during DKA treatment?",
 ["200 mg/dL per hour || Too fast; risk of cerebral edema.","*About 50–70 mg/dL per hour",
  "As fast as possible || Rapid drops cause cerebral edema.","10 mg/dL per day || Too slow."],
 "A steady drop, not an abrupt one.")
q("dkatx","During DKA treatment the glucose reaches 200 mg/dL but the anion gap is still elevated. What should the nurse anticipate?",
 ["Stop the insulin drip || Acidosis isn't resolved; never stop insulin unless ordered.","*Add dextrose (D5) to the IV fluids and continue insulin",
  "Give D50 || Not indicated.","Switch to oral agents || Not yet."],
 "Dextrose prevents hypoglycemia while insulin keeps clearing the ketones.")
q("dkatx","Which findings show DKA has resolved and the client can switch to SubQ insulin? "+SATA,
 ["*Glucose under 200 mg/dL","*pH over 7.30","*Bicarbonate over 18 mEq/L","*Anion gap under 12",
  "Kussmaul respirations continue || Should be absent."],
 "Also stable VS (MAP over 65, HR under 100) and urine output 30–50 mL/hr.")
q("dkatx","Which nursing care applies to a client on an insulin drip for DKA? "+SATA,
 ["*Glucose checks every 1–2 hours","*Hourly vital signs and neuro checks","*Strict I&O","*Cardiac monitoring",
  "Stop insulin when glucose looks normal without an order || Never stop unless ordered."],
 "Watch for cerebral edema (mental status changes), hypoglycemia, and fluid overload.")
q("dkatx","How do DKA fluid boluses differ for children?",
 ["*They're given more slowly, over 30–60 minutes","They're given faster than adults || Slower.","No fluids are given || They're needed.","Only dextrose is used || Isotonic saline."],
 "Rapid shifts in children can cause cerebral edema and arrhythmias.")

# ---------- HHS ----------
q("hhs","How does HHS differ from DKA? "+SATA,
 ["*Glucose is usually over 600 mg/dL (often over 1,000)","*Minimal or no ketosis","*No Kussmaul respirations or fruity breath","*Slower onset over days to weeks","*Higher mortality (10–20%)",
  "More common in type 1 || More common in type 2."],
 "Type 2 clients still make some insulin, enough to prevent ketosis.")
q("hhs","What is the PRIORITY treatment for HHS?",
 ["Insulin infusion || May not even be necessary.","*Fluid resuscitation","Sodium bicarbonate || No significant acidosis.","Glucagon || Glucose is high."],
 "Fluid deficit is often 8–12 L; normal saline 1–2 L the first hour.")
q("hhs","Why is fluid correction in HHS done gradually (first half over 12 hours)?",
 ["*To prevent cerebral edema from rapid fluid and electrolyte shifts","To save IV fluid || Not the reason.",
  "To allow ketones to build || Not the reason.","Because the client isn't dehydrated || Severe dehydration is the hallmark."],
 "Watch elderly clients for fluid overload and pulmonary edema.")
q("hhs","Which nursing care applies to HHS? "+SATA,
 ["*Neuro checks every 1–2 hours (Glasgow Coma Scale)","*Seizure precautions","*Strict I&O, urine goal over 0.5 mL/kg/hr","*DVT and fall prevention","*Daily weights",
  "Ambulate right away to prevent clots || Bed rest until hemodynamically stable."],
 "Look for precipitating factors: infection, steroids or diuretics, MI or stroke, nonadherence.")
q("hhs","Which precipitating factors can lead to HHS? "+SATA,
 ["*Infection such as pneumonia or UTI","*Steroids or diuretics","*Not taking diabetes medications","*MI or stroke",
  "Regular exercise || Not a precipitating factor."],
 "Emphasize sick day rules, hydration and follow-up.")

# ---------- chronic complications ----------
q("chronic","Which are MICROVASCULAR complications of diabetes? "+SATA,
 ["*Retinopathy","*Nephropathy","*Neuropathy",
  "Coronary artery disease || Macrovascular.","Stroke || Macrovascular."],
 "The lecture notes the kidney is the first organ affected by diabetes.")
q("chronic","A client with diabetes has autonomic neuropathy. Which problems may occur? "+SATA,
 ["*Orthostatic hypotension","*Silent MI","*Gastroparesis",
  "Improved wound healing || Healing is delayed."],
 "Peripheral neuropathy causes glove-and-stocking numbness; cranial neuropathy (CN III, IV, VI) causes diplopia.")
q("chronic","Which follow-up does a client with diabetes need? "+SATA,
 ["*Provider visits every 3–6 months","*Yearly eye exam","*Regular foot care","*Proper footwear",
  "Eye exam only if vision changes || Yearly regardless."],
 "Neuropathy plus poor perfusion leads to foot ulcers, infection and possible amputation.")

# ---------- sick day ----------
q("sick","A client with type 1 diabetes has the flu and isn't eating much. What should the nurse teach about insulin?",
 ["Stop insulin until eating normally || Never stop insulin without the provider; DKA risk.","*Keep taking basal insulin and check glucose and ketones often",
  "Take only oral agents || Not the teaching.","Double the insulin dose || Not without provider guidance."],
 "Illness raises glucose. Check glucose about every 4 hours.")
q("sick","Which sick day rules are correct? "+SATA,
 ["*Drink 8–12 oz of sugar-free fluid every hour while awake","*Use liquid or soft carbohydrate foods if solids aren't tolerated","*Use sugar-free cough and cold medicines","*Check temperature and daily weight",
  "Stop all medications until well || Don't stop without the provider."],
 "Notify the provider before stopping any diabetes medication.")
q("sick","When should a sick client with diabetes seek emergency care? "+SATA,
 ["*Vomiting more than 6 hours","*Glucose persistently over 240 mg/dL","*Ketones in the urine","*Fruity breath or confusion",
  "Mild runny nose || Not an emergency."],
 "These signal DKA risk.")

# ---------- discharge ----------
q("dc","Which discharge teaching applies to a client newly on insulin? "+SATA,
 ["*Wear a medical alert bracelet","*How to store, dispose of and refill insulin","*How to use a glucose kit, glucagon pen, or glucose snack","*Avoid exercising in extreme heat or cold",
  "Skip meals to lose weight faster || Hypoglycemia risk."],
 "Reinforce the diabetes educator's teaching and involve family and community resources.")
q("dc","What daily calorie target does the lecture's carb counting slide give?",
 ["10–15 kcal/kg/day || Too low.","*About 25–30 kcal/kg/day (varies by activity)","50–60 kcal/kg/day || Too high.","No target || A target is given."],
 "Goal: 45–60 g carbs per main meal and 15–30 g per snack (individualized).")
q("dc","A client with diabetes scrapes a toe. What should the nurse teach?",
 ["Ignore minor scratches || Sensation may be impaired; small wounds become ulcers.","*Inspect and care for even minor wounds and report signs of infection",
  "Soak the foot in hot water || Burns from impaired sensation.","Go barefoot to air it out || Wear proper footwear."],
 "Skin and wound care education is part of discharge planning.")
