"""Display formatting applied to every question when questions.js is generated:
 - medications: generic name with the brand in parentheses, e.g. furosemide (Lasix)
 - medical abbreviations: spelled out in parentheses at their first use in each question, e.g. NPO (nothing by mouth)
First use is counted across the question in reading order: stem, options, rationale, wrong-answer notes."""
import re

DRUGS = {  # generic -> brand
 "furosemide":"Lasix","bumetanide":"Bumex","torsemide":"Demadex","spironolactone":"Aldactone","eplerenone":"Inspra",
 "lisinopril":"Zestril","enalapril":"Vasotec","captopril":"Capoten","losartan":"Cozaar","candesartan":"Atacand","valsartan":"Diovan",
 "sacubitril/valsartan":"Entresto","carvedilol":"Coreg","metoprolol succinate":"Toprol-XL","bisoprolol":"Zebeta","propranolol":"Inderal",
 "empagliflozin":"Jardiance","dapagliflozin":"Farxiga","canagliflozin":"Invokana","ertugliflozin":"Steglatro",
 "digoxin immune Fab":"DigiFab","digoxin":"Lanoxin","isosorbide dinitrate":"Isordil","hydralazine":"Apresoline","nitroglycerin":"Nitrostat",
 "dobutamine":"Dobutrex","milrinone":"Primacor","sildenafil":"Viagra","tadalafil":"Cialis",
 "ibuprofen":"Advil, Motrin","naproxen":"Aleve","acetaminophen":"Tylenol","warfarin":"Coumadin",
 "baclofen":"Lioresal","dantrolene":"Dantrium","phenytoin":"Dilantin","carbamazepine":"Tegretol","valproic acid":"Depakene",
 "oxcarbazepine":"Trileptal","topiramate":"Topamax","phenobarbital":"Luminal","lidocaine":"Xylocaine","methohexital":"Brevital",
 "midazolam":"Versed","fentanyl":"Sublimaze","naloxone":"Narcan","flumazenil":"Romazicon","methylphenidate":"Ritalin",
 "amphetamine/dextroamphetamine":"Adderall","modafinil":"Provigil","levodopa/carbidopa":"Sinemet","pramipexole":"Mirapex",
 "ropinirole":"Requip","selegiline":"Eldepryl","entacapone":"Comtan","amantadine":"Symmetrel","quetiapine":"Seroquel",
 "donepezil":"Aricept","memantine":"Namenda","interferon beta-1a":"Avonex","interferon beta-1b":"Betaseron",
 "sumatriptan":"Imitrex","meperidine":"Demerol","phenelzine":"Nardil","amitriptyline":"Elavil",
 "cimetidine":"Tagamet","famotidine":"Pepcid","pantoprazole":"Protonix","omeprazole":"Prilosec","sucralfate":"Carafate",
 "metoclopramide":"Reglan","aluminum hydroxide":"Amphojel","ceftriaxone":"Rocephin","metronidazole":"Flagyl","psyllium":"Metamucil",
 "pancrelipase":"Creon",
 "semaglutide":"Ozempic, Wegovy","liraglutide":"Victoza, Saxenda","tirzepatide":"Mounjaro, Zepbound","metformin":"Glucophage",
 "atorvastatin":"Lipitor","glipizide":"Glucotrol","repaglinide":"Prandin","pioglitazone":"Actos","acarbose":"Precose",
 "miglitol":"Glyset","sitagliptin":"Januvia","pramlintide":"Symlin","insulin lispro":"Humalog","lispro":"Humalog",
 "insulin aspart":"NovoLog","aspart":"NovoLog","glulisine":"Apidra","glargine":"Lantus","detemir":"Levemir","degludec":"Tresiba",
 "albuterol":"ProAir","amlodipine":"Norvasc","prednisone":"Deltasone","tranexamic acid":"Cyklokapron","desmopressin":"DDAVP","epinephrine":"EpiPen",
}
# brand written alone (no generic) -> generic to put in front
BRAND_ONLY = {"Entresto":"sacubitril/valsartan","Jardiance":"empagliflozin","Farxiga":"dapagliflozin","Ozempic":"semaglutide",
 "Creon":"pancrelipase","Januvia":"sitagliptin","Symlin":"pramlintide","Lasix":"furosemide","Mylanta":"aluminum/magnesium hydroxide",
 "Tums":"calcium carbonate","DigiFab":"digoxin immune Fab","Humalog":"insulin lispro","Lantus":"insulin glargine"}

ABBR = {
 "IV":"intravenous","IM":"intramuscular","SC":"subcutaneous","SUBQ":"subcutaneous","SubQ":"subcutaneous","PO":"by mouth","PRN":"as needed",
 "OTC":"over-the-counter","ODT":"orally disintegrating tablet","NPO":"nothing by mouth","NG":"nasogastric","HOB":"head of bed",
 "I&O":"intake and output","VS":"vital signs","BP":"blood pressure","SBP":"systolic blood pressure","DBP":"diastolic blood pressure",
 "HR":"heart rate","RR":"respiratory rate","SpO2":"oxygen saturation","SOB":"shortness of breath","LOC":"level of consciousness",
 "CNS":"central nervous system","PNS":"peripheral nervous system","GI":"gastrointestinal","ECG":"electrocardiogram","CT":"computed tomography",
 "MRI":"magnetic resonance imaging","PET":"positron emission tomography","BiPAP":"bilevel positive airway pressure","CPR":"cardiopulmonary resuscitation",
 "NCLEX":"National Council Licensure Examination","ATI":"Assessment Technologies Institute","ADA":"American Diabetes Association",
 "HF":"heart failure","HFrEF":"heart failure with reduced ejection fraction","HFpEF":"heart failure with preserved ejection fraction",
 "EF":"ejection fraction","CO":"cardiac output","CO2":"carbon dioxide","SV":"stroke volume","BNP":"B-type natriuretic peptide",
 "TEE":"transesophageal echocardiogram","JVD":"jugular vein distension","CVP":"central venous pressure","MAP":"mean arterial pressure",
 "MI":"myocardial infarction","CAD":"coronary artery disease","COPD":"chronic obstructive pulmonary disease","HTN":"hypertension",
 "DVT":"deep vein thrombosis","PE":"pulmonary embolism","NYHA":"New York Heart Association","RAAS":"renin-angiotensin-aldosterone system",
 "SNS":"sympathetic nervous system","DCM":"dilated cardiomyopathy","HCM":"hypertrophic cardiomyopathy","RCM":"restrictive cardiomyopathy",
 "ICD":"implantable cardioverter-defibrillator","LVAD":"left ventricular assist device","VAD":"ventricular assist device","LV":"left ventricle",
 "VT":"ventricular tachycardia","VF":"ventricular fibrillation","PND":"paroxysmal nocturnal dyspnea","PDE-5":"phosphodiesterase-5",
 "ACE":"angiotensin-converting enzyme","ARB":"angiotensin II receptor blocker","ARBs":"angiotensin II receptor blockers",
 "ARNI":"angiotensin receptor–neprilysin inhibitor","SGLT2":"sodium-glucose cotransporter-2","SGLT2s":"sodium-glucose cotransporter-2 inhibitors",
 "NSAID":"nonsteroidal anti-inflammatory drug","NSAIDs":"nonsteroidal anti-inflammatory drugs","K+":"potassium","K⁺":"potassium",
 "Na+":"sodium","Na⁺":"sodium","WBC":"white blood cell count","RBC":"red blood cell","CBC":"complete blood count","BUN":"blood urea nitrogen",
 "LFTs":"liver function tests","TSH":"thyroid-stimulating hormone","ABG":"arterial blood gas","ABGs":"arterial blood gases",
 "AST":"aspartate aminotransferase","ALT":"alanine aminotransferase","ALP":"alkaline phosphatase","CRP":"C-reactive protein",
 "CEA":"carcinoembryonic antigen","CA 19-9":"cancer antigen 19-9","PSA":"prostate-specific antigen","MCV":"mean corpuscular volume",
 "AKI":"acute kidney injury","CKD":"chronic kidney disease","DIC":"disseminated intravascular coagulation","UTI":"urinary tract infection",
 "UTIs":"urinary tract infections","CMV":"cytomegalovirus","TIA":"transient ischemic attack","SIRS":"systemic inflammatory response syndrome",
 "GABA":"gamma-aminobutyric acid","NMDA":"N-methyl-D-aspartate","MAO-B":"monoamine oxidase type B","MAO":"monoamine oxidase",
 "MAOI":"monoamine oxidase inhibitor","MAOIs":"monoamine oxidase inhibitors","SSRI":"selective serotonin reuptake inhibitor",
 "SSRIs":"selective serotonin reuptake inhibitors","TCAs":"tricyclic antidepressants","COMT":"catechol-O-methyltransferase",
 "BBB":"blood-brain barrier","ASM":"antiseizure medication","SJS":"Stevens-Johnson syndrome","HLA":"human leukocyte antigen",
 "ADHD":"attention-deficit/hyperactivity disorder","MS":"multiple sclerosis","RLS":"restless legs syndrome","CN":"cranial nerve",
 "GERD":"gastroesophageal reflux disease","GE":"gastroesophageal","LES":"lower esophageal sphincter","PUD":"peptic ulcer disease",
 "H2":"histamine-2","PPI":"proton pump inhibitor","PPIs":"proton pump inhibitors","TPN":"total parenteral nutrition",
 "PPN":"peripheral parenteral nutrition","RUQ":"right upper quadrant","RLQ":"right lower quadrant","LLQ":"left lower quadrant",
 "IBD":"inflammatory bowel disease","HIDA":"hepatobiliary iminodiacetic acid","ERCP":"endoscopic retrograde cholangiopancreatography",
 "MRCP":"magnetic resonance cholangiopancreatography","PERT":"pancreatic enzyme replacement therapy","CHG":"chlorhexidine gluconate",
 "H&H":"hemoglobin and hematocrit","BMI":"body mass index","HDL":"high-density lipoprotein","LDL":"low-density lipoprotein",
 "HLD":"hyperlipidemia","OSA":"obstructive sleep apnea","PCOS":"polycystic ovary syndrome","DASH":"Dietary Approaches to Stop Hypertension",
 "A1C":"hemoglobin A1C","OGTT":"oral glucose tolerance test","MODY":"maturity-onset diabetes of the young","T2DM":"type 2 diabetes mellitus",
 "DKA":"diabetic ketoacidosis","HHS":"hyperosmolar hyperglycemic state","CGM":"continuous glucose monitor","GLP-1":"glucagon-like peptide-1",
 "DPP-4":"dipeptidyl peptidase-4","NPH":"neutral protamine Hagedorn","TZD":"thiazolidinedione","TZDs":"thiazolidinediones",
 "AGI":"alpha-glucosidase inhibitor","AGIs":"alpha-glucosidase inhibitors","CV":"cardiovascular","CHF":"congestive heart failure",
 "PRBCs":"packed red blood cells","PRBC":"packed red blood cell","RBCs":"red blood cells","WBCs":"white blood cells","FFP":"fresh frozen plasma","TRALI":"transfusion-related acute lung injury","TACO":"transfusion-associated circulatory overload","ITP":"immune thrombocytopenia","IgA":"immunoglobulin A","PT/INR":"prothrombin time/international normalized ratio","aPTT":"activated partial thromboplastin time","Hgb":"hemoglobin","Hct":"hematocrit","LR":"lactated Ringer's","NS":"normal saline","EPO":"erythropoietin","ICU":"intensive care unit", "RRT":"Rapid Response Team","ERT":"Emergency Response Team","SBAR":"Situation, Background, Assessment, Recommendation","ROSC":"return of spontaneous circulation","BLS":"Basic Life Support","ACLS":"Advanced Cardiovascular Life Support","AED":"automated external defibrillator","AHA":"American Heart Association","ED":"emergency department","ER":"emergency room","NP":"nurse practitioner","PA":"physician assistant","MD":"physician","PCTs":"patient care technicians","ABCs":"airway, breathing, circulation","IO":"intraosseous","RT":"respiratory therapist", "O2":"oxygen","SCDs":"sequential compression devices","D50":"50% dextrose","D10":"10% dextrose","D5":"5% dextrose","D5W":"5% dextrose in water","A-fib":"atrial fibrillation","VTE":"venous thromboembolism","GIP":"glucose-dependent insulinotropic polypeptide","RN":"registered nurse","TBSA":"total body surface area","SMBG":"self-monitoring of blood glucose",
}
_GEN = {k.lower(): (k, v) for k, v in DRUGS.items()}
_keys = sorted(list(DRUGS) + list(BRAND_ONLY) + list(ABBR), key=len, reverse=True)
_parts = []
for k in _keys:
    esc = re.escape(k)
    left = r"(?<![\w/-])" ; right = r"(?![\w/-])" if k[-1].isalnum() else ""
    if k in DRUGS: _parts.append(f"(?i:{left}{esc}{right})")
    else:
        r2 = r"(?![\w-])" if k[-1].isalnum() else ""
        _parts.append(r"(?<![\w-])" + esc + r2)
_RX = re.compile("|".join(_parts))

def format_question(texts):
    """texts: list of strings in reading order. Returns formatted list."""
    whole = " ".join(texts)
    seen = set()
    out = []
    for t in texts:
        def sub(m, t=t):
            word = m.group(0); rest = t[m.end():]; pre = t[:m.start()]
            paren = re.match(r" ?\(([^)]*)\)", rest); paren = paren.group(1).lower() if paren else ""
            low = word.lower()
            if low in _GEN:
                key, brand = _GEN[low]
                if key in seen: return word
                seen.add(key)
                first_brand = brand.split(",")[0].strip().lower()
                if first_brand in paren or first_brand in whole.lower(): return word
                return f"{word} ({brand})"
            if word in BRAND_ONLY:
                gen = BRAND_ONLY[word]
                if word in seen: return word
                seen.add(word); seen.add(gen)
                if gen.lower() in whole.lower(): return word
                return f"{gen} ({word})"
            if word in ABBR:
                if word in seen: return word
                seen.add(word)
                exp = ABBR[word].lower()
                if exp in paren or (pre.endswith("(") and exp in pre.lower()): return word
                return f"{word} ({ABBR[word]})"
            return word
        out.append(_RX.sub(sub, t))
    return out
