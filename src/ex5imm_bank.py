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
