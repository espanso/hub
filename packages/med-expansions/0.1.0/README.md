This package provides a very large number of expansions written by someone taking notes as a medical student. The content included in the expansions from this package are generally more academic and less clinical than the Medical-Docs package which is written for use in facilitating clinical practice.

Note, the rules below are as of yet NOT completely adhered to, the rules below apply generally but triggers are not fully compliant as of yet.


Legend:
- `SPC` — Spacebar

Below are some guiding principles as to how expansions work, generally speaking
* RULE #1 — If the expansion is a common acronym, BP for blood pressure, ACS for Acute Coronary Syndrome, etc, the trigger is the acronym followed by a trailing "."
    * NOTE THE CONTRARY APPLIES. if a trigger is an acronym BUT NOT A COMMONLY USED ACRONYM (think jp → J-point) then there is NO DOT required after the trigger
    * This includes things which are best referred to as shorthand, typically expansions which are multiple words (think typically 3+ words) in length, for example soboe. → shortness of breath on exertion, cccp. → crushing central chest pain.   
    * Press `SPC` after typing the "." and the trigger will expand.
* RULE #2 If the expansion is a medical term with multiple syllables (pneumothorax, cardiomegaly, pleural effusion), the trigger is the first LETTER followed by the first THREE letters of the first distinguishing syllable
    * "Distinguishing syllable" in this context refers to the first syllable that distinguishes the word from other words means that cardiomegaly has a trigger of cmeg, as opposed to cdio, because many words will have a first letter of c and second syllable starting with "dio". This sounds complicated but 95%+ of the time, it is extremely intuitive and will probably be what rolls off your tongue naturally
    * "Cardiac tamponade" is "ctam", "pleural effusion" is "peff", "rhabdomyolysis" is "rmyo" etc.
    * Why do it this way? It's the way we most naturally think of shorthand terms, think about afib and vfib, which follow this rule
* Where this rule is not possible to follow, which is rare, a common sense alternative is used. This will mean applying rule #2 if possible
    * If rule #1 or #2 (whichever not first applied) can be used, and a common-sense/intuitive alternative exists, BOTH will be valid triggers. Otherwise, ONLY the intuitive trigger is valid
        * For example, following the above rules, "ischaemia" would be iaem, because some dialects omit the a in -aemia, the iaem is foregone
        * ...Rule #1 cannot be applied here
        * The intuitive expansions "isc" AND "isch" are used instead
        * An effort is made to document exceptions with comments (lines above the trigger line marked with a "#") in the yml files
* RULE #3 — For bacteria / fungi, the following is always a valid trigger (except in salmonella enteritidis)
        * First letter of genus followed by first three letters of species followed by `SPC`
        * Where an intuitive expansion exists that does not follow the above, both are valid triggers
            * e.g — While the rule for Haemophilus influenzae is hinf (first letter of Haemophilus is H, first three letters of influenza is inf). But "hflu" is the most reasonable trigger here
            * So, in this (and in similar cases), both "hflu" and "hinf" are both valid triggers
* RULE #4a — For Viruses, if the virus is one syllable followed by "virus" (e.g togavirus), trigger is simply the first syllable followed by v
* RULE #4b —  For viruses with multiple syllables, rule #2 applies with the exception that the trigger ends in "v" and ONLY TWO LETTERS are required from the first distinguishing syllable (as viruses are narrow enough in scope that two letters is sufficient).
        * omyv → Orthomyxovirus
        * crov → Coronaviridae  
            * EXTRA FEATURE: adding two v's at the end will yield the plural
            * crovv → Coronaviridae  
        * For ease of use, and for consistency, IN FUTURE, simply applying rule #2 will trigger the expansion (i.e — Orthomyxovirus will be triggered by omyv and omyx and omyxv)

Some notable exceptions:
* EXCEPTION #1 — Common shorthand follows a simple rule, take the common shorthand and append a trailing "." and press `SPC`
        * E.g
        * tx. → Treatment.  hx. → history.
            * etc.
        * qds. → four times daily  
        * 4/12. → four month
        * hb. → haemoglobin
            * etc.
        * a. → artery
        * as. → arteries
            * etc.

* EXCEPTION #2 — 
            
## Bacteria
HOW-TO USE:
In almost all cases, the trigger for the bacterial species will be four characters long.
For the full name of the bacteria (ie — Staphylococcus aureus as opposed to the shortened S. aureus) use the FIRST LETTER of the GENUS followed by the first three letters of the species.
    e.g —  Spne → Streptococcus pneumoniae 
For the SHORTENED name (ie —  B. pertussis as opposed to Bordetella pertussis) use the FIRST LETTER of the GENUS followed by "." followed by the first syllable of the species
    e.g —  c.tet → C. tetani
|           Bacteria           |           Expansion          |
|:----------------------------:|:----------------------------:|
|                              |                              |
| Actinomyces                  | amyc                         |
| B. anthracis                 | b.ant                        |
| B. cereus                    | b.cer                        |
| B. melitensis                | b.mel                        |
| B. pertussis                 | b.per                        |
| Bacillus                     | bac.                         |
| Bacillus anthracis           | banth †                      |
| Bacillus cereus              | bcer                         |
| Bartonella                   | bart.                        |
| Bordetella                   | bord.                        |
| Bordetella pertussis         | bper                         |
| Brucella                     | bruc.                        |
| Brucella abortus             | babo                         |
| Brucella melitensis          | bmel                         |
| Burkholderia                 | burk.                        |
| C. botulinum                 | c.bot                        |
| C. burnetii                  | c.burn                       |
| C. coli                      | c.col                        |
| C. difficile                 | c.dif                        |
| C. diphtheriae               | c.dip                        |
| C. fetus                     | c.fet                        |
| C. jejuni                    | c.jej                        |
| C. perfringens               | c.per                        |
| C. pneumoniae                | c.pne                        |
| C. pylori                    | c.pyl                        |
| C. tetani                    | c.tet                        |
| C. trachomatis               | c.tra or c.trac or c.trach   |
| Campylobacter                | camp.                        |
| Campylobacter coli           | ccol                         |
| Campylobacter fetus          | cfet                         |
| Campylobacter jejuni         | cjej                         |
| Campylobacter pylori         | cpyl                         |
| Chlamydia                    | chlam.                       |
| Chlamydophila trachomatis    | ctra orctrac or ctrach       |
| Chlamydophila pneumoniae     | cpne                         |
| Chlamydophila psittaci       | cpsi                         |
| Clostridium                  | clos.                        |
| Clostridium botulinum        | cbot                         |
| Clostridium difficile        | cdif                         |
| Clostridium perfringens      | cper                         |
| Clostridium tetani           | ctet                         |
| Corynebacterium              | cory.                        |
| Corynebacterium diphtheriae  | cdip                         |
| Coxiella burnetii            | cbur                         |
| E. coli                      | e.col                        |
| Enterococcus                 | ecoc                         |
| Enterococcus faecium         | efaeci                       |
| Enterococcus faecalis        | efaeca                       |
| Escherichia coli             | ecoli                        |
| Francisella tularensis       | ftul                         |
| H. influenzae                | h.inf or h.flu               |
| H. parainfluenzae            | h.par                        |
| H. pylori                    | h.pyl                        |
| H. vaginalis                 | h.vag                        |
| Haemophilus                  | hphil                        |
| Haemophilus influenzae       | hinf or hflu                 |
| Haemophilus parainfluenzae   | hpar                         |
| Haemophilus vaginalis        | hvag                         |
| Helicobacter                 | hel.                         |
| Helicobacter pylori          | hpyl                         |
| K. pneumoniae                | k.pne or k.pneu              |
| Klebsiella                   | kleb                         |
| Klebsiella pneumoniae        | kpne or kpneu                |
| L. Pneumophila               | L.pne                        |
| L. monocytogenes             | L.mon                        |
| Lactobacillus                | Lacb.                        |
| Legionella                   | legi.                        |
| Legionella Pneumophila       | Lpne                         |
| Listeria                     | Lis.                         |
| Listeria monocytogenes       | Lmon                         |
| M. bovis                     | m.bov                        |
| M. diphtheriae               | m.dip                        |
| M. leprae                    | m.lep                        |
| M. pneumoniae                | m.pne                        |
| M. tuberculosis              | m.tub                        |
| Mycobacterium                | mycob                        |
| Mycobacterium bovis          | mbov                         |
| Mycobacterium diphtheriae    | mdip                         |
| Mycobacterium leprae         | mlep                         |
| Mycobacterium pneumoniae     | mpne                         |
| Mycobacterium tuberculosis   | mtub                         |
| Mycoplasma                   | mycop                        |
| Mycoplasma pneumoniae        | mpne                         |
| N. gonorrhoaea               | n.gon                        |
| N. meningitidis              | n.men                        |
| Neisseria gonorrhoaea        | ngon                         |
| Neisseria meningitidis       | nmen                         |
| Nocardia                     | noc                          |
| P. aeruginosa                | p.aer                        |
| Pseudomonas aeruginosa       | paer                         |
| Rickettsia                   | rick.                        |
| S. agalactiae                | s.aga                        |
| S. aureus                    | s.aur                        |
| S. dysenteriae               | s.dys                        |
| S. enteritidis               | s.ent †                      |
| S. epidermidis               | s.epi                        |
| S. pneumoniae                | s.pne                        |
| S. pyogenes                  | s.pyo                        |
| S. saprophyticus             | s.sap                        |
| S. typhi                     | s.typ                        |
| Salmonella                   | salm.                        |
| Salmonella enteritidis       | senter or salme or salment † |
| Salmonella typhi             | styp                         |
| Shigella                     | shig.                        |
| Shigella dysenteriae         | sdys                         |
| Staphylococcus               | staph.                       |
| Staphylococcus aureus        | saur                         |
| Staphylococcus epidermidis   | sepi                         |
| Staphylococcus saprophyticus | ssap                         |
| Streptococcus                | strep                        |
| Streptococcus agalactiae     | saga                         |
| Streptococcus pneumoniae     | spne                         |
| Streptococcus pyogenes       | spyo                         |
| V. cholerae                  | v.cho or v.chol              |
| Vibrio cholerae              | vcho or vchol                |
† — These stray somewhat from the rule of "first letter from genus followed by first three letters of species"
Note that _pneumoniae_ species accept either *pne or *pneu 

## Viruses
|          Expansion           |      Viruses       |
|:----------------------------:|:------------------:|
|          Adenovirus          | anov, adenov, adev |
|          Arenavirus          |       arenav       |
|          Calcivirus          |        cciv        |
|        Coronaviridae         |        crov        |
|        Coxsackievirus        |     csav, coxv     |
|       Cytomegalovirus        |     :cmv, cmev     |
|      Epstein-Barr Virus      |     :ebv, ebav     |
|          Filovirus           |       filov        |
|          Flavivirus          |        fviv        |
|     Herpes Simplex Virus     |     :hsv, hsev     |
|      Human Herpesvirus       |     :hhv, hhev     |
| Human Immunodeficiency Virus |     himv, :hiv     |
|        Orthomyxovirus        |     omyv, :omv     |
|        Papillomavirus        |     pilv, papv     |
|        Paramyxovirus         |        pmyv        |
|         Picornavirus         |        pcov        |
|          Poliovirus          | pliv, polv, poliov |
|         Polyomavirus         |        pomv        |
|           Poxvirus           |        poxv        |
|           Reovirus           |        reov        |
|          Rhinovirus          |    rnov, rhinov    |
|          Togavirus           |       togav        |
|    Varicella Zoster Virus    |     :vzv, vzov     |
