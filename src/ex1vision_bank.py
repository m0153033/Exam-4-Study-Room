# Week 1.1 Visual Variations Across the Lifespan — lecture, PowerPoint, notes, lesson plan, mind map.
EXAM = "e1"
T = "vision"
CONCEPTS = {
 "sensory":"Sensory deficit vs deprivation vs overload",
 "history":"Ocular history & nursing role",
 "external":"External eye findings",
 "acuity":"Visual acuity testing",
 "color":"Color vision testing",
 "amsler":"Amsler grid",
 "scopes":"Ophthalmoscopy & slit lamp",
 "tono":"Tonometry",
 "cataract":"Cataract findings & risks",
 "catcare":"Cataract surgery nursing care",
 "blind":"Legal blindness & coping",
 "blindcare":"Communicating with & guiding a blind client",
 "glauc":"Open-angle vs angle-closure glaucoma",
 "glaucare":"Glaucoma nursing care & iridotomy",
 "glaumed":"Glaucoma medications",
 "drops":"Giving eye drops",
 "md":"Macular degeneration",
 "mdtypes":"Dry vs wet macular degeneration",
 "conj":"Conjunctivitis types",
 "conjteach":"Conjunctivitis care & teaching",
 "promo":"Health promotion across the lifespan",
}
HI = ["glauc","glaucare","cataract","catcare","drops","md","conj","blindcare"]

SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

# ---------- sensory perception ----------
q("sensory","A client with low vision who needs glasses has which level of sensory alteration?",
 ["*Sensory deficit","Sensory deprivation || Deprivation means the sense is absent, as in blindness.","Sensory overload || Overload is too much input to process.","Sensory perception || That's the normal ability to interpret input, not an alteration."],
 "Deficit = part of a sense is impaired (low vision). Deprivation = a sense is absent (blindness). Overload = can't process excess stimuli.")
q("sensory","An ICU client exposed to constant alarms, bright lights and noise becomes confused and can't process what is happening. This is:",
 ["*Sensory overload","Sensory deficit || A deficit is impaired sensing, not too much input.","Sensory deprivation || Deprivation is too little or absent input.","Legal blindness || Unrelated to sensory input level."],
 "Sensory overload is the inability to process excessive or multiple stimuli; it's sometimes called ICU psychosis.")
q("sensory","Total blindness is an example of:",
 ["*Sensory deprivation","Sensory deficit || A deficit is partial loss, like low vision.","Sensory overload || Overload is too much stimulation.","Presbyopia || That's age-related near-vision loss."],
 "Deprivation = absence of visual sensory stimulation.")
q("sensory","Which related concepts does the lecture link to visual variations? "+SATA,
 ["*Safety","*Mobility","*Infection","Nutrition only || Nutrition is discussed under health promotion but isn't one of the three related concepts.","Elimination || Not a listed related concept."],
 "Vision loss raises fall/hazard risk (safety), may need help moving (mobility), and some infections cause visual problems (infection).")

# ---------- history & nursing role ----------
q("history","Which clients should the nurse identify as at risk for vision problems and refer to an eye-care specialist? "+SATA,
 ["*A client with long-standing hypertension","*A client with diabetes","A healthy 25-year-old with no symptoms || No listed risk factor.","A client with a sprained ankle || Not an eye risk."],
 "The nursing role includes identifying at-risk clients, such as those with hypertension or diabetes, and referring them.")
q("history","A client reports eye pain. Which follow-up questions belong in the ocular history? "+SATA,
 ["*Is the pain sharp or dull, and is it worse with blinking?","*Are both eyes affected?","*Is there discharge, and what color, consistency and odor?","*Has a family member had the same symptoms?","What is your favorite color? || Not part of the ocular history."],
 "The ocular history covers the client's view of the problem, acuity changes, pain, both eyes, discharge, onset, self-treatment, ADLs, other conditions, eye surgery and family members.")
q("history","Which is one of the four parts of the nurse's overall role with visual variations?",
 ["*Help clients adapt to impaired vision","Perform laser iridotomy || A provider procedure.","Prescribe glasses || Done by an eye-care provider.","Give intravitreal injections || A provider procedure."],
 "Nursing role: obtain an ocular history, identify at-risk clients and refer, prevent further vision loss, and help clients adapt.")

# ---------- external eye ----------
q("external","An older adult's lower eyelid turns outward. The nurse documents:",
 ["*Ectropion","Ptosis || Ptosis is a drooping upper eyelid.","Trichiasis || Trichiasis is eyelashes turning inward.","Nystagmus || Nystagmus is rhythmic eye movement."],
 "Ectropion = lower lid turns outward; more common in older adults as muscles weaken (about 2%).")
q("external","Which finding describes trichiasis?",
 ["*Eyelashes turn inward toward the eye","Drooping of the upper eyelid || That's ptosis.","Lower lid turns outward || That's ectropion.","Involuntary rhythmic eye movement || That's nystagmus."],
 "Trichiasis = lashes turn inward.")
q("external","Involuntary, rhythmic oscillation of the eyeballs is called:",
 ["*Nystagmus","Ptosis || Upper lid droop.","Ectropion || Lower lid outward.","Diplopia || Double vision."],
 "Nystagmus = involuntary rhythmic oscillation of the eyes.")
q("external","A drooping upper eyelid in a child or adult is documented as:",
 ["*Ptosis","Trichiasis || Inward lashes.","Ectropion || Outward lower lid.","Presbyopia || Loss of lens elasticity."],
 "Ptosis = drooping of the upper eyelid.")

# ---------- acuity ----------
q("acuity","At what distances does the nurse test near and distance vision?",
 ["*Near at 14 inches; distance at 20 feet with a Snellen chart","Near at 20 inches; distance at 14 feet || The numbers are reversed.","Both at 10 feet || Not the lecture distances.","Near at 6 inches; distance at 40 feet || Not the lecture distances."],
 "Near vision = 14 inches. Distance = 20 feet with a standardized Snellen chart. Test each eye separately.")
q("acuity","Visual acuity testing assesses which cranial nerve?",
 ["*Cranial nerve II (optic)","Cranial nerve III (oculomotor) || Controls most eye movement and pupil size.","Cranial nerve V (trigeminal) || Facial sensation and chewing.","Cranial nerve VII (facial) || Facial expression."],
 "Visual acuity evaluates cranial nerve II, the optic nerve.")
q("acuity","A client can't read English. How should the nurse test visual acuity?",
 ["*Use a chart with pictures or numbers","Skip the test || Acuity still needs to be assessed.","Have a family member read for the client || That doesn't test the client's vision.","Test both eyes together only || Each eye is tested separately."],
 "Use pictures or numbers if the client is illiterate or can't read English, and test each eye separately.")

# ---------- color ----------
q("color","Which test screens for color-vision deficiency?",
 ["*Ishihara polychromatic plates","Snellen chart || Tests distance acuity.","Amsler grid || Tests macular changes.","Tonometry || Measures intraocular pressure."],
 "Ishihara plates screen color vision.")
q("color","Which client is MOST likely to have trouble identifying colors?",
 ["*A client with macular degeneration","A client with open-angle glaucoma || Glaucoma affects peripheral vision; color is identified by central vision.","A client with ectropion || A lid problem, not a vision problem.","A client with presbyopia || Affects near focus, not color."],
 "Central vision identifies color, so macular degeneration (central loss) affects color more than a peripheral condition like glaucoma.")
q("color","Which can cause ACQUIRED color-vision loss? "+SATA,
 ["*Digoxin","*Cataracts","Being male || Inherited red-green deficiency is more common in men, but that isn't acquired.","Moxifloxacin eye drops || Not listed as a cause."],
 "Digitalis/digoxin and cataracts can cause acquired color loss. Inherited red-green deficiency: 8% of men vs 0.5% of women.")

# ---------- amsler ----------
q("amsler","A client with macular degeneration is sent home with an Amsler grid. Which teaching is correct?",
 ["*Check it daily and report squares that look faded or lines that look wavy","Use it once a year at the eye exam || It's used daily at home.","It measures eye pressure || That's tonometry.","Look at it with both eyes from 20 feet || It's a near grid with a central fixation point."],
 "The Amsler grid detects macular changes early; faded squares or wavy lines are abnormal. Use daily at home.")
q("amsler","The Amsler grid is used to detect problems with which part of the eye?",
 ["*The macula","The lens || Lens clouding is a cataract.","The eyelid || Lids are inspected on the external exam.","The aqueous drainage angle || That's glaucoma."],
 "Amsler grid = geometric grid of identical squares with a central fixation point, used for macular problems.")

# ---------- ophthalmoscopy & slit lamp ----------
q("scopes","Before direct ophthalmoscopy, what should the nurse do with the room?",
 ["*Darken it","Turn on all overhead lights || Bright light constricts the pupil.","Open the blinds || Same problem.","Nothing special || The room is darkened."],
 "Darken the room for direct ophthalmoscopy (rotating plus and minus lenses).")
q("scopes","Which findings may be seen on direct ophthalmoscopy? "+SATA,
 ["*Flame-shaped hemorrhages from hypertension","*Small, yellow, globular drusen in macular degeneration","*Yellow lipid deposits linked to high cholesterol or diabetes","Colored halos around lights || That's a symptom the client reports in angle-closure glaucoma."],
 "Ophthalmoscopy looks for intraretinal hemorrhages (flame-shaped with HTN), lipid deposits and drusen.")
q("scopes","What is a slit-lamp examination?",
 ["*A table-mounted binocular microscope that examines the eye at 10–40× magnification","A handheld chart read at 20 feet || That's a Snellen chart.","A grid checked daily at home || That's the Amsler grid.","A color-plate booklet || That's Ishihara."],
 "Slit lamp = table-mounted binocular microscope, 10–40× magnification.")

# ---------- tonometry ----------
q("tono","Which test is the most common and reliable way to measure intraocular pressure?",
 ["*Tonometry","Amsler grid || Macular changes.","Ishihara plates || Color vision.","Snellen chart || Distance acuity."],
 "Tonometry measures IOP and determines glaucoma risk.")
q("tono","A client is nervous about tonometry. What should the nurse teach?",
 ["*It's painless; numbing drops are placed first","It requires general anesthesia || It doesn't.","Expect severe pain for a day || It's painless.","You'll need an eye patch for a week || Not needed."],
 "Numbing drops → the client sits at the slit lamp → the provider gently flattens a small area of cornea; IOP is based on the force required.")
q("tono","Before any eye diagnostic test, which nursing responsibilities apply? "+SATA,
 ["*Explain the purpose, what to expect and possible side effects","*Know contraindications and possible complications","*Follow result trends over time","Tell the client results never change || Trends show progression or response to therapy."],
 "Trends can show disease progression or response to therapy.")

# ---------- cataract ----------
q("cataract","What is a cataract?",
 ["*Clouding of the eye's lens that makes vision blurry, hazy or less colorful","Elevated intraocular pressure || That's glaucoma.","Deterioration of the macula || That's macular degeneration.","Inflammation of the conjunctiva || That's conjunctivitis."],
 "Cataracts develop slowly in one or both eyes; about half of people have one by age 75.")
q("cataract","Which are risk factors for cataracts? "+SATA,
 ["*Older age","*Diabetes mellitus","*Eye trauma","*History of radiation","Low-sodium diet || Not a risk factor."],
 "Risks: trauma, diabetes or other chronic disease, older age, radiation.")
q("cataract","Which is the PRIORITY assessment finding in a client with cataracts?",
 ["*Decreased or blurred vision","Sudden severe eye pain with vomiting || That's angle-closure glaucoma.","Purulent crusted discharge || That's bacterial conjunctivitis.","Wavy lines on the Amsler grid || That's macular degeneration."],
 "Decreased/blurred vision is the priority finding; others include abnormal color, glare with night driving and diplopia.")
q("cataract","Which symptoms fit cataracts? "+SATA,
 ["*Glare when driving at night","*Diplopia (double vision)","*Colors look less bright","Sudden loss of central vision with drusen || That's macular degeneration.","Itchy, watery eyes || That's allergic conjunctivitis."],
 "Cataract: blurred vision, abnormal color perception, glare at night, diplopia.")

# ---------- cataract care ----------
q("catcare","Before cataract surgery, mydriatic drops are given. What should the nurse do next?",
 ["*Dim the lights","Shine a penlight to check the pupils every 5 minutes || The dilated pupil is light-sensitive.","Have the client read to test vision || Vision will be blurred.","Lay the client flat || Not the post-drop action."],
 "Mydriatics are anticholinergic drops that dilate the pupil; dim the lights afterward.")
q("catcare","After cataract surgery, how should the nurse position the client?",
 ["*HOB 30–40° and off the operative side","Flat on the back || Don't keep the client flat.","On the operative side || Position off the operative side.","Trendelenburg || Increases eye pressure."],
 "HOB 30–40°, off the operative side, not flat.")
q("catcare","Which post-cataract instructions prevent a rise in intraocular pressure? "+SATA,
 ["*Avoid bending at the waist","*Don't lift more than 5 lb","*Call for prescribed cough medicine if coughing","Do sit-ups to stay active || Straining raises IOP.","Bend over to tie shoes || Bending raises IOP."],
 "Avoid bending, coughing and lifting over 5 lb. Get cough medicine if needed.")
q("catcare","A client after cataract surgery reports eye pain. Which statement reflects the lecture?",
 ["*Eye pain can be severe; give analgesics as needed","Eye pain never happens after cataract surgery || The lecture stresses it can be severe.","Pain means the surgery failed || Not stated.","Withhold analgesics to monitor vision || Treat the pain."],
 "Give analgesics as needed. Also assess eye-patch placement and assist with ambulation and toileting.")
q("catcare","Why is the client taught to wear sunglasses after cataract surgery?",
 ["*To reduce or prevent photophobia","To prevent infection || Not the purpose.","To lower eye pressure || Not the purpose.","To hide bruising || Not the purpose."],
 "Sunglasses reduce photophobia.")

# ---------- blindness ----------
q("blind","Which client meets the definition of legal blindness?",
 ["*Best-corrected acuity of 20/200 in the better eye","Best-corrected acuity of 20/40 in the better eye || Better than 20/200.","Visual field of 60° || Must be 20° or less.","20/200 in one eye only, 20/20 in the other || Measured in the better eye."],
 "Legal blindness = 20/200 or worse in the better eye with best correction, OR widest visual field 20° or less.")
q("blind","A client who just became blind is withdrawn and tearful. What is the nurse's best understanding?",
 ["*New blindness is a major loss and the client may move through grieving","The client should be encouraged to learn Braille right away || Braille is often less important to adults who lose vision later.","This means the client needs a psychiatric consult || Grief is expected.","The client is overreacting || Dismisses a real loss."],
 "Promote coping: allow time and support for processing, acceptance and rehabilitation.")
q("blind","Who should help assess the home and support system of a client with new vision loss? "+SATA,
 ["*The nurse","*A social worker","*The family","*A low-vision specialist or occupational therapist","Only the client, alone || A team approach is used."],
 "Nurse, social worker and family assess the home; consult a low-vision specialist or occupational therapist.")
q("blind","Which statement about legal blindness is from the lecture?",
 ["*About half of legally blind clients are 65 or older","It always means no light perception || It ranges from no light perception to some remaining vision.","It disqualifies a client from disability help || They may qualify for assistance.","It's defined by the worse eye || It's the better eye."],
 "Half of legally blind clients are 65 or older; they may qualify for government financial assistance.")

# ---------- blind care ----------
q("blindcare","How should the nurse guide a blind client while walking?",
 ["*Let the client hold the nurse's arm and walk a half step behind","Push the client from behind || Unsafe and disorienting.","Hold the client's wrist and pull || Not the technique.","Walk a step behind the client || The nurse leads."],
 "The client holds your arm and walks one-half step behind you.")
q("blindcare","Which actions are appropriate when caring for a blind client? "+SATA,
 ["*Identify yourself before touching the client","*Say when you are leaving the room","*Describe where items are, such as the phone on the table to the left","*Let the client feel where assistive devices are placed","Raise your voice so the client can hear || Use a normal tone unless asked."],
 "Introduce yourself and others, state when you leave, describe locations (or the clock method), keep devices nearby, ask 'How can I help you?'")
q("blindcare","A visitor reaches to pet a blind client's guide dog. What should the nurse say?",
 ["*'Please don't pet or distract the dog unless the owner says it's okay.'","'Go ahead; it helps the dog relax.' || Distracting a working dog is unsafe.","'Dogs aren't allowed in hospitals.' || Service animals have access rights.","'Feed it a treat first.' || Still distracts the dog."],
 "Don't distract or pet a service animal without the owner's permission.")
q("blindcare","Which words are acceptable when speaking with a blind client?",
 ["*Words like 'see' and 'look' are fine","Avoid the word 'see' completely || The lecture says these words are acceptable.","Speak only to the family || Face and speak directly to the client.","Use a louder voice || Normal tone."],
 "Speak honestly and respectfully as with anyone.")
q("blindcare","Which environmental action best prevents falls for a client with vision loss?",
 ["*Keep the room free of hazards such as cords","Rearrange furniture daily || Disorienting.","Keep lights off || Not the safety action.","Place the call light out of reach to promote independence || Unsafe."],
 "Keep the environment free of fall hazards and offer to read written material like menus.")

# ---------- glaucoma types ----------
q("glauc","Which description fits primary OPEN-angle glaucoma?",
 ["*Most common; pressure builds slowly with gradual loss of peripheral vision","Sudden severe eye pain with nausea and halos || That's angle-closure.","Loss of central vision with drusen || That's macular degeneration.","Cloudy lens with glare || That's a cataract."],
 "Open-angle = 'silent thief of sight'; usually no symptoms except gradual peripheral narrowing.")
q("glauc","A client has sudden severe eye pain, nausea and vomiting, blurred vision and colored halos. What is the priority?",
 ["*Treat it as a medical emergency: angle-closure glaucoma","Schedule a routine eye exam next month || This is an emergency.","Give ocular lubricant and reassess || Doesn't treat angle-closure.","Teach Amsler grid use || That's for macular problems."],
 "Primary angle-closure (narrow-angle) glaucoma is an emergency, caused by pupil dilation or a bulging lens.")
q("glauc","Why is early detection of glaucoma so important?",
 ["*Vision loss from glaucoma is irreversible","Glaucoma always causes pain early || Open-angle is usually silent.","Glaucoma is curable with glasses || It isn't.","It only affects children || It affects all ages."],
 "Glaucoma damages vision permanently; it's a problem with drainage of the fluid the eye produces, so pressure builds.")
q("glauc","Which term does the lecture also use for glaucoma?",
 ["*Ocular hypertension","Presbyopia || Age-related near-vision loss.","Ectropion || Lid turning outward.","Diplopia || Double vision."],
 "Glaucoma = a group of conditions with elevated IOP; called ocular hypertension in the slides.")
q("glauc","Which findings point to ANGLE-CLOSURE glaucoma? "+SATA,
 ["*Sudden severe eye pain","*Nausea and vomiting","*Blurred vision","*Colored halos around lights","Slow peripheral loss with no pain || That's open-angle."],
 "Four classic angle-closure findings: sudden severe pain, N/V, blurred vision, colored halos.")

# ---------- glaucoma care ----------
q("glaucare","What does a laser iridotomy do for angle-closure glaucoma?",
 ["*Creates a hole in the iris so aqueous humor can flow out","Replaces the cloudy lens || That's cataract surgery.","Injects medicine into the vitreous || That's wet macular degeneration treatment.","Reattaches the retina || Not discussed."],
 "Iridotomy creates a new outflow pathway for aqueous humor.")
q("glaucare","Which teaching applies to a client with open-angle glaucoma? "+SATA,
 ["*Take eye drops as prescribed to lower IOP","*Wear sunglasses to prevent photophobia","*Avoid bending and coughing","*Report redness, drainage, floaters or flashes of light","Stop drops once vision feels normal || Glaucoma is chronic; keep taking them."],
 "Open-angle care: IOP-lowering drops, sunglasses, avoid bending/coughing, report redness, drainage, floaters or flashes.")
q("glaucare","After laser iridotomy, which nursing actions are correct? "+SATA,
 ["*Elevate the HOB 30–40°","*Position the client off the operative side","*Give analgesics as needed","*Avoid bending, coughing or lifting over 5 lb","Keep the client flat for 24 hours || HOB is elevated."],
 "Same positioning and IOP precautions as cataract surgery; an eye patch may or may not be used.")
q("glaucare","A client with glaucoma reports sudden black spots floating in their vision. What should the nurse do?",
 ["*Tell the client to report floaters to the provider","Reassure them that floaters are always harmless || Many are harmless, but glaucoma teaching says report them.","Increase the drops on their own || Never self-adjust.","Ignore it if there's no pain || Still report it."],
 "Floaters (sudden black areas or circles) should be reported in glaucoma teaching.")

# ---------- glaucoma meds ----------
q("glaumed","How does timolol eye drop work, and how is it usually dosed?",
 ["*Ophthalmic beta blocker; 1 drop twice daily","Antibiotic; 1 drop 3 times a day for 7 days || That's moxifloxacin.","Lubricant; as needed || That's ocular lubricant.","Intravitreal injection every 4–6 weeks || That's wet macular degeneration treatment."],
 "Timolol: ophthalmic beta blocker, 1 drop twice daily (lecture example 10 AM and 10 PM); for open-angle glaucoma and ocular hypertension.")
q("glaumed","How does brinzolamide (Azopt) lower intraocular pressure?",
 ["*It reduces formation of aqueous humor","It dilates the pupil || That's a mydriatic.","It kills bacteria || That's an antibiotic.","It moistens the eye || That's a lubricant."],
 "Brinzolamide reduces aqueous-humor formation; indicated for open-angle and angle-closure glaucoma.")
q("glaumed","What is aqueous humor?",
 ["*The clear liquid in the front of the eye","The jelly in the back of the eye || Not the lecture definition.","Tears made by the lacrimal gland || Not aqueous humor.","Pus from infection || Not aqueous humor."],
 "Aqueous humor is the clear fluid in the front of the eye; poor drainage raises IOP.")
q("glaumed","Which glaucoma drop is indicated for BOTH open-angle and angle-closure glaucoma, per the slides?",
 ["*Brinzolamide (Azopt)","Moxifloxacin || An antibiotic for bacterial conjunctivitis.","Ocular lubricant || Comfort drop only.","Mydriatic drops || Dilating the pupil can trigger angle closure."],
 "Timolol is listed for open-angle and ocular hypertension; brinzolamide for both open- and closed-angle.")

# ---------- eye drops ----------
q("drops","A client has two different eye drops ordered at the same time. What should the nurse do?",
 ["*Wait 5 minutes between the drops","Give them back to back || The second washes out the first.","Mix them in one dropper || Never mix.","Give one in each eye || Both are ordered for the same eye."],
 "Wait 5 minutes between different drops so each can work; the eMAR times this interval.")
q("drops","Why does technique matter when giving eye drops?",
 ["*The conjunctival sac holds about 50 mcL and one drop is 20–35 mcL","The eye can hold several drops at once || It holds only about 50 mcL.","Eye drops are absorbed through the skin || Not the reason.","One drop is 100 mcL || A drop is 20–35 mcL."],
 "Tearing, blinking and drainage can dilute or expel a drop.")
q("drops","Which steps are correct when instilling eye drops? "+SATA,
 ["*Remove contact lenses first","*Have the client tilt the head back and look up","*Pull down the lower lid to make a pocket","*Recap the bottle after each use","Touch the tip to the eye to be sure the drop goes in || Contaminates the dropper."],
 "Hand hygiene, remove contacts, head back and look up, pocket the lower lid, don't touch the tip, recap.")
q("drops","Which action by a client giving their own eye drops needs correction?",
 ["*Touching the bottle tip to the eyelid","Washing hands first || Correct.","Looking up at the ceiling || Correct.","Waiting 5 minutes before the second drop || Correct."],
 "Don't touch the eye with the bottle tip or contaminate the dropper.")

# ---------- macular degeneration ----------
q("md","Which vision is lost in macular degeneration?",
 ["*Central vision; peripheral vision may stay intact","Peripheral vision first || That's glaucoma.","Only night vision || Not the lecture description.","Near vision only || That's presbyopia."],
 "The macula is the central part of the retina; MD is the leading cause of irreversible blindness worldwide and isn't curable.")
q("md","Which are risk factors for macular degeneration? "+SATA,
 ["*Increasing age","*Smoking or secondhand smoke","*Family history","*Cardiovascular disease","*White ethnicity","Being under 20 || Risk rises with age."],
 "MD risks: age, genetics/family history, white ethnicity, cardiovascular disease, smoking/secondhand smoke.")
q("md","Which teaching is appropriate for macular degeneration? "+SATA,
 ["*Use handheld electronic magnifiers or e-readers","*Check an Amsler grid at home daily","*Stop smoking","Wear an eye patch at night || Not part of the teaching."],
 "Visual aids, daily Amsler grid, smoking cessation.")
q("md","Small yellow globular deposits seen on the retina are called:",
 ["*Drusen","Halos || A symptom of angle-closure glaucoma.","Floaters || Black spots the client sees.","Cataracts || Lens clouding."],
 "Drusen are common in macular degeneration.")

# ---------- dry vs wet ----------
q("mdtypes","Which statement about DRY macular degeneration is correct?",
 ["*It's the most common type and has no treatment or cure","It's treated with injections every 4–6 weeks || That's wet MD.","It's caused by leaking blood vessels || That's wet MD.","It's curable with surgery || Not curable."],
 "Dry MD: drusen increase in size and number (atrophy); goal is visual aids and monitoring.")
q("mdtypes","How is WET macular degeneration treated?",
 ["*A prescribed inhibitor given by intravitreal injection every 4–6 weeks","Laser iridotomy || That's angle-closure glaucoma.","Moxifloxacin drops || That's bacterial conjunctivitis.","No treatment is available || That's dry MD."],
 "Wet MD: abnormal vessels leak fluid and blood and scar; the injection inhibits endothelial growth factor and slows vision loss.")
q("mdtypes","Which type of macular degeneration involves abnormal blood vessels that leak fluid and blood?",
 ["*Wet","Dry || Dry is drusen and atrophy.","Both equally || Only wet.","Neither || Wet involves leaking vessels."],
 "Wet is less common; leaking vessels cause scars that distort vision.")

# ---------- conjunctivitis ----------
q("conj","A client has purulent eye discharge with crusting. Which type of conjunctivitis is most likely?",
 ["*Bacterial","Viral || Viral discharge is serous and watery.","Allergic || Allergic is marked by itching.","Macular || Not a type of conjunctivitis."],
 "Bacterial = purulent, may crust. Viral = serous/watery. Allergic = itching.")
q("conj","Which conjunctivitis is characterized mainly by itching?",
 ["*Allergic","Bacterial || Purulent discharge.","Viral || Watery discharge.","None of them || Allergic is the itchy type."],
 "Allergic drainage ranges from watery to thick; itching is the defining feature.")
q("conj","Which medication do the slides list for bacterial conjunctivitis?",
 ["*Moxifloxacin antibiotic drops, 1 drop 3 times a day for 7 days","Ocular lubricant || Soothes but doesn't treat bacteria.","Timolol || A glaucoma drop.","Brinzolamide (Azopt) || A glaucoma drop."],
 "Moxifloxacin treats bacterial conjunctivitis; lubricant is for viral/allergic symptoms.")
q("conj","A client with viral conjunctivitis asks about treatment. Which is correct?",
 ["*An ocular lubricant eases dryness and irritation","Antibiotic drops cure it || Antibiotics treat bacteria, not viruses.","Laser treatment is needed || Not for conjunctivitis.","Intravitreal injection || That's wet MD."],
 "Ocular lubricant moistens the eye but doesn't treat bacterial infection.")
q("conj","Why is the conjunctiva prone to infection?",
 ["*It's a thin, transparent membrane constantly exposed to the environment","It has no blood supply || Not the lecture reason.","It's inside the eyeball || It covers the eye's surface.","It produces aqueous humor || It doesn't."],
 "Constant exposure makes it vulnerable to viruses, irritants and bacteria.")

# ---------- conjunctivitis teaching ----------
q("conjteach","Which teaching is correct for a client with conjunctivitis? "+SATA,
 ["*Throw away eye makeup, especially mascara","*Don't share washcloths or towels","*Stop wearing contact lenses until it clears","*Perform meticulous hand hygiene","Share eye drops with family members who have red eyes || Never share drops."],
 "Also: don't touch the eye with the dropper.")
q("conjteach","Which priority nursing interventions apply to conjunctivitis? "+SATA,
 ["*Give prescribed eye drops","*Maintain strict infection control","*Apply cold or warm compresses for comfort","Patch the eye for a week || Not listed."],
 "Drops, strict infection control, compresses.")

# ---------- health promotion ----------
q("promo","A 45-year-old has new trouble reading up close. What is the likely cause?",
 ["*Presbyopia, an age-related loss of lens elasticity","Glaucoma || Causes peripheral loss.","Macular degeneration || More common later and affects central vision.","Conjunctivitis || An infection or irritation."],
 "Presbyopia: near-vision difficulty can begin in the 40s.")
q("promo","Which nutrition teaching supports eye health? "+SATA,
 ["*Vitamin A deficiency can cause eye dryness","*Lutein and beta-carotene help maintain retinal function","Vitamin A causes cataracts || Not stated.","Caffeine improves night vision || Not stated."],
 "Vitamin A deficiency → dryness; lutein and beta-carotene support the retina.")
q("promo","Which health-promotion teaching does the lecture include? "+SATA,
 ["*Wear eye protection for sports, work, gardening and lawn care","*Avoid smoking and vaping","*Manage diabetes, hypertension, lupus and heart disease","*Ask about family history of glaucoma and macular degeneration","Rub the eyes to remove makeup || Avoid rubbing; remove makeup properly."],
 "Exam frequency depends on race/ethnicity, age and health conditions.")
q("promo","Which conditions does the slide list as lifespan or pediatric eye-check concerns? "+SATA,
 ["*Myopia","*Amblyopia","*Strabismus","*Nasolacrimal duct obstruction","Ectropion || An external lid finding in older adults."],
 "Slide list: myopia, amblyopia, astigmatism, strabismus, nasolacrimal duct obstruction.")
