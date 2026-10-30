# Week 11.2 Blood Products & Administration — Prof. Hanikeh's two slide decks (Intro to Blood Products; Compatibility & Blood Product Administration).
T = "blood"
CONCEPTS = {
 "comp":"Blood components",
 "why":"Why patients need blood products",
 "prod":"Blood product types",
 "choose":"Choosing the product (scenarios)",
 "abo":"ABO system",
 "rh":"Rh & donor/recipient rules",
 "jw":"Jehovah's Witness / bloodless care",
 "labs":"Labs & orders to expect",
 "pre":"Pre-transfusion checks",
 "admin":"During the transfusion",
 "post":"Post-transfusion",
 "ahtr":"Acute hemolytic reaction",
 "fnh":"Febrile non-hemolytic reaction",
 "allergy":"Allergic & anaphylactic reactions",
 "lung":"TRALI vs TACO",
 "delayed":"Delayed hemolytic reaction",
 "steps":"Steps when a reaction is suspected",
}
HI = ["abo","rh","steps","ahtr","lung","admin","pre","jw","choose"]

SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

# ---------- components ----------
q("comp","Which blood component carries oxygen?",
 ["*Red blood cells","White blood cells || Fight infection.","Platelets || Help with clotting.","Plasma || Fluid carrying nutrients, hormones and waste."],
 "Blood is responsible for oxygen delivery, immunity and clotting.")
q("comp","Match each component to its job. Which pairs are correct? "+SATA,
 ["*White blood cells: fight infection","*Platelets: help with clotting","*Plasma: carries nutrients, hormones and waste",
  "Red blood cells: fight infection || RBCs carry oxygen.","Platelets: carry oxygen || Platelets help with clotting."],
 "Related concepts: oxygenation (PRBCs restore Hgb), perfusion (circulating volume), immunity (foreign antigens can trigger reactions), safety.")

# ---------- why ----------
q("why","Which conditions are reasons patients may need blood products? "+SATA,
 ["*Acute blood loss from trauma, surgery or a GI bleed","*Anemia from chronic illness or bone marrow suppression","*Coagulation disorders such as hemophilia, DIC or liver failure",
  "*Platelet deficiency such as ITP or chemotherapy-induced thrombocytopenia","*Severe hemorrhage needing a massive transfusion protocol"],
 "All five appear on the 'Why patients need blood products' slide.")

# ---------- product types ----------
q("prod","Which blood product contains clotting factors and is used for coagulopathy and liver disease?",
 ["Packed red blood cells || Increase oxygen-carrying capacity.","Platelets || Treat thrombocytopenia.",
  "*Plasma (fresh frozen plasma)","Whole blood || Rarely used; massive hemorrhage."],
 "Plasma also appears in massive transfusion protocols.")
q("prod","Which product is rich in fibrinogen, factor VIII and von Willebrand factor?",
 ["Fresh frozen plasma || Contains clotting factors generally.","*Cryoprecipitate","Platelets || Help form clots, but aren't fibrinogen-rich.","Packed red blood cells || Carry oxygen."],
 "Cryoprecipitate is used for bleeding disorders and fibrinogen replacement (fibrinogen under 100 mg/dL).")
q("prod","How are platelets stored?",
 ["Frozen || That's fresh frozen plasma.","*At room temperature, with a short shelf life","Refrigerated for months || Not how platelets are stored.","In the blood bank freezer with cryoprecipitate || Not how platelets are stored."],
 "Platelets treat thrombocytopenia or platelet dysfunction.")
q("prod","Which statement about whole blood is correct?",
 ["*It contains RBCs, plasma and platelets, and is rarely used today except mainly for massive hemorrhage",
  "It's the most commonly transfused product || Rarely used today.","It contains only clotting factors || That's plasma.","It's used for low fibrinogen || That's cryoprecipitate."],
 "RBCs are usually transfused as packed RBCs.")
q("prod","What is the main purpose of a packed red blood cell transfusion?",
 ["*Increase oxygen-carrying capacity in anemia or blood loss","Replace clotting factors || Plasma.","Replace fibrinogen || Cryoprecipitate.","Raise the platelet count || Platelets."],
 "PRBCs quickly restore hemoglobin.")

# ---------- scenarios ----------
q("choose","A 45-year-old has a hemoglobin of 6.5 g/dL with fatigue, shortness of breath and dizziness. Which product is most appropriate?",
 ["*Packed red blood cells","Platelets || Platelet count isn't the problem.","Fresh frozen plasma || For clotting factor replacement.","Oral iron alone || Takes days to weeks; not for acute symptoms."],
 "Symptoms show symptomatic anemia with reduced oxygen delivery. PRBCs quickly raise hemoglobin and oxygen-carrying capacity.")
q("choose","Why is a transfusion chosen over oral or IV iron for a symptomatic client with Hgb 6.5 g/dL?",
 ["*Iron takes days to weeks to raise hemoglobin, which is too slow for acute symptoms","Iron is contraindicated in anemia || Not the reason.",
  "Iron causes transfusion reactions || Not the reason.","Iron only raises platelets || Not the reason."],
 "From the professor's Scenario 1 answer.")
q("choose","A 32-year-old on chemotherapy has a platelet count of 8,000/µL and occasional nosebleeds, but isn't actively bleeding. Which product is appropriate?",
 ["Packed red blood cells || Hemoglobin isn't the problem.","*Platelet transfusion","Cryoprecipitate || For low fibrinogen.","No transfusion until she actively bleeds || Risk is too high."],
 "Below 10,000/µL, even minor trauma or spontaneous vessel rupture can cause life-threatening bleeding.")
q("choose","Match the problem to the product. Which pairs are correct? "+SATA,
 ["*Low hemoglobin with symptoms: packed RBCs","*Very low platelets: platelets","*Clotting factor deficiency (prolonged PT/INR or aPTT): plasma","*Fibrinogen under 100 mg/dL: cryoprecipitate",
  "Low fibrinogen: packed RBCs || Cryoprecipitate replaces fibrinogen."],
 "Pick the product that replaces exactly what's missing.")

# ---------- ABO ----------
q("abo","Which antibodies are in the plasma of a person with type A blood?",
 ["Anti-A || That would attack their own cells.","*Anti-B","Both anti-A and anti-B || That's type O.","Neither || That's type AB."],
 "Antibodies target the antigens you DON'T have.")
q("abo","Which blood type is the universal donor for red blood cells, and why?",
 ["*Type O, because its RBCs have no A or B antigens","Type AB, because it has both antigens || AB is the universal recipient.",
  "Type A, because it has anti-B antibodies || Not a universal donor.","Type B, because it has the B antigen || Not a universal donor."],
 "Type AB is the universal recipient because it has both A and B antigens and no anti-A or anti-B.")
q("abo","A client has type AB blood. Which red cell types can they safely receive? "+SATA,
 ["*A","*B","*AB","*O"],
 "AB has no anti-A or anti-B antibodies, so it can receive any ABO type (universal recipient).")
q("abo","A client has type O blood. Which red cell type can they receive?",
 ["A or O || A has the A antigen; type O has anti-A.","AB only || AB cells would be attacked.","*O only","Any type || That describes AB."],
 "Type O has both anti-A and anti-B antibodies.")
q("abo","Which ABO facts are correct? "+SATA,
 ["*Type B has the B antigen and anti-A antibodies","*Type AB has both A and B antigens and no anti-A or anti-B antibodies","*Type O has neither A nor B antigens",
  "Type A has the A antigen and anti-A antibodies || Type A has anti-B.","Type O has no antibodies || Type O has both anti-A and anti-B."],
 "A blood group is classified by the presence or absence of specific antigens on the RBC surface. Mismatched blood can be fatal.")

# ---------- Rh ----------
q("rh","A client with type B negative blood is scheduled for a transfusion. Which donor types are compatible?",
 ["B positive, B negative, O positive, O negative || Rh-negative clients need Rh-negative blood.","*B negative and O negative",
  "B positive and O positive || Wrong Rh.","B negative only || O negative is also compatible."],
 "Type B has anti-A, so B or O; Rh-negative clients must receive Rh-negative blood to prevent sensitization.")
q("rh","A trauma client with type O negative blood is in hypovolemic shock. Which blood type is safest?",
 ["O positive only || Rh-positive could sensitize the client.","*O negative only","O positive and O negative || Rh-negative needs Rh-negative.","Any type, since O negative is the universal recipient || O negative is the universal DONOR, not recipient."],
 "O− has no A, B or Rh antigens, making it the universal donor. O− clients can only receive O−.")
q("rh","Why must an Rh-negative client receive Rh-negative red cells?",
 ["*To prevent sensitization","Rh-positive blood clots faster || Not the reason.","Rh-negative blood has more hemoglobin || Not the reason.","It's only a hospital preference || It's a safety rule."],
 "Rh-positive means the D antigen is present; Rh-negative means it's absent.")
q("rh","Which statement is correct?",
 ["*O negative is the universal donor; AB positive is the universal recipient","O negative is the universal recipient || O− can only receive O−.",
  "AB negative is the universal donor || AB is the universal recipient.","O positive is safe for every client || Rh-negative clients need Rh-negative."],
 "Compatibility charts are for red cells; always follow blood bank testing.")

# ---------- JW ----------
q("jw","A 42-year-old Jehovah's Witness with Hgb 6.8 g/dL says, \"I cannot accept blood transfusions for religious reasons.\" Two units of PRBCs are ordered. What is the MOST appropriate action?",
 ["Explain the risks and proceed if she stays unstable || Violates patient autonomy.",
  "*Notify the provider and discuss alternatives such as iron and erythropoietin",
  "Document the refusal but transfuse in an emergency || Blood can't be given without consent, even in emergencies.",
  "Ask the family to persuade her to consent || Family can't override a competent adult's decision."],
 "A competent adult has the right to refuse blood products. Respect the decision, notify the provider, and explore alternatives.")
q("jw","Which blood products does a Jehovah's Witness patient always refuse? "+SATA,
 ["*Whole blood","*Red blood cells","*White blood cells","*Platelets","*Plasma",
  "Normal saline || A non-blood alternative."],
 "These are listed as 'always avoid.'")
q("jw","Which options MAY be acceptable to a Jehovah's Witness patient, depending on individual choice? "+SATA,
 ["*Albumin","*Clotting factors","*Erythropoietin with iron","*Tranexamic acid","*IV fluids such as NS or LR"],
 "Fractions are an individual choice, so ask each patient. Non-blood alternatives also include recombinant clotting factors, folic acid, B12 and desmopressin.")
q("jw","Which nursing actions apply to bloodless care? "+SATA,
 ["*Respect and document the patient's wishes clearly","*Minimize blood loss: cluster labs, use pediatric tubes, limit phlebotomy","*Optimize oxygenation","*Provide emotional and spiritual support",
  "Assume every Jehovah's Witness accepts the same fractions || Ask each patient."],
 "Also discuss the care plan with the patient, family, provider and ethics team as needed, and monitor closely for bleeding and anemia.")

# ---------- labs & orders ----------
q("labs","Below what hemoglobin level is a transfusion usually indicated, per the lecture?",
 ["12 g/dL || Normal female range starts here.","10 g/dL || Not the threshold given.","*7–8 g/dL (varies with the patient's condition)","4 g/dL || Too low a threshold."],
 "Normal Hgb: 12–16 g/dL (female), 14–18 g/dL (male).")
q("labs","When is a platelet transfusion indicated, per the lecture? "+SATA,
 ["*Platelets under 10,000–20,000/µL","*Platelets under 50,000/µL with active bleeding",
  "Platelets of 160,000/µL || Normal is 150,000–400,000.","Any platelet count under 400,000 || That's the top of normal."],
 "Below 10,000/µL, spontaneous bleeding can occur.")
q("labs","A client's PT/INR and aPTT are prolonged and they're bleeding. Which product does the nurse anticipate?",
 ["*Plasma","Platelets || Count is the issue for platelets.","Packed RBCs || Don't replace clotting factors.","Albumin || Not a clotting product."],
 "Prolonged clotting times = risk of bleeding; plasma replaces clotting factors.")
q("labs","What is the difference between a type and screen and a crossmatch?",
 ["*Type and screen finds ABO and Rh type and screens for antibodies; crossmatch checks compatibility with the donor unit",
  "They're the same test || The slide separates them.","Crossmatch finds the ABO type; type and screen checks the donor unit || Reversed.","Both only check platelets || Not what they test."],
 "Both happen before blood is released.")
q("labs","Which special product requirements might a transfusion order include? "+SATA,
 ["*Irradiated","*Leukoreduced","*CMV-negative",
  "Sugar-free || Not a blood product requirement."],
 "Orders also state the product type, number of units, and rate (or 'as tolerated').")

# ---------- pre-transfusion ----------
q("pre","Which IV access is preferred for packed RBCs in an adult?",
 ["24 gauge || Too small.","*18 gauge or a central line (20 gauge acceptable)","22 gauge only || Acceptable for platelets, not preferred for PRBCs.","Any existing IV with a running medication || Blood needs its own line with saline."],
 "A 22 gauge is acceptable for platelets.")
q("pre","Which items must be in place before a transfusion starts? "+SATA,
 ["*Signed blood transfusion consent","*Health care provider order","*Type and crossmatch","*Verification with a second licensed RN","*Emergency medications on the unit"],
 "Equipment: IV pump and Y-tubing with an inline filter.")
q("pre","Consent for a transfusion is missing when the blood arrives on the unit. What should the nurse do?",
 ["Start the transfusion and get consent afterward || Consent must be signed before release.","*Not start it; resolve the consent with the provider first",
  "Have the family sign while it runs || Not appropriate.","Start slowly and monitor || Still no consent."],
 "Consent must be signed before blood is released.")
q("pre","Which questions should the nurse answer before administering blood? "+SATA,
 ["*Is there consent and an order?","*Any previous transfusion reaction?","*What are the baseline vital signs?","*Any signs of fluid overload or respiratory distress?","*What size IV does the client have?"],
 "Also: why the client needs blood, the blood type, Hgb/Hct/platelets, and any barriers to giving it.")

# ---------- administration ----------
q("admin","The blood bank releases a unit of PRBCs. Within what time must the nurse begin the transfusion?",
 ["4 hours || That's the time to complete it.","*30 minutes","2 hours || Too long.","15 minutes || That's the slow-start window."],
 "Begin within 30 minutes of release; complete within 4 hours.")
q("admin","Which IV solution may hang with blood on the Y-set?",
 ["Dextrose 5% in water || Not compatible.","Lactated Ringer's || Not the lecture's solution.","*0.9% normal saline only","Any running medication || Never mix medications with blood."],
 "Use Y-tubing with an inline filter.")
q("admin","What is the vital sign schedule for a blood transfusion, per the lecture?",
 ["*15 minutes before starting, 15 minutes after starting, then every hour until complete","Only at the end of the unit || Too late to catch a reaction.",
  "Every 4 hours || Too infrequent.","Every 5 minutes for the whole unit || Not the schedule taught."],
 "The first 15 minutes are the highest-risk period.")
q("admin","Why does the nurse stay with the client and infuse slowly for the first 15 minutes?",
 ["*Severe reactions are most likely to appear early","It saves blood || Not the reason.","The pump needs to warm up || Not the reason.","It's only for platelets || Applies to transfusions generally."],
 "Watch for chills, rash, dyspnea and chest pain.")
q("admin","How long can a unit of PRBCs take to infuse, at most?",
 ["1 hour || Too short as a limit.","*4 hours total from pickup","8 hours || Too long.","24 hours || Too long."],
 "Platelets are transfused over 15–30 minutes.")
q("admin","How quickly are platelets usually transfused?",
 ["Over 4 hours || That's the PRBC limit.","*Over 15–30 minutes","Over 8 hours || Too long.","As an IV push || Not how platelets are given."],
 "A 22 gauge IV is acceptable for platelets.")

# ---------- post ----------
q("post","What should the nurse do when a transfusion finishes without a reaction? "+SATA,
 ["*Flush the line with 0.9% normal saline","*Dispose of the bag and tubing per facility policy (usually biohazard waste)","*Document the transfusion","*Watch for delayed reactions",
  "Hang D5W to keep the vein open || Not the lecture's flush."],
 "The saline flush clears remaining blood into the patient and keeps blood from mixing with other IV medications.")
q("post","Which findings hours after a transfusion suggest a delayed reaction? "+SATA,
 ["*Fever","*Rash or itching","*Dark urine","*Shortness of breath"],
 "The risk window doesn't close when the blood stops.")
q("post","A reaction occurred during the transfusion. What happens to the blood bag and tubing?",
 ["Discard them in biohazard waste || Not after a reaction.","*Send them back to the blood bank for investigation","Keep them in the client's room || Not the lecture's action.","Flush and reuse the tubing || Use new tubing."],
 "Without a reaction, they usually go in biohazard waste per policy.")

# ---------- acute hemolytic ----------
q("ahtr","What causes an acute hemolytic transfusion reaction?",
 ["*ABO incompatibility destroying the donor RBCs","Donor WBC cytokines || Febrile non-hemolytic.","Donor plasma proteins || Allergic.","Volume overload || TACO."],
 "Rare but severe and life-threatening.")
q("ahtr","Which findings suggest an acute hemolytic reaction? "+SATA,
 ["*Fever and chills","*Flank or back pain, or chest pain","*Hypotension","*Dark or red urine (hemoglobinuria)","*Anxiety and shortness of breath"],
 "Can progress to shock, DIC (oozing from the IV) and kidney injury.")
q("ahtr","Ten minutes into a transfusion, a client reports back pain and chills, and the urine is dark. What is the FIRST action?",
 ["Slow the transfusion rate || Stop it completely.","*Stop the transfusion immediately","Give acetaminophen || Not the first action.","Call the blood bank || After stopping."],
 "Then keep the IV open with saline in new tubing, and notify the provider and blood bank.")
q("ahtr","After an acute hemolytic reaction, which interventions should the nurse anticipate? "+SATA,
 ["*Normal saline at 100–200 mL/hr or a bolus","*IV diuretics","*Testing for DIC","*Transfer to the ICU",
  "Restarting the same unit once fever resolves || Never restart an incompatible unit."],
 "From the nursing management graphic on the slide.")

# ---------- febrile ----------
q("fnh","Which transfusion reaction is the most common?",
 ["Acute hemolytic || Rare but severe.","*Febrile non-hemolytic","Anaphylactic || Uncommon.","TRALI || Uncommon."],
 "Caused by the recipient's antibodies reacting to donor WBCs or cytokines.")
q("fnh","Which findings fit a febrile non-hemolytic reaction? "+SATA,
 ["*Temperature rise of 1°C or more","*Chills and rigors","*Mild headache or malaise",
  "Hypotension with dark urine || Suggests hemolysis.","Hives and wheezing || Allergic or anaphylactic."],
 "Usually no hypotension or hemolysis.")
q("fnh","How is a febrile non-hemolytic reaction managed?",
 ["*Stop the transfusion and assess; restart only if the provider approves; give antipyretics such as acetaminophen",
  "Keep it running and give acetaminophen || Stop it first.","Give epinephrine || For anaphylaxis.","Give a diuretic || For TACO."],
 "Any suspected reaction starts with stopping the transfusion.")

# ---------- allergic / anaphylactic ----------
q("allergy","A client develops itching and hives during a transfusion with stable vitals. What reaction is this, and how is it treated?",
 ["*Mild allergic reaction: stop, give an antihistamine, and the transfusion may restart if symptoms resolve",
  "Acute hemolytic: never restart || Hives without hemolysis signs point to allergy.","TACO: give a diuretic || No overload signs.","Anaphylaxis: give epinephrine || No airway or BP problems."],
 "Allergic reactions come from donor plasma proteins and can occur during or up to 24 hours after.")
q("allergy","Which client is at highest risk for an anaphylactic transfusion reaction?",
 ["*A client with IgA deficiency who has anti-IgA antibodies","A client with type AB blood || Not a listed risk.","A client with heart failure || Risk for TACO.","A client receiving platelets only || Not a listed risk."],
 "Onset: seconds to minutes after starting.")
q("allergy","A client receiving blood suddenly has wheezing, respiratory distress and a dropping BP. Which actions are correct? "+SATA,
 ["*Stop the transfusion","*Maintain the airway","*Give epinephrine as ordered","*Notify the provider",
  "Restart once the antihistamine works || Not for anaphylaxis."],
 "Anaphylaxis: bronchospasm, hypotension, shock.")

# ---------- TRALI vs TACO ----------
q("lung","A client receiving a rapid, large-volume transfusion develops dyspnea, hypertension, JVD and crackles. What is happening?",
 ["TRALI || TRALI causes hypotension and noncardiogenic edema.","*TACO (transfusion-associated circulatory overload)","Febrile reaction || No fever pattern.","Delayed hemolytic reaction || Happens days later."],
 "TACO = volume overload. Stop the transfusion, sit the client upright, give diuretics and oxygen.")
q("lung","Within 6 hours of a transfusion, a client has acute respiratory distress, hypoxia, fever and hypotension. A chest x-ray shows bilateral infiltrates. What is happening?",
 ["TACO || TACO causes hypertension and JVD.","*TRALI (transfusion-related acute lung injury)","Mild allergic reaction || No hives.","Acute hemolytic reaction || No flank pain or dark urine."],
 "Donor antibodies activate the recipient's lung neutrophils, causing capillary leak (noncardiogenic pulmonary edema).")
q("lung","Which findings point to TACO rather than TRALI? "+SATA,
 ["*Hypertension","*Jugular venous distension","*Volume overload from a rapid or large transfusion",
  "Hypotension || More typical of TRALI.","Noncardiogenic pulmonary edema || TRALI."],
 "TACO also causes tachycardia and headache.")
q("lung","How is TACO managed? "+SATA,
 ["*Stop the transfusion","*Sit the client upright","*Give diuretics as ordered","*Give oxygen",
  "Speed up the transfusion to finish sooner || Adds more volume."],
 "TRALI: stop, oxygen, supportive care (possibly ventilation).")

# ---------- delayed ----------
q("delayed","A client transfused 10 days ago now has jaundice, mild anemia, fever and an elevated bilirubin. What is the likely cause?",
 ["*Delayed hemolytic reaction","Acute hemolytic reaction || Occurs within 24 hours.","TACO || Occurs during or soon after.","Febrile non-hemolytic reaction || Occurs during the transfusion."],
 "An immune response to minor RBC antigens, days to weeks later. Usually less severe; supportive care and lab monitoring.")
q("delayed","The HALO mnemonic sorts transfusion reactions. What does the 'H' stand for?",
 ["*Hemolysis (acute or delayed hemolytic reactions)","Hypertension || Not the H.","Hives || That's under Allergy.","Hypoxia || That's under Lung."],
 "Fever = febrile non-hemolytic; Hemolysis = acute or delayed; Allergy = anaphylactic; Lung = TRALI; Overload = TACO.")

# ---------- steps ----------
q("steps","A client shows signs of a transfusion reaction. Put the first steps in the correct order: which comes FIRST?",
 ["*Stop the transfusion","Notify the blood bank || Step 3.","Obtain urine and blood samples || Step 4.","Document || Step 5."],
 "1 Stop · 2 Notify provider · 3 Notify blood bank · 4 Obtain urine and blood samples · 5 Document · 6 Advise patient.")
q("steps","After stopping a transfusion for a suspected reaction, how is IV access maintained?",
 ["Keep running the blood at a slower rate || The blood must stop.","*Infuse normal saline (250 mL) through NEW tubing",
  "Flush through the blood tubing || Would push more blood in.","Remove the IV || Access must be kept."],
 "New tubing keeps any remaining blood from reaching the client.")
q("steps","What happens after a suspected transfusion reaction? "+SATA,
 ["*Notify the provider with assessment findings (cardiac, respiratory, vital signs)","*Notify the blood bank and return the blood container and tubing","*Obtain urine and blood samples","*Document the reaction","*Let the client know a reaction occurred and how it can be prevented"],
 "Urine and blood samples are used for hemolytic and allergic reactions.")
q("steps","Which step comes immediately after stopping the transfusion and keeping the IV open?",
 ["Document || Step 5.","*Notify the provider","Advise the client || Step 6.","Obtain samples || Step 4."],
 "Order: stop, notify provider, notify blood bank, samples, document, advise.")
