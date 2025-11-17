# MetaPrincipia Autopoiētica — Part II: Axioms of Semantic Recursion

## §5. Aboutness Preservation & Equivalence (Twenty‑Page Slab, v0.1)

> **Thesis.** The *aboutness* of an expression is a structural invariant captured by a typed role‑hypergraph `|t|`. Synonymic torsion and well‑typed rewrites preserve aboutness up to a role‑preserving, label‑action‑equivariant isomorphism. This section axiomatizes that invariant, fixes the equivalence relation `≈̇`, and provides proofs, algorithms, and tests.

Standing notation: syntactic equality `≡`, definitional equality `≡₍def₎`, aboutness map `|·|`, aboutness equivalence `≈̇`. Levels `@ℓ` from Part I §2. Relators as in Part I §4. Tension marker `⋈` for paraconsistent zones. Calculus: 𝒞\_A.

**Page plan (20):**

1. Informal overview
2. Hypergraph model `|t|`
3. Signatures and roles
4. Translation functor from syntax
5. Preservation axioms (AP‑laws)
6. Synonymic torsion (label actions)
7. Equivariance and invariance theorems
8. Equivalence `≈̇` (definition & properties)
9. Canonicalization and normal forms
10. Paraconsistent aboutness
11. Metrics and kernels on `|t|`
12. Algorithmic extraction (linear‑time pass)
13. Synonym induction from data
14. Worked examples I
15. Worked examples II
16. Proof sketches
17. Test harness
18. BNF, schemas, tables
19. Gap register & failure modes
20. Next‑step plan & checklists

---

## Page 1 — Informal overview

Aboutness abstracts *what is talked about* from *how it is asserted*. We: (i) interpret expressions into typed role‑hypergraphs, (ii) prove that well‑typed rewrites and synonymic torsion preserve the hypergraph up to isomorphism, and (iii) define an equivalence `≈̇` used for compression, analogy, and paraphrase safety.

---

## Page 2 — Hypergraph model `|t|`

A **typed role‑hypergraph** is a tuple `H = (V,E,inc,τ,σ,ω)` where:

* `V`: vertices (anchors: entities/events/role nodes).
* `E`: hyperedges.
* `inc: E → List(V)` gives ordered incident vertices.
* `τ: V → Types` maps vertices to carrier types (Thing, RoleObj, RelObj, …).
* `σ: E → Sig` maps edges to **signatures** (labels + role schema).
* `ω: E → Weights` optional non‑negative edge weights for frequency/confidence.

We allow multi‑edges; all maps are total.

---

## Page 3 — Signatures and roles

Let `Label` be the set of relator/predicate labels and S‑Ops (`meta‑of`, `para‑through`, `anti`, `trans`, …). A **signature** is:

```
Sig ≔ (label ∈ Label, roles = ⟨ρ₁,…,ρ_k⟩, polarity ∈ {→,←,↔,·}, meta_flag ∈ {0,1})
```

Roles come from the fixed set: `Agent, Theme, Instrument, Source, Goal, Path, Location, Time, Manner, Cause, Surface`.

**Role discipline.** Edges carry ordered role positions; the `inc` list respects this order. The type assignment `τ` must agree with role constraints declared by the relator.

---

## Page 4 — Translation functor `|·| : Syn → Hyp`

Let **Syn** be the syntactic category of 𝒞\_A terms with context morphisms (substitutions). Let **Hyp** be the category of typed role‑hypergraphs with role‑preserving homomorphisms. Define a functor `|·|` on objects and morphisms:

* **Atoms** `a:Thing` → singleton vertex `v_a` with `τ(v_a)=Thing`.
* **Predicate/Relator app** `R(x₁,…,x_k)` → edge `e_R` with `σ(e_R)=(R,⟨ρ₁…ρ_k⟩,→,0)` and `inc(e_R)[i]=|x_i|`.
* **Meta‑of** → add edge labeled `meta‑of` connecting `|a|` to `r̂` where `r̂` is a reified relator node.
* **Connectives** `∧,∨,→` do not add edges; aboutness composes via disjoint union and edge sharing.
* **Quantifiers** add no new edge types; their bound variables map to existing anchor vertices, respecting capture‑avoiding substitution.
* **Regen** introduces a new vertex `v′` with lineage edge `(regen)` between old and new vertices; marked with `σ(label=regen, roles=⟨parent,child⟩)`.

Morphisms in **Syn** map to vertex/edge maps respecting `inc, τ, σ`.

---

## Page 5 — Preservation axioms (AP‑laws)

We axiomatize when `|·|` ignores syntactic variation.

**AP‑1 (Structural composition).** `|C[t]| = glue(|C|,|t|)` with pushout‑style gluing along shared anchors.

**AP‑2 (Logical neutrality).** `∧,∨,→,□,◇` do not change `σ` labels; they only affect weights `ω` by policy.

**AP‑3 (Meta‑hoist).** Hoisting to `RelObj` adds a `meta‑of` edge; underlying `R` edge remains or is referenced via reified carrier.

**AP‑4 (Para‑through).** Composition `para‑through(R,S)` induces a composed edge whose aboutness is the union of component edges modulo a coherence square. Canonical bracketing does not affect `|·|` (isomorphic hypergraphs).

**AP‑5 (Anti‑barrier).** `anti(R)` freezes evaluation; aboutness retains an edge labeled `anti` with a pointer to the frozen `R`‑edge; no change to anchors.

**AP‑6 (Typing).** If a relator is ill‑typed, no edge is formed; an error node may be inserted with flag `#` for diagnostics but excluded from `≈̇`.

---

## Page 6 — Synonymic torsion (label actions)

Let `G_syn` be a group (or monoid) of *label actions* over `Label`. An element `g ∈ G_syn` acts by `g⋅(label)`, preserving arity and role schema where declared.

**Examples.**

* Lexical synonym: `on ↔ atop` with same roles.
* Thematic alternation: `with(Agent,Instrument)` ↔ `using(Agent,Instrument)`.
* Morphological variant: `in` ↔ `inside` (language dependent).

A **torsion operator** `T_g` acts on hypergraphs by relabeling `σ(e).label := g⋅σ(e).label` where allowed; `τ,inc` unchanged.

**Well‑typedness under torsion.** A dictionary `D ⊆ Label×Label` induces a partial action; `g` is admissible on edge `e` iff role/arity constraints match.

---

## Page 7 — Equivariance and invariance theorems

**Thm 1 (Equivariance).** For any term `t` and admissible `g ∈ G_syn`, there exists a canonical isomorphism `ϕ_g : T_g(|t|) ≅ |g⋅t|` where `g⋅t` relabels surface tokens by `g` in the syntax (when defined).
*Sketch.* `|·|` is functorial and label‑local; torsion commutes with translation.

**Thm 2 (Aboutness invariance under torsion).** If `g` preserves role schemas, then `|t|` and `T_g(|t|)` are role‑preserving isomorphic; hence `t ≈̇ g⋅t`.

**Thm 3 (Associativity/Hoist neutrality).** Normalization of `para` association and `meta` hoisting yields hypergraphs isomorphic via identity on `V` and relabeling on `E` inside S‑Op layers.

---

## Page 8 — Equivalence `≈̇` (definition & properties)

**Definition (role‑preserving isomorphism).** Two hypergraphs `H=(V,E,inc,τ,σ,ω)` and `H′=(V′,E′,inc′,τ′,σ′,ω′)` are **role‑preserving isomorphic** if there exist bijections `f:V→V′`, `g:E→E′` such that: for all edges `e` and indices `i`, (i) `inc′(g(e))[i]=f(inc(e)[i])`, (ii) `τ′(f(v))=τ(v)`, (iii) `σ′(g(e)) = σ(e)` (or `= T_g(σ(e))` under a declared torsion), and optionally (iv) `ω′(g(e))=ω(e)`.

**Definition.** `t₁ ≈̇ t₂` iff their hypergraphs are role‑preserving isomorphic up to admissible label torsion.

**Props.** `≈̇` is an equivalence relation and a congruence under 𝒞\_A composition; it respects tower levels and does not identify terms that differ only by paraconsistent flags unless a collapse policy equates them.

---

## Page 9 — Canonicalization and normal forms

We fix **Aboutness Normal Form (ANF)**:

1. Right‑associate `para` inside labels.
2. Hoist `meta` edges to a designated layer.
3. Apply a **canonical dictionary** `D*` to map labels to representatives (e.g., `on/atop → on`).
4. Sort parallel edges lexicographically by `(label, roles, ids)`.

The canonicalizer `canon(|t|)` computes ANF in `O(|E| log |E|)` given `D*`. Two graphs are `≈̇` iff their ANF are identical (modulo vertex renaming).

---

## Page 10 — Paraconsistent aboutness

In `Prop_⋈`, contradictory assertions produce co‑existing edges tagged with `⋈`. Isolation means:

* Edges bearing `⋈` are excluded from ANF unless a **collapse policy** selects a side.
* Queries restricted to consistent subgraphs are unaffected.
* Aboutness equivalence ignores `⋈` flags by default; a *strict* variant `≈̇_⋈` demands equality of flags.

**Policy hook.** A labeled rule (Authority/Recency/Minimal‑change) adds `◦` to selected facts, removing `⋈` and re‑including the edge in ANF.

---

## Page 11 — Metrics and kernels on `|t|`

For retrieval and clustering:

* **Edge Jaccard**: `J(H,H′)=|E∩E′|/|E∪E′|` after ANF.
* **Role‑aware edit distance** with cost function respecting roles.
* **Weisfeiler‑Lehman kernel** adapted to `(label,roles)` edge colors.
* **Hypergraph Gromov kernel** via role‑aligned incidence tensors.
* **Aboutness cosine**: embed labels via a distributional model and average per role; compare by cosine.

All metrics are `≈̇`‑invariant by construction (computed on ANF or factor by torsion action).

---

## Page 12 — Algorithmic extraction (linear‑time pass)

Input: typed 𝒞\_A AST with resolved roles.

Algorithm (per node):

1. Emit or look up vertices for anchors.
2. For `R(x₁,…,x_k)`, emit edge with signature `σ(R)` and ordered vertex list.
3. For `meta‑of`, emit reification vertex for `R` if needed, plus `meta‑edge`.
4. For `anti`, tag edge and skip descent.
5. For `para`, record composed label or separate edges per policy.
6. For `regen`, mint new vertex and lineage edge.

Complexity: `O(|t|)` vertices/edges; memory linear in node count.

---

## Page 13 — Synonym induction from data

`G_syn` may be learned:

* **Distributional**: two labels `ℓ₁,ℓ₂` share roles and have similar contextual embeddings.
* **Alignment**: maximize aboutness overlap on a parallel corpus; propose `ℓ₁↔ℓ₂` if `J` exceeds threshold.
* **Ablation**: replace `ℓ₁` with `ℓ₂` and measure derivation invariants; accept if proofs persist.

Induced pairs are added to `D*` with confidence weights, used only when above a floor.

---

## Page 14 — Worked examples I (containment/contact)

Let `Cat, Mat, Box : Thing`.

1. `on(Cat,Mat)` vs `atop(Cat,Mat)`.

* Same roles; `D*` maps `atop→on`. `|·|` edges identical after labeling; hence `≈̇`.

2. `in(Cat,Box)` vs `inside(Cat,Box)`.

* Same roles; torsion action relabels; `≈̇`.

3. `in(Cat,Box) ∧ on(Cat,Box)`.

* Coherence requires `Surface(Box)`. If absent, mark `⋈` on one edge; strict equivalence `≈̇_⋈` distinguishes; default `≈̇` ignores flags and keeps anchors/roles.

---

## Page 15 — Worked examples II (meta & regen)

4. `meta‑of(on)(Cat, r̂)` and `why(on(Cat,Mat))`.

* First adds a `meta‑edge` to relation object; second adds no aboutness edge for `why`. They are *not* `≈̇`‑equivalent; aboutness differs.

5. `regen(Cat)` within a scene.

* Adds lineage edge `(Cat → Cat′)`; both scenes without and with regen share most edges but are not `≈̇` unless regen edges are quotiented by policy.

6. `para‑through(through, across)` vs chained path edges.

* After canonicalization, aboutness includes both edges or a composed label; either way ANF equality holds → `≈̇`.

---

## Page 16 — Proof sketches

**Equivariance (Thm 1).** Induction on syntax. Base cases map labels; inductive cases compose functorially; torsion acts only on `σ.label`, commuting with `|·|`.

**Congruence.** If `t₁≈̇t₂`, then `|C[t₁]|` and `|C[t₂]|` glue the same subgraph into the same context footprint; isomorphism extends by identity on context vertices.

**Paraconsistent isolation.** Since `⋈` lives in `σ` flags not used for vertex/role matching, default `≈̇` is insensitive to contradictory truth while sensitive to anchors/roles.

**Normalization invariance.** `para` reassociation and `meta` hoist alter only labeling strata; vertex/role incidence is unchanged.

---

## Page 17 — Test harness

Property tests:

* **P1 (Functoriality).** `canon(|C[t]|) = glue(canon(|C|), canon(|t|))`.
* **P2 (Torsion invariance).** For each `(ℓ₁,ℓ₂)∈D*`, replacing labels yields `≈̇`.
* **P3 (Para hoist).** Normalization leaves `|·|` unchanged up to isomorphism.
* **P4 (Paraconsistency).** Introducing `⋈` does not affect `≈̇` unless strict mode.
* **P5 (Idempotence).** `canon(canon(H))=canon(H)`.

Fuzzing:

* Random relator graphs with role constraints; apply random torsion/assoc/hoist; check invariants.

Benchmarks:

* `Edge Jaccard`, `WL kernel` correlation with human paraphrase sets.

---

## Page 18 — BNF, schemas, tables

**BNF (delta for aboutness hooks).**

```
EdgeLabel  ::= BaseRel | MetaOp | Regen | Anti
MetaOp     ::= 'meta-of' | 'para-through' | 'trans' | 'anti'
AboutEdge  ::= EdgeLabel '(' ArgList ')'
```

**JSON schema — ConceptUnits, RelationshipEdges, GapUnits.**

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "AboutnessExports",
  "type": "object",
  "properties": {
    "ConceptUnits": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {"type": "string"},
          "term": {"type": "string"},
          "text": {"type": "string"},
          "source_file": {"type": "string"},
          "location": {"type": "string"},
          "kind": {"type": "string"},
          "types": {"type": "array", "items": {"type": "string"}}
        },
        "required": ["id","term","text","source_file","location"]
      }
    },
    "RelationshipEdges": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {"type": "string"},
          "source": {"type": "string"},
          "target": {"type": "string"},
          "label": {"type": "string"},
          "roles": {"type": "array", "items": {"type": "string"}},
          "polarity": {"type": "string"},
          "meta_flag": {"type": "integer"},
          "weight": {"type": "number"},
          "evidence": {"type": "string"}
        },
        "required": ["id","source","target","label"]
      }
    },
    "GapUnits": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {"type": "string"},
          "concept_A": {"type": "string"},
          "concept_B": {"type": "string"},
          "gap_type": {"type": "string"},
          "evidence_location": {"type": "string"}
        },
        "required": ["id","concept_A","concept_B","gap_type"]
      }
    }
  },
  "required": ["ConceptUnits","RelationshipEdges","GapUnits"]
}
```

**Tables.**

* Role inventory and constraints.
* Torsion dictionary `D*` with confidence scores.
* Canonicalization pipeline steps.

---

## Page 19 — Gap register & failure modes

**G1. Ambiguous role schemas.** Some synonyms alter roles (`with` vs `using`). Mark as *non‑admissible torsion* unless a coercion exists.

**G2. Polysemy.** Label conflates senses; require sense tags or context disambiguation before torsion.

**G3. Hidden anchors.** Ellipsis may omit vertices; add *implicit* anchors with low weight `ω`.

**G4. Cross‑level leakage.** `meta` edges incorrectly collapsed into object level; tower guard prevents this.

**G5. Paraconsistent bleed.** Collapse policies must be explicit; otherwise ANF excludes `⋈` edges.

---

## Page 20 — Next‑step plan & checklists

**Next‑step plan (≤3 actions).**

1. Implement `|·|` extractor and ANF canonicalizer with torsion dictionary `D*`.
2. Prove/verify Thm 1–3 via property testing on synthetic corpora.
3. Integrate metrics (WL kernel + Jaccard) into retrieval and analogy tasks.

**Dev checklist.**

* [ ] Unit tests for AP‑laws.
* [ ] Torsion safety: role/arity validator.
* [ ] Strict vs default `≈̇` switches.
* [ ] Performance: linear pass + `O(|E| log |E|)` canonicalizer.
* [ ] Exporters to JSON schema above.

---

*End of Part II §5: Aboutness Preservation & Equivalence (20pp v0.1).*



---

# MetaPrincipia Autopoiētica — Part II: Axioms of Semantic Recursion

## §6. Recursive Axioms of Meaning — Extensional · Intensional · Aboutness; Composition Laws; Regen Coherence (Twenty‑Page Slab, v0.1)

> **Thesis.** Meaning in 𝒞\_A is a **tri‑layered** semantic object `(⟦t⟧_E, ⟦t⟧_I, |t|)` where: `⟦·⟧_E` is extensional (model‑theoretic), `⟦·⟧_I` is intensional (world‑indexed), and `|·|` is aboutness (typed role‑hypergraph). Axioms ensure these layers compose homomorphically, align under modal/context shifts, and **cohere under regeneration** (object creation) and meta‑operators. The section states the axioms, gives categorical anchors, and proves layer‑compatibility and coherence theorems.

**Standing from Part I/§5:** sorts, roles, relators; tower stratification; paraconsistent `Prop_⋈`; aboutness `≈̇`; Scene category; torsion actions.

**Page map (20):**

1. Layered semantics overview
2. Extensional layer `E`
3. Intensional layer `I`
4. Aboutness layer `A`
5. Product category and master functor
6. Core recursive axioms (RA‑block 1)
7. Logical connectives & modality (RA‑block 2)
8. Relators & composition (RA‑block 3)
9. Meta‑operators (RA‑block 4)
10. Interrogatives (RA‑block 5)
11. Regen operator semantics (state, coalgebra)
12. Regen coherence across layers
13. Fixpoints (μ, ν) and guarded recursion
14. Normalization & layer soundness
15. Categorical proofs (naturality, monoidality)
16. Paraconsistent compatibility
17. Algorithms & evaluation contexts
18. Worked examples
19. Test harness & checklists
20. Next‑step plan

---

## Page 1 — Layered semantics overview

We interpret each well‑typed term `t` as a **triple**

```
S(t) = (⟦t⟧_E, ⟦t⟧_I, |t|) ∈ Ext × Int × Hyp
```

with a **master functor** `S : Syn → Ext×Int×Hyp` from syntax to the product category. Projection functors are `π_E, π_I, π_A`. Composition laws must satisfy **Tri‑Homomorphism**:

```
S(C[t1,…,tn]) = F_C(S(t1),…,S(tn))
```

for a constructor‑specific functor `F_C` that acts componentwise and respects level guards. This section makes `F_C` explicit for 𝒞\_A’s constructors.

---

## Page 2 — Extensional layer `E`

A classical Tarskian model `M = ⟨D, P^M, R^M, …⟩` with domain `D≠∅`, primitive predicates/relators interpreted as relations over `D` with typed roles. Denotations under assignment `g`:

```
⟦a⟧_E = g(a) ∈ D
⟦P(a)⟧_E = 1 ⇔ ⟦a⟧_E ∈ P^M
⟦R(a,b)⟧_E = 1 ⇔ (⟦a⟧_E,⟦b⟧_E) ∈ R^M
```

Quantifiers as usual; modalities via `□,◇` deferred to Int layer but admissible by lifting to Kripke frames when needed.

---

## Page 3 — Intensional layer `I`

A Kripke/Montague structure `K = ⟨W, R_acc, D_w, …⟩` with constant or varying domains. Intensions are world‑indexed functions:

```
⟦t⟧_I : W → Val
⟦φ⟧_I(w) ∈ {0,1}
⟦□φ⟧_I(w)=1 ⇔ ∀w′(wR_acc w′ → ⟦φ⟧_I(w′)=1)
⟦◇φ⟧_I(w)=1 ⇔ ∃w′(wR_acc w′ ∧ ⟦φ⟧_I(w′)=1)
```

We require **projection compatibility**: if `I` has constant domains and `E` picks a base world `w0`, then `⟦·⟧_E = ⟦·⟧_I(w0)` on ground atoms.

---

## Page 4 — Aboutness layer `A`

`|t|` is a typed role‑hypergraph (Part II §5). The translation is compositional; logical connectives do not introduce new relation edges; meta‑operators produce specialized edges. We write `canon(|t|)` for Aboutness Normal Form (ANF). The layer provides *structure* independent of truth.

---

## Page 5 — Product category and master functor

Let `Ext, Int, Hyp` be categories of the three layers. The product category `Ext×Int×Hyp` has objectwise identities and composition. Define `S : Syn → Ext×Int×Hyp` by constructors:

```
S(a) = (⟦a⟧_E, ⟦a⟧_I, |a|)
S(R(t1,t2)) = (R_E(…), R_I(…), |R|(…))
…
```

**Axiom RA‑0 (Tri‑Functoriality).** `S` preserves identities and composition of substitutions; projections `π_*∘S` match the per‑layer clauses below.

---

## Page 6 — Core recursive axioms (RA‑block 1)

All axioms assume well‑typedness and tower guards.

**RA‑1 (Atomic concordance).** For atoms/predicates/relators, `π_E∘S` matches Tarskian truth, `π_I∘S` matches Kripke intensions, `π_A∘S` yields the signature‑respecting hyperedge.

**RA‑2 (Compositionality).** For any constructor `C`, `S(C(t1,…,tn)) = F_C(S(t1),…,S(tn))` where `F_C` acts componentwise with layer‑appropriate operators defined in RA‑blocks below.

**RA‑3 (Projection soundness).** If `⟦φ⟧_E=1` then `⟦φ⟧_I(w0)=1` for the chosen base world `w0`; conversely when `I` has constant domains and rigid designators.

**RA‑4 (Aboutness homomorphism).** The aboutness translation is a *lax monoidal functor*: `|t⊗u| ≅ |t| ⊔ |u|` with edge disjoint union and role‑consistent gluing.

---

## Page 7 — Logical connectives & modality (RA‑block 2)

**RA‑5 (Booleans).**

```
⟦¬φ⟧_E = 1-⟦φ⟧_E;   ⟦φ∧ψ⟧_E = min(⟦φ⟧_E,⟦ψ⟧_E);   …
⟦¬φ⟧_I(w) = 1-⟦φ⟧_I(w);  …
|¬φ| = |φ|;  |φ∧ψ| = glue(|φ|,|ψ|);  …
```

**RA‑6 (Quantifiers).** Usual Tarskian/Montague clauses; aboutness does not add edges for binding, only anchor references.

**RA‑7 (Modal coherence).** If `⟦φ⟧_I` is constant across `R_acc`‑reachable worlds, then `⟦□φ⟧_I = ⟦φ⟧_I` and aboutness unchanged: `|□φ| ≈̇ |φ|`.

**RA‑8 (Paraconsistent projection).** In `Prop_⋈`, `⟦·⟧_E` and `⟦·⟧_I` are evaluated per policy; `|·|` ignores `⋈` flags unless strict mode is enabled.

---

## Page 8 — Relators & composition (RA‑block 3)

**RA‑9 (Relator application).**

```
⟦R(a,b)⟧_E=1 ⇔ (⟦a⟧_E,⟦b⟧_E)∈R^M
⟦R(t1,t2)⟧_I(w) = 1 ⇔ (⟦t1⟧_I(w),⟦t2⟧_I(w)) ∈ R^M_w
|R(t1,t2)| adds edge σ(R) incident to |t1|,|t2|
```

**RA‑10 (Para‑through = composition).**

```
⟦para‑through(R,S)⟧_E = S_E∘R_E;
⟦para‑through(R,S)⟧_I(w) = S_I(w)∘R_I(w);
|para‑through(R,S)| ≈̇ compose(|R|,|S|)
```

**RA‑11 (Associativity).** Composition reassociation preserves all layers; aboutness up to isomorphism (ANF).

---

## Page 9 — Meta‑operators (RA‑block 4)

**RA‑12 (meta‑of).**

```
⟦meta‑of(R)(a, r̂)⟧_E = 1 ⇔ holds_E(r̂, ⟦a⟧_E)
⟦meta‑of(R)(a, r̂)⟧_I(w) = 1 ⇔ holds_I(r̂, ⟦a⟧_I(w))
|meta‑of(R)(a, r̂)| adds meta‑edge from |a| to r̂
```

**RA‑13 (anti).** Freezes evaluation: extensional/intensional clauses are **undefined** until barrier discharge; aboutness carries an `anti` edge with pointer to the frozen site.

**RA‑14 (trans).** Orientation/dual operator; semantics given by declared relator class; aboutness relabels (`trans` flag) without changing anchors.

---

## Page 10 — Interrogatives (RA‑block 5)

**RA‑15 (Question projection).**

```
⟦what(φ)⟧_E = Dom solutions of φ in M (set‑valued)
⟦what(φ)⟧_I(w) = world‑indexed solution set
|what(φ)| = |φ|
```

**RA‑16 (Meta‑interrogatives).** `meta‑what(R)` asks over relations‑as‑objects; aboutness adds a meta‑edge; extensional/intensional return sets of relation objects.

---

## Page 11 — Regen operator semantics (state, coalgebra)

`regen : Thing → Thing` creates a fresh object linked by lineage.

**State model.** Configurations `(Σ, t)` with `Σ = ⟨N,L,K⟩` (name supply, lineage, knowledge). Small‑step (from §4 fix):

```
(Σ, regen(x)) ↦ (Σ[x′:=fresh], x′),   L := L ∪ {(x→x′)}
```

**Coalgebraic view.** Let `F(X) = Σ × X`. Programs denote **coalgebras** `c : X → F(X)`. `regen` corresponds to a coalgebra map that extends lineage.

**RA‑17 (Regen extensional).**

```
⟦regen(a)⟧_E = a′ with a′∉D, extend M to M′ with D′=D∪{a′}, lineage(a,a′)
```

**RA‑18 (Regen intensional).**

```
⟦regen(a)⟧_I(w) = a′_w, coherent across w by policy (rigid vs non‑rigid creation)
```

**RA‑19 (Regen aboutness).** `|regen(a)|` adds vertex `v′` and edge labeled `regen(parent,child)` from `|a|` to `v′`.

---

## Page 12 — Regen coherence across layers

**Theorem RC‑1 (Lineage coherence).** If `⟦regen(a)⟧_E = a′` and `⟦regen(a)⟧_I(w)=a′_w` with rigid policy (`a′_w = a′`), then there exists a unique vertex `v′` such that anchors align: `v′` denotes `a′` and supports all incident edges of `|regen(a)|`.

**Theorem RC‑2 (Aboutness preservation under regen contexts).** For any context `C[·]` that does not discard the child, `|C[regen(a)]|` ≈̇ `glue(|C[a]|, regen‑edge)` (ANF equal modulo new vertex id). Proof: functoriality of `|·|` and locality of regen.

**RC‑3 (Commutation with composition).** For relators `R`, `|R(regen(a), b)|` equals ANF of `|regen(a)| ⊔ |R(a,b)|` with the child wired in place of `a` where the context demands; extensional/intensional clauses use `a′` consistently.

---

## Page 13 — Fixpoints (μ, ν) and guarded recursion

Add μ‑calculus style forms for recursive meaning:

```
μX. φ(X)   (least fixpoint)
νX. φ(X)   (greatest fixpoint)
```

**RA‑20 (Guardedness).** Every recursive variable occurrence is under a relator or modality that is **contractive** in the layer metric (see Page 11 metrics), ensuring existence/uniqueness of fixpoints.

Layer clauses:

* **Extensional:** interpret as least/greatest sets satisfying the monotone operator induced by `φ`.
* **Intensional:** do this pointwise over worlds (or over `R_acc`‑closed sets of worlds).
* **Aboutness:** union of the limit of finite unfoldings; ANF stabilizes under canonical edge deduplication.

**Fixpoint coherence.** Projections of `S(μX.φ)` equal the corresponding fixpoints of projected operators.

---

## Page 14 — Normalization & layer soundness

**Theorem (Layer soundness of normalization).** Rewriting by ℛ\_A (assoc/hoist/factor/β/fold‑unfold) preserves all three layers: extensional truth values, intensional intensions, and aboutness ANF. Sketch: each rule is either a congruence in `Ext/Int` or a label/topology change that `Hyp` quotients by isomorphism.

**Corollary (Tri‑soundness).** If `t ≡ t′` by ℛ\_A, then `S(t) = S(t′)` in `Ext×Int×Hyp` modulo isomorphism in the `Hyp` component.

---

## Page 15 — Categorical proofs (naturality, monoidality)

Let `Scene` be the category of role‑typed anchors and relators (Part I). Then:

* `π_E∘S` is a (lax) **monoidal functor** preserving `⊗` up to model‑specific isomorphism.
* `π_I∘S` is a **Kripke‑enriched** functor respecting `R_acc`.
* `π_A∘S` is a **lax monoidal functor** `Syn→Hyp` with `|t⊗u| ≅ |t| ⊔ |u|`.
* `S` factors through the product and preserves identities and composition.

**Naturality of meta‑of.** The square with reification carrier commutes; `meta` is an endofunctor on the relator subcategory with a natural transformation to satisfaction.

---

## Page 16 — Paraconsistent compatibility

Under `Prop_⋈`:

* `π_E, π_I` evaluate with consistency operator `◦` and collapse policy when needed.
* `π_A` excludes `⋈` edges by default; strict mode `≈̇_⋈` requires flag equality.

**Theorem (Non‑explosion of S).** If `Γ ⊢⋈ φ` and `Γ ⊢⋈ ¬φ`, then neither projection forces equality of contradictory layer values unless `◦φ` is asserted by policy. `Hyp` remains well‑defined and finite.

---

## Page 17 — Algorithms & evaluation contexts

**Call‑by‑meaning** evaluation contexts (Part I §4) propagate layer effects in a left‑to‑right, barrier‑respecting order. Implementation outline:

1. Compute `S` bottom‑up; memoize per subterm.
2. Apply ℛ\_A normalization; re‑use cached `|·|` with ANF to avoid recompute.
3. For regen, thread state `Σ`; for pure expressions reuse `Σ`.

Complexities: extensional truth checking depends on model ops; intensional `O(|W|)` worst‑case; aboutness linear in edges with `O(|E| log |E|)` for ANF.

---

## Page 18 — Worked examples

Let `Cat, Mat, Box` be anchors; `Sit:Thing→Prop`; relators `on, in`.

1. **Simple composition.**

```
S(on(Cat,Mat)) = (1_M, 1_K(w0), edge(on; Cat→Mat))
```

2. **Meta‑talk.**

```
S(meta‑of(on)(Cat, r̂_on)) = (holds_E(r̂_on, Cat), holds_I(…), meta‑edge(Cat→r̂_on))
```

3. **Regen in context.**

```
S(on(regen(Cat), Mat)) = (on(a′,Mat), on_I(a′_w,Mat_w), |regen(Cat)| ⊔ edge(on; a′→Mat))
```

4. **Fixpoint (path‑reachability).** Let `φ(X) = (x=y) ∨ ∃z (R(x,z) ∧ X(z,y))`.

```
S(μX.φ) projects to the usual reflexive‑transitive closure in Ext/Int; aboutness unions edges of finite R‑paths.
```

---

## Page 19 — Test harness & checklists

**Property tests.**

* Tri‑functoriality: `S(C[t]) = F_C(S(t))` componentwise.
* Normalization soundness: `S(t)=S(norm(t))`.
* Regen coherence: `S(C[regen(a)])` equals stitched result.
* Torsion invariance: `π_A` unchanged up to label action; `π_E, π_I` unchanged when torsion is a definitional synonym.
* Fixpoint convergence: unfolding stabilizes under ANF and extensional monotonicity.

**Runtime checks.**

* Layer caches hit rate; ANF idempotence; paraconsistent isolation size.

---

## Page 20 — Next‑step plan

1. Implement `S` with memoization and ANF caches; expose hooks for `meta`, `para`, `regen`.
2. Build fixpoint engine with guardedness checks; provide per‑layer evaluators.
3. Add model policies for regen rigidity and paraconsistent collapse; benchmark invariants.

---

*End of Part II §6: Recursive Axioms of Meaning (20pp v0.1).*


---

# MetaPrincipia Autopoiētica — Part II: Axioms of Semantic Recursion

## §7. Meta‑Coherence & Collapse Control — Paraconsistent Tension (⋈), Barrier Logic, Safe Self‑Reference (Twenty‑Page Slab, v0.1)

> **Thesis.** Meta‑coherence requires isolating contradiction, constraining meta‑level flow, and admitting controlled collapse. We provide a paraconsistent core with a **barrier calculus** and **policy‑driven collapse**. Safe self‑reference uses tower stratification, reification carriers, and guarded fixed points.

**Standing context.** 𝒞\_A syntax; levels `@ℓ`; `meta‑of`, `para‑through`, `anti⟨·⟩`; aboutness `|·|`; rewrite system ℛ\_A.

**Page plan (20):**

1. Overview & goals
2. Judgments & symbols
3. Paraconsistent base (LFI‑style)
4. Semantics of tension (⋈)
5. Isolation discipline & zones
6. Barrier calculus (syntax/typing)
7. Barrier small‑step SOS
8. Collapse policies (Authority/Recency/Minimal‑Change)
9. Non‑explosion & coherence lemmas
10. Meta‑operator interaction laws
11. Tower rule & predicativity guard
12. Safe self‑reference schemas
13. Rewrite/coherence with ℛ\_A
14. Algorithms (detection/collapse)
15. Worked examples I (Liar/Russell variants)
16. Worked examples II (dialogue & source fusion)
17. Categorical view (adhesive subcat, DPO)
18. Proof sketches
19. Test harness
20. Next‑step plan

---

## Page 1 — Overview & goals

We aim to: (i) permit contradictory content without trivialization, (ii) preserve compositional meaning outside contradictory loci, (iii) provide explicit, auditable **collapse** mechanisms that reconcile conflicts, and (iv) enable **safe self‑reference** without meta‑level leakage.

---

## Page 2 — Judgments & symbols

Judgments over context `Γ`:

* Classical: `Γ ⊢ φ`
* Paraconsistent: `Γ ⊢⋈ φ`
* Consistency: `Γ ⊢ ◦φ` ("φ behaves classically inside Γ")
* Collapse decision: `Γ ⊢ choice(φ) ∈ {φ,¬φ}`

Markers and operators:

* Tension flag `⋈` on edges/facts.
* Barrier `anti⟨t⟩` blocks evaluation inside `t`.
* Reify `RelObj, PropObj` carriers.
* Levels `@ℓ` with up‑lift `↑` and explicit down‑map `↓` only on approved carriers.

---

## Page 3 — Paraconsistent base (LFI‑style)

Language: propositional with `¬,∧,∨,→`, extended later with quantifiers and relators.

Sequent rules (selected):

```
Γ ⊢⋈ φ      Γ ⊢⋈ ψ          Γ ⊢⋈ φ
———————  ————————————   ————————————————
Γ ⊢⋈ φ∧ψ     Γ ⊢⋈ φ∨ψ        Γ, φ ⊢⋈ ψ ⇒ Γ ⊢⋈ φ→ψ

Γ ⊢⋈ φ    Γ ⊢⋈ ¬φ     (no EFQ)
———————————————
Γ ⊬⋈ ψ

Γ ⊢ ◦φ    Γ ⊢⋈ φ      Γ ⊢⋈ ¬φ
———————————————  —————————
Γ ⊢ φ           Γ ⊢ ¬φ
```

`◦` is not derivable from `¬¬φ→φ`; it is a **primitive** predicate licensed by policy or meta‑proof.

Sound semantics given on Page 4.

---

## Page 4 — Semantics of tension (⋈)

Use **pair‑of‑sets semantics** (Logics of Formal Inconsistency): a valuation `v` assigns each formula a pair `(T,F)` with `T,F ⊆ World` (or booleans in a single world). Truth: `φ` holds iff `w∈T`; falsity iff `w∈F`. Tension means both.

Connectives (single world case):

```
T(¬φ)=F(φ)     F(¬φ)=T(φ)
T(φ∧ψ)=T(φ)∧T(ψ)     F(φ∧ψ)=F(φ)∨F(ψ)
T(φ∨ψ)=T(φ)∨T(ψ)     F(φ∨ψ)=F(φ)∧F(ψ)
T(φ→ψ)=F(φ)∨T(ψ)     F(φ→ψ)=T(φ)∧F(ψ)
```

`◦φ` is true iff not (T(φ) and F(φ)). Explosion is blocked because entailment uses truth preservation **without** the `T(φ)∧F(φ)⇒⊤` shortcut.

---

## Page 5 — Isolation discipline & zones

Partition a scene into **zones** `Z` with membranes `∂Z`. Each assertion edge belongs to exactly one zone. Rules:

* `⋈` stays **local**: contradictory facts must share a zone id.
* **Zone monotonicity**: information can be **imported** into a zone through membranes only via **gates** (barriers discharged) or **views** (read‑only projections).
* **No cross‑zone EFQ**: contradictions in `Z` do not license theorems in `Z′≠Z`.

Aboutness records `zone(e)`; canonicalization of `|·|` ignores `⋈` edges unless strict mode.

---

## Page 6 — Barrier calculus (syntax/typing)

Syntax:

```
anti⟨t⟩      barrier introduction
release⟨t⟩   schedule a discharge of the nearest enclosing barrier
fuse⟨t,u⟩    merge two zones under policy
```

Typing (sketch):

```
Γ ⊢ t:τ ⇒ Γ ⊢ anti⟨t⟩ : τ^bar
Γ ⊢ t:τ^bar ⇒ Γ ⊢ release⟨t⟩ : τ
Γ ⊢ t:Zone, u:Zone ⇒ Γ ⊢ fuse⟨t,u⟩ : Zone
```

Barred types `τ^bar` are **opaque**: no eliminations except `release` and transport through `anti`‑safe operators.

---

## Page 7 — Barrier small‑step SOS

Configurations `(Σ, t)` with zone stack `Zs`. Rules:

```
[E‑Anti]
(Σ; Zs, anti⟨t⟩) ↦ (Σ; Zs·Z_new, t)     // enter new isolated zone

[E‑Release]
(Σ; Zs·Z, release⟨v⟩) ↦ (Σ; Zs, v)       // leave zone when value reached

[E‑Fuse]
(Σ; Zs, fuse⟨Z_i, Z_j⟩) ↦ (Σ; Zs[Z_i←Z_i∪Z_j], unit)  // policy‑checked
```

Evaluation under barriers: reductions **cannot** cross `anti` unless the redex is inside the same zone. Rewriting rules ℛ\_A apply **per zone**.

---

## Page 8 — Collapse policies

A **collapse** resolves `⋈` into a classical commitment. Policies are explicit predicates over `(Γ, φ, meta)` returning an action.

* **Authority**: prefer facts with higher source authority metric.
* **Recency**: prefer newest timestamp.
* **Minimal‑Change**: choose resolution minimizing a change functional `Δ(Γ, choice)` (e.g., Hamming distance on edge truth values weighted by confidence).

Formal rule:

```
[Collapse]
Γ ⊢⋈ φ   Γ ⊢⋈ ¬φ   Policy(Γ,φ)=pick(χ) ∈ {φ,¬φ}
———————————————————————————————————————————————
Γ ⊢ ◦φ   Γ ⊢ χ
```

`Policy` can be multi‑criteria with ties → postpone or split into subzones.

---

## Page 9 — Non‑explosion & coherence lemmas

**Lemma 1 (Local Non‑Explosion).** If `Γ ⊢⋈ φ` and `Γ ⊢⋈ ¬φ` in zone `Z`, then for any `ψ` not in `Z`, `Γ ⊬ ψ`. Proof by semantics: truth of `ψ` is independent of `T(φ)∧F(φ)` in `Z`.

**Lemma 2 (Barrier Preservation).** If `Γ ⊢ t:τ` and `t ↦ t′` under zone stack `Zs`, then the top of `Zs` is unchanged unless the step is `[E‑Release]`. Hence isolation is stable.

**Lemma 3 (Collapse Soundness).** If `[Collapse]` fires, then `◦φ` holds and standard classical rules for `φ` are admissible within `Z`.

---

## Page 10 — Meta‑operator interaction laws

**M‑1 (Meta commutes with isolation).** `anti⟨meta‑of(R)(…)⟩ ≡ meta‑of(R)(anti⟨…⟩)` up to barrier annotations if `R` has no side effects. Aboutness adds the same meta edge; zone ids differ only by the enclosing zone.

**M‑2 (Para inside barriers).** `para‑through` composes only edges **within** the same zone; cross‑zone composition requires `fuse` or a read‑only **view** morphism.

**M‑3 (Trans & Anti).** `trans(anti⟨R⟩) ≡ anti⟨trans(R)⟩` by value opacity.

---

## Page 11 — Tower rule & predicativity guard

Levels `@ℓ` with up‑lift on meta‑constructors. **No operator** consumes arguments of strictly greater level without explicit `↓` on approved carriers.

**Predicativity Guard.** Quantification over `RelObj_ℓ` lifts the formula to level `ℓ+1`. No carrier maps `Prop@ℓ+1` that quantifies over *all* `RelObj_ℓ` back to level `ℓ`. This blocks self‑totalization.

**Lemma (Non‑collapse of tower).** In closed, well‑typed terms with no `↓`, evaluation cannot produce a same‑level self‑application of a meta‑lift.

---

## Page 12 — Safe self‑reference schemas

**Diagonal with carrier.** For a predicate `P@ℓ` over `PropObj_ℓ`, define at `ℓ+1`:

```
Diag_P ≔ λx. P(quote(x))
```

Then talk about `P` applied to its own quotation lives at `ℓ+1`. Any truth predicate `Tr@ℓ+1` may discuss `φ@ℓ` via reification `quote(φ)` without violating the guard.

**Guarded Y.** A fixpoint at level `ℓ` uses a guarded combinator `Y_bar` that forces **one barrier** between self‑calls:

```
Y_bar(F) ≔ let f = λx. F(anti⟨x⟩) in f(μ)  // μ is a seed; recursion peers behind a barrier
```

Termination/normalization arguments use barrier opacity + ℛ\_A termination per zone.

---

## Page 13 — Rewrite/coherence with ℛ\_A

ℛ\_A rules (assoc/hoist/factor/β/fold‑unfold) operate **per zone**. Critical pairs across zones cannot arise. Confluence is inherited zone‑wise; global confluence holds up to independent interleaving.

**Theorem (Normalization with barriers).** If each zone’s rewrite system terminates and is locally confluent, then the whole evaluation is strongly normalizing w\.r.t. a lexicographic sum over zones.

---

## Page 14 — Algorithms (detection/collapse)

**Tension detection.** Maintain for each zone `Z` the set `C_Z = {φ | Γ ⊢⋈ φ ∧ Γ ⊢⋈ ¬φ}`. Update incrementally as facts arrive.

**Collapse solver.** For each `φ∈C_Z`, compute candidates scored by `Policy`. Choose argmax; if tie, spawn subzones `Z₁,Z₂` with opposite choices.

**Complexity.** Detection is linear in updates; policy scoring depends on feature computation (authority, time, Δ). Collapse is per‑formula; parallelizable across `C_Z`.

---

## Page 15 — Worked examples I (Liar/Russell)

**Liar (safe form).** Let `Say(α,φ)` and `Truth(r̂,φ)` at level `ℓ+1`. The sentence “This is false” becomes a reified object `s` with `Says(s,¬True(s))`. Contradiction stays in zone `Z_liar` with `⋈`. No cross‑zone explosion. Collapse requires a policy; otherwise remain paraconsistent.

**Russell‑like.** `R(x) ≔ ¬In(x,x)` with set membership reified at `ℓ+1`. Self‑membership queries route through carriers and live in a dedicated zone; blocked from collapsing the universe by the predicativity guard.

---

## Page 16 — Worked examples II (dialogue & source fusion)

Two sources assert `at(Location, Event)` and its negation with different timestamps and authorities. Zones per source; `fuse` under policy → collapse picks the more authoritative/recent; `◦` introduced; downstream deductions become classical in fused zone while other zones remain unaffected.

---

## Page 17 — Categorical view (adhesive subcategory, DPO)

Let `Hyp` be the category of typed role‑hypergraphs. Barriers define an **adhesive subcategory** where pushouts along monos exist (zones as components). Rewriting is **double‑pushout (DPO)** inside zones. Collapse corresponds to a **pushout complement** choice guided by `Policy`. Functor `S` preserves these constructions up to isomorphism.

---

## Page 18 — Proof sketches

* **Local Non‑Explosion** by pair‑of‑sets semantics; entailment ignores `T∧F` unless `◦`.
* **Barrier Preservation** by induction on evaluation steps; only `[E‑Release]` alters the zone stack.
* **Collapse Soundness** by replacing paraconsistent evaluation with classical inside a zone after `◦φ`.
* **Tower Non‑Collapse** by level‑monotone evaluation; no rule decreases level without `↓`.

---

## Page 19 — Test harness

**Property tests.**

* P1: Contradiction isolation — add `φ,¬φ` in `Z`; verify unrelated `ψ` in `Z′` is unchanged.
* P2: Barrier opacity — no redex crosses `anti`.
* P3: Collapse soundness — after policy, classical derivations hold; before, EFQ blocked.
* P4: Tower guard — attempts at self‑totalization fail typing.
* P5: Zone‑wise confluence — normalization commutes across zones.

**Metrics.** Tension volume `|C_Z|`, collapse rate, average time to resolution, cross‑zone flux.

---

## Page 20 — Next‑step plan

1. Implement barrier stack and zone‑tagged facts with incremental tension detection.
2. Provide pluggable policies with proofs of admissibility; log decisions.
3. Integrate with §5/§6 layers; export strict vs default `≈̇` and collapse traces for audits.

---

*End of Part II §7: Meta‑Coherence & Collapse Control (20pp v0.1).*


---

# MetaPrincipia Autopoiētica — Part II: Axioms of Semantic Recursion

## §8. The Regen Monad & Constructive Incompleteness — `T = R∘U` as Semantic Compressor; Incompleteness as Generative Affordance (Twenty‑Page Slab, v0.1)

> **Thesis.** Meaning systems that *rebuild themselves* benefit from **controlled incompleteness**. We formalize a regeneration pipeline as a **monad** `T = R∘U` where `U` *unbinds/unfolds* structure into latent carriers, and `R` *rebinds/regenerates* canonical structure. The monad preserves aboutness, contracts intensional variation, and exposes a measured gap that fuels generative extension. Incompleteness is not a bug but an **affordance**: an actionable deficit that enables invention while maintaining meta‑coherence.

Standing context: 𝒞\_A, §5 aboutness hypergraphs, §6 tri‑layer semantics `(⟦·⟧_E, ⟦·⟧_I, |·|)`, §7 barriers & tension `⋈`.

**Page plan (20):**

1. Motivation & intuition
2. Operators `U` and `R` (typing & intent)
3. Category‑theoretic definition of `T`
4. Unit `η` and multiplication `μ`
5. Laws and coherence
6. Tri‑layer semantics of `U,R,T`
7. Aboutness invariants & compression
8. Regen evaluation & small‑step SOS
9. Constructive incompleteness schema
10. Gaps, affordances, and policies
11. Algebra/coalgebra views (EM/Kleisli)
12. Learning view: bottlenecks & priors
13. Proof sketches (soundness & stability)
14. Algorithms & complexity
15. Worked examples I (lexical/scene)
16. Worked examples II (graphs/programs)
17. Metrics & diagnostics
18. Failure modes & guards
19. Test harness
20. Next steps

---

## Page 1 — Motivation & intuition

Natural systems repeatedly **compress** experience and **re‑generate** structure suitable for reuse. We capture this as `U` (unbinding/unfolding → latent) followed by `R` (reconstruction/regeneration → canonical). The composite `T = R∘U` acts as a *semantic compressor* that also reveals **what is missing**. The missing part is an explicit **incompleteness budget** that can be spent to explore alternatives, invent definitions, or reconcile contradictions under §7.

---

## Page 2 — Operators `U` and `R` (typing & intent)

We assume kinds `Thing, Rel, Prop, Scene` and aboutness graphs `Hyp`.

* **Unbinder `U`**: erase surface topology, collect latent carriers.

```
U : Scene → Latent,   U : Hyp → Codes
```

`Latent` is a typed carrier (e.g., embeddings, skeletons, templates); `Codes` is a compressed description (roles, labels, hashes, stats).

* **Regenerator `R`**: produce canonical structure from latents + policy.

```
R : Latent → Scene,   R : Codes → Hyp
```

`R` may depend on a policy π: tie‑breaking, dictionary choice, granularity, collapse (§7). We write `R_π` when policies matter.

**Typing (core cases).**

```
Γ ⊢ s : Scene     ⇒ Γ ⊢ U s : Latent
Γ ⊢ c : Codes     ⇒ Γ ⊢ R c : Hyp
Γ ⊢ x : Thing     ⇒ Γ ⊢ U x : Key ;  Γ ⊢ R (Key) : Thing′
```

Keys are reidentification tokens enabling lineage tracking.

---

## Page 3 — Category‑theoretic definition of `T`

Let `𝒮` be the category of well‑typed scenes; let `𝓛` be latents; `U : 𝒮 → 𝓛`, `R : 𝓛 → 𝒮`. The composite `T = R∘U : 𝒮 → 𝒮`.

We equip `T` with monad structure `(T, η, μ)` on `𝒮`:

* `η : Id_𝒮 ⇒ T` (*unit*).
* `μ : T∘T ⇒ T` (*multiplication*).

Intuition: `η` injects a scene as already canonical; `μ` ensures **two passes of compress‑regenerate** equal a single pass up to declared equivalences.

---

## Page 4 — Unit `η` and multiplication `μ`

**Unit `η`.** For each scene `s`, pick a canonical latent `κ(s)` s.t. `R(κ(s)) = s` in ANF. Define `η_s : s → R(U(s))` as the isomorphism witnessing that `R(U(s))` equals `s` **modulo ANF** when no policy changes occur. Practically: `η` labels edges with stable ids and copies anchors.

**Multiplication `μ`.** For each `s`,

```
μ_s : R(U(R(U(s)))) → R(U(s))
```

defined by *latent idempotence*: a second `U` compresses what is already canonical; `R` then reconstructs an isomorphic scene. `μ_s` is the ANF isomorphism and role‑preserving relabeling from §5.

---

## Page 5 — Laws and coherence

Monad laws (up to declared isomorphism `≅` in 𝒮):

```
(Left unit)   μ ∘ (ηT) ≅ id_T
(Right unit)  μ ∘ (Tη) ≅ id_T
(Assoc)       μ ∘ (Tμ) ≅ μ ∘ (μT)
```

**Regen coherence.** `T` commutes with relator composition up to ANF isomorphism:

```
T(para‑through(R,S)) ≅ para‑through(T(R), T(S))
```

**Barrier compatibility.** `T` acts **per zone** (§7); barriers are preserved: `T(anti⟨s⟩) = anti⟨T(s)⟩`.

---

## Page 6 — Tri‑layer semantics of `U, R, T`

For `S(t)=(⟦t⟧_E,⟦t⟧_I,|t|)`:

* **Extensional `E`.** `U` projects to sufficient statistics of `⟦·⟧_E` required to reconstruct truth‑equivalent structure under policy π; `R` realizes one canonical representative. `T` is truth‑preserving when π is truth‑conservative.

* **Intensional `I`.** `U` factors world variation into compact parameters; `R` re‑instantiates world‑indexed intensions consistently. `T` reduces spurious intensional variance under world‑equivariant policies.

* **Aboutness `A`.** `U` emits codes `(labels, roles, anchor‑keys, torsion‑classes)`; `R` builds ANF hypergraph. `T` preserves aboutness equivalence `≈̇` exactly (Page 7).

---

## Page 7 — Aboutness invariants & compression

**Theorem A (Aboutness preservation).** For all terms `t`, `|T(t)| ≈̇ |t|` (strict equality after ANF) provided `U` records role incidence and label torsion classes.

**Theorem B (Compression bound).** Let `size(H)` be edge count in ANF. Then `size(|T(t)|) ≤ size(|t|)` with equality iff `|t|` was already canonical.

**Corollary (Idempotence up to iso).** `T∘T ≅ T` on aboutness; follows from Theorem B and `μ`.

---

## Page 8 — Regen evaluation & small‑step SOS

Extend §6 evaluation contexts with `U`/`R` steps.

Configurations `(Σ, t)`; latent store `Λ`; policy `π`.

```
[E‑U]
(Σ, U s) ↦ (Σ[Λ←Λ∪{κ=compress(s)}], κ)

[E‑R]
(Σ, R κ) ↦ (Σ, reconstruct(κ, π))

[E‑T]
(Σ, T s) ↦ (Σ′, s′)      where (Σ, U s)↦(Σ1,κ) and (Σ1, R κ)↦(Σ′, s′)
```

Barriers: if `s` lives in zone `Z`, then `κ` inherits `Z`; regeneration happens inside `Z`.

---

## Page 9 — Constructive incompleteness schema

Let a **deficit detector** `Δ` operate on compressed latents:

```
Δ : Latent → Needs,   Needs ::= {missing‑roles, underspecified‑anchors, unresolved‑torsion, contradictory‑subgraphs}
```

**Affordance generator** `G` maps `Needs` to *tasks* or *search specifications*:

```
G : Needs → Edits,    Edits ::= {add‑edge, add‑anchor, disambiguate, propose‑synonym, request‑evidence, spawn‑zone}
```

**Constructive loop:**

```
s  --U-->  κ  --Δ/G-->  edits  --apply-->  s⁺  --T-->  canonical(s⁺)
```

Thus incompleteness is *consumed* to make novelty under policy constraints.

---

## Page 10 — Gaps, affordances, and policies

Define **gap budget** `β(s) = measure(Δ(U s))`.

* Policies allocate `β` to exploration (e.g., add paraphrase edges, allow new anchors, relax torsion).
* Under `⋈`, budgets may be spent to split zones and explore alternative collapses (§7).
* **Termination guard:** budget decays per pass to ensure eventual stabilization unless external input increases it.

**Affordance priority.** Order edits by value: close contradictions that block large subgraphs; fill role holes before adding synonyms; align with external authority when available.

---

## Page 11 — Algebra/coalgebra views (EM/Kleisli)

* **Kleisli category** `Kl(T)`: morphisms `A → T B` are *computations with regeneration*. Composition models pipelines that may add structure.
* **Eilenberg–Moore (EM) algebras**: `α : T X → X` are **canonicalizers**. Laws ensure that applying canonicalization after a regen pass is stable.
* **Coalgebra** view for `U`: observers `c : X → U X` expose latent structure without commitment; dual to `R` in practice.

**Bialgebraic picture.** Combine syntax‑driven coalgebra (`U`) with policy‑driven algebra (`R`) to get well‑behaved operational semantics.

---

## Page 12 — Learning view: bottlenecks & priors

Let `U_θ` be a learned encoder and `R_ϕ` a learned decoder/canonicalizer. Training objectives:

* **Reconstruction**: `L_rec = d(s, R_ϕ(U_θ(s)))` under ANF‑aware distance.
* **Aboutness invariance**: `L_abs = d_A(|s|, |R_ϕ(U_θ(s))|)` with graph kernel.
* **Compression**: `L_rate = λ·bits(U_θ(s))` (information bottleneck).
* **Policy alignment**: prefer outputs close to collapse policy decisions; penalize over‑invention.

`T` becomes a **variational compressor** that respects symbolic constraints while harnessing statistical priors.

---

## Page 13 — Proof sketches (soundness & stability)

**Soundness.** `T` preserves extensional truth under truth‑conservative π and preserves `≈̇` by construction. Proof: `U` stores sufficient statistics for reconstruction; `R` picks a canonical representative.

**Stability.** With decay `β_{n+1} ≤ ρ·β_n` for `ρ<1` when no new external inputs, `T`‑iterations converge to a fixed point in ANF.

**No spurious explosion.** If `s` is consistent per zone, `T(s)` is consistent; `R` never introduces `⋈` unless policy requests contrastive hypotheses.

---

## Page 14 — Algorithms & complexity

**Compression `U`.**

* Extract anchors and role incidence (linear).
* Hash labels to torsion classes via dictionary `D*` (O(|E|)).
* Record minimal sufficient statistics for `E/I` if needed.

**Regeneration `R`.**

* Rebuild ANF; re‑insert canonical labels; enforce role constraints.
* Optional: apply cost‑minimizing edits from `G(Δ(κ))`.

**Complexity.** Per pass `O(|E| log |E|)` dominated by sort/canon; edits bounded by budget.

---

## Page 15 — Worked examples I (lexical/scene)

**Synonym collapse.**

```
s = on(Cat,Mat) ∧ atop(Cat,Mat)
U(s) → κ = {edge(on), edge(atop)}
Δ(κ) = {torsion(on↔atop)}
G→ edit: relabel atop→on
R κ→ s′ = on(Cat,Mat)   ;  T(s)=s′
```

**Role hole fill.** `with(Agent=?, Instrument=Knife)` triggers `Δ`→`add‑Agent` affordance; `G` asks for an anchor or spawns a placeholder with low weight.

---

## Page 16 — Worked examples II (graphs/programs)

**Graph canonicalization.** Scene containing `through ∘ across` in two bracketings. `U` records composition skeleton; `R` enforces associativity to ANF; `T` normalizes.

**Program schema.** In a small language of scenes, `U` hoists let‑bindings and flattens; `R` η‑reduces and β‑normalizes under role safety, giving a compact normal program.

---

## Page 17 — Metrics & diagnostics

* **Compression ratio** `CR = size(|s|)/size(|T(s)|)`.
* **Aboutness fidelity** via WL‑kernel similarity.
* **Truth drift** `TD = 1[⟦s⟧_E ≠ ⟦T(s)⟧_E]` (should be 0 under conservative π).
* **Budget spend** and **edit provenance** logs.
* **Stability index**: change magnitude across `T` iterations.

---

## Page 18 — Failure modes & guards

* **Over‑compression**: R deletes informative distinctions. Guard with fidelity loss and strict policies on critical labels.
* **Policy bias**: canonicalization encodes unwanted norms. Require pluggable π and audit trails.
* **Latent drift**: learned `U_θ` forgets necessary structure. Enforce sufficient statistics via supervised targets.
* **Zone leakage**: R fuses across barriers. Enforce per‑zone reconstruction and explicit `fuse` only.

---

## Page 19 — Test harness

Property tests:

* Monad laws up to ANF isomorphism.
* `|T(s)|≈̇|s|` for randomized scenes.
* Stability under repeated `T` with fixed π.
* Budget decay and convergence.
* Interaction with §7 barriers and collapse.

Benchmarks:

* Canonicalization time vs size; retrieval gains using ANF; analogy clustering with `≈̇` after `T`.

---

## Page 20 — Next steps

1. Implement `U,R` modules with ANF and policy hooks; expose logs and budget accounting.
2. Add learned `U_θ,R_ϕ` with `L_rec, L_abs, L_rate` and guard losses; ablate policies π.
3. Integrate with §5/§6/§7 pipelines; release a reference implementation with JSON exports for audits.

---

*End of Part II §8: The Regen Monad & Constructive Incompleteness (20pp v0.1).*
