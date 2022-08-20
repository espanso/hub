# What's this about?
This package ships a variety of unicode symbols commonly used by working mathematicians in a coherent syntax roughly based on LaTeX.

# Why would I need this?
It is much easier to communicate about mathematics i.e. in a math discord or via email with a collaborator when you read statements like 

    π₋ₙ(map(Σ₊Y, 𝐇(A))) ⋍ Hⁿ(Y, A)

compared to the currently widely adopted

    \pi_{-n}(map(\Sigma_{+}Y, \mathbf{H}(A))) \simeq \mathsf{H}^{n}(Y, A)

# What's inside?

The basic syntax for maths symbols is ```:trigger:```, where 'trigger' is the maths command in question.
For example:

    - ```:to:```     ⟶ ```⟶```
    - ```:epi:```    ⟶ ```↠```
    - ```:mono:```   ⟶ ```⮩``` 
    - ```:infty:```  ⟶ ```∞```
    - ```:calC:```   ⟶ ```𝓒```
    - ```:Lambda:``` ⟶ ```Λ```
    - ```X:_1:```    ⟶ ```X₁```

Here's an exhaustive list of symbols that are currently supported together with their ```trigger```.

### Arrows
| Trigger | Replace |
| ------- | ------- |
|:to:|⟶|
|:arrow_right:|⟶|
|:ot:|⟵|
|:arrow_left:|⟵|
|:arrow_up:|↑|
|:arrow_down:|↓|
|:arrow_left_and_right:|⇄|
|:arrow_leftright:|⟷|
|:to_short:|→|
|:epi:|↠|
|:epi_left:|↞|
|:mono:|⮩|
|:mono_left:|⮨|
|:acts:|↷|
|:acts_left:|↶|
|:auto:|⟲|
|:simto:|⭇|
|:simot:|⭁|
|:emb_open:|⇴|
|:emb_closed:|↛|
|:mapsto:|⟼|
|:mapsto_short:|↦|
|:rrarrow:|⇉|
|:rrrarrow:|⇶|
|:arroww:|⟹|
|:arrowww:|⇛|
|:arrow_squiggly:|⇝|
|:arrow_squiggly_left:|⇜|
|:arrow_squiggly_long:|⟿|

### Logic & Category Theory
| Trigger | Replace |
| ------- | ------- |
|:forall:|∀|
|:exists:|∃|
|:not_exists:|∄|
|:not_equals:|≠|
|:and:|∧|
|:or:|∨|
|:xor:|⩛|
|:not:|¬|
|:impl:|⇒|
|:simeq:|⋍|
|:not_simeq:|≄|
|:cong:|≌|
|:coloneqq:|≔|
|:eqqcolon:|≕|
|:leq:|≦|
|:geq:|≧|
|:ladj:|⊣|
|:radj:|⊢|
|:times:|×|
|:point:|∗|
|:circ:|∘|
|:prod:|∏|
|:coprod:|∐|
|:sum:|∑|

### Set Theory
| Trigger | Replace |
| ------- | ------- |
|:cap:|∩|
|:cup:|∪|
|:empty:|∅|
|:in:|∈|
|:not_in:|∉|
|:ni:|∋|
|:not_ni:|∌|
|:subset:|⊂|
|:superset:|⊃|

### Greek
| Trigger | Replace |
| ------- | ------- |
|:alpha:|α|
|:Alpha:|Α|
|:beta:|β|
|:Beta:|Β|
|:gamma:|γ|
|:Gamma:|Γ|
|:delta:|δ|
|:Delta:|Δ|
|:epsilon:|ε|
|:Epsilon:|Ε|
|:zeta:|ζ|
|:Zeta:|Ζ|
|:eta:|η|
|:Eta:|Η|
|:theta:|θ|
|:Theta:|Θ|
|:iota:|ι|
|:Iota:|Ι|
|:kappa:|κ|
|:Iota:|Κ|
|:lambda:|λ|
|:Lambda:|Λ|
|:mu:|μ|
|:Mu:|Μ|
|:nu:|ν|
|:Nu:|Ν|
|:xi:|ξ|
|:Xi:|Ξ|
|:omicron:|ο|
|:Omicron:|Ο|
|:pi:|π|
|:Pi:|Π|
|:rho:|ρ|
|:Rho:|Ρ|
|:sigma:|σ|
|:Sigma:|Σ|
|:tau:|τ|
|:Tau:|Τ|
|:upsilon:|υ|
|:Upsilon:|Υ|
|:phi:|φ|
|:varphi:|ϕ|
|:Phi:|Φ|
|:chi:|χ|
|:Chi:|Χ|
|:psi:|ψ|
|:Psi:|Ψ|
|:omega:|ω|
|:Omega:|Ω|

### Latin lowercase superscripts
| Trigger | Replace |
| ------- | ------- |
|:^a:|ᵃ|
|:^b:|ᵇ|
|:^c:|ᶜ|
|:^d:|ᵈ|
|:^e:|ᵉ|
|:^f:|ᶠ|
|:^g:|ᵍ|
|:^h:|ʰ|
|:^i:|ⁱ|
|:^j:|ʲ|
|:^k:|ᵏ|
|:^l:|ˡ|
|:^m:|ᵐ|
|:^n:|ⁿ|
|:^o:|ᵒ|
|:^p:|ᵖ|
|:^r:|ʳ|
|:^s:|ˢ|
|:^t:|ᵗ|
|:^u:|ᵘ|
|:^v:|ᵛ|
|:^w:|ʷ|
|:^x:|ˣ|
|:^y:|ʸ|
|:^z:|ᶻ|

Note the missing superscript q.

### Latin lowercase subscripts
| Trigger | Replace |
| ------- | ------- |
|:_a:|ₐ|
|:_e:|ₑ|
|:_h:|ₕ|
|:_i:|ᵢ|
|:_j:|ⱼ|
|:_k:|ₖ|
|:_l:|ₗ|
|:_m:|ₘ|
|:_n:|ₙ|
|:_o:|ₒ|
|:_p:|ₚ|
|:_r:|ᵣ|
|:_s:|ₛ|
|:_t:|ₜ|
|:_u:|ᵤ|
|:_v:|ᵥ|
|:_x:|ₓ|

### Subscript digits and special characters
| Trigger | Replace |
| ------- | ------- |
|:_0:|₀|
|:_1:|₁|
|:_2:|₂|
|:_3:|₃|
|:_4:|₄|
|:_5:|₅|
|:_6:|₆|
|:_7:|₇|
|:_8:|₈|
|:_9:|₉|
|:_(:|₍|
|:_):|₎|
|:_+:|₊|
|:_-:|₋|

### mathbb
| Trigger | Replace |
| ------- | ------- |
|:bbA:|𝔸|
|:bbB:|𝔹|
|:bbC:|ℂ|
|:bbD:|𝔻|
|:bbE:|𝔼|
|:bbF:|𝔽|
|:bbG:|𝔾|
|:bbH:|ℍ|
|:bbI:|𝕀|
|:bbJ:|𝕁|
|:bbK:|𝕂|
|:bbL:|𝕃|
|:bbM:|𝕄|
|:bbN:|ℕ|
|:bbO:|𝕆|
|:bbP:|ℙ|
|:bbQ:|ℚ|
|:bbR:|ℝ|
|:bbS:|𝕊|
|:bbT:|𝕋|
|:bbU:|𝕌|
|:bbV:|𝕍|
|:bbW:|𝕎|
|:bbX:|𝕏|
|:bbY:|𝕐|
|:bbZ:|ℤ|

### mathsf
| Trigger | Replace |
| ------- | ------- |
|:sfA:|𝖠|
|:sfB:|𝖡|
|:sfC:|𝖢|
|:sfD:|𝖣|
|:sfE:|𝖤|
|:sfF:|𝖥|
|:sfG:|𝖦|
|:sfH:|𝖧|
|:sfI:|𝖨|
|:sfJ:|𝖩|
|:sfK:|𝖪|
|:sfL:|𝖫|
|:sfM:|𝖬|
|:sfN:|𝖭|
|:sfO:|𝖮|
|:sfP:|𝖯|
|:sfQ:|𝖰|
|:sfR:|𝖱|
|:sfS:|𝖲|
|:sfT:|𝖳|
|:sfU:|𝖴|
|:sfV:|𝖵|
|:sfW:|𝖶|
|:sfX:|𝖷|
|:sfY:|𝖸|
|:sfZ:|𝖹|

### mathbf
| Trigger | Replace |
| ------- | ------- |
|:bfA:|𝐀|
|:bfB:|𝐁|
|:bfC:|𝐂|
|:bfD:|𝐃|
|:bfE:|𝐄|
|:bfF:|𝐅|
|:bfG:|𝐆|
|:bfH:|𝐇|
|:bfI:|𝐈|
|:bfJ:|𝐉|
|:bfK:|𝐊|
|:bfL:|𝐋|
|:bfM:|𝐌|
|:bfN:|𝐍|
|:bfO:|𝐎|
|:bfP:|𝐏|
|:bfQ:|𝐐|
|:bfR:|𝐑|
|:bfS:|𝐒|
|:bfT:|𝐓|
|:bfU:|𝐔|
|:bfV:|𝐕|
|:bfW:|𝐖|
|:bfX:|𝐗|
|:bfY:|𝐘|
|:bfZ:|𝐙|

### mathsc
| Trigger | Replace |
| ------- | ------- |
|:scA:|𝒜|
|:scC:|𝒞|
|:scD:|𝒟|
|:scG:|𝒢|
|:scJ:|𝒥|
|:scK:|𝒦|
|:scN:|𝒩|
|:scO:|𝒪|
|:scP:|𝒫|
|:scQ:|𝒬|
|:scS:|𝒮|
|:scT:|𝒯|
|:scU:|𝒰|
|:scV:|𝒱|
|:scW:|𝒲|
|:scX:|𝒳|
|:scY:|𝒴|
|:scZ:|𝒵|

### mathcal
| Trigger | Replace |
| ------- | ------- |
|:calA:|𝓐|
|:calB:|𝓑|
|:calC:|𝓒|
|:calD:|𝓓|
|:calE:|𝓔|
|:calF:|𝓕|
|:calG:|𝓖|
|:calH:|𝓗|
|:calI:|𝓘|
|:calJ:|𝓙|
|:calK:|𝓚|
|:calL:|𝓛|
|:calM:|𝓜|
|:calN:|𝓝|
|:calO:|𝓞|
|:calP:|𝓟|
|:calQ:|𝓠|
|:calR:|𝓡|
|:calS:|𝓢|
|:calT:|𝓣|
|:calU:|𝓤|
|:calV:|𝓥|
|:calW:|𝓦|
|:calX:|𝓧|
|:calY:|𝓨|
|:calZ:|𝓩|

### miscellaneous
| Trigger | Replace |
| ------- | ------- |
|:doubleslash:|⫽|
|:qed:|□|
|:vC:|Č|
|:mid:|∣|
|:not_mid:|∤|
|:infty:|∞|
|:e_acute:|é|
|:etale:|étale|
|:et:|ét|
|:^et:|ᵉᵗ|
|:_et:|ₑₜ|