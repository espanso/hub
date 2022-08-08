## What's this about?
This package ships a variety of unicode symbols commonly used by working mathematicians in a coherent syntax roughly based on LaTeX.

## Why would I need this?
It is much easier to communicate about mathematics i.e. in a math discord or via email with a collaborator when you read statements like 

    π₋ₙ(map(Σ₊Y, 𝐇(A))) ⋍ Hⁿ(Y, A)

compared to the currently widely adopted

    \pi_{-n}(map(\Sigma_{+}Y, \mathbf{H}(A))) \simeq \mathsf{H}^{n}(Y, A)

## What's inside?

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


| Trigger      | Replace   |
|--------------|-----------|
| :ket:        | ⟩         |
| :bra:        | ⟨         |
| :identity:   | 𝟙         |
| :sqrt:       | √         |
| :int:        | ∫         |
| :iint:       | ∬         |
| :iiint:      | ∭         |
| :oint:       | ∮         |
| :oint:       | ∯         |
| :oint:       | ∰         |
| :sum:        | ∑         |
| :prod:       | ∏         |
| :Box:        | □         |
| :cdot:       | ⋅         |
| :pm:         | ±         |
| :mp:         | ∓         |
| :equiv:      | ≡         |
| :nequiv:     | ≢         |
| :neq:        | ≠         |
| :approx:     | ≈         |
| :leq:        | ≤         |
| :geq:        | ≥         |
| :gg:         | ≫         |
| :ll:         | ≪         |
| :leftarrow:  | ←         |
| :rightarrow: | →         |
| :implies:    | ⇒         |
| :iff:        | ⇔         |
| :infty:      | ∞         |
| :nabla:      | ∇         |
| :partial:    | 𝜕         |
| :forall:     | ∀         |
| :exists:     | ∃         |
| :nexists:    | ∄         |
| :hslash:     | ℏ         |
| :emptyset:   | ∅         |
| :varnothing: | ∅         |
| :in:         | ∈         |
| :notin:      | ∉         |
| :smallin:    | ∊         |
| :land:       | ∧         |
| :lor:        | ∨         |
| :propto:     | ∝         |
| :neg:        | ¬         |
| :times:      | ×         |