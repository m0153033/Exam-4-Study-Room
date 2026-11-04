# Week 11.2 Blood Products & Administration — Prof. Hanikeh's two slide decks (Intro to Blood Products; Compatibility & Blood Product Administration).
# Classmate update (Nov 3): compatibility is NOT select-all (know O- = universal donor); gauge 18-20; know product types;
# know reaction SIGNS (specific reaction type not tested); when to use normal saline; pre-transfusion steps; Jehovah's Witness.
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
  "*Plasma (fresh frozen plasma)","Whole blood || Massive hemorrhage and trauma."],
 "Plasma also appears in massive transfusion protocols and can reverse warfarin effect.")
q("prod","Which product is rich in fibrinogen, factor VIII and von Willebrand factor?",
 ["Fresh frozen plasma || Contains clotting factors generally.","*Cryoprecipitate","Platelets || Help form clots, but aren't fibrinogen-rich.","Packed red blood cells || Carry oxygen."],
 "Cryoprecipitate is used for low fibrinogen (under 100 mg/dL).")
q("prod","How are platelets stored?",
 ["Frozen || That's fresh frozen plasma.","*At room temperature, with a short shelf life","Refrigerated for months || Not how platelets are stored.","In the blood bank freezer with cryoprecipitate || Not how platelets are stored."],
 "Platelets treat a low platelet count (thrombocytopenia).")
q("prod","Which statement about whole blood is correct?",
 ["*It contains RBCs, plasma and platelets and is used for trauma and massive hemorrhage",
  "It's the most commonly transfused product || Rarely used today.","It contains only clotting factors || That's plasma.","It's used for low fibrinogen || That's cryoprecipitate."],
 "Whole blood = trauma / massive hemorrhage, when rapid replacement of RBCs, plasma and platelets is needed.")
q("prod","What is the main purpose of a packed red blood cell transfusion?",
 ["*Increase oxygen-carrying capacity in anemia or blood loss (hemorrhage)","Replace clotting factors || Plasma.","Replace fibrinogen || Cryoprecipitate.","Raise the platelet count || Platelets."],
 "PRBCs: symptomatic anemia, significant blood loss, low Hgb (about 7–8 g/dL). One unit raises Hgb about 1 g/dL.")
q("prod","Match each blood product to its main use. Which is correct?",
 ["*Whole blood: trauma and massive hemorrhage","Platelets: low hemoglobin || PRBCs are for low hemoglobin.",
  "Packed RBCs: low platelet count || Platelets are for a low platelet count.","Cryoprecipitate: anemia || Cryo replaces fibrinogen."],
 "Whole blood = trauma; platelets = low platelets; PRBCs = hemorrhage and anemia (low Hgb); plasma = clotting factors; cryo = fibrinogen.")
q("prod","A client's platelet count is 9,000/µL. Which product does the nurse expect?",
 ["*Platelets","Packed red blood cells || For low hemoglobin.","Whole blood || For trauma and massive hemorrhage.","Albumin || Not a blood product for low platelets."],
 "Platelet transfusion: under 10,000–20,000/µL, or under 50,000/µL with active bleeding.")

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
q("choose","A client arrives from a car crash with massive bleeding and needs rapid replacement of red cells, plasma and platelets. Which product fits?",
 ["*Whole blood","Platelets only || Doesn't replace red cells or plasma.","Cryoprecipitate || Fibrinogen only.","Albumin || Not a blood product for hemorrhage."],
 "Whole blood = trauma / massive hemorrhage (per protocol).")
q("choose","A client with a GI bleed has a hemoglobin of 6.9 g/dL and is pale and tachycardic. Which product does the nurse anticipate?",
 ["*Packed red blood cells","Platelets || The platelet count isn't the problem.","Cryoprecipitate || For low fibrinogen.","Normal saline alone || Doesn't restore oxygen-carrying capacity."],
 "PRBCs = hemorrhage and anemia with low Hgb (about 7–8 g/dL or as ordered).")

# ---------- ABO ----------
q("abo","Which antibodies are in the plasma of a person with type A blood?",
 ["Anti-A || That would attack their own cells.","*Anti-B","Both anti-A and anti-B || That's type O.","Neither || That's type AB."],
 "Antibodies target the antigens you DON'T have.")
q("abo","Which blood type is the universal donor for red blood cells?",
 ["*O negative, because its RBCs have no A, B or Rh (D) antigens","AB positive || AB positive is the universal RECIPIENT.",
  "A negative || Has the A antigen.","O positive || Rh-positive cells can sensitize an Rh-negative client."],
 "O negative = universal donor. AB positive = universal recipient.")
q("abo","A client has type AB positive blood. Which statement about the red cells they can receive is correct?",
 ["*They can receive any ABO type, because AB has no anti-A or anti-B antibodies (universal recipient)","AB only || AB can receive A, B, AB or O.",
  "O only || That's the rule for type O.","A or O only || That's the rule for type A."],
 "AB has both A and B antigens and no anti-A or anti-B antibodies.")
q("abo","A client has type O blood. Which red cell type can they receive?",
 ["A or O || A has the A antigen; type O has anti-A.","AB only || AB cells would be attacked.","*O only","Any type || That describes AB."],
 "Type O has both anti-A and anti-B antibodies.")
q("abo","Which statement about type B blood is correct?",
 ["*It has the B antigen and anti-A antibodies, so it can receive B or O","It has anti-B antibodies || Type B has anti-A.",
  "It can receive A or B || A cells would be attacked by anti-A.","It can receive any type || That's AB."],
 "A blood group is classified by the antigens on the RBC surface. Mismatched blood can be fatal.")
q("abo","A client has type A blood. Which red cell types can they receive?",
 ["*A or O","A or B || B cells would be attacked by anti-B.","AB only || AB has the B antigen.","Any type || That's AB."],
 "Type A has anti-B antibodies, so B and AB cells are incompatible.")

# ---------- Rh ----------
q("rh","A client with type A negative blood needs packed RBCs. Which donor blood is compatible?",
 ["*A negative and O negative","A positive and O positive || Rh-negative clients need Rh-negative blood.",
  "A negative only || O negative is also compatible.","AB negative and A negative || AB has the B antigen."],
 "A− can receive from A− and O−. Type A has anti-B, so A or O; Rh-negative must receive Rh-negative.")
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
q("rh","A client with type A positive blood needs red cells. Which donor blood is compatible?",
 ["*A positive, A negative, O positive or O negative","A positive only || Rh-positive can also receive Rh-negative.",
  "A negative and O negative only || Rh-positive clients can receive Rh-positive too.","AB positive || AB has the B antigen."],
 "Rh-positive clients can receive Rh-positive or Rh-negative; type A can receive A or O.")

# ---------- JW ----------
q("jw","A 42-year-old Jehovah's Witness with Hgb 6.8 g/dL says, 'I cannot accept blood transfusions for religious reasons.' Two units of PRBCs are ordered. What is the MOST appropriate action?",
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
 ["12 g/dL || Normal female range starts here.","10 g/dL || Not the threshold given.","*About 7–8 g/dL (or as ordered)","4 g/dL || Too low a threshold."],
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
q("pre","Which IV catheter size does the lecture recommend for a blood transfusion?",
 ["24 gauge || Too small.","*18 to 20 gauge","26 gauge || Too small.","Any existing IV with a running medication || Blood needs its own line with saline."],
 "Use an 18 to 20 gauge needle with normal saline Y-tubing.")
q("pre","Which are correct for setting up a blood transfusion? "+SATA,
 ["*An 18 gauge IV","*A 20 gauge IV","*0.9% normal saline on Y-tubing with an inline filter",
  "Dextrose 5% in water on the Y-set || Not compatible with blood.","A 24 gauge IV || Too small.","Lactated Ringer's on the Y-set || Normal saline only."],
 "Gauge 18–20, normal saline only.")
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
q("pre","At the bedside, the nurse and a second RN find that the client's identification band number doesn't match the blood bag label. What should the nurse do?",
 ["*Don't start the transfusion; contact the blood bank","Start it if the names match || All identifiers must match.",
  "Start slowly and watch for a reaction || Never start mismatched blood.","Fix the label and start || Not the nurse's role."],
 "A bedside mismatch or unresolved consent issue means do not start the transfusion.")
q("pre","When are baseline vital signs taken for a transfusion?",
 ["*Within 15 minutes before starting","Only after the transfusion is done || Too late.","1 hour after starting || Baseline is before.","Only if the client has a fever || Always taken."],
 "Baseline vitals give the comparison for spotting a reaction.")

# ---------- administration ----------
q("admin","The blood bank releases a unit of PRBCs. Within what time must the nurse begin the transfusion?",
 ["4 hours || That's the time to complete it.","*30 minutes","2 hours || Too long.","15 minutes || That's the slow-start window."],
 "Begin within 30 minutes of release; complete within 4 hours.")
q("admin","What is the vital sign schedule for a blood transfusion, per the lecture?",
 ["*15 minutes before starting, 15 minutes after starting, then every hour until complete","Only at the end of the unit || Too late to catch a reaction.",
  "Every 4 hours || Too infrequent.","Every 5 minutes for the whole unit || Not the schedule taught."],
 "The first 15 minutes are the highest-risk period.")
q("admin","Fifteen minutes after starting a unit of PRBCs, what does the nurse assess?",
 ["*A full set of vital signs, compared with baseline","Temperature only || Take a full set.","Nothing until the unit is done || The first 15 minutes are highest risk.","Blood glucose || Not the check taught."],
 "Also assess skin, breathing and comfort. Watch for chills, rash, dyspnea and chest pain.")
q("admin","Why does the nurse stay with the client and infuse slowly for the first 15 minutes?",
 ["*Severe reactions are most likely to appear early","It saves blood || Not the reason.","The pump needs to warm up || Not the reason.","It's only for platelets || Applies to transfusions generally."],
 "Watch for chills, rash, dyspnea and chest pain.")
q("admin","How long can a unit of PRBCs take to infuse, at most?",
 ["1 hour || Too short as a limit.","*4 hours total from pickup","8 hours || Too long.","24 hours || Too long."],
 "Start within 30 minutes of pickup; finish within 4 hours.")
q("admin","How quickly are platelets usually transfused?",
 ["Over 4 hours || That's the PRBC limit.","*Over 15–30 minutes","Over 8 hours || Too long.","As an IV push || Not how platelets are given."],
 "PRBCs: start within 30 minutes and finish within 4 hours.")

# ---------- normal saline ----------
q("ns","Which IV solution may hang with blood on the Y-set?",
 ["Dextrose 5% in water || Not compatible.","Lactated Ringer's || Not the lecture's solution.","*0.9% normal saline only","Any running medication || Never mix medications with blood."],
 "ALWAYS use normal saline. Use Y-tubing with an inline filter.")
q("ns","A client's IV has D5W running when a unit of PRBCs arrives. What should the nurse do?",
 ["Piggyback the blood into the D5W line || D5W is not compatible.","*Set up Y-tubing with 0.9% normal saline for the blood",
  "Add the blood to the D5W bag || Never mix.","Switch to lactated Ringer's || Normal saline only."],
 "Do not mix medications or other solutions with blood.")
q("ns","When does the nurse use normal saline during blood administration? "+SATA,
 ["*To prime the Y-tubing with the blood","*To keep the IV open in NEW tubing after stopping for a reaction","*To flush the line when the transfusion is done",
  "To dilute IV medications in the blood bag || Never add medications to blood.","Only if the client is dehydrated || Normal saline is always used with blood."],
 "Normal saline is the only fluid used with blood.")
q("ns","A transfusion is stopped for a suspected reaction. How is the IV kept open?",
 ["Keep the blood running slowly || The blood must stop.","*Normal saline through NEW tubing",
  "Flush with saline through the blood tubing || Pushes more blood in.","Remove the IV || Access must be kept."],
 "New tubing keeps any remaining blood from reaching the client.")

# ---------- post ----------
q("post","What should the nurse do when a transfusion finishes without a reaction? "+SATA,
 ["*Flush the line with 0.9% normal saline","*Dispose of the bag and tubing per facility policy (usually biohazard waste)","*Document the transfusion","*Watch for delayed reactions",
  "Hang D5W to keep the vein open || Not the lecture's flush."],
 "The saline flush clears remaining blood into the patient and keeps blood from mixing with other IV medications.")
q("post","A reaction occurred during the transfusion. What happens to the blood bag and tubing?",
 ["Discard them in biohazard waste || Not after a reaction.","*Send them back to the blood bank for investigation","Keep them in the client's room || Not the lecture's action.","Flush and reuse the tubing || Use new tubing."],
 "Without a reaction, they usually go in biohazard waste per policy.")

# ---------- reaction signs: hemolysis pattern ----------
q("ahtr","Which findings during a transfusion are signs of a serious reaction? "+SATA,
 ["*Fever and chills","*Flank or back pain, or chest pain","*Hypotension","*Dark or red urine","*Anxiety and shortness of breath"],
 "Can progress to shock, oozing from the IV site (DIC) and kidney injury.")
q("ahtr","Ten minutes into a transfusion, a client reports back pain and chills, and the urine is dark. What is the FIRST action?",
 ["Slow the transfusion rate || Stop it completely.","*Stop the transfusion immediately","Give acetaminophen || Not the first action.","Call the blood bank || After stopping."],
 "Then keep the IV open with saline in new tubing, and notify the provider and blood bank.")
q("ahtr","A transfusion was stopped for back pain, low blood pressure and dark urine. Which interventions should the nurse anticipate? "+SATA,
 ["*Normal saline at 100–200 mL/hr or a bolus","*IV diuretics","*Testing for DIC","*Transfer to the ICU",
  "Restarting the same unit once the fever resolves || Never restart that unit."],
 "From the nursing management graphic on the slide.")
q("ahtr","During a transfusion, the client becomes anxious and says, 'Something is wrong. My back hurts.' What should the nurse do first?",
 ["*Stop the transfusion","Reassure the client and keep it running || A possible reaction.","Speed it up to finish sooner || More blood worsens it.","Reposition the client || Not the first action."],
 "Any suspected reaction: stop the transfusion (stop the pump) first.")

# ---------- reaction signs: fever ----------
q("fnh","Which findings during a transfusion can signal a reaction? "+SATA,
 ["*Temperature rise of 1°C or more","*Chills and rigors","*Mild headache or malaise",
  "Stable temperature and the client feels fine || No reaction signs.","Mild thirst only || Not a listed sign."],
 "Watch closely in the first 15 minutes and throughout.")
q("fnh","Twenty minutes into a transfusion, the client's temperature rises 1.2°C and they have chills. What does the nurse do?",
 ["*Stop the transfusion and assess; restart only if the provider approves; give antipyretics such as acetaminophen as ordered",
  "Keep it running and give acetaminophen || Stop it first.","Give epinephrine || For airway or BP problems.","Give a diuretic || For fluid overload."],
 "Any suspected reaction starts with stopping the transfusion.")

# ---------- reaction signs: allergy ----------
q("allergy","A client develops itching and hives during a transfusion with stable vital signs. What should the nurse do?",
 ["*Stop the transfusion, notify the provider and give an antihistamine as ordered; it may restart only if symptoms resolve and the provider approves",
  "Keep it running and ignore the hives || Stop first.","Give a diuretic || No fluid overload signs.","Give epinephrine first || No airway or BP problems."],
 "Allergic signs can occur during or up to 24 hours after a transfusion.")
q("allergy","A client receiving blood suddenly has wheezing, respiratory distress and a dropping BP. Which actions are correct? "+SATA,
 ["*Stop the transfusion","*Maintain the airway","*Give epinephrine as ordered","*Notify the provider",
  "Restart once the antihistamine works || Not with airway and BP problems."],
 "Signs: bronchospasm, hypotension, shock. Onset can be seconds to minutes after starting.")

# ---------- reaction signs: lungs / overload ----------
q("lung","A client receiving a rapid, large-volume transfusion develops dyspnea, high blood pressure, JVD and crackles. Which actions are correct? "+SATA,
 ["*Stop the transfusion","*Sit the client upright","*Give diuretics as ordered","*Give oxygen",
  "Speed up the transfusion to finish sooner || Adds more volume."],
 "These are fluid overload signs. Also tachycardia and headache.")
q("lung","Which findings during a transfusion suggest fluid overload? "+SATA,
 ["*High blood pressure","*Jugular venous distension","*Crackles and shortness of breath","*Rapid or large-volume transfusion",
  "Dry lungs and flat neck veins || Not overload."],
 "Check for fluid overload and respiratory distress BEFORE starting, too.")
q("lung","Within 6 hours of a transfusion, a client has acute respiratory distress, low oxygen, fever and low blood pressure. What should the nurse do?",
 ["*Stop the transfusion if it is still running, give oxygen and notify the provider immediately","Encourage coughing and recheck in 1 hour || Too slow.",
  "Give a diuretic and continue || BP is already low.","Document it as expected || A red flag."],
 "Supportive care may include ventilation.")

# ---------- delayed ----------
q("delayed","A client transfused 10 days ago now has jaundice, mild anemia, fever and an elevated bilirubin. What should the nurse do?",
 ["*Report it; transfusion reactions can show up days to weeks later","Ignore it; reactions only happen during the transfusion || The risk window stays open.",
  "Give another unit of blood || Not without evaluation.","Tell the client it is the flu || Not the concern."],
 "Usually less severe; supportive care and lab monitoring.")
q("delayed","Which findings hours or days after a transfusion suggest a reaction? "+SATA,
 ["*Fever","*Rash or itching","*Dark urine","*Shortness of breath"],
 "The risk window doesn't close when the blood stops.")

# ---------- steps ----------
q("steps","A client shows signs of a transfusion reaction. What does the nurse do FIRST?",
 ["*Stop the transfusion (stop the pump)","Notify the blood bank || Step 3.","Obtain urine and blood samples || Step 4.","Document || Step 5."],
 "1 Stop · 2 Notify provider · 3 Notify blood bank · 4 Obtain urine and blood samples · 5 Document · 6 Advise patient.")
q("steps","After stopping a transfusion for a suspected reaction, how is IV access maintained?",
 ["Keep running the blood at a slower rate || The blood must stop.","*Infuse normal saline (250 mL) through NEW tubing",
  "Flush through the blood tubing || Would push more blood in.","Remove the IV || Access must be kept."],
 "New tubing keeps any remaining blood from reaching the client.")
q("steps","What happens after a suspected transfusion reaction? "+SATA,
 ["*Notify the provider with assessment findings (cardiac, respiratory, vital signs)","*Notify the blood bank and return the blood container and tubing","*Obtain urine and blood samples","*Document the reaction","*Let the client know a reaction occurred and how it can be prevented"],
 "Urine and blood samples are sent for testing.")
q("steps","Which step comes immediately after stopping the transfusion and keeping the IV open?",
 ["Document || Step 5.","*Notify the provider","Advise the client || Step 6.","Obtain samples || Step 4."],
 "Order: stop, notify provider, notify blood bank, samples, document, advise.")
q("steps","A client has hives, chills or shortness of breath during a transfusion. The nurse isn't sure which reaction it is. What is the first action?",
 ["*Stop the transfusion; the first step is the same for any reaction","Identify the reaction type first || Stop first, no matter the type.",
  "Slow the rate and recheck in 15 minutes || Stop it completely.","Call the family || Not the priority."],
 "Every suspected reaction starts with stopping the transfusion.")
