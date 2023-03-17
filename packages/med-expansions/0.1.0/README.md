
<h1 align="center">
Med-Expansions <br></br>

</h1>


<h4 align="center">A comprehensive and systematic set of keyboard expansions for medical note-taking using Espanso</h4>

<p align="center">
<a href="#install">Install</a> •
<a href="#demo">Demo</a> •
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#credits">Credits</a> •
  <a href="#license">License</a> 
</p>

# Install
    `espanso install med-expansions`
    

## Demo
![screenshot](./demo.gif)

## Key Features

* **Systematic**
	- forget remembering complicated triggers
  - Simple rules yield consistent results.
* **Cut down on typing**
  - Medical terminology is often painfully protracted to type, often for no good reason, if you need to type supraventricular tachycardia often, you're going to love this package.
* **We have it all covered**
   - Viruses, fungi, pathology, clinical terminology, everything medical, we've got it down†.
* **Cross platform**
  - Windows, macOS and Linux enabled, thanks to [Espanso](http://espanso.org "Espanso")

† *this is totally a lie (for now)*
## How To Use

Legend:
* `SPC` refers to the spacebar


##### RULE #1
###### If the expansion is a common acronym*, the trigger **is the acronym** *followed by a trailing* `.`

e.g — (ACS, BP, HTN), triggers are:
* `acs. → acute coronary syndrome`
* `bp. → blood pressure`
* `htn. → hypertension`  

- If the expansion is not referred to by its acronym (like `jp → J-point`), a trailing `.` is not required
    * Press `SPC` after typing the `.` and the trigger will expand.

##### RULE #2 
###### If the expansion is a medical term with **multiple syllables*** , the trigger is the **first LETTER** *followed by* the **first THREE letters** of the ***first* distinguishing syllable**.

e.g — (pneumothorax, cardiomegaly, pleural effusion), triggers are:
* `ptho → pneuomothorax`
* `cmeg → cardiomegaly`
* `peff → pleural effusion`

* *"Distinguishing syllable"* in this context refers to the first syllable *that distinguishes the word from other words*. This means that `cardiomegaly` has a trigger of `cmeg`, as opposed to `cdio`, because many words will have a first letter of c and second syllable starting with "dio". 
	* This sounds complicated but 95%+ of the time, it is extremely intuitive and will probably be what rolls off your tongue naturally
    * `Cardiac tamponade` is `ctam`, `pleural effusion` is `peff`, `rhabdomyolysis` is `rmyo` etc.
    * Why do it this way? It's the way we most naturally think of shorthand terms, think about `afib` and `vfib`, which follow this rule.
* Where this rule is not possible to follow, which is rare, a common sense alternative is used
    * If rule #1 or #2 (whichever not first applied) can be used, **and** a common-sense/intuitive alternative exists, **BOTH** will be valid triggers. Otherwise, ONLY the intuitive trigger is valid
        * An effort is made to document exceptions with comments (lines above the trigger line marked with a `#`) in the .yml files

##### RULE #3
> For bacteria / fungi, the following is always a valid trigger (except in salmonella enteritidis and Bacillus anthracis)

###### First letter of genus followed by first three letters of species followed by `SPC`


* Where an intuitive expansion exists that does not follow the above, both are valid triggers
	* e.g — While the rule for Haemophilus influenzae is hinf (first letter of Haemophilus is H, first three letters of influenza is inf). But "hflu" is the most reasonable trigger here
	* So, in this case (and in similar cases), both "hflu" and "hinf" are both valid triggers
	
	Exceptions are the following working triggers `Senter → Salmonella enteritidis` and `banth → Bacillus anthracis`  
	
##### RULE #4a
###### For Viruses, *if the virus is one or two short syllables* followed by `virus` (e.g `togavirus`), the trigger is simply the first syllable followed by `v`ᵃ

##### RULE #4b 
###### For viruses with *multiple syllables*, the trigger is the **first letter**, followed by the **first two letters from the next distinguishing syllable** followed by `v`

    * `omyv → Orthomyxovirus`
    * `crov → Coronaviridae` 
		* **Plurals**: adding two `v`'s at the end will yield the plural form
        * `crovv → Coronaviridae`
        * For ease of use, and for consistency, *in future*, simply applying **rule #2** alone and adding a trailing v will trigger the expansion (i.e — `Orthomyxovirus` will be triggered by `omyv` as per **rule #4b** and `omyx` as per **rule #2** and `omyxv` as a fallback)
		
ᵃ — * For short viruses obeying **rule #4a**, which are on the border between 4a and 4b, both triggers will be valid.
		
#### Some notable exceptions:
##### Exception #1
###### Common shorthand follows a simple rule, take the common shorthand and append a trailing "." and press `SPC`
* E.g:
	* `tx. → treatment`.  `hx. → history`.
		* etc.
	* `qds. → four times daily`  
	* `4/12. → four month`
	* `hb. → haemoglobin`
		* etc.
	* `a. → artery`
	* `as. → arteries`
		* etc.

## Credits

This software uses the following open source packages:

- [Espanso](http://espanso.org)

## License

GNU GPLv3

---

> Cillian Scott •
> GitHub [@CillySu](https://github.com/CillySu) •
> E-mail: scottci@tcd.ie

