# Week 12.1 Pharmacology: The Immune System — lesson plan, PowerPoint, notes, slide infographics, poster.
# Lesson plan: vaccines are excluded. Dosage calculation (mercaptopurine) left out per the no-math rule.
EXAM = "e5"
T = "e5imm"
CONCEPTS = {
 "cycle":"Cell cycle phases",
 "types":"Cancer types by tissue",
 "why":"Why chemo is combined & given in cycles",
 "tox":"Rapidly dividing cells & shared chemo toxicities",
 "nadir":"Bone marrow suppression & nadir",
 "antimet":"Antimetabolites",
 "alkyl":"Alkylating agents: cyclophosphamide & carmustine",
 "vesicant":"Vesicants & extravasation",
 "cis":"Cisplatin",
 "doxo":"Doxorubicin (antitumor antibiotic)",
 "antimit":"Antimitotics: vincristine & paclitaxel",
 "topo":"Topoisomerase inhibitors",
 "horm":"Hormonal agents",
 "target":"Biologic response modifiers & targeted therapy",
 "hivgoal":"HIV therapy: life cycle, adherence & monitoring",
 "entry":"Entry/fusion inhibitor & CCR5 antagonist",
 "rti":"Reverse transcriptase inhibitors",
 "pi":"Protease & integrase inhibitors",
}
HI = ["cis","nadir","antimit","alkyl","doxo","horm","rti","pi","hivgoal","vesicant"]

SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

# ---------- cell cycle ----------
q("cycle","In which phase of the cell cycle is DNA made?",
 ["*S (synthesis)","G1 || The cell prepares to make DNA.","G2 || The cell prepares for mitosis.","M || The cell divides into two."],
 "G1 prepares → S makes DNA → G2 prepares for mitosis → M divides. G0 = resting, doing its specialized job.")
q("cycle","What happens in the G0 phase?",
 ["*Cells are metabolically active and carry out their specialized (differentiated) function","Cells copy their DNA || That's S phase.","Cells divide into two || That's M phase.","Cells prepare for mitosis || That's G2."],
 "Differentiated function means cells behave by specialty: GI cells make mucus, blood cells carry oxygen.")
q("cycle","Why does knowing the cell cycle help guide cancer treatment?",
 ["*Chemotherapy drugs attack cells at specific points by interfering with DNA synthesis or mitosis","Chemo only works on resting G0 cells || It targets dividing cells.","The cell cycle doesn't affect chemo || Drugs are phase-specific.","It tells which antibiotics to give || Chemo isn't antibiotic therapy."],
 "Different classes hit different phases (S, G2, M).")
q("cycle","Match the drug class with the phase it mainly acts on. Which pairing is correct?",
 ["*Antimetabolites — S phase","Antimitotics — S phase || Antimitotics act in G2/M.","Cisplatin — G1 only || It causes G2/M arrest.","Topoisomerase inhibitors — G0 || They act during replication (S/G2)."],
 "Antimetabolites = S. Antimitotics = G2/M. Platinum = G2/M arrest. Topoisomerase inhibitors = S/G2.")

# ---------- types ----------
q("types","A cancer that starts in epithelial tissue is a:",
 ["*Carcinoma","Sarcoma || Bone and soft tissue.","Lymphoma || Lymph tissue.","Leukemia || Blood-forming tissue."],
 "Carcinoma = epithelial; sarcoma = bone/soft tissue; lymphoma = lymph; leukemia = blood.")
q("types","Which pairings are correct? "+SATA,
 ["*Sarcoma — bone tissue","*Lymphoma — lymph tissue","*Leukemia — blood-forming tissue","Carcinoma — blood tissue || Carcinoma is epithelial."],
 "Cancer is classified by the tissue where it starts.")
q("types","How does the lecture define cancer?",
 ["*Abnormal cells divide uncontrollably, can invade tissue, and spread through blood and lymph","A bacterial infection of tissue || Not infection.","Cells that stop dividing || They divide without control.","Normal cells in the wrong place || Not the definition."],
 "Spread through blood and lymph is metastasis.")

# ---------- why combo ----------
q("why","Why are chemotherapy drugs given in combination?",
 ["*Different drugs hit different phases of the cell cycle","To lower the cost || Not the reason.","So each drug can be given at a higher dose || Not the reason.","Because one drug always fails || Not the reason."],
 "Several types and routes together impact multiple phases.")
q("why","Why is chemotherapy given in cycles over time?",
 ["*So the drug is available as cells grow back and enter susceptible phases","To let the tumor grow first || Not the reason.","Because chemo only works once a month || Not the reason.","To avoid all side effects || Side effects still happen."],
 "Intermittent dosing reaches cells as they enter vulnerable phases.")

# ---------- toxicity ----------
q("tox","Which normal cells are most affected by chemotherapy because they divide rapidly? "+SATA,
 ["*Hair follicle cells","*Cells lining the GI tract","*Bone marrow cells","Nerve cells || Not listed as rapidly dividing."],
 "Rapidly dividing normal cells explain alopecia, GI effects and marrow suppression.")
q("tox","Which are common chemotherapy adverse effects? "+SATA,
 ["*Nausea and vomiting","*Alopecia","*Stomatitis and GI ulceration","*Teratogenic effects","Weight gain from increased appetite || Expect loss of appetite and weight."],
 "Also neuropathy, liver, kidney and lung damage, and cognitive difficulty.")
q("tox","Why does chemotherapy damage normal cells?",
 ["*It destroys normal cells in the same way it destroys cancer cells","It only attacks cancer cells || It affects normal cells too.","Normal cells are infected || Not the reason.","It's an allergic reaction || Not the mechanism."],
 "That shared mechanism causes the side effects.")
q("tox","A client on chemotherapy asks if they can get pregnant during treatment. What should the nurse teach?",
 ["*Chemotherapy can harm a fetus; follow pregnancy precautions","It's safe any time || Chemo is teratogenic.","Only radiation affects pregnancy || Chemo does too.","Pregnancy prevents side effects || Not true."],
 "Teratogenic effects are a listed adverse effect.")

# ---------- nadir ----------
q("nadir","What is the nadir?",
 ["*The time after chemo when blood counts are at their lowest","The highest blood count || It's the lowest.","The first dose of chemo || Not the term.","The time hair grows back || Not the term."],
 "Nadir is about day 10–14; risk of infection and bleeding is greatest.")
q("nadir","Which risks come with chemo-induced bone marrow suppression? "+SATA,
 ["*Infection from low WBCs","*Bleeding from low platelets","*Fatigue from anemia","High blood pressure || Not a marrow effect."],
 "Monitor the CBC and watch for infection, bleeding and anemia.")
q("nadir","A client on paclitaxel has very low neutrophils, platelets and hemoglobin 12 days after treatment. What may be ordered?",
 ["*A chemo 'vacation' and/or filgrastim for severe neutropenia","Double the next chemo dose || Worsens suppression.","Stop all fluids || Not the treatment.","Start cardiac monitoring only || Doesn't treat the counts."],
 "Colony-stimulating medication like filgrastim raises neutrophils.")
q("nadir","Around when does the chemotherapy nadir usually occur?",
 ["*About days 10–14","Within 1 hour || Too early.","After 6 months || Too late.","Only on the day of infusion || Too early."],
 "Follow neutropenic precautions during the nadir.")

# ---------- antimetabolites ----------
q("antimet","When do antimetabolites exert their cytotoxic effect?",
 ["*During S phase, suppressing DNA synthesis","During M phase || That's antimitotics.","Only in G0 || They act on dividing cells.","They don't affect DNA || They block DNA synthesis."],
 "Antimetabolites look like normal folate, purines or pyrimidines and block DNA replication.")
q("antimet","Which drug is a folic acid analog that is also used at lower doses for rheumatoid arthritis and psoriasis?",
 ["*Methotrexate","Cytarabine || Pyrimidine analog.","Mercaptopurine || Purine analog.","Cyclophosphamide || Alkylating agent."],
 "Methotrexate = folic acid analog.")
q("antimet","Cytarabine can be given intrathecally. What is the concern with this route?",
 ["*Arachnoiditis","Hemorrhagic cystitis || Cyclophosphamide.","Bradycardia || Paclitaxel.","Ototoxicity || Cisplatin."],
 "Cytarabine = pyrimidine analog.")
q("antimet","Which drug is a purine analog given with weight-based dosing?",
 ["*Mercaptopurine","Methotrexate || Folic acid analog.","Cytarabine || Pyrimidine analog.","Topotecan || Topoisomerase inhibitor."],
 "Mercaptopurine = purine analog.")

# ---------- alkylating ----------
q("alkyl","A client receiving cyclophosphamide has blood in the urine. What complication is this?",
 ["*Hemorrhagic cystitis","Ototoxicity || Cisplatin.","Cardiotoxicity || Doxorubicin.","Arachnoiditis || Intrathecal cytarabine."],
 "Cyclophosphamide (nitrogen mustard) → hemorrhagic cystitis; give mesna as ordered.")
q("alkyl","Which nursing actions help prevent hemorrhagic cystitis with cyclophosphamide? "+SATA,
 ["*Encourage prescribed hydration","*Monitor urine for blood","*Give the chemo-protectant mesna as ordered","Restrict fluids || Fluids protect the bladder."],
 "Also monitor the CBC.")
q("alkyl","Which alkylating agent crosses the blood-brain barrier and can be a vesicant when given IV?",
 ["*Carmustine","Cyclophosphamide || Known for hemorrhagic cystitis.","Cisplatin || A platinum compound.","Methotrexate || An antimetabolite."],
 "Carmustine = nitrosourea; watch for delayed marrow suppression.")
q("alkyl","How do alkylating agents damage cancer cells?",
 ["*They cause breaks in DNA bonds and abnormal DNA pairing","They block estrogen || Hormonal agents.","They stop the mitotic spindle || Antimitotics.","They block reverse transcriptase || HIV drugs."],
 "They act mostly in S and G1.")

# ---------- vesicant ----------
q("vesicant","What is a vesicant?",
 ["*A substance that causes blistering and severe tissue damage if it leaks outside the vein","A drug that prevents nausea || An antiemetic.","A drug that protects the bladder || That's mesna.","A drug that lowers blood counts || Many chemo drugs do that."],
 "Extravasation of a vesicant can cause tissue necrosis.")
q("vesicant","During a vesicant infusion, the client reports burning and swelling at the IV site. What should the nurse do first?",
 ["*Stop the infusion immediately","Slow the rate and continue || Keeps vesicant flowing into tissue.","Apply heat to every site || Treatment is drug-specific.","Flush the IV forcefully || Pushes more drug into tissue."],
 "Then notify the provider and follow the drug-specific extravasation protocol.")
q("vesicant","How can extravasation of a vesicant be prevented or treated? "+SATA,
 ["*Give it through a central line","*Assess the IV site often for pain, swelling or redness","*Follow the drug-specific protocol (cold therapy, antidote, bicarbonate infusion as ordered)","Use a small hand vein near a joint || Avoid joints; use a good large or central vein."],
 "Not every agent uses the same antidote or temperature treatment.")

# ---------- cisplatin ----------
q("cis","Before starting cisplatin, which actions should the nurse take? "+SATA,
 ["*Infuse IV fluids as ordered","*Give an antiemetic","*Evaluate the client's hearing","*Weigh the client","Check peripheral pulses || Cisplatin causes neuropathy, not a circulation problem."],
 "Cisplatin: severe N/V, ototoxic, nephrotoxic, fluid retention, peripheral neuropathy.")
q("cis","Which lab is most important to check before cisplatin?",
 ["*BUN and creatinine","Troponin || Cardiac; doxorubicin is the heart drug.","Lipase || Not cisplatin.","TSH || Not cisplatin."],
 "Cisplatin is nephrotoxic; monitor renal function, weight and fluid balance.")
q("cis","A client receiving cisplatin reports ringing in the ears. What does this suggest?",
 ["*Ototoxicity","Expected relaxation response || It's a toxicity.","Hemorrhagic cystitis || Cyclophosphamide.","Cardiotoxicity || Doxorubicin."],
 "Assess hearing at baseline and ongoing.")
q("cis","Cisplatin is which type of chemotherapy drug?",
 ["*Platinum (heavy metal) compound","Antimetabolite || S-phase folate/purine/pyrimidine analogs.","Vinca alkaloid || Vincristine.","Aromatase inhibitor || Anastrozole."],
 "It causes cell-cycle arrest during G2/M.")

# ---------- doxorubicin ----------
q("doxo","A client with bladder cancer is receiving doxorubicin, an antitumor antibiotic. What is its purpose?",
 ["*It interferes with cancer cell DNA","It treats a coexisting UTI || It never treats infection.","It prevents superinfection || Not its use.","It acts as a vaccine || Not a vaccine."],
 "Antitumor antibiotics treat cancer only.")
q("doxo","Which is the priority monitoring for doxorubicin?",
 ["*Cardiac function","Hearing || Cisplatin.","Urine for blood || Cyclophosphamide.","Bowel movements || Vincristine."],
 "Doxorubicin (anthracycline) is cardiotoxic; it's also a vesicant.")
q("doxo","A client asks why their urine is red after doxorubicin. Best response?",
 ["*'Temporary red urine or tears can happen after this drug.'","'You're bleeding; go to the ER.' || Expected discoloration.","'Your kidneys are failing.' || Not the cause.","'You have a UTI.' || Not the cause."],
 "Still assess the IV site for extravasation and monitor CBC and liver function.")

# ---------- antimitotics ----------
q("antimit","A client on vincristine hasn't had a bowel movement in 4 days. Why is this a concern?",
 ["*Vincristine can cause severe constipation, ileus or obstruction","It's expected and harmless || Can progress to ileus.","It means the cancer is cured || Unrelated.","It's from dehydration only || The drug is the key cause."],
 "Vinca alkaloid: peripheral neuropathy and severe constipation.")
q("antimit","Which nursing action is the priority during a paclitaxel infusion?",
 ["*Cardiac monitoring","Weigh the client || Not the priority.","Keep NPO || Not needed.","Apply compression stockings || Not the priority."],
 "Paclitaxel (taxane) can cause severe bradycardia during infusion.")
q("antimit","Which assessments are important for vincristine? "+SATA,
 ["*Numbness or tingling in hands and feet","*Bowel function","*The IV site for extravasation","Hearing tests before each dose || Cisplatin."],
 "Prevent constipation with fluids and ordered stool softeners.")
q("antimit","How do antimitotics work?",
 ["*They disrupt mitosis during G2 and M phase","They block DNA synthesis in S phase || Antimetabolites.","They block hormone receptors || Hormonal agents.","They block HIV entry || HIV drugs."],
 "Vincristine and paclitaxel stop the mitotic spindle.")
q("antimit","Besides bradycardia, what else should the nurse watch for with paclitaxel? "+SATA,
 ["*Hypersensitivity reactions","*Bone marrow suppression","Hemorrhagic cystitis || Cyclophosphamide.","Red urine || Doxorubicin."],
 "Monitor HR and rhythm during the infusion.")

# ---------- topoisomerase ----------
q("topo","What do topoisomerase enzymes normally do?",
 ["*Make temporary breaks in DNA to relieve coiling and tangles so DNA can replicate","Build the mitotic spindle || Not their role.","Make estrogen || Aromatase does that.","Copy viral RNA into DNA || Reverse transcriptase."],
 "Topoisomerase inhibitors (topotecan) block this, so DNA can't replicate.")
q("topo","Which drug is a topoisomerase inhibitor, and what is its main risk?",
 ["*Topotecan; severe bone marrow suppression","Tamoxifen; blood clots || Estrogen receptor blocker.","Vincristine; constipation || Antimitotic.","Carmustine; crosses the BBB || Alkylating agent."],
 "Watch for neutropenia and thrombocytopenia.")

# ---------- hormonal ----------
q("horm","A client on tamoxifen reports calf pain and swelling. Why is this a priority?",
 ["*Tamoxifen raises the risk of blood clots (DVT, PE, stroke)","It's expected muscle soreness || Clot risk.","It's hot flashes || Not related.","It's bone loss || That's anastrozole."],
 "Tamoxifen blocks estrogen in breast cancer cells; also report abnormal vaginal bleeding.")
q("horm","Which drug is an aromatase inhibitor, and what should be monitored?",
 ["*Anastrozole; bone health (osteoporosis)","Flutamide; liver function || Androgen blocker.","Leuprolide; hormone flare || GnRH agonist.","Tamoxifen; blood clots || Estrogen receptor blocker."],
 "Anastrozole lowers estrogen production in postmenopausal hormone-sensitive breast cancer.")
q("horm","A client on flutamide for prostate cancer reports dark urine and yellow skin. What does the nurse suspect?",
 ["*Liver toxicity","Hemorrhagic cystitis || Cyclophosphamide.","Expected hot flashes || Not these findings.","Blood clots || Tamoxifen."],
 "Flutamide blocks androgens; monitor LFTs.")
q("horm","Why might prostate cancer symptoms briefly worsen after leuprolide is started?",
 ["*An initial hormone flare happens before hormone production is suppressed","The drug failed || Flare is expected.","It's an allergic reaction || Not the reason.","It causes hemorrhagic cystitis || Not the reason."],
 "GnRH agonist: initial flare, then suppression. Hot flashes, decreased libido, bone loss.")
q("horm","Match each hormonal drug with its main risk. "+SATA,
 ["*Tamoxifen — blood clots","*Anastrozole — bone loss","*Flutamide — liver toxicity","Leuprolide — hearing loss || Leuprolide = initial flare."],
 "Trastuzumab = heart.")

# ---------- targeted ----------
q("target","Which drug targets HER2-positive cancer, and what is the priority assessment?",
 ["*Trastuzumab; cardiac function and heart-failure signs","Imatinib; hearing || Not the priority.","Interferon alfa; urine color || Not the priority.","Tamoxifen; liver || Not the priority."],
 "Also watch for infusion reactions.")
q("target","How does targeted therapy differ from traditional chemotherapy?",
 ["*It attacks a specific molecule on cancer cells, with less harm to normal cells","It kills all rapidly dividing cells equally || That's traditional chemo.","It's a vaccine || Vaccines are excluded.","It's an antibiotic || Not an antibiotic."],
 "Examples: trastuzumab (HER2) and imatinib (abnormal tyrosine kinase).")
q("target","A client receiving interferon alfa should be monitored for which effects? "+SATA,
 ["*Flu-like symptoms","*Mood changes","*Bone marrow suppression","*Liver dysfunction","Hemorrhagic cystitis || Cyclophosphamide."],
 "Interferon alfa is a biologic response modifier.")

# ---------- HIV goals ----------
q("hivgoal","Why is HIV treated with combination antiretroviral therapy (cART)?",
 ["*Using 2 or more drugs reduces the chance of resistance","It cures HIV in 2 weeks || There's no cure.","It lets clients skip doses || Doses must not be skipped.","It replaces CD4 cells || It protects them by suppressing the virus."],
 "Drugs block different steps of the viral life cycle.")
q("hivgoal","Which results show HIV therapy is working? "+SATA,
 ["*Viral load decreasing, ideally undetectable","*CD4 count increasing","Viral load rising || Treatment failure.","CD4 count falling || Weaker immune system."],
 "Adherence → lower viral load, higher CD4, less resistance.")
q("hivgoal","A client on HIV medications says they skip doses on weekends. What should the nurse teach?",
 ["*Missed doses let the virus mutate and become drug-resistant","Weekend breaks are fine || They promote resistance.","Double up on Monday || Not the fix.","Skipping only affects side effects || It affects viral control."],
 "Take antiretrovirals exactly as prescribed.")
q("hivgoal","What is the order of steps in the HIV life cycle that drugs target?",
 ["*Entry → reverse transcription → integration → protease maturation","Protease → entry → integration → reverse transcription || Wrong order.","Integration → entry → protease → reverse transcription || Wrong order.","Reverse transcription → protease → entry → integration || Wrong order."],
 "Entry/fusion inhibitors, RTIs, integrase inhibitors, protease inhibitors.")

# ---------- entry ----------
q("entry","Which HIV drug is given by subcutaneous injection and causes injection-site reactions?",
 ["*Enfuvirtide","Maraviroc || Oral CCR5 antagonist.","Zidovudine || NRTI.","Ritonavir || Protease inhibitor."],
 "Enfuvirtide is an entry/fusion inhibitor; teach injection technique.")
q("entry","Before maraviroc is started, what must be confirmed?",
 ["*The client's HIV is CCR5-tropic","The client's CD4 is over 1,000 || Not the requirement.","The client has hepatitis || Not the requirement.","The client has no rash || Not the requirement."],
 "Maraviroc blocks CCR5 co-receptors; monitor for liver injury.")
q("entry","How do entry and fusion inhibitors work?",
 ["*They keep HIV from attaching to and entering the CD4 cell","They block viral protein maturation || Protease inhibitors.","They block integration into host DNA || Integrase inhibitors.","They block reverse transcriptase || RTIs."],
 "First step in the life cycle.")

# ---------- RTIs ----------
q("rti","A client on zidovudine should have which lab monitored closely?",
 ["*CBC for anemia and neutropenia","Creatine kinase || Raltegravir.","Lipids only || Ritonavir.","Urine for blood || Cyclophosphamide."],
 "Zidovudine (NRTI) causes severe bone marrow suppression.")
q("rti","Which adverse effects are linked to delavirdine (NNRTI)? "+SATA,
 ["*Rash","*Liver toxicity","Bone marrow suppression || Zidovudine.","Muscle injury || Raltegravir."],
 "Severe rash needs prompt evaluation.")
q("rti","What do reverse transcriptase inhibitors block?",
 ["*Conversion of viral RNA into DNA","Viral entry into the cell || Entry inhibitors.","Insertion of viral DNA into host DNA || Integrase inhibitors.","Maturation of new virus particles || Protease inhibitors."],
 "Two types: nucleoside RTIs like zidovudine and non-nucleoside RTIs like delavirdine.")

# ---------- PI / integrase ----------
q("pi","A client on ritonavir takes several other medications. What is the priority teaching?",
 ["*Ritonavir has many drug interactions; review all prescriptions, OTC drugs and supplements","It has no interactions || It has many.","Take it only when ill || Take as prescribed.","Stop other meds without telling the provider || Unsafe."],
 "Ritonavir (protease inhibitor) also boosts other antiretrovirals.")
q("pi","Which effects are associated with ritonavir? "+SATA,
 ["*Many drug interactions","*GI effects such as nausea and diarrhea","*High blood glucose and lipid changes","*Fat redistribution","Severe rash as its signature effect || Delavirdine."],
 "Monitor glucose and lipids.")
q("pi","A client on raltegravir reports muscle pain and weakness. Which lab does the nurse expect?",
 ["*Creatine kinase (CK)","Hearing test || Cisplatin.","INR || Not related.","Urinalysis for blood || Cyclophosphamide."],
 "Raltegravir (integrase inhibitor) can cause muscle injury.")
q("pi","How does raltegravir work?",
 ["*It prevents viral DNA from being inserted into the host's DNA","It blocks protease so new virus can't mature || Protease inhibitors.","It blocks viral entry || Entry inhibitors.","It blocks estrogen || Not an HIV drug."],
 "Integrase inhibitors; reinforce consistent dosing.")
q("pi","Match each HIV drug with its signature effect. "+SATA,
 ["*Zidovudine — bone marrow suppression","*Delavirdine — rash","*Raltegravir — muscle injury (high CK)","*Enfuvirtide — injection-site reactions","Ritonavir — no interactions || Ritonavir has many interactions."],
 "Know the signature adverse effect of each.")

# ================= ATI Pharmacology Made Easy supplement (PowerPoint stays the main source) =================
q("nadir","Which teaching applies to a client with chemotherapy-induced neutropenia? "+SATA,
 ["*Use scrupulous handwashing and avoid people who are ill","*Wash fresh fruits and vegetables well and cook foods properly","*Report fever, sore throat or unusual fatigue","*Frequent oral care to prevent stomatitis","Take rectal temperatures daily || Not part of the teaching."],
 "ATI repeats this teaching for nearly every chemo drug.")
q("nadir","A client with thrombocytopenia after chemotherapy needs an injection. Which actions reduce bleeding? "+SATA,
 ["*Use a small-gauge needle","*Apply prolonged pressure to the puncture site","*Teach use of a soft toothbrush and electric razor","Massage the site vigorously || Increases bruising."],
 "Watch for bleeding from the gums and GI tract (melena).")
q("nadir","Why might an infected wound in a leukopenic client on cyclophosphamide NOT contain pus?",
 ["*There are too few white cells to form pus","The wound is healing normally || Infection can be hidden.","Cyclophosphamide sterilizes wounds || Not true.","Pus only forms with fever || Not the reason."],
 "Fever may also be a late sign in leukopenia, so monitor closely.")
q("antimet","A client on high-dose methotrexate develops severe bone marrow depression. Which antidote does the nurse expect?",
 ["*Leucovorin","Mesna || Protects the bladder from cyclophosphamide.","Protamine || Reverses heparin.","Vitamin K || Reverses warfarin."],
 "Leucovorin is a reduced form of folic acid.")
q("antimet","Which instructions are correct for a client on methotrexate? "+SATA,
 ["*Avoid alcohol","*Report yellowing of the skin or eyes","*Report shortness of breath","*Use contraception during and after therapy","Take extra folic acid on your own || Folic acid changes the response to methotrexate."],
 "Methotrexate can cause liver damage and pulmonary fibrosis; NSAIDs and salicylates can cause toxicity.")
q("antimet","A client takes allopurinol for gout and is starting mercaptopurine. What is the concern?",
 ["*Allopurinol can cause mercaptopurine toxicity, so the dose is reduced","No interaction || There is one.","Allopurinol makes mercaptopurine ineffective || It raises levels.","It causes hemorrhagic cystitis || Cyclophosphamide."],
 "Mercaptopurine is oral only; watch bilirubin and transaminases.")
q("antimet","Which medication is given with intrathecal cytarabine?",
 ["*Dexamethasone","Mesna || With cyclophosphamide.","Leucovorin || With high-dose methotrexate.","Hyaluronidase || For vincristine extravasation."],
 "Intrathecal cytarabine can cause arachnoiditis: nausea, vomiting, headache, fever.")
q("alkyl","Besides hemorrhagic cystitis, which effects are listed for cyclophosphamide? "+SATA,
 ["*Alopecia","*Severe nausea and vomiting","*Leukopenia","*Hyperkalemia and hyponatremia","Bradycardia during infusion || Paclitaxel."],
 "Tell clients early about hair loss; it grows back.")
q("alkyl","Which instruction helps protect the bladder during cyclophosphamide?",
 ["*Void before the dose and increase fluid intake","Hold urine as long as possible || Increases bladder contact.","Restrict fluids to 1 L || Opposite.","Take with a diuretic only || Not the teaching."],
 "Report blood in the urine or pain with voiding; mesna is given with each dose.")
q("alkyl","When is the critical time for low counts after IV carmustine?",
 ["*4–6 weeks after each treatment","Day 1 || Too early.","10–14 days || That's most chemo, not carmustine.","After 1 year || Too late."],
 "Carmustine has a delayed nadir; it can also cause irreversible pulmonary fibrosis.")
q("alkyl","A client on carmustine reports a new cough and shortness of breath. Why is this a concern?",
 ["*Carmustine can cause pulmonary fibrosis","It's expected nausea || Not related.","It's hemorrhagic cystitis || Not related.","It's a sign of hair loss || Not related."],
 "Listen to breath sounds and monitor pulmonary function tests.")
q("vesicant","Why should a vesicant such as doxorubicin or carmustine NOT be given in a vein near the wrist or antecubital space?",
 ["*Extravasation near joints can cause necrosis, tendon or nerve injury","The drug won't absorb there || Not the reason.","It causes bradycardia || Not the reason.","It's too painful only || Damage is the concern."],
 "Use a central line when possible.")
q("vesicant","Vincristine infiltrates. Which antidote and site care does ATI list?",
 ["*Warm compress (heat) and local hyaluronidase injection","Cold compress and sodium bicarbonate || That's carmustine.","Leucovorin || Methotrexate antidote.","Mesna || Bladder protection."],
 "Treatments are drug-specific: carmustine uses bicarbonate and cold; vincristine uses heat and hyaluronidase.")
q("cis","When does severe nausea and vomiting usually start with cisplatin, and how is it prevented?",
 ["*About 1 hour after the infusion starts; premedicate with an antiemetic 30 minutes before","Only 1 week later || Starts within about an hour.","It never causes nausea || It's severe.","Only if the client eats || Not the trigger."],
 "Take antiemetics for several days after treatment.")
q("cis","Which client should NOT receive cisplatin?",
 ["*A client also taking a loop diuretic like furosemide","A client with normal hearing || Hearing is assessed, not a reason to withhold.","A client who weighs 70 kg || Weight guides dosing.","A client with testicular cancer || An indication."],
 "Other ototoxic drugs (furosemide) raise the risk of permanent hearing loss.")
q("cis","Which preparation detail is specific to platinum compounds?",
 ["*Don't use equipment containing aluminum","Mix with dextrose only || Not the rule.","Give IM || IV only.","Protect from light in a lead bag || Not the rule."],
 "Also have epinephrine ready for anaphylaxis to platinum.")
q("cis","When is the critical time for low counts after cisplatin?",
 ["*Days 18–23","Days 1–2 || Too early.","Weeks 4–6 || Carmustine.","Days 10–14 || Doxorubicin."],
 "Monitor CBC before each treatment and weekly after.")
q("doxo","A client on doxorubicin is told what to expect. Which statements are correct? "+SATA,
 ["*Complete hair loss that's reversible","*Red urine for up to 2 days","*Report palpitations, shortness of breath or chest pain","*Heart damage can show up months or years later","Hair loss is permanent || It's reversible."],
 "Dexrazoxane or an ACE inhibitor may be ordered to protect the heart.")
q("doxo","Which client should NOT receive doxorubicin?",
 ["*A client with existing cardiac disorders","A client with bladder cancer || An indication.","A client with breast cancer || An indication.","A client with lymphoma || An indication."],
 "Also contraindicated in existing marrow suppression and after a prior full course of doxorubicin.")
q("antimit","Which assessment detects vincristine or paclitaxel neuropathy?",
 ["*Check deep tendon reflexes, especially the Achilles reflex, and hand/foot strength","Check hearing || Cisplatin.","Check urine for blood || Cyclophosphamide.","Check the Amsler grid || Eyes."],
 "The dose may be decreased if neuropathy develops.")
q("antimit","Which premedication is given before the solvent form of paclitaxel?",
 ["*An antihistamine, a corticosteroid and an H2 blocker 30 minutes before","Mesna || Not for paclitaxel.","Leucovorin || Not for paclitaxel.","Atropine || Not the premedication."],
 "This prevents allergic reactions; it's infused over 3 hours with an in-line filter.")
q("antimit","Vincristine is contraindicated in a client with:",
 ["*Intestinal ileus","Leukemia || An indication.","Breast cancer || An indication.","Normal bowel function || Not a contraindication."],
 "It causes severe constipation and impaction; monitor bowel sounds.")
q("topo","When should filgrastim be given in relation to topotecan?",
 ["*24 hours after the topotecan infusion is complete","At the same time || Worsens marrow suppression.","1 hour before || Not the timing.","Never || It may be prescribed."],
 "Topotecan's neutropenia nadir is about day 12.")
q("horm","Which effects should a client on tamoxifen report? "+SATA,
 ["*Blurred vision","*Abnormal menstrual or vaginal bleeding","*Leg pain or swelling","*Sudden chest pain or one-sided weakness","Hair growth || Not listed."],
 "Tamoxifen raises the risk of uterine cancer, clots and retinopathy/cataracts; regular eye exams.")
q("horm","Which teaching applies to anastrozole? "+SATA,
 ["*Increase calcium and vitamin D","*Do weight-bearing exercise","*Take on an empty stomach at the same time daily","*Take acetaminophen for muscle pain if approved","Take with estrogen for hot flashes || Don't take estrogen."],
 "Only for postmenopausal clients; a bisphosphonate may be prescribed for fracture risk.")
q("horm","How long should flutamide be monitored for liver function at first?",
 ["*Monthly for the first few months","Never || Liver monitoring is key.","Only after 5 years || Too late.","Only if pregnant || Not applicable."],
 "Flutamide begins when the GnRH drug starts and may raise INR with warfarin.")
q("horm","Which teaching applies to leuprolide? "+SATA,
 ["*Do weight-bearing exercise daily","*Get enough calcium and vitamin D","*Report headache, dizziness or numbness","It's taken orally once a day || It's given SQ or IM."],
 "Bone loss is a major adverse effect; monitor bone density.")
q("target","What should the nurse do if a client has wheezing and hypotension during the first trastuzumab infusion?",
 ["*Stop the infusion and prepare epinephrine as prescribed","Speed up the infusion || Worsens the reaction.","Give it with dextrose || Don't mix with dextrose.","Ignore it; it's expected || It's an allergic reaction."],
 "Allergic reactions usually occur with the first dose or within 12 hours.")
q("target","Trastuzumab should not be given at the same time as which drug?",
 ["*Doxorubicin (an anthracycline)","Acetaminophen || Not contraindicated.","Filgrastim || Not listed.","Ondansetron || Not listed."],
 "Combined cardiotoxicity.")
q("target","Which instructions apply to imatinib? "+SATA,
 ["*Take with a meal and at least 8 oz of water","*Avoid grapefruit juice","*Report sudden weight gain, swelling or shortness of breath","Take on an empty stomach || Take with a meal."],
 "Imatinib causes fluid retention that can lead to pulmonary edema.")
q("target","A client on interferon alfa asks how to manage flu-like symptoms. What does the nurse suggest, if the provider approves?",
 ["*Premedicate with acetaminophen","Take aspirin and ibuprofen together || Not the teaching.","Stop the drug when feverish || Don't stop on your own.","Drink less fluid || Stay well hydrated."],
 "Interferon is dosed in million units (MU), not mg or mL. Watch for depression.")
q("entry","Which instructions apply to enfuvirtide? "+SATA,
 ["*Rotate injection sites (thigh, upper arm, abdomen)","*Avoid discolored or scarred skin","*Report cough, fever or shortness of breath","Give it as a deep IM injection || It's subcutaneous only."],
 "It can cause pneumonia; it's given twice a day.")
q("entry","A client on maraviroc develops an itchy rash. Why is this important?",
 ["*Allergic signs like rash often come before liver damage","Rash is always harmless || Can precede liver damage.","It means the virus is gone || Not the meaning.","It's injection-site irritation || Maraviroc is oral."],
 "Also report abdominal pain and jaundice; maraviroc has many interactions.")
q("rti","When do anemia and neutropenia typically appear on zidovudine?",
 ["*Anemia in 2–4 weeks; neutropenia after about 6 weeks","Within 24 hours || Too early.","Only after 1 year || Too late.","Never || Marrow suppression is the key effect."],
 "Monitor Hgb and neutrophils monthly; epoetin alfa or filgrastim may be given.")
q("rti","Zidovudine is also used for which purpose?",
 ["*Preventing maternal HIV transmission to the fetus","Treating hepatitis C || Interferon.","Preventing ileus || Not related.","Treating breast cancer || Not related."],
 "In pregnancy, oral doses start at 14 weeks, with IV during delivery.")
q("rti","A client on delavirdine develops a rash with fever and mouth lesions. What is the priority?",
 ["*Report it; the drug may need to be stopped (risk of Stevens-Johnson syndrome)","Apply lotion and continue || Could be life-threatening.","Double the dose || Not appropriate.","It's expected; ignore it || Not with fever and lesions."],
 "Don't take delavirdine with antacids.")
q("pi","Which findings show fat redistribution from ritonavir? "+SATA,
 ["*Thin arms, legs and face","*Increased abdominal fat","*Fat between the shoulder blades ('buffalo hump')","Weight loss everywhere || Not redistribution."],
 "Ritonavir also raises glucose and lipids and lowers bone density.")
q("pi","Which drugs are contraindicated with protease inhibitors like ritonavir? "+SATA,
 ["*Simvastatin and lovastatin","*Midazolam and alprazolam","*St. John's wort","Acetaminophen || Not listed."],
 "PDE-5 inhibitors like sildenafil are given in reduced doses; ritonavir lowers oral contraceptive levels.")
q("pi","How should ritonavir be taken?",
 ["*Twice daily with food or a snack","On an empty stomach || Food improves absorption.","Once a week || Twice daily.","Only when the viral load rises || Take as prescribed."],
 "Food also reduces GI effects and altered taste.")
q("pi","Which adverse effects does ATI list for raltegravir? "+SATA,
 ["*Nausea, vomiting and diarrhea","*Dizziness and headache","Hemorrhagic cystitis || Cyclophosphamide.","Red urine || Doxorubicin."],
 "The lecture slide also flags muscle injury (high CK). Avoid driving until effects are known.")
