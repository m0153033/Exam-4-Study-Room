# Week 11.2 Blood Products & Administration — Prof. Hanikeh's two slide decks (Intro to Blood Products; Compatibility & Blood Product Administration).
# Classmate update (Nov 3): compatibility is NOT select-all (know O- = universal donor); gauge 18-20; know product types;
# know reaction SIGNS (specific reaction type not tested); when to use normal saline; pre-transfusion steps; Jehovah's Witness.
# VERSION 2 (Nov 8): every question re-worded with new scenarios/distractors.
# Where the classmate notes and the lecture differ, the lecture wins (e.g., Hgb ~7-8 g/dL; start within 30 min; finish within 4 h).
T = "blood"
CONCEPTS = {
 "comp":"Blood components",
 "why":"Why patients need blood products",
 "prod":"Blood product types (FOCUS)",
 "choose":"Choosing the product (FOCUS)",
 "abo":"ABO compatibility (FOCUS)",
 "rh":"Rh & O negative universal donor (FOCUS)",
 "jw":"Jehovah's Witness / bloodless care (FOCUS)",
 "labs":"Labs & orders to expect",
 "pre":"Before giving blood (FOCUS)",
 "admin":"During the transfusion (FOCUS)",
 "ns":"When to use normal saline (FOCUS)",
 "post":"Post-transfusion",
 "ahtr":"Reaction signs: back pain, dark urine, low BP (FOCUS)",
 "fnh":"Reaction signs: fever & chills",
 "allergy":"Reaction signs: hives & wheezing",
 "lung":"Reaction signs: breathing & fluid overload",
 "delayed":"Reaction signs days later",
 "steps":"Steps when a reaction is suspected (FOCUS)",
}
HI = ["prod","choose","abo","rh","jw","pre","admin","ns","ahtr","steps"]

SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

# ---------- components ----------
q("comp","A client's lab shows a very low red blood cell count. Which job of the blood is most affected?",
 ["*Carrying oxygen to the tissues","Fighting infection || White blood cells.","Forming clots || Platelets.","Carrying hormones and nutrients || Plasma."],
 "Blood handles oxygen delivery, immunity and clotting.")
q("comp","Which pairs of blood component and job are correct? "+SATA,
 ["*Platelets: clotting","*White blood cells: fighting infection","*Plasma: carrying nutrients, hormones and waste","*Red blood cells: carrying oxygen",
  "Plasma: carrying oxygen || Red blood cells carry oxygen."],
 "Each blood product replaces one of these parts.")

# ---------- why ----------
q("why","Which clients might need a blood product? "+SATA,
 ["*A client with a large GI bleed","*A client with anemia from chemotherapy","*A client with hemophilia who is bleeding","*A client with a very low platelet count from ITP","*A trauma client on a massive transfusion protocol"],
 "Blood loss, anemia, clotting disorders, low platelets, and massive hemorrhage.")

# ---------- product types (FOCUS) ----------
q("prod","Which blood product replaces CLOTTING FACTORS?",
 ["*Fresh frozen plasma","Packed red blood cells || Carry oxygen.","Platelets || Help form a plug, but aren't clotting factors.","Albumin || Not a clotting product."],
 "Plasma: coagulopathy, liver disease, massive transfusion, reversing warfarin.")
q("prod","A client's fibrinogen is 80 mg/dL and they are bleeding. Which product is used?",
 ["*Cryoprecipitate","Packed red blood cells || Carry oxygen.","Platelets || For low platelet counts.","Normal saline || Not a blood product."],
 "Cryo is rich in fibrinogen, factor VIII and von Willebrand factor. Used for fibrinogen under 100.")
q("prod","Which blood product is stored at ROOM temperature?",
 ["*Platelets","Fresh frozen plasma || Frozen.","Cryoprecipitate || Frozen.","Packed red blood cells || Refrigerated."],
 "Platelets have a short shelf life.")
q("prod","Which product is used for trauma and massive hemorrhage because it replaces red cells, plasma and platelets together?",
 ["*Whole blood","Cryoprecipitate || Fibrinogen only.","Platelets || Platelets only.","Albumin || Not for hemorrhage."],
 "Whole blood is rarely used today, mainly in trauma.")
q("prod","What does a unit of packed red blood cells do for an anemic client?",
 ["*Raises oxygen-carrying capacity; one unit raises Hgb about 1 g/dL","Replaces clotting factors || That's plasma.","Raises the platelet count || That's platelets.","Replaces fibrinogen || That's cryoprecipitate."],
 "PRBCs: hemorrhage, symptomatic anemia, low Hgb.")
q("prod","Which pairing of product and use is correct?",
 ["*Platelets: low platelet count","Whole blood: low fibrinogen || That's cryoprecipitate.","Packed RBCs: clotting factor deficiency || That's plasma.","Plasma: anemia || That's packed RBCs."],
 "Whole blood = trauma; PRBCs = hemorrhage/anemia; platelets = low platelets; plasma = clotting factors; cryo = fibrinogen.")
q("prod","Which pairs of blood product and use are correct? "+SATA,
 ["*Whole blood: trauma","*Packed RBCs: hemorrhage and anemia","*Platelets: low platelets","*Cryoprecipitate: low fibrinogen","Plasma: low hemoglobin || PRBCs."],
 "Match the product to what is missing.")

# ---------- choosing ----------
q("choose","A client with leukemia has a platelet count of 7,000/µL and bleeding gums. Which product does the nurse expect?",
 ["*Platelets","Packed red blood cells || Hemoglobin isn't the problem.","Cryoprecipitate || Fibrinogen.","Whole blood || Trauma."],
 "Platelets are given under 10,000–20,000/µL, or under 50,000/µL with active bleeding.")
q("choose","A client with a GI bleed is pale, dizzy and tachycardic with an Hgb of 6.7 g/dL. Which product is best?",
 ["*Packed red blood cells","Platelets || The platelet count isn't the problem.","Fresh frozen plasma || Clotting factors.","Oral iron || Too slow."],
 "PRBCs restore oxygen-carrying capacity quickly.")
q("choose","Why does a symptomatic client with Hgb 6.5 get a transfusion instead of iron alone?",
 ["*Iron takes days to weeks to raise hemoglobin; the client needs help now","Iron is never used in anemia || It's used, just slowly.",
  "Iron causes reactions || Not the reason.","Iron only raises platelets || Not true."],
 "From the professor's scenario: the client's symptoms need a fast fix.")
q("choose","A client with liver failure has a prolonged PT/INR and is oozing from IV sites. Which product?",
 ["*Fresh frozen plasma","Platelets || The platelet count isn't the issue.","Packed RBCs || Don't replace clotting factors.","Whole blood || Trauma."],
 "Prolonged clotting times = clotting factors are missing.")
q("choose","A motorcycle crash victim is bleeding heavily and needs red cells, plasma and platelets fast. Which product?",
 ["*Whole blood","Albumin || Not for hemorrhage.","Cryoprecipitate only || Fibrinogen only.","Platelets only || Not enough."],
 "Whole blood = trauma and massive hemorrhage.")
q("choose","A client on chemotherapy has platelets of 9,000/µL and no active bleeding. Should they receive platelets?",
 ["*Yes; below 10,000, spontaneous bleeding can happen","No; only if actively bleeding || The risk is too high.","No; give packed RBCs instead || Wrong product.","No; platelets are only for surgery || Not true."],
 "Even minor trauma can cause life-threatening bleeding.")

# ---------- ABO (FOCUS) ----------
q("abo","A client has type B blood. Which antibody is in their plasma?",
 ["*Anti-A","Anti-B || Would attack their own cells.","Both anti-A and anti-B || Type O.","Neither || Type AB."],
 "Antibodies target the antigens you DON'T have.")
q("abo","Which donor red cells can a type B client receive?",
 ["*B or O","A or O || Anti-A would attack A cells.","AB only || AB has the A antigen.","Any type || That's AB."],
 "Type B has anti-A antibodies.")
q("abo","A client with type O blood needs packed red cells. Which type can they receive?",
 ["*O only","O or A || Type O has anti-A.","O or B || Type O has anti-B.","Any type || That's AB."],
 "Type O has BOTH anti-A and anti-B antibodies.")
q("abo","Which blood type can receive red cells from ANY ABO type?",
 ["*AB (the universal recipient)","O || O can only receive O.","A || A can receive A or O.","B || B can receive B or O."],
 "AB has no anti-A or anti-B antibodies.")
q("abo","Which blood type is the universal DONOR for red cells?",
 ["*O negative","AB positive || Universal recipient.","A negative || Has the A antigen.","O positive || Rh-positive can sensitize an Rh-negative client."],
 "O negative red cells have no A, B or Rh (D) antigens.")
q("abo","A type A client needs blood. Which donor types are compatible?",
 ["*A or O","A or B || Anti-B attacks B cells.","AB || Has the B antigen.","B or O || Anti-B attacks B cells."],
 "Type A has anti-B antibodies.")

# ---------- Rh (FOCUS) ----------
q("rh","A client with A-negative blood needs red cells. Which donor blood can they safely receive?",
 ["*A negative or O negative","A positive or O positive || Rh-negative clients need Rh-negative blood.","A negative only || O negative also works.","AB negative || AB has the B antigen."],
 "A− receives A− and O−.")
q("rh","An unknown-type trauma client is bleeding out in the ED and blood is needed now. Which type is given?",
 ["*O negative","AB positive || The universal recipient, not donor.","O positive only || Can sensitize an Rh-negative client.","A negative || Has the A antigen."],
 "O negative = universal donor.")
q("rh","A client with O-negative blood needs red cells. Which type can they receive?",
 ["*O negative only","O positive or O negative || Rh-negative needs Rh-negative.","Any type, since O is universal || O is the universal donor, not recipient.","AB negative || AB has A and B antigens."],
 "O-negative clients can only receive O negative.")
q("rh","A client with B-positive blood needs red cells. Which donor blood is compatible?",
 ["*B positive, B negative, O positive or O negative","B positive only || Rh-positive can also receive Rh-negative.","B negative or O negative only || Rh-positive can also receive Rh-positive.","AB positive || Has the A antigen."],
 "Rh-positive clients can receive Rh-positive or Rh-negative.")
q("rh","Why is an Rh-negative client given only Rh-negative red cells?",
 ["*To prevent sensitization to the Rh (D) antigen","Rh-negative blood carries more oxygen || Not the reason.","Rh-positive blood clots too fast || Not the reason.","It's only a preference || It's a safety rule."],
 "Rh-positive = D antigen present. Rh-negative = absent.")
q("rh","Which statement about universal donor and recipient is correct?",
 ["*O negative is the universal donor; AB positive is the universal recipient","AB negative is the universal donor || AB is the recipient.",
  "O positive is the universal donor || Rh-negative clients need Rh-negative.","O negative is the universal recipient || O negative receives only O negative."],
 "Always follow blood bank testing.")

# ---------- Jehovah's Witness (FOCUS) ----------
q("jw","A client who is a Jehovah's Witness has Hgb 6.6 g/dL and refuses the ordered blood. What should the nurse do?",
 ["*Respect the refusal, notify the provider and discuss alternatives","Give the blood once the client becomes sleepy || Never without consent.",
  "Ask the family to override the decision || A competent adult decides.","Give it if the client becomes unstable || Never without consent, even in emergencies."],
 "Alternatives: erythropoietin with iron, tranexamic acid, IV fluids.")
q("jw","Which products does a Jehovah's Witness ALWAYS refuse? "+SATA,
 ["*Red blood cells","*Platelets","*Plasma","*Whole blood","*White blood cells","Lactated Ringer's || A non-blood fluid."],
 "These are the 'always avoid' products.")
q("jw","Which options might a Jehovah's Witness accept, depending on their personal choice? "+SATA,
 ["*Albumin","*Clotting factors","*Erythropoietin with iron","*Tranexamic acid","*Normal saline or lactated Ringer's"],
 "Ask each client which fractions they accept.")
q("jw","Which nursing actions support bloodless care for a Jehovah's Witness? "+SATA,
 ["*Cluster lab draws and use small (pediatric) tubes","*Document the client's wishes clearly","*Monitor closely for bleeding","*Provide emotional and spiritual support",
  "Assume all Jehovah's Witnesses accept albumin || Ask each client."],
 "Involve the provider, family and ethics team as needed.")

# ---------- labs & orders ----------
q("labs","Around what hemoglobin does the lecture say a red cell transfusion is usually given?",
 ["*About 7–8 g/dL (or as ordered)","12 g/dL || Normal for women starts here.","10 g/dL || Not the threshold given.","4 g/dL || Too low."],
 "Normal Hgb: women 12–16, men 14–18 g/dL.")
q("labs","Which platelet counts call for a platelet transfusion? "+SATA,
 ["*Under 10,000–20,000/µL","*Under 50,000/µL with active bleeding","180,000/µL || Normal is 150,000–400,000.","300,000/µL || Normal."],
 "Under 10,000, spontaneous bleeding can occur.")
q("labs","Which test checks the donor unit against the client's blood right before release?",
 ["*Crossmatch","Type and screen || Finds ABO/Rh and screens for antibodies.","CBC || Not a compatibility test.","PT/INR || Clotting test."],
 "Type and screen first, then crossmatch with the donor unit.")
q("labs","A transfusion order lists 'leukoreduced, irradiated, CMV-negative.' What are these?",
 ["*Special product requirements","Lab tests the client needs || Not lab tests.","Types of IV fluid || Not fluids.","Reaction treatments || Not treatments."],
 "Orders also list the product, number of units and rate.")

# ---------- before giving blood (FOCUS) ----------
q("pre","Which IV gauge is used for a blood transfusion?",
 ["*18–20 gauge","22–24 gauge || Too small.","26 gauge || Too small.","Any gauge works || The lecture specifies 18–20."],
 "18–20 gauge with normal saline Y-tubing.")
q("pre","A client has a 24-gauge IV in the hand and a unit of blood is ordered. What should the nurse do?",
 ["*Start a new 18–20 gauge IV for the blood","Run the blood through the 24 gauge slowly || Too small.","Give the blood IM || Not possible.","Skip the transfusion || Get proper access."],
 "Blood needs 18–20 gauge access.")
q("pre","Which items must be confirmed BEFORE a transfusion starts? "+SATA,
 ["*Signed consent","*A provider order","*Type and crossmatch","*A second RN checks with you at the bedside","*Emergency medications on the unit"],
 "Equipment: an IV pump and Y-tubing with an inline filter.")
q("pre","The blood arrives, but the consent form isn't signed. What should the nurse do?",
 ["*Don't start; get the consent signed first","Start it and get consent later || Consent comes first.","Start slowly and watch closely || Still no consent.","Have the family sign as it runs || Not appropriate."],
 "Consent must be signed before blood is released.")
q("pre","During the bedside check, the medical record number on the blood bag is one digit off from the client's band. What should the nurse do?",
 ["*Do not give it; return it and call the blood bank","Give it, since the name matches || Every identifier must match.",
  "Correct the number and give it || Not the nurse's role.","Give it slowly || Never give mismatched blood."],
 "Two RNs verify at the bedside.")
q("pre","When are baseline vital signs taken for a transfusion?",
 ["*Within 15 minutes before it starts","After the first hour || Too late for a baseline.","Only at the end || Too late.","Only if the client has a fever || Always."],
 "The baseline is what you compare against to spot a reaction.")
q("pre","What should the nurse ask or check before starting blood? "+SATA,
 ["*Any past transfusion reactions","*Baseline vital signs","*Signs of fluid overload or breathing problems","*IV size","*Consent and order in place"],
 "Also why the client needs blood and the blood type.")

# ---------- during the transfusion (FOCUS) ----------
q("admin","The nurse picks up a unit of PRBCs from the blood bank at 1400. By what time must it be started?",
 ["*1430","1500 || More than 30 minutes.","1800 || That's the 4-hour finish time.","1415 || Not the rule."],
 "Start within 30 minutes of pickup; finish within 4 hours.")
q("admin","A unit of PRBCs was picked up at 0900. By what time must it be finished?",
 ["*1300 (within 4 hours)","1700 || Too long.","1000 || Not the rule.","0930 || That's the start deadline."],
 "Start within 30 minutes; finish within 4 hours.")
q("admin","What does the nurse do 15 minutes after starting a blood transfusion?",
 ["*Take a full set of vital signs and compare to baseline","Take only the temperature || A full set is needed.","Nothing until the end || The first 15 minutes are the riskiest.","Check the blood glucose || Not the check."],
 "Then vital signs every hour until done.")
q("admin","Why does the nurse stay with the client and run blood slowly for the first 15 minutes?",
 ["*The most serious reactions usually happen early","To warm the blood || Not the reason.","To save blood || Not the reason.","Because the pump is slow to start || Not the reason."],
 "Watch for chills, rash, shortness of breath and chest pain.")
q("admin","How fast are platelets usually given?",
 ["*Over 15–30 minutes","Over 4 hours || That's the PRBC limit.","By IV push || Not how platelets are given.","Over 12 hours || Too long."],
 "PRBCs: start within 30 minutes and finish within 4 hours.")
q("admin","Which vital sign schedule is correct during a blood transfusion?",
 ["*Before starting, 15 minutes after starting, then every hour","Only at the end || Too late.","Every 4 hours || Too infrequent.","Only if the client complains || Routine checks are required."],
 "The first 15 minutes are the highest-risk period.")

# ---------- normal saline (FOCUS) ----------
q("ns","Which fluid is the ONLY one hung with blood?",
 ["*0.9% normal saline","Lactated Ringer's || Not used with blood.","D5W || Not compatible.","0.45% saline || Not the lecture's fluid."],
 "Always normal saline.")
q("ns","A client has D5W running when blood arrives. What should the nurse do?",
 ["*Set up the blood on Y-tubing with 0.9% normal saline","Piggyback the blood into the D5W || Not compatible.","Mix the blood into the D5W bag || Never mix.","Switch the D5W to lactated Ringer's || Normal saline only."],
 "Never mix medications or other solutions with blood.")
q("ns","At which points is normal saline used with a blood transfusion? "+SATA,
 ["*Priming the Y-tubing","*Keeping the IV open in NEW tubing after a reaction","*Flushing the line when the blood is done","Diluting a medication in the blood bag || Never add meds to blood.","Only for dehydrated clients || Always used with blood."],
 "Normal saline is the only fluid used with blood.")
q("ns","A transfusion was stopped for a reaction. How does the nurse keep the vein open?",
 ["*Hang normal saline through NEW tubing","Flush saline through the blood tubing || Pushes more blood in.","Keep the blood running very slowly || Must stop.","Pull the IV || Keep access."],
 "New tubing keeps leftover blood out of the client.")

# ---------- post ----------
q("post","A transfusion finishes with no problems. What does the nurse do? "+SATA,
 ["*Flush the line with normal saline","*Throw away the bag and tubing per policy (usually biohazard)","*Document the transfusion","*Watch for delayed reactions","Hang D5W to keep the vein open || Not the flush."],
 "The flush clears the last of the blood into the client.")
q("post","What happens to the blood bag and tubing after a reaction?",
 ["*They go back to the blood bank for testing","They go in the biohazard bin || Not after a reaction.","They stay in the room || Not the action.","The tubing is reused || Never."],
 "Without a reaction, they usually go in biohazard waste.")

# ---------- reaction signs (FOCUS: signs, not names) ----------
q("ahtr","Five minutes into a transfusion, the client says their lower back hurts and they feel cold. What should the nurse do FIRST?",
 ["*Stop the transfusion","Slow it down || Stop completely.","Give acetaminophen || Not first.","Call the blood bank || After stopping."],
 "Then normal saline in new tubing, notify the provider and blood bank.")
q("ahtr","Which findings during a transfusion are signs of a serious reaction? "+SATA,
 ["*Back or flank pain","*Dark red urine","*Low blood pressure","*Chills and fever","*Sudden anxiety"],
 "Can lead to shock, oozing at the IV site (DIC) and kidney injury.")
q("ahtr","A client says, 'Something feels wrong,' 10 minutes into a unit of blood. What is the best action?",
 ["*Stop the transfusion and assess","Reassure them and continue || Take it seriously.","Speed it up to finish faster || More blood worsens a reaction.","Give a sedative || Not appropriate."],
 "A feeling of doom can be an early sign.")
q("ahtr","After stopping blood for back pain, dark urine and low BP, which orders does the nurse expect? "+SATA,
 ["*Normal saline 100–200 mL/hr or a bolus","*IV diuretics","*Labs to check for DIC","*Transfer to the ICU","Restart the same unit later || Never restart it."],
 "From the nursing management slide.")
q("fnh","Thirty minutes into a transfusion, the temperature rises from 98.6°F to 100.9°F and the client has chills. What does the nurse do?",
 ["*Stop the transfusion, assess, and give acetaminophen as ordered; restart only if the provider approves","Keep it running and give acetaminophen || Stop first.",
  "Give epinephrine || For airway or BP problems.","Give furosemide || For fluid overload."],
 "Any temperature rise of 1°C (about 2°F) or more = stop and assess.")
q("fnh","Which findings during a transfusion should make the nurse stop it? "+SATA,
 ["*Temperature up 1°C or more","*Shaking chills","*New headache or malaise","Stable vitals and the client feels well || No reaction.","Client asks for a blanket because the room is cold, with normal vitals || Not a reaction sign alone."],
 "Compare every set of vitals with the baseline.")
q("allergy","Twenty minutes into a transfusion, the client is itchy with hives on the chest. Vitals are stable. What should the nurse do?",
 ["*Stop the transfusion, notify the provider and give an antihistamine as ordered","Ignore it; hives are minor || Stop first.",
  "Give furosemide || No overload signs.","Give epinephrine first || No airway or BP problem."],
 "It may restart only if symptoms resolve and the provider approves.")
q("allergy","A client receiving blood suddenly wheezes, can't catch their breath and their BP drops. Which actions are correct? "+SATA,
 ["*Stop the transfusion","*Support the airway","*Give epinephrine as ordered","*Notify the provider","Restart after an antihistamine || Not with airway and BP problems."],
 "Can start within seconds to minutes.")
q("lung","An older client receiving a second unit of blood quickly develops crackles, JVD, high BP and shortness of breath. What does the nurse do? "+SATA,
 ["*Stop the transfusion","*Sit the client upright","*Give oxygen","*Give a diuretic as ordered","Speed up the transfusion to finish || Adds more volume."],
 "These are fluid overload signs.")
q("lung","Which findings during a transfusion point to fluid overload? "+SATA,
 ["*Rising blood pressure","*Distended neck veins","*Crackles in the lungs","*Shortness of breath","Low BP and clear lungs || Not overload."],
 "Check for overload risk before starting, too.")
q("lung","Four hours after a transfusion, a client has severe trouble breathing, low oxygen, fever and low BP. What should the nurse do?",
 ["*Give oxygen and notify the provider immediately","Encourage deep breathing and recheck later || Too slow.","Give a diuretic || BP is already low.","Document it as expected || A red flag."],
 "May need ventilator support.")
q("delayed","A client who got blood 2 weeks ago now has yellow skin, fever and anemia. What should the nurse do?",
 ["*Report it; reactions can appear days to weeks later","Ignore it; reactions only happen during transfusion || Not true.","Give more blood || Not without evaluation.","Tell them it's a cold || Not the concern."],
 "Delayed reactions are usually milder.")
q("delayed","Which signs in the days after a transfusion should a client report? "+SATA,
 ["*Fever","*Itching or rash","*Dark urine","*Shortness of breath"],
 "The risk doesn't end when the blood stops.")

# ---------- steps when a reaction is suspected (FOCUS) ----------
q("steps","The nurse suspects a transfusion reaction but doesn't know which type. What is the FIRST action?",
 ["*Stop the transfusion (stop the pump)","Figure out the reaction type || Stop first, for any reaction.","Slow the rate || Stop completely.","Call the blood bank || Step 3."],
 "The first step is the same for every reaction.")
q("steps","Put the reaction steps in order. Which comes SECOND, right after stopping the blood and keeping the IV open?",
 ["*Notify the provider","Notify the blood bank || Third.","Collect urine and blood samples || Fourth.","Document || Fifth."],
 "Stop · notify provider · notify blood bank · samples · document · advise the client.")
q("steps","After a suspected reaction, which actions are part of the process? "+SATA,
 ["*Send the bag and tubing back to the blood bank","*Collect urine and blood samples","*Notify the provider with your findings","*Document the reaction","*Tell the client a reaction happened"],
 "Advise the client how future reactions can be prevented.")
q("steps","Which is the LAST step after a transfusion reaction?",
 ["*Advise the client about the reaction and prevention","Stop the transfusion || First.","Notify the provider || Second.","Collect samples || Fourth."],
 "Stop, notify provider, notify blood bank, samples, document, advise.")
q("steps","After stopping blood for a reaction, which IV fluid and setup does the nurse use?",
 ["*Normal saline through new tubing","Normal saline through the same blood tubing || Pushes more blood in.","D5W through new tubing || Normal saline only.","No fluid; remove the IV || Keep access."],
 "Keep the line open with normal saline (about 250 mL) in new tubing.")
