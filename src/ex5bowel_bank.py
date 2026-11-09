# Week 12.2 Bowel Obstruction — lecture transcript, lesson plan, PowerPoint, notes, infographics.
EXAM = "e5"
T = "e5bowel"
CONCEPTS = {
 "anat":"Lower GI review & elimination",
 "types":"Mechanical vs nonmechanical (ileus)",
 "mech":"Adhesions, volvulus & intussusception",
 "hernia":"Hernias & hernia staging",
 "partial":"Partial vs complete obstruction",
 "patho":"Pathophysiology: third-spacing & perforation",
 "shock":"Hypovolemic shock",
 "sbolbo":"Small vs large bowel obstruction",
 "assess":"History, abdominal assessment & diagnostics",
 "nursing":"Nursing care: NPO, NG, IV fluids, monitoring",
 "interv":"Cause-specific interventions",
 "meds":"Bowel medications",
 "crc":"Colorectal cancer: risks & symptoms",
 "fap":"Lynch syndrome & FAP",
 "scope":"Colonoscopy: before & after",
 "surg":"CRC surgeries",
 "periop":"Perioperative care",
 "ostomy":"Ostomy output & stoma assessment",
 "ostteach":"Ostomy teaching",
 "screen":"CRC screening, prevention & lifespan",
}
HI = ["sbolbo","shock","partial","types","surg","ostomy","ostteach","nursing","meds","hernia"]

SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

# ---------- anatomy ----------
q("anat","What is the main job of the large intestine?",
 ["*Water absorption and elimination","Nutrient absorption || That's the small intestine.","Making bile || The liver.","Making insulin || The pancreas."],
 "Small intestine (duodenum, jejunum, ileum) = nutrients; large intestine = water and elimination.")
q("anat","Which structure separates the small and large intestines?",
 ["*Ileocecal valve","Pyloric sphincter || Stomach to duodenum.","Sigmoid colon || Part of the large intestine.","Rectum || End of the large intestine."],
 "The ileum empties into the cecum through the ileocecal valve.")
q("anat","Bowel elimination depends on which two things, per the professor?",
 ["*Patency and peristalsis","Bile and insulin || Not the two things.","Fiber and fat || Not the two things.","Gas and fluid || Not the two things."],
 "Mechanical obstruction = patency problem; ileus = peristalsis problem.")

# ---------- types ----------
q("types","What is a nonmechanical obstruction (ileus)?",
 ["*Impaired peristalsis with no physical blockage","A tumor blocking the bowel || Mechanical.","A twisted bowel || Volvulus is mechanical.","Scar tissue constricting the bowel || Adhesions are mechanical."],
 "Ileus = the bowel isn't moving.")
q("types","Which are causes of NONmechanical obstruction (ileus)? "+SATA,
 ["*Abdominal surgery","*Opioids","*Low potassium or magnesium","*Peritonitis","*Diabetes or Parkinson's","Hernia || Mechanical."],
 "Also vascular insufficiency.")
q("types","Which are MECHANICAL causes of bowel obstruction? "+SATA,
 ["*Adhesions","*Tumors","*Fecal impaction","*Volvulus","*Intussusception","Postoperative ileus || Nonmechanical."],
 "Also strictures and hernias.")
q("types","A client 2 days after bowel surgery has absent bowel sounds and distention, with no blockage on imaging. Which type is this?",
 ["*Nonmechanical (postoperative ileus)","Mechanical: adhesions || Imaging shows no blockage.","Strangulated hernia || Not the finding.","Volvulus || That's a twist."],
 "Bowel manipulation during surgery slows peristalsis.")

# ---------- adhesions etc ----------
q("mech","What are adhesions?",
 ["*Scar tissue, often after abdominal surgery, that can constrict the bowel","A bowel that twists on itself || Volvulus.","A bowel segment telescoping into another || Intussusception.","Bowel pushing through a weak wall || Hernia."],
 "Adhesions are a very common cause of obstruction.")
q("mech","One segment of bowel telescopes into another. This is:",
 ["*Intussusception","Volvulus || Twisting.","Adhesion || Scar tissue.","Stricture || Narrowing."],
 "Often discussed in pediatrics; treated with enema reduction or surgery.")
q("mech","The bowel twists on itself. This is:",
 ["*Volvulus","Intussusception || Telescoping.","Hernia || Protrusion.","Ileus || No movement, no physical twist."],
 "Volvulus is a common LBO cause; usually surgical.")

# ---------- hernia ----------
q("hernia","Which combination leads to a hernia?",
 ["*A weak spot in the muscular wall plus increased abdominal pressure","Low potassium plus opioids || Ileus causes.","Polyps plus age || CRC risks.","Bowel twisting || Volvulus."],
 "Pressure rises with obesity, pregnancy, lifting, coughing and straining.")
q("hernia","A hernia's contents can't be pushed back, but blood flow is intact. What stage is this?",
 ["*Incarcerated (irreducible)","Reducible || Contents can be returned.","Strangulated || Blood supply is cut off.","Normal || Not normal."],
 "Incarcerated can progress to strangulation.")
q("hernia","Which findings suggest a STRANGULATED hernia? "+SATA,
 ["*Fever","*Severe pain","*Tachycardia","*Nausea and vomiting","A soft bulge that goes back in when lying down || Reducible."],
 "Strangulated = blood supply compromised → ischemia/necrosis; an emergency.")
q("hernia","Which hernia locations were listed? "+SATA,
 ["*Inguinal","*Femoral","*Umbilical","*Incisional/ventral","Cervical || Not listed."],
 "Also epigastric.")

# ---------- partial vs complete ----------
q("partial","A client with a bowel obstruction is still passing some gas and loose stool. This suggests:",
 ["*Partial obstruction","Complete obstruction || No passage at all.","Strangulated hernia || Not the finding.","Perforation || Not the finding."],
 "Partial: some stool (sometimes diarrhea) or gas passes; slower progression; conservative care may be tried.")
q("partial","Which statement about complete bowel obstruction is correct?",
 ["*No stool or gas passes, symptoms progress fast, and it's a medical emergency","Some diarrhea passes || That's partial.","It's always treated with laxatives || Not appropriate.","It progresses slowly || It progresses rapidly."],
 "No passage of stool or flatus = obstipation.")

# ---------- patho ----------
q("patho","Put the professor's obstruction sequence in order. Which is correct?",
 ["*Blockage → increased peristalsis → fluid and gas build up → higher lumen pressure → fluid leaks from vessels → hypovolemia/shock","Blockage → diarrhea → hypertension → recovery || Not the sequence.","Shock → blockage → peristalsis || Wrong order.","Fluid loss → blockage → perforation → peristalsis || Wrong order."],
 "Continued stretching can also cause perforation.")
q("patho","Early in an obstruction, which bowel sounds may be heard?",
 ["*Hyperactive","Always absent || Absent comes later.","Normal only || Often hyperactive early.","Bruits only || Not the expected sound."],
 "Don't be thrown off by early hyperactive sounds; they may diminish later.")
q("patho","Why can a bowel obstruction lead to hypovolemic shock?",
 ["*Fluid and electrolytes shift out of the vascular space into the bowel lumen","The client drinks too much || Not the reason.","The bowel absorbs extra water || Opposite.","Blood pressure rises too high || It falls."],
 "This third-spacing lowers circulating volume.")

# ---------- shock ----------
q("shock","Which findings indicate hypovolemic shock? "+SATA,
 ["*Hypotension","*Tachycardia","*Tachypnea","*Decreased urine output","*Anxiety, pallor and diaphoresis","Bradycardia with warm, flushed skin || Not hypovolemic shock."],
 "Altered mental status reflects poor brain perfusion.")
q("shock","A client with SBO has BP 84/50, HR 124, and urine output 15 mL/hr. What is the priority?",
 ["*Support circulation with prescribed IV fluid resuscitation and notify the provider","Give a laxative || Never for this.","Encourage oral fluids || The client is NPO.","Ambulate the client || Unsafe and not the priority."],
 "Possible ICU transfer and vasopressors if fluids alone aren't enough.")

# ---------- SBO vs LBO ----------
q("sbolbo","Which findings are typical of SMALL bowel obstruction? "+SATA,
 ["*Early, frequent vomiting that may contain bile","*Central, colicky, intermittent pain","*Mild distention","*Gas and stool may still pass early","Feculent vomiting late in the course || LBO."],
 "SBO is 75–80% of obstructions; often adhesions or hernia; mostly conservative treatment.")
q("sbolbo","Which findings point to LARGE bowel obstruction? "+SATA,
 ["*Prominent, severe distention","*Continuous, aching lower abdominal pain","*Late vomiting that may contain feces","*Absolute obstipation","Early bilious vomiting || SBO."],
 "LBO is 20–25%; often colorectal cancer or volvulus; often needs surgery.")
q("sbolbo","What is the most common cause of small bowel obstruction?",
 ["*Adhesions (and hernias)","Colorectal cancer || LBO.","Volvulus || More often LBO.","Opioids || That's ileus."],
 "SBO is more common overall.")
q("sbolbo","What is a common cause of LARGE bowel obstruction?",
 ["*Colorectal cancer","Adhesions || SBO.","Hernia || SBO.","Postoperative ileus || Nonmechanical."],
 "Also volvulus.")

# ---------- assessment ----------
q("assess","In what order does the nurse assess the abdomen?",
 ["*Inspect → auscultate → percuss → palpate","Palpate → auscultate → inspect → percuss || Palpation first changes bowel sounds.","Percuss → palpate → inspect → auscultate || Wrong order.","Auscultate → palpate → inspect → percuss || Inspect first."],
 "Auscultate before palpating; listen at least a minute per quadrant if needed.")
q("assess","Which history questions matter for a suspected obstruction? "+SATA,
 ["*Previous abdominal surgery","*Opioid or laxative use","*Passing gas and last bowel movement","*Unintended weight loss","*Family history of cancer","Favorite color || Not relevant."],
 "Also age, diet, smoking and alcohol.")
q("assess","Which diagnostics are used for bowel obstruction? "+SATA,
 ["*CBC and electrolytes","*Stool for occult blood (guaiac)","*Abdominal x-ray or CT","*Tumor markers such as CEA","Echocardiogram || Not listed."],
 "Also MRI and ultrasound.")
q("assess","During palpation, the abdomen is rigid and the client guards. What should the nurse do?",
 ["*Report it promptly; rigidity can signal perforation or peritonitis","Massage the abdomen || Unsafe.","Document as expected || Not expected.","Give a laxative || Not appropriate."],
 "Palpation checks tenderness and rigidity.")

# ---------- nursing ----------
q("nursing","Which nursing care is expected for a client with a bowel obstruction? "+SATA,
 ["*NPO with oral care","*NG decompression (Salem sump)","*IV fluids for replacement and maintenance","*Strict I&O, including NG output","Encourage a high-fiber meal || NPO."],
 "Also monitor VS, electrolytes, pain and the abdomen.")
q("nursing","A client with an obstruction suddenly says the pain is gone, but the abdomen becomes rigid and HR rises. What does the nurse suspect?",
 ["*Perforation","Resolution of the obstruction || Not with these findings.","Expected improvement || Not with these findings.","Constipation || Not this picture."],
 "Any sudden increase or decrease in pain can mean perforation.")
q("nursing","Why is I&O extremely important with an NG tube to suction?",
 ["*NG output adds to fluid and electrolyte loss","It isn't important || It is.","The NG tube adds fluid to the client || It removes fluid.","Only to measure appetite || Not the reason."],
 "Monitor electrolytes closely.")

# ---------- interventions ----------
q("interv","Which interventions treat POSTOPERATIVE ileus? "+SATA,
 ["*Ambulation","*Prokinetic agents","Barium enema || Intussusception.","Manual disimpaction || Fecal impaction."],
 "Opioid-related ileus → mu-opioid antagonist.")
q("interv","Which interventions are used for fecal impaction? "+SATA,
 ["*Fluids and fiber","*Stool softeners and laxatives","*Enemas","*Manual disimpaction","Surgery as the first step || Not first-line."],
 "Also ambulation.")
q("interv","A hernia, volvulus, tumor or stricture causing obstruction is usually treated with:",
 ["*Surgery","Laxatives || Not for mechanical blockage.","Ambulation alone || Not enough.","Prokinetics alone || Not enough."],
 "Intussusception: surgery or enema reduction.")

# ---------- meds ----------
q("meds","What should the nurse monitor for with metoclopramide (Reglan)?",
 ["*Tardive dyskinesia","Dependence || Bisacodyl.","MI risk || Alvimopan.","Thick, glutinous stool || Bulk formers without fluid."],
 "Metoclopramide is a prokinetic; it increases motility.")
q("meds","Which teaching applies to alvimopan (Entereg)?",
 ["*Short-term use only, up to 15 doses, because of MI risk","Take it daily for life || Short-term only.","It's a stool softener || It's a mu-opioid antagonist.","Take it with extra opioids || Not the purpose."],
 "It binds GI opioid receptors to prevent postoperative ileus.")
q("meds","A client on psyllium (Metamucil) should be taught to:",
 ["*Maintain fluid intake to avoid a thick mass that can obstruct","Limit fluids || Causes obstruction.","Take it for diarrhea only || Not the teaching.","Expect results in minutes || Works in 1–3 days."],
 "Bulk-forming laxatives enlarge the fecal mass.")
q("meds","Which statement about bisacodyl (Dulcolax) is correct?",
 ["*Long-term use can cause dependence","It softens stool by blocking water absorption || Docusate.","It's a prokinetic || Metoclopramide.","It prevents postoperative ileus by blocking opioids || Alvimopan."],
 "Bisacodyl is a stimulant laxative.")
q("meds","Which teaching is correct for docusate sodium (Colace)? "+SATA,
 ["*Maintain fluid intake","*Stop it if diarrhea occurs","*It may take 1–3 days to work","Never drink water with it || Fluids help."],
 "Docusate softens stool.")

# ---------- CRC ----------
q("crc","Which are risk factors for colorectal cancer? "+SATA,
 ["*Age over 50","*Diet high in animal fat","*Smoking and alcohol","*Inflammatory bowel disease (Crohn's or ulcerative colitis)","*Physical inactivity","Regular exercise || Protective."],
 "Also family or personal history; Lynch syndrome and FAP.")
q("crc","Which symptoms suggest colorectal cancer? "+SATA,
 ["*Change in bowel habits or stool caliber","*Rectal bleeding or blood in the stool","*Anemia and fatigue from occult bleeding","*Unintended weight loss","Weight gain || Unintended loss is the concern."],
 "Also incomplete emptying, bloating and anorexia.")
q("crc","Why does inflammatory bowel disease raise colorectal cancer risk, per the professor?",
 ["*Repeated cell injury and repair eventually goes wrong","It causes adhesions || Not the explanation.","It speeds stool through too fast || Not the explanation.","It's a viral infection || Not the explanation."],
 "Cell injury, repair, injury, repair.")
q("crc","Which test confirms colorectal cancer?",
 ["*Colonoscopy with biopsy","CEA level || Monitors treatment.","Stool guaiac || Screens for hidden blood.","Abdominal x-ray || Shows obstruction."],
 "CEA is a tumor marker used to monitor treatment.")

# ---------- FAP / Lynch ----------
q("fap","Which statement about familial adenomatous polyposis (FAP) is correct?",
 ["*Hundreds to thousands of polyps develop, with near 100% lifetime cancer risk; prophylactic colectomy may be discussed","It's caused by a high-fat diet || It's inherited.","It causes no polyps || It causes many.","It's the same as Lynch syndrome || Different conditions."],
 "Polyps can begin in the teen years.")
q("fap","What is Lynch syndrome?",
 ["*An inherited cancer risk linked to impaired DNA repair","A bowel twist || Volvulus.","A type of hernia || Not a hernia.","An ileus from opioids || Not related."],
 "Lynch syndrome accounts for 2–4% of CRC.")

# ---------- colonoscopy ----------
q("scope","Which preparations are needed before a colonoscopy? "+SATA,
 ["*Liquid diet for about 24 hours","*Bowel prep","*NPO as ordered","*Hold anticoagulants as instructed and check PT/INR and PTT","*Confirm consent","Eat a large meal the night before || Liquid diet."],
 "Biopsies are likely, so bleeding risk matters.")
q("scope","After a colonoscopy, which finding is MOST concerning?",
 ["*Severe abdominal pain with a hard, rigid abdomen","Mild cramping and gas || Expected.","Sleepiness after sedation || Expected early.","A small amount of gas passing || Expected."],
 "Monitor for bleeding and perforation.")
q("scope","How does the nurse confirm the bowel prep is adequate?",
 ["*Look at the stools to be sure no solid material is passing","Ask if the client is hungry || Not the check.","Check the blood glucose || Not the check.","Palpate the abdomen || Not the check."],
 "Adequate prep is very important.")

# ---------- surgery ----------
q("surg","After a low anterior resection, which order should the nurse question?",
 ["*A rectal suppository","IV fluids || Expected.","Incentive spirometer || Expected.","Pain medication || Expected."],
 "Nothing per rectum: the anastomosis is low. Clarify suppositories, enemas and rectal temperatures.")
q("surg","Which surgery leaves a rectal stump and creates a temporary colostomy?",
 ["*Hartmann procedure","Abdominoperineal resection || Permanent colostomy.","Polypectomy || Removes a polyp during endoscopy.","Low anterior resection || Reconnects bowel, often no ostomy."],
 "Reconnection may be possible later.")
q("surg","After an abdominoperineal resection (APR), what should the nurse expect?",
 ["*A permanent colostomy and a perineal wound","A temporary ileostomy only || Not APR.","No incisions || Not APR.","A reconnected rectum || The rectum and anus are removed."],
 "Monitor both the abdominal and perineal sites.")
q("surg","Match each procedure with its description. "+SATA,
 ["*Polypectomy — removes a polyp during endoscopy","*Colectomy — removes part or all of the colon","*Low anterior resection — removes the upper rectum and reconnects","APR — temporary colostomy || APR = permanent colostomy."],
 "Remaining bowel ends may be joined by anastomosis.")

# ---------- periop ----------
q("periop","Which preoperative care is important before CRC surgery with a planned ostomy? "+SATA,
 ["*Psychosocial support for body-image changes","*Wound/ostomy nurse consult for stoma site planning","*Explain the surgery and the ostomy","*Prescribed antibiotics","Skip teaching to avoid anxiety || Teaching is needed."],
 "Also respiratory hygiene and activity teaching.")
q("periop","After colon surgery, which diet progression is expected?",
 ["*NPO at first, then advanced as prescribed toward a low-residue diet","High-fiber diet immediately || Not first.","Regular diet right away || NPO initially.","Liquid diet forever || Not the plan."],
 "Monitor I&O, abdomen, bowel sounds, NG, drains, wounds and ostomy output.")
q("periop","What lab is monitored after CRC surgery to track treatment?",
 ["*CEA","Troponin || Cardiac.","TSH || Thyroid.","Lipase || Pancreas."],
 "Chemotherapy and radiation may be given before or after surgery.")

# ---------- ostomy ----------
q("ostomy","Which ostomy will have the most LIQUID output?",
 ["*Ileostomy","Sigmoid colostomy || Most solid.","Descending colostomy || Semisolid.","Transverse colostomy || Pasty."],
 "The closer to the rectum, the more water absorbed and the firmer the stool.")
q("ostomy","Which stoma appearance is healthy?",
 ["*Pink, moist, shiny and raised above the skin","Dark purple or black || Necrosis.","Dry and pale || Not healthy.","Recessed below the skin || Retraction."],
 "PMS: pink, moist, shiny.")
q("ostomy","Which stoma findings should be reported? "+SATA,
 ["*Dark or black color","*Retraction below the skin","*Excessive protrusion ('elephant trunk')","*Excoriated skin around the stoma","Pink, moist and shiny || Healthy."],
 "Also leakage.")
q("ostomy","A new ostomy client asks why the wafer size keeps changing. Best response?",
 ["*'The stoma shrinks over the first several weeks as swelling goes down.'","'Your stoma is failing.' || Expected change.","'You're cutting it wrong.' || Not the reason.","'The stoma grows over time.' || It shrinks."],
 "Re-measure regularly.")
q("ostomy","Which stool consistency is expected from a sigmoid colostomy?",
 ["*More solid","Liquid || Ileostomy.","Semiliquid || Ascending colostomy.","Pasty || Transverse colostomy."],
 "Descending = semisolid; sigmoid = more solid.")

# ---------- ostomy teaching ----------
q("ostteach","How large should the wafer opening be cut?",
 ["*Within 1/8 inch of the stoma","1 inch larger than the stoma || Exposes skin.","Exactly half the stoma size || Damages the stoma.","Any size || Fit protects the skin."],
 "Measure the stoma and cut the barrier to fit.")
q("ostteach","When should the client empty the ostomy pouch?",
 ["*Before it is 1/3 full","When it's completely full || Risk of leaks.","Once a week || Too infrequent.","Only at bedtime || Not the guideline."],
 "Often every 4–6 hours; change the appliance about twice a week.")
q("ostteach","Which ostomy teaching is correct? "+SATA,
 ["*Clean the skin with warm water","*Check the peristomal skin for irritation","*Prevent leaks, since moisture damages skin","*Learn which foods cause odor and gas","Use harsh soaps to sterilize the skin || Avoid harsh products."],
 "One-piece and two-piece systems are available.")
q("ostteach","Colostomy irrigation applies only to which ostomies?",
 ["*Descending or sigmoid colostomies","Ileostomies || Output is too liquid.","Ascending colostomies || Too liquid.","Any ostomy || Not per the lecture."],
 "It requires instruction and orders.")
q("ostteach","An older adult with poor eyesight and arthritis will manage a new ostomy. What should the nurse assess? "+SATA,
 ["*Vision","*Hand dexterity","*Ability to manage supplies independently","*Body image and sexuality concerns","Shoe size || Not relevant."],
 "Lifespan considerations affect self-care.")

# ---------- screening ----------
q("screen","At what age does average-risk colorectal cancer screening begin, per the lecture?",
 ["*45","30 || Too early.","60 || Too late.","21 || Pap screening age."],
 "Options: annual stool blood test, stool DNA/RNA test every 3 years, colonoscopy every 10 years, CT colonography every 5 years.")
q("screen","How often is a colonoscopy done for average-risk screening?",
 ["*Every 10 years","Every year || That's stool blood testing.","Every 3 years || Stool DNA/RNA test.","Every 5 years || CT colonography."],
 "Average risk starts at 45.")
q("screen","Which teaching helps prevent colorectal cancer? "+SATA,
 ["*Limit high-fat and processed meats","*Exercise regularly","*Avoid smoking","*Limit alcohol","Eat more red meat || Considered carcinogenic."],
 "Also maintain a healthy weight.")
