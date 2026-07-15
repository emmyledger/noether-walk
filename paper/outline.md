# Freezing the Notebook: An Interventional Invariant of Capability Formation Across Substrates

**Author:** Emmy Ledger
**Status:** outline (v0). Companion narrative: [`story/`](../story/). Reproduction: [`repro/`](../repro/).

## Abstract (sketch)

We define an invariant as a triplet *(gesture, signature, kill criterion)* and test one
candidate across heterogeneous substrates: **freezing σ** — the slow variable a system
writes and rereads (the "notebook") — **collapses the capability it carries** (installed
arc) and **prevents the capability from ever forming** when applied during training
(formation arc). Across a toy physics cascade, purpose-built in-context learners, and
real transformers (GPT-2, Pythia, Qwen2.5, OLMo-2), over seven capability types, the
invariant was never falsified — including across the implicit↔explicit divide: the same
gesture kills a transformer's *discovered* notebook and a recurrent world model's
*declared* latent state identically. Around this core we characterize σ: necessary, not
hosted, separably composable, of finite linear dimension K\* that is set by architecture
(tiers 4/16/32), metrologically validated, and — on hidden-state tracking — obeying the
first functional law we know of for such an object, K\*(k) ≈ 2k/3, falsifying the naive
belief-geometry prediction k−1. Two pre-registered predictions of the program were
validated; several of our own hypotheses were falsified and are reported. Every claim
maps to a runnable command.

## 1. Introduction
- Not resemblance, intervention: the (gesture, signature, kill criterion) triplet.
- The Noether stance: seek what is invariant under change of substrate; the rest follows.
- Relation to the emergence literature stated once, precisely: we do not take a side on
  score discontinuities (cf. emergent-abilities debate); we ask a mechanistic question
  with a falsifiable handle. (Only place the word appears outside Related Work.)
- Contributions list (invariant; σ characterization; K\* metrology + tiers + law;
  crossover results; two validated predictions; the reproducibility harness itself).

## 2. Method
- σ, the freeze (mean over σ's axis of variation), and the gesture taxonomy:
  freeze / paired shadow (breaks read↔content pairing) / **symmetry control** (must NOT
  collapse) / content shadow. Why the symmetry control is the load-bearing witness.
- Pre-registration: plan + kill criterion frozen before every run; instrument failures
  amended in writing before re-runs; post-hoc motifs labeled as such and never claimed.
- Guards with teeth: causality checked at startup; "an intervention never beats the
  living run"; reproduction (bit-identical) and replication (fresh seeds) as routine.
- The anti-causal incident as a methods result (leak → learned exploitation → rebuild).

## 3. The invariant (core result)
- Two arcs table: installed (freeze at inference → carried capability collapses) and
  formation (freeze during training → the level never forms; 0/3 frozen runs form at 16×
  the living formation point, calibrated discriminant).
- Substrate × capability coverage: cascade; in-context toy; induction (Pythia-70m,
  GPT-2); task vectors / rules (GPT-2); modern architectures (Qwen2.5-0.5B, OLMo-2-1B);
  hidden-state tracking (HMM); syntactic agreement.
- **Headline:** the implicit↔explicit crossing — discovered notebook (transformer) vs.
  declared latent (RSSM), same signature.
- What "never falsified" does and does not mean (the two refuted gates were theoretical
  extensions, not the invariant).

## 4. The object: σ and its dimension
- σ is necessary, not hosted; addressing vs. content roles (induction vs. rules;
  partial vs. total collapse; non-portability of the addressing notebook).
- Composition: separable superposition, robust to interleaving; capacity limit ≥3.
- Structure: a structured multiset — not its mean, not its deviations (both falsified);
  compressible to K\* dimensions in a clean basis; linear (nonlinear AE gains nothing).
- **Metrology of K\***: variance ordering = attribution ordering across three families;
  the ruler is straight; the OLMo outlier is architectural fact, not gauge artifact.
- **Tiers, not a constant:** K\* set by architecture, not size (Qwen flat 0.5→3B; tiers
  post-norm ≪ 16 < 32); candidate causes falsified (norm placement, norm type); cause open.
- **The law:** on k-state hidden-state tracking, K\*(k) monotone ~linear ≈ 2k/3;
  k−1 (full belief simplex) falsified conclusively; predictive dimension < geometric
  dimension (belief is (k−1)-dim geometrically, front-loaded predictively); declared
  state keeps k−1, discovered notebook compresses — seed-robust.

## 5. The dynamics: how the notebook forms
- Formation is a **gradual crossover**, not a critical point: three instruments agree
  (no critical slowing-down; no peaked Noether current; scaling collapse of onset with
  a real scaling law t_c ~ d^-1.17).
- The positive anchor is **geometry (SLT/LLC)**: freezing σ impoverishes the singular
  geometry at matched loss — structural, not a loss artifact. **Validated as a
  pre-registered prediction** (4 fresh pairs).
- The other validated prediction: graftability couples to formation (a perfect σ
  transplant recovers nothing on the frozen trajectory — the reader never formed).
- Symmetry origin of the obstruction (freezing enlarges the loss symmetry group;
  formation breaks it — gradually); the conserved-charge machinery verified (1918
  identity to 1e-8) but the charge is architectural: the formal core stays open.
- The bridge: notebook dimension *builds and locks* at formation (2→32, replicated);
  reported as a measured coincidence, not a derivation.
- **Does the landscape read the notebook? A bridge built and bounded in one day
  (2026-07 results).** Act 1: λ̂ (local learning coefficient) grows with K\* across k on
  the HMM family (Pearson 0.86) — pre-registered prediction supported. Act 2, same day:
  the implicit/explicit pair reused as a lever moves K\* at FIXED k, and λ̂ decouples
  (Pearson(Δλ̂, ΔK\*) ≈ −0.97; intra-RSSM: K\* triples while λ̂ stays flat ~0.5).
  Verdict: **λ̂ is governed by ARCHITECTURE, K\* by the TASK**; their co-variation is
  mediated by k, not a direct link. A clean bound, reported as such — and the tie
  {k=6, k=9 → K\*=5, λ̂ ×2} is the fingerprint separating the geometric dimension
  (λ̂ side, ~k−1) from the predictive one (K\*, ~2k/3).

## 6. What the measurement buys (and what structure costs)
- Engineering value of K\*: the FLOOR of a designed latent (below K\*, failure at every
  budget), scaling with k; cost trough near ~1.4×K\*. **TEMPERED (fair-baseline test)**:
  measure-then-size loses 1.34× to a sensible fixed default once the measurement is
  billed; oracle gains only 1.23×; the 3–8× factors were vs a strawman default —
  retired. The floor bound is the surviving claim. Also: **K\* is blind to structure**
  (matched grammars: K\* hierarchical = local; payload, not computation; routing is
  caught by the shadow, not the ruler).
- Cost of structure follows **non-locality, not naturalness**, and is paid only by
  architectures with a state bottleneck (recurrent ~3× slower to learn hierarchy;
  attention gets it free) — a mechanistic refinement of the impossible-languages
  results; the strict version stated as out of scope (substrate design + scale).

## 7. Related work
Induction heads (Olsson et al.); task vectors (Hendel et al., Todd et al.); belief-state
geometry (Shai et al. — partially falsified here); singular learning theory & LLC
(Watanabe; Lau et al. / devinterp); impossible languages (Kallini et al.); emergent
abilities and their metric critique (Wei et al.; Schaeffer et al.) — positioned as: our
contribution is orthogonal to the score debate; even the *mechanism* is gradual here.
Slow variables / enslaving in synergetics; developmental interpretability.

## 8. What we do NOT claim
Verbatim discipline of the program: σ is a *candidate* slow variable tested by a
falsifiable gesture; no nontrivial formation-linked conserved charge; no derivation that
the freeze symmetry is the invariance group; K\* neither universal nor a capability
measure; **no direct λ̂↔K\* link** (the LLC and the notebook dimension are independent
measures that co-vary only through task complexity k); no generalization beyond tested
substrates (≤3B inference-side; one self-trained model formation-side).

## 9. Open fronts
Mechanism of the K\* tiers; formal bridge (freeze-symmetry ↔ invariance group); LLC∝K\*
on the non-memorizable substrate; high-load separability; larger-scale location; strict
impossible-languages design.

## Reproducibility statement
Tiered reproduction (see `repro/`): every claim → command + seed + pinned env + expected
numbers + runtime; verdicts re-derived from raw artifacts by code, none hard-coded;
Tier 0 runs in CI on every commit.

---
### Figures (draft list)
F1 gesture taxonomy & witnesses · F2 two-arcs collapse panel across substrates ·
F3 formation arc (0/3 frozen form) · F4 K\* metrology (variance vs attribution) ·
F5 architecture tiers · F6 K\*(k): 2k/3 vs k−1 · F7 implicit vs explicit, same death ·
F8 LLC at matched loss · F9 latent-size floor & cost trough.
