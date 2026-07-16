# Freezing the Notebook: An Interventional Invariant of Capability Formation Across Substrates

**Emmy Ledger**
*Draft v0.3 — abstract + §1–4 drafted; remaining sections: [`outline.md`](outline.md).
Citations are (Author, year); full entries in [`references.md`](references.md). Every
quantitative claim will link to a reproduction command; see [`../repro/`](../repro/).*

## Abstract

Claims that unrelated learning systems share deep organizational principles usually rest
on resemblance — similar curves, similar phase-transition narratives — and resemblance
is unfalsifiable. We propose a stricter currency. Define an invariant as a triplet
*(gesture, signature, kill criterion)*: a physical intervention performable identically
across substrates, a predicted effect, and a pre-registered outcome that would falsify
the claim. We test one candidate invariant: **freezing σ, the slow variable a system
writes and rereads (its "notebook"), collapses the capability that σ carries** — at
inference for an installed capability, and, applied during training, it prevents the
capability from ever forming. Across a toy physics cascade, purpose-built in-context
learners, and pretrained transformers (GPT-2, Pythia, Qwen2.5, OLMo-2), over seven
capability types (induction, in-context rules, hidden-state tracking, syntactic
agreement, among others), with matched-budget shuffles and symmetry controls as
witnesses, **the invariant was never falsified** — including across the
implicit↔explicit divide: the same freeze kills a transformer's *discovered* notebook
and a recurrent world model's *declared* latent state with the same signature. Around
this core we characterize σ interventionally: it is necessary and not merely
epiphenomenal; composable by separable superposition; of finite, linear dimension K\*.
We validate K\* metrologically (variance ordering matches attribution ordering across
three model families), find it set by architecture rather than scale (tiers 4/16/32;
size-invariant from 0.5B to 3B), and establish its first functional law on k-state
tracking tasks: K\*(k) is monotone and near-linear but ≈ k/2 (our own first fit read
2k/3 until a longer range corrected it — and the slope itself was then derived: it
tracks the process's spectral gap), falsifying the naive
belief-geometry prediction k−1 — the *predictively load-bearing* dimension is smaller
than the geometric one, and only declared states retain the full k−1 geometry. Two
pre-registered predictions of the program were validated (formation-coupled
graftability; a loss-independent geometric imprint of σ via the local learning
coefficient); several of our own hypotheses were falsified and are reported alongside a
training-time causality artifact we discovered, fixed, and now guard against
automatically. All results reproduce from pinned environments and registered seeds; the
core collapse runs on a laptop in minutes.

## 1. Introduction

### 1.1 Resemblance is not evidence

When a new capability appears in a learning system — a language model that abruptly
starts using in-context information, a physical system that organizes into a new level
of structure — it is tempting to reach for unification by resemblance: the curves look
alike, therefore the mechanisms must be kin. The temptation is old, and the literature
it produced is largely a graveyard, because resemblance has no kill criterion. Two
trajectories can match for a hundred spurious reasons, and a theory that predicts
"things will look similar" cannot lose.

This paper takes the opposite route, borrowing a stance from Emmy Noether's two great
legacies — objects understood by their invariants under transformation, and symmetries
tied to what dynamics conserve. We do not import her theorems wholesale; we import the
discipline. If heterogeneous systems share something real, it should show up as an
**invariant under change of substrate**: a statement that survives the replacement of
every implementation detail, and that could have died at each attempt.

### 1.2 Interventional invariants

We define an invariant as a triplet:

- **Gesture** — an intervention performable identically across substrates;
- **Signature** — the predicted effect of the gesture, stated in advance;
- **Kill criterion** — the pre-registered outcome that falsifies the claim.

The gesture at the center of this work targets a specific structural motif: many systems
steer fast activity by writing and rereading a **slow variable** — call it σ, or the
*notebook*. The motif is old: slow modes that "enslave" fast dynamics are the organizing
objects of synergetics (Haken, 1983). In a transformer solving an in-context task, σ is
the residual-stream content that downstream heads reread — the residual stream as a
communication channel in the sense of Elhage et al. (2021); in a recurrent world model,
σ is the latent state by construction (Hafner et al., 2019); in our toy cascade, σ is a
slow memory that gates a second instability.
The gesture is to **freeze** σ: replace its content by its mean over σ's own axis of
variation — same magnitude budget, zero information — while the rest of the system runs
untouched.

The candidate invariant has two arcs:

- **Installed arc.** If a deployed capability is carried by σ, freezing σ at inference
  collapses it.
- **Formation arc.** If a capability *forms* by building σ and its reader, freezing σ
  during training prevents the capability from ever existing.

Crucially, "freezing breaks things" would be trivial. The claim earns its content from
three witnesses, pre-registered alongside every experiment: a **twin without a
notebook** (a system solving the task from parameters, which the same gesture must
leave intact), a **paired shadow** (matched-budget destruction of the read↔content
pairing, which must collapse like the freeze), and a **symmetry control** (a
transformation preserving that pairing, which must *not* collapse). Each experiment is
thus four opportunities to falsify, with the discriminating thresholds calibrated and
frozen before the run.

### 1.3 What we found

Across substrates that share no parts — a toy physics cascade; hand-built in-context
learners where memorization is impossible by construction; pretrained models from four
architecture families, untouched by us; and one small transformer we trained from
scratch on real code — the invariant held every time it was put at risk, across seven
types of capability. Its strongest form is a crossing of the implicit↔explicit divide:
the freeze kills the *discovered* notebook of a transformer and the *declared* latent
state of a recurrent world model with the same signature (§3). Freezing σ during
training prevented induction heads from forming in a real network (0/3 frozen runs
formed at 16× the living formation point, under a calibrated discriminant; §3.3).

The invariant then becomes an instrument, and the rest of the paper is what it measured:

- **The object** (§4). σ is not epiphenomenal and not its summary statistics (both
  reductions falsified); in a clean basis it compresses to a low, *linear* dimension
  K\*. K\* survives metrological scrutiny — ordering directions by variance or by
  task-attribution yields the same dimension across three model families — and is set
  by **architecture, not scale** (tiers 4/16/32; constant across a 6× size range). On
  k-state hidden-state tracking, K\* obeys the first functional law we know of for this
  object: monotone, near-linear, **≈ k/2 rather than the k−1** the belief-simplex
  geometry predicts. The belief *is* geometrically (k−1)-dimensional; its predictive
  weight is front-loaded. Declared states keep the full geometry; discovered notebooks
  compress.
- **The dynamics** (§5). Formation is a **gradual crossover**, not a critical point:
  no critical slowing-down, no peaked conserved current, but a genuine scaling law for
  the onset with scale-collapse of the rescaled transition. The positive anchor is
  geometric: freezing σ measurably impoverishes the singular geometry of the loss
  landscape at matched loss (local learning coefficient), a **pre-registered
  prediction** validated on fresh runs — as was a second prediction, that σ-grafting
  only works once formation has built the reader.
- **The price of structure, and what the measurement buys** (§6). K\* bounds the
  *floor* of a designed latent — below it, failure at every budget tried — though the
  finer right-sizing claim is tempered by a fair-baseline test (§6.1); and the cost of
  maintaining non-local structure is paid only by architectures that bottleneck state —
  a mechanistic refinement of the impossible-languages debate.

### 1.4 Relation to the emergence literature

We use the word once, deliberately. A lively debate asks whether "emergent abilities"
of large models are real discontinuities (Wei et al., 2022) or artifacts of metric
choice (Schaeffer et al., 2023) — the modern echo of a question at least as old as
Anderson's "More is Different" (1972). We take no side
on score curves. Our contribution is orthogonal and mechanistic: with a falsifiable
handle on the *mechanism*, we find that even the mechanism is gradual — a
developmental, constructive process whose dimension locks in at formation — while being
causally load-bearing at every scale we tested. Interventional necessity, not
discontinuity, is the robust phenomenon.

### 1.5 Contributions

1. A definition of cross-substrate invariance with teeth (gesture / signature / kill
   criterion + witness taxonomy), and one candidate invariant that survived every
   attempt on its life, across seven capabilities and the implicit↔explicit divide.
2. An interventional characterization of the slow variable σ: necessity, separable
   composition, structured-multiset nature, finite linear dimension.
3. A metrology of K\* and two structural results: architecture-set tiers (with the
   obvious causal candidates falsified on matched toys), and the law K\*(k) ≈ k/2
   falsifying the belief-simplex prediction.
4. Two validated pre-registered predictions (formation-coupled graftability;
   loss-independent geometric imprint via LLC), and a catalogue of our own falsified
   hypotheses, including a training-time causality artifact now caught by automated
   guards.
5. A reproduction harness as a first-class artifact: every claim maps to a command,
   pinned environment, registered seed, and expected numbers; the core result runs on a
   laptop in minutes and in CI on every commit.

### 1.6 Scope and honesty

Inference-side results cover models up to 3B parameters from four families; the
formation-arc result on a real network covers one small transformer trained by us. We
claim nothing beyond the substrates tested. The bridge between the freeze-symmetry and
a bona fide invariance group is empirical (a measured, replicated coincidence of
dimensions), not derived. Section 8 states everything this paper does *not* claim.

## 2. Method

### 2.1 Designating σ a priori (the anti-hosting rule)

The single most important discipline in this work concerns *when* σ is chosen. A slow
variable selected after the fact — by searching a system for whatever, once perturbed,
reproduces a desired signature — proves nothing: any sufficiently rich system *hosts*
arbitrarily many such variables, and the experimenter has merely projected the
conclusion into the substrate. We therefore require that σ be designated **before any
intervention is run**, by a published criterion that does not consult the outcome:

- *Toy in-context learner*: the layer-1 writes reread by layer 2, fixed by construction.
- *Pretrained transformers (induction)*: the K/V content reread by induction heads,
  where the heads are selected a priori by a documented prefix-matching criterion — the
  selector, run blind, recovers the induction heads independently reported for these
  models (Olsson et al., 2022).
- *Task vectors / in-context rules*: the residual-stream content at the demonstration
  positions, at a layer fixed in the plan.
- *Hidden-state tracking*: the residual content carrying the belief estimate, localized
  by an R² probe **on held-out runs before** the freeze experiment (and §4.4 reports how
  this localization must move with depth — itself a pre-registered re-test).
- *Explicit world model (RSSM)*: the declared latent state, σ by construction.
- *Toy cascade*: the slow memory gating the second instability, σ by construction.

Where σ is structural (declared or by construction), the anti-hosting risk is nil; where
it must be *found* (pretrained models), the selection criterion is frozen in the plan
and its blind agreement with independently documented structure is reported.

### 2.2 The gesture and its witnesses

**The freeze.** Replace σ's content by its mean **over σ's own axis of variation** —
time for a temporal trace, demonstration positions for in-context rules, the batch
elicitation axis for weight-borne probes. The mean preserves the magnitude budget
(norms, energy, footprint) while destroying information: a capability that dies under
the freeze died of information loss, not of a changed operating point. The freeze is
applied to the *full* pre-registered path (dose-response reported as threshold curves),
with collapse criteria stated as **absolute floors**, never relative slippage.

**Why "freeze" rather than ablate or noise.** Ablation confounds information loss with
budget change (downstream components react to absence); noise injection confounds it
with perturbation. Our freeze is kin to the mean-ablation of the interpretability
literature (Wang et al., 2023; Zhang & Nanda, 2024) — with two differences that carry
the argument: the mean is taken over σ's *own axis of variation*, and the gesture never
travels alone (witnesses below). The frozen page is the calmest object in the system; the only thing
removed is what it *said*.

**The witness taxonomy.** "Freezing breaks things" is not a finding. Every experiment
pre-registers four conditions beyond the living run, each with a predicted outcome, each
an independent opportunity to falsify:

| condition | operation | must |
|---|---|---|
| live | none | perform |
| **freeze** | σ → mean over its variation axis | collapse |
| **paired shadow** | destroy the read↔content *pairing* at conserved marginals (e.g. independent permutations of keys and values) | collapse like the freeze |
| **symmetry control** | a transformation that *preserves* the pairing (e.g. jointly permuting key–value pairs) | **survive** |
| **notebook-free twin** | same task solved from parameters (memorization possible by design), same freeze applied | **not flinch** |

The symmetry control is the load-bearing witness, and it was learned the hard way: in an
early experiment our planned "shadow" (a joint time-shuffle) collapsed nothing, because
it was in fact a quasi-symmetry of the reading mechanism — shuffling *whole* key–value
pairs is like shuffling the cards of a phone directory, which no lookup notices. The run
was declared non-conclusive under its pre-registered criterion, the mechanism was
understood, and the taxonomy was repaired so that every subsequent experiment carries
both a pairing-breaking shadow (must kill) and a pairing-preserving control (must not).
The repaired pair is what makes a collapse *specific*.

**The two arcs.** *Installed*: freeze at inference; the carried capability must
collapse. *Formation*: freeze throughout training; the capability must never form, while
(i) the same architecture under the same schedule *without* the freeze forms reliably,
and (ii) a twin task learnable without σ proceeds under the freeze — the gesture
obstructs the capability, not learning itself.

### 2.3 Pre-registration and kill criteria

Every experiment follows the same lifecycle, and the repository preserves it:

1. A **plan is frozen before the run**: gesture, path, metrics, discriminant thresholds
   (calibrated in advance, non-saturated), and the explicit kill criterion.
2. The verdict is read **only** against the frozen plan. Thresholds are never moved
   after contact with data.
3. **Instrument failures** (a probe that fails its own sanity check, a control that
   saturates) are amended in a written, dated addendum *before* the re-run; the failed
   attempt remains on record. Several of our headline numbers were reached only on a
   second or fourth pre-registered attempt, and the paper reports the full sequence.
4. **Post-hoc motifs are labeled, never claimed.** When an unpredicted regularity
   appeared (e.g. an apparent K\* ≈ k−1 saturation pattern, §4.5), it was recorded as a
   motif and promoted to a claim only after an independent, pre-registered test on fresh
   settings — which in that instance *falsified* it.

### 2.4 Guards with teeth

Manual discipline fails eventually, so the harness enforces three properties
mechanically; violating any of them aborts or flags the run:

- **Causality at training time.** An intervention applied during training must respect
  the causal structure of the loss. This guard exists because we violated it: our first
  formation-arc campaign froze σ using intra-sequence statistics, which leaks future
  tokens into the training signal — and the network *learned to exploit the leak*. The
  artifact was discovered, the campaign interrupted and discarded, the freeze rebuilt
  causally, and the property is now checked automatically at startup. We report this
  incident in full because it is the strongest argument for the guard: the failure mode
  is invisible in the loss curve and produces beautiful, wrong results.
- **An intervention never beats the living run.** Evaluated continuously; on the
  archived anti-causal logs this guard fires, as it should.
- **Verdict re-derivation.** No number in this paper is hard-coded: an independent
  module re-derives every verdict from raw run artifacts, and the reproduction harness
  (§ Reproducibility) re-executes the derivation in CI.

### 2.5 Reproduction, replication, and what "held" means

Every reported verdict satisfies both: **reproduction** — identical seeds, identical
artifacts to the last logged digit — and **replication** — fresh seeds, verdict
unchanged under the frozen criteria. When we write that the invariant *held*, we mean
precisely: the pre-registered kill criterion was armed, the four witnesses behaved as
predicted, the verdict was re-derived from raw artifacts by independent code, and the
result replicated on seeds chosen after the plan was frozen.

## 3. The invariant

### 3.1 Coverage

The candidate invariant was put at risk on substrates chosen to share nothing — a toy
physics cascade; purpose-built in-context learners in which memorization is impossible
by construction; pretrained transformers from four architecture families, untouched by
us (Radford et al., 2019; Biderman et al., 2023; Qwen Team, 2024; OLMo Team, 2024); and
one small transformer we trained from scratch on real code — across seven capability
types: fresh-pair recall, induction (Olsson et al., 2022), in-context rules in the sense
of task/function vectors (Hendel et al., 2023; Todd et al., 2024), rule composition,
hidden-state tracking, syntactic agreement, and explicit world-model state maintenance.

### 3.2 Installed arc: freeze at inference

Representative verdicts (capability scores under the pre-registered conditions; every
freeze row had a calibrated collapse bar, every symmetry-control row a survival bar):

| substrate | capability | live | freeze | paired shadow | symmetry control |
|---|---|---|---|---|---|
| built toy | fresh-pair recall | 1.000 | 0.119 | collapses alike | twin without notebook: unaffected |
| Pythia-70m | induction | 0.756 | 0.108 | 0.050 | **0.725 (survives)** |
| GPT-2-small | induction | 0.989 | 0.001 | collapses alike | survives |
| GPT-2-small | in-context rules | 0.652 | 0.000 | collapses alike | demo-order symmetry intact |
| Qwen2.5-0.5B | in-context rules | 0.975 | 0.100 | 0.041 | **0.975 (survives)** |
| OLMo-2-1B | in-context rules | 0.988 | 0.394* | 0.212 | **0.969 (survives)** |
| toy transformer | hidden-state tracking | live | ≈16 % of live | negative | survives |
| toy transformer | syntactic agreement | ≈1.0 | 0.70 | → chance | survives |
| RSSM world model | state maintenance (declared z) | live | ≈0 | negative | survives |

\* below its pre-registered collapse bar. The residual 0.119 on the built toy is the
task's chance structure (1-in-8), quantified in the plan.

Two structural nuances, established interventionally and developed in §4: for
*induction*, σ carries the **addressing** (the pointer into context), not the copied
content — hence a partial, localized collapse under per-source freezing (0.77 → 0.46)
versus the total collapse of rules (→ 0.000), and hence σ's non-portability to foreign
contexts. And on *hidden-state tracking*, σ (the belief estimate) is **carried forward**
along the query path rather than reread from context — the freeze gesture must follow σ
where it actually lives, a pre-registered adaptation, not a post-hoc rescue.

### 3.3 Formation arc: freeze during training

*Toy.* Under a permanent, causally-clean freeze of σ throughout training, the in-context
capability never forms: the learning curve plateaus at chance indefinitely, while (i)
living twins form reliably and (ii) a memorizable twin task *is* learned under the very
same freeze — the gesture obstructs the capability, not optimization. No rerouting was
observed: the network does not build an alternative notebook elsewhere.

*Real network.* We trained a small transformer from scratch on real code, where
induction heads form abruptly at 145–195M tokens — the onset has the shape documented
by Olsson et al. (2022).
Under the causally-rebuilt permanent freeze (§2.4):

- **Formation clause: 0/3 frozen runs formed** — max induction score ≤ 0.012 against a
  formation bar of 0.25, observed out to **16× the living formation point** (3.2B
  tokens). All 6 living runs formed. Matched surrogates: likewise 0/3.
- **Calibrated discriminant clause: 0/3 exceeded the information ceiling.** From living
  runs alone we calibrated how much local structure σ carries (0.894 ± 0.059 nats;
  ceiling 1.012). The frozen runs' early-loss excesses (+0.149 / +0.197 / +0.207) sit
  far *below* that ceiling: the frozen models recovered roughly three quarters of the
  local structure through σ-free reorganization — as they are entitled to — but never
  approached what σ carries, and never formed. The capability did not take another door.

Freezing the notebook during training of a real network prevents the capability from
ever existing. This is the costliest and strongest single result of the program; its
stated reserve is that it covers one architecture, trained by us.

### 3.4 The crossing: discovered σ vs. declared σ

The two arcs above concern notebooks we had to *find*. The sharpest test of
substrate-independence opposes two architectures with opposite ontologies for σ:

- **Implicit** — a transformer trained to predict a k-state hidden process whose
  emissions are ambiguous, so tracking a belief over states is obligatory and
  memorization is impossible (fresh sequences). σ is the belief content *discovered* in
  the residual stream (probe R² 0.60–0.74, localized on held-out runs beforehand).
  Freeze: the tracking capability collapses to ≈16 % of live, below the unigram
  baseline; shadow negative; control survives.
- **Explicit** — a recurrent world model (RSSM; Hafner et al., 2019) on the *same*
  process, whose state z is σ **by construction** (R²(z→belief) 0.93–0.98). Freeze z: capability ≈ 0, shadow
  negative — the **same signature**.

One gesture, two architectures that share neither mechanism, training objective, nor
even whether σ is an emergent object or a declared one — and the same death. This is
the result that carries the trans-substrate thesis, and it sets up a quantitative twist
(§4.6): the *declared* state retains the full belief geometry (K\* ≈ k−1), while the
*discovered* notebook compresses it (K\* ≈ k/2).

### 3.5 What "never falsified" means

Every experiment above armed a pre-registered kill criterion; none fired. Across the
program, plenty else did fire — two theoretical gates, several of our hypotheses about
K\*, one prediction of ours about σ's internal structure (§4, §6) — which is the
falsification machinery working as designed. The distinction matters: the *invariant*
survived every attempt on its life; our *interpretations* around it did not always, and
the paper reports both. The invariant also has a stated blind spot: it detects that σ is
necessary; it does not by itself discriminate *kinds* of structure (§6 shows learnability
does).

## 4. The object: what σ is, measured by intervention

Having established that σ is necessary, we characterize it — always by the same
currency: a pre-registered gesture, never a resemblance.

### 4.1 Composition: separable superposition

Two rules held simultaneously in one context (GPT-2-small): freezing one rule's notebook
kills exactly *its* task (0.323 → 0.002) and spares the other (0.519 intact); freezing
the other reverses the pattern (→ 0.000, first task spared); freezing both collapses
everything. The result survives interleaving the demonstrations (dispersed-position
freeze: 0.412 → 0.005, other task spared) — notebooks are not positional blocks. Two
qualifications: competition is *soft* (freezing one slightly raises the other), and
beyond two notebooks the test becomes non-conclusive for capacity reasons, not
separability ones — at N ≥ 3 the *living* capability itself falls below the
pre-registered bar (0.16 / 0.09 / 0.11 < 0.30, roughly halving per added notebook on a
124M model). We never observed notebooks entangle; a larger model is needed to probe
high load.

### 4.2 A structured multiset, irreducible to its summaries

What structure inside σ carries a rule? Two candidate reductions, both pre-registered,
both **falsified**: replacing σ by its mean (its first order-symmetric coordinate) kills
the capability entirely (0.000, exactly like the full freeze) — and so does keeping only
the centered deviations (0.000). One of these was our own predicted answer; it died like
the others. Dose–response is threshold-like: ≥ 75 % of the full σ is needed. Combined
with the demo-order symmetry control (which survives), the picture is: the notebook of a
rule is a **multiset** (order-invariant) that is **structured** (not reducible to low
moments; the per-position structure is necessary).

### 4.3 A clean basis: K\*, finite and linear

The puzzle of §4.2 resolves in a proper basis. In a PCA basis of σ's variation, the
notebook of a rule compresses to **K\* = 32 of 768 dimensions** at the pre-registered
fidelity bar (full fidelity by ~128). The earlier reductions failed because they tested
*one* coordinate — far below thirty-two, not because the object is incompressible.

K\* is robust in three directions. **Across model sizes within a family**: GPT-2-small
(d=768) and GPT-2-medium (d=1024) both give exactly 32 — the dimension belongs to the
notebook, not the embedding width. **Across families**: Pythia-160m gives 16, same
order. **Across function classes**: a nonlinear autoencoder compresses no further than
PCA (K\*_nl = K\*_PCA = 32; the first autoencoder failed its sanity check and was
amended, in writing, before any verdict was read). The notebook is essentially a *linear
subspace*, not a curved manifold.

One reading rule, to prevent a confusion we fell into ourselves: **K\* is
notebook-specific, not universal.** In-context rules on pretrained models measure
~O(20–32); a one-bit syntactic-agreement notebook measures 1 (§6.2); a k-state belief notebook
measures ~k/2 (§4.6). These are different objects; comparing their K\* across tasks is
a category error.

### 4.4 Metrology: is the ruler straight?

Before comparing K\* across families we attacked the measurement itself. The concern:
PCA orders directions by *variance*, and variance might be a gauge artifact — a few
high-variance directions irrelevant to the task could inflate K\*, or a crucial
low-variance direction could hide. The test: re-order the same directions by
**attribution** (content × task-sensitivity, |Σ (σ·vⱼ)(∂loss/∂(σ·vⱼ))| over the full
pool of d directions) and re-measure. Result, on three families (in the pooled basis
this test uses): **K\*_variance = K\*_attribution exactly** (64=64, 16=16, 8=8), with
attribution-ordered accuracy tracking variance-ordered accuracy at every K — including
on the outlier family. Two further gauges were checked (layer-norm folding: innocent;
raw rank-1 variance: identified and excluded). Variance is a faithful proxy for task
relevance here; the cross-family differences below are properties of the models, not of
the ruler.

### 4.5 Architecture sets K\*, not scale — and not capability

With the ruler validated, a campaign across sizes and families:

- **Qwen2.5 is flat at K\* = 16 from 0.5B to 3B** — a 6× size range moves nothing.
- **Pythia makes a single step 16 → 32** (present already at 410m, flat after) — a
  saturating finite-size effect, not a scaling law.
- **OLMo-2-1B sits at K\* = 4**, confirmed on fresh seeds — a real architectural fact
  (§4.4), not evaluation noise.

K\* arranges in **tiers** (≈4 ≪ ≈16 < ≈32) set by architecture; "K\* is a universal
constant ~O(20–32)" is hereby retracted as our own earlier over-reading. So is a second
tempting reading: K\* does **not** track capability — the family at K\*=16 outperforms
the family at K\*=4 on standard benchmarks. What *causes* the tiers is open, and two
obvious candidates are dead: on purpose-built toys matched to the formation setting,
neither the **placement** of normalization (none / pre / post: all K\*=32) nor its
**type** (LayerNorm / RMSNorm, five variants: all 32) compresses the notebook. The
minimal toy caps at 32 and cannot reach the low tier at all — the mechanism lives in
properties of real architectures we have not yet isolated. Reserves: the size grid is
coarse (tiers are robust; the numbers are intervals), and the cross-family comparison
correlates several factors rather than isolating one.

### 4.6 The first functional law: K\*(k) ≈ k/2 — reached by falsifying k−1, and then our own first coefficient

The tiers are categorical. A *law* needs a substrate where theory predicts K\* as a
function of a dial we control. Hidden-state tracking provides one: a k-state hidden
process with ambiguous emissions forces the system to carry a belief over states;
belief-state geometry (Shai et al., 2024) predicts that belief lives on the (k−1)-simplex, so the naive
prediction is **K\* = k−1**, with k as the dial. Sequences are fresh, so memorization is
impossible; the number is declared before the measurement.

It took four pre-registered rounds to get an answer this test could not take back:

1. *Exploratory* (k = 3, 5, 9): under the pre-registered metric, K\* came out flat —
   the prediction failed its first contact. A saturation pattern suggestively near k−1
   was visible, recorded as a **post-hoc motif, explicitly not claimed**.
2. *Fresh k* (4, 7, 10, 13), saturation metric pre-declared: strict monotonicity
   appeared (and near k−1), but the round's own pre-registered sanity criterion
   (probe R² ≥ 0.80) failed (0.52–0.71) → **formally non-conclusive**, no claim.
3. *Deeper toy*: worse (R² 0.41–0.59) — with a mechanistic explanation that became a
   finding (§4.7): in deep models the belief is built *across* layers, so a layer-1 σ is
   only an early partial estimate. **The notebook migrates with depth.**
4. *The clean round*: σ probed at the belief-complete layer, fresh k = (6, 12, 15, 18),
   retrained. Sanity finally passed everywhere (R² 0.91–0.95) — the test could speak.
   Verdict: **monotone, near-linear — and k−1 falsified.** K\*_sat90 = {5, 7, 9, 11},
   strictly increasing, undershooting k−1 by a growing gap (k=18 → 11 vs 17); on that
   range, the fitted slope read ≈ 2/3. Replicated on a fresh seed ({5, 7, 9} at
   k = 9, 12, 15).
5. *The coefficient falls too.* Round four's published reserve — "the exact factor
   would need more k" — was cashed by extending the dial to k = 24, 30, 36 (two seeds
   each, on top of the consolidated three-seed points below 18). Over **eight values of
   k** the law is **K\* = 0.443·k + 2.07 (R² = 0.984)**, and the through-origin
   comparison is unambiguous: **k/2 fits six times better than 2k/3** (residuals 12.9
   vs 77.1) — at the three largest k the measurement *is* k/2 exactly (12.5, 15.5, 18).
   Our "2/3" was an artifact of fitting through the origin on a short dial range, where
   the +2 intercept masquerades as slope. **The coefficient is one half.**

The resolution of the apparent paradox is itself a result: the belief **is**
geometrically (k−1)-dimensional (that is what the high R² says), but its predictive
weight is front-loaded. K\* measures the *predictively load-bearing* dimension, not the
geometric one. The control that clinches it is the explicit world model (§3.4): its
*declared* state z gives K\* = {6, 11, 16, 16} against k−1 = {5, 11, 14, 17} — the
declared state keeps the whole simplex; the discovered notebook compresses it. Both laws
replicate across seeds, with explicit > implicit at every k.

**The coefficient, derived.** A pre-registered follow-up asked whether the slope b
tracks the hidden process's **spectral gap** |λ₂| — how slowly the world forgets —
holding the architecture fixed and sweeping |λ₂| ∈ {0.90, 0.95, 0.99} over k = 12…30:
**b = 0.425, 0.461, 0.583** — monotone, clearing the pre-registered bar (Δb > 0.10;
measured 0.158). An unpredicted but coherent bonus: the +2 intercept vanishes as
|λ₂| → 1 (2.95 → 1.65 → 0.00) — slope rising toward 1 and floor dissolving, both
pointing to the geometric limit k−1 for near-deterministic processes. **"One half" is
b(|λ₂|) evaluated at 0.95**, the mixing rate used since the first hidden-state
experiment; the law is spectral, **K\* ≈ b(|λ₂|)·k**. Reserves: three gap values
(monotonicity leans on the 0.99 point), a single family of transition structures (the
*dependence* is established, not the functional form), and the emission-ambiguity
lever untouched.

This is the first *functional* dependence of K\* we know of (versus the categorical
tiers of §4.5), and it was reached by falsifying the beautiful prediction, then our own
first coefficient — and then deriving the one that replaced them. The corrections
strengthen the message rather than weakening it: the law is better measured
(R² = 0.984 over eight k, 2–3 seeds per point), the discovered notebook sits even
*further* below the geometric k−1 than we first reported, and its slope is no longer a
bare number but a measured property of the process being tracked.

### 4.7 Mechanistic byproducts

Two facts any reuser of the instrument needs. **Carried vs. reread**: for hidden-state
tracking, σ is carried *forward* along the computation at the current position — not
reread from past context as induction and rules are; freezing the reading path alone is
not sufficient, and the correct gesture (freeze both routes) was pre-registered once
this was understood. **Layer migration**: σ lives at layer 1 in a 2-layer model but at
the belief-complete layer in deeper ones. **Task richness moves σ too**: a probe basis
validated on a lean task (the belief HMM, where the belief is nearly all the useful
computation) does not transport to a rich one — on language-model training, the total
written residual conflates every capability's notebook, and a probe built on it
saturates; our first depth×norm campaign for the tiers was disqualified by exactly this
and declared inconclusive rather than read (§9). Notebooks have addresses, and the
addresses depend on architecture, depth, *and the task's richness*.

## 5. The dynamics: how the notebook forms

The formation arc (§3.3) says freezing σ during training prevents the capability from
existing. This section asks what kind of process the freeze is interrupting.

### 5.1 Formation is a gradual crossover

Three pre-registered instruments, three verdicts. **No critical slowing-down**: the
susceptibility proxy does not peak at formation — the signature of a second-order
critical point is absent (gate NOT SUPPORTED). **No peaked conserved current**: the
instantaneous Noether-current probe stays flat through formation, robust to refining
the generator (NOT SUPPORTED; the obstruction exists only in integrated form, below).
**But a real scaling law for the onset**: across five model sizes, the formation onset
scales as t_c ~ d^-1.17 (with a threshold size that never forms and a plateau growing
with size), and the transition rescaled by t_c collapses onto a single curve
(SUPPORTED, nuanced: the law concerns the *onset*, not K\*). Verdict: formation is a
**gradual crossover**, not a critical point — the metric critique of emergent-ability
score curves (Schaeffer et al., 2023) holds one level deeper here: even the *mechanism*
is gradual.

### 5.2 The geometric anchor: the landscape sees the freeze (validated prediction #2)

Singular learning theory (Watanabe, 2009) says the local geometry of the loss landscape
carries a complexity measure — the local learning coefficient λ̂ (Lau et al., 2024;
used developmentally by Hoogland et al., 2024). Pre-registered prediction: freezing σ
should *impoverish* that geometry, independently of the loss level. Verdict: λ̂ of the
living model exceeds λ̂ under the freeze; and **at matched loss** the gap persists — on
four fresh pre-registered pairs, gaps of 324/173/162/175 against a pre-set threshold of
50, consistent sign at all three analysis levels. The freeze's imprint on the singular
geometry is **structural**, not a loss artifact. This is the program's second validated
prediction.

### 5.3 Grafting couples to formation (validated prediction #1)

If formation builds a *reader* for the notebook, then transplanting a correct σ should
help only once the reader exists. Verdict: the graft score is ≈0 before formation,
rises with a gradual onset (~169M tokens — of which the abrupt prefix-matching jump at
~210M is a late marker), and is *specific*: correct σ +0.44, scrambled −0.07, random
−0.18. On the frozen trajectory the graft score is **0.000 everywhere**: a perfect
notebook recovers nothing, because the reader never formed. First validated prediction
of the program.

### 5.4 The symmetry origin — and exactly how far it goes

Freezing σ **enlarges the symmetry group of the loss**; formation is the breaking of
that added symmetry. Tested dynamically: from identical pre-formation weights, gradient
bursts under the frozen loss *dismantle* the reader (ΔQ ≤ 0, most negative near
formation) while living bursts build it. The Noether machinery itself is exact here — a
scale-symmetry conservation identity holds to 1e-8 (Noether, 1918, applies literally) —
but that conserved charge is **architectural** (it holds live and frozen, on any input):
we claim no formation-linked conserved charge, and the derivation that the freeze
symmetry *is* the notebook's invariance group remains the program's open formal core.

### 5.5 The bridge: the dimension is built at formation

On the living trajectory, the notebook's dimension (the K90 of §4.3's measurement,
tracked checkpoint by checkpoint) climbs 2 → 4 → 8 → 16 → **32** and **locks** at
formation, stable thereafter — replicated on a fresh seed under a pre-registered
metric (24/24 post-formation checkpoints locked). The locked value echoes the
rules-notebook's ~32 across arcs. We report this as a **measured, replicated
coincidence**, not a derivation — with two standing reserves: the echo compares an
*addressing* notebook to a *content* notebook (an echo of order, not identity), and
the capability curve itself is smooth (what locks is the dimension, not a score).

### 5.6 Does the landscape read the notebook? A bridge built and bounded in one day

The two arcs of measurement — K\* on activations, λ̂ on weights — invite a conjecture:
the landscape's complexity *reads* the notebook's size.

**Act 1 (prediction supported).** On the k-state family at fixed architecture, λ̂ of
the living model grows with K\* (0.552 → 1.572 over k = 6…18; Pearson 0.86). Flagged
reserve, pre-registered: λ̂ correlates better with k itself (0.95), and at equal K\*
(k = 6 and k = 9 both give K\* = 5) λ̂ nearly doubles — correlation does not show that
λ̂ *reads* K\*.

**Act 2 (falsified, same day).** The implicit/explicit pair of §3.4 is exactly the
lever the reserve demands: it moves K\* at *fixed* k (discovered notebook ≈ k/2,
declared state ≈ k−1). Verdict: Δλ̂ **anti-correlates** with ΔK\* (Pearson ≈ −0.97);
and within the recurrent model alone, K\* more than triples (5 → 18) while λ̂ stays
flat (~0.5). **λ̂ does not read K\*.** The local learning coefficient is governed by
the *architecture's* landscape; the notebook's dimension by the *task*; they co-vary
only when k drags both. Act 1 is thereby reinterpreted: a k-mediated co-variation, not
a direct link — a clean bound, reported as such. Both acts — and both K\*(k) laws —
have since been consolidated across **three seeds**, the fresh two run on two different
machines, with the intra-RSSM flatline holding on every seed (λ̂ growth < 2× while K\*
triples): the single-seed reserve is lifted. One elegant byproduct: the fingerprint
{k=6, k=9 → same K\*, λ̂ ×2} independently confirms §4.6's split — λ̂ sits on the
*geometric* side of the belief (~k−1), K\* on the *predictive* side (~k/2), the same
front-loading seen from the weights.

### 5.7 What kind of process, then?

The thermodynamic frame — emergence as a critical phase transition with a singularity
and a conserved current — is **closed** for this system (§5.1, §5.4): a negative that
eliminates a whole family of analogies. What replaces it is developmental and
constructive: a low-dimensional, linear object that assembles gradually, whose
dimension locks at formation (§5.5), which becomes causally load-bearing (§3), and
whose construction is visible in the singular geometry of the loss (§5.2) as the
gradual breaking of a symmetry (§5.4). Interventional necessity — not discontinuity —
is the robust phenomenon.

## 6. What the measurement buys — and what structure costs

Two pragmatic questions close the empirical part: does the interventional dimension K\*
have engineering value, and does *structure* (in the linguistic sense) cost anything a
mechanist can measure?

### 6.1 K\* predicts the floor of a designed latent

If K\* measures the predictively load-bearing dimension of a notebook, it should bound
the size of a latent one *designs*. Test, on the explicit world model (k = 12 hidden
states, K\*(declared) ≈ 11): sweep the latent size d_z and measure FLOPs-to-target.
Latents **below K\*** (d_z = 6, 9) **never reach the target**; d_z ≥ 12 do. The
cost-to-target curve has a trough near d_z = 16 (~1.4×K\* at k = 12); gross oversizing
(d_z = 192) costs 5.5× — though only 1.36× against a moderately-sized baseline
(d_z = 48): the economy factor depends on how naive the baseline is, and we report it
that way. Sweeping k = 6…18: the **floor scales with k** (≈k to 1.5k) and so does the
trough (9 → 16 → 24 → 48) — though the trough-to-K\* ratio itself drifts (from just
above 1× to ~2.8×), so no single multiplier deserves quoting — while the economy factor
honestly *decreases* (8.3× → 3.1×, large only when the fixed default is absurdly
oversized).

**Tempered by a fair adversary (pre-registered).** The factors above price the
measurement at zero and the alternative as naive; billing honestly reverses the fine
verdict. A *measure-then-size* strategy (dedicated pilot → measure K\* → size to
~1.4×K\* → train) costs **1.34× more** than an engineer who fixes one sensible default
(d_z = 48) forever, summed over k = 6…18; even an **oracle** handed the ideal size for
free beats that default by only 1.23×; and the 3–8× savings were real but scored
against an absurd default (192) — a strawman, retired here as an engineering claim.
What survives is the **floor**: below K\*, failure at every budget tried — and the
floor *scales with the task* (≈ k to 1.5k), so K\* would earn its measurement cost
exactly where no single default can cover the task range, or where the measurement
rides free on runs already needed. The honest summary: **an interventional dimension
bounds where failure is certain, not where the optimum sits** — a floor you don't have
to guess, not an energy law, and not a sizing oracle.

### 6.2 The cost of structure follows non-locality, and the architecture decides who pays

The Chomskyan question, made mechanistic: does *hierarchical* structure cost a learner
anything? Substrate: matched grammars where agreement must track either the
hierarchically correct subject across nested clauses (non-local) or the nearest noun
(local). First finding (invariant side): the freeze collapses syntactic agreement like
every other capability — a seventh capability type, with the smallest notebook
measured in this program (**K\* = 1** on the matched grammars, three seeds each; an
earlier, easier agreement grammar read ≈2) — but the invariant does not *discriminate*
structure: it detects necessity wherever a notebook exists. A second pre-registered
negative sharpens this: on matched grammars, **K\*(hierarchical) = K\*(local) exactly**
(three seeds each) — **K\* measures the payload carried, not the computation that fills
it.** The agreement notebook is the same one bit whether the correct subject was
tracked across an embedded distractor or read off at a fixed distance; what differs is
the *routing* — which noun gets to write into σ — and routing is precisely what the
paired shadow catches (collapse to chance in both grammars). So neither the invariant
nor K\* discriminates structure. What discriminates is **learnability**:

- **Attention**: hierarchy is free. Even a weak model learns hierarchical = local = 1.0;
  attention reaches any position at the same price, so non-locality costs nothing.
- **Recurrent state bottleneck** (RSSM): hierarchy has a real price — at matched
  configuration, ~**3× more training** to form (13,500 vs 4,500 steps at d_z = 16),
  because carrying the subject across distractors must squeeze through the small state.
  And it is a *speed* cost, not a capability ceiling: run long enough and even d_z = 8
  reaches 1.0.
- **The control that sharpens it**: an *unnatural* counting rule forms as fast as the
  local one. The cost tracks **non-locality** — the need to maintain state — not
  "naturalness" as such.

### 6.3 What this does and does not say about impossible languages

The claims at stake go back to Chomsky (1957; 1965): (1) linguistic competence is
structured hierarchically; (2) humanly *impossible* languages — violating that
structure — should be unlearnable, or at least harder; a claim sharpened for the LLM
era by Moro (2016) and by Chomsky, Roberts & Watumull (2023), who asserted that
language models learn impossible languages as easily as possible ones. Kallini et al.
(2024) tested that assertion and found the opposite: GPT-2 learns impossible languages
*worse*. Our contribution is a mechanistic refinement of *why*, and of *when the effect
should vanish*: on attention, any deterministic reordering is free (consistently, our
own scaled-down replication attempt failed instructively — bijective "impossible"
languages like shuffles and reversals were learned *better* than natural text, because
attention undoes bijections at no cost); the cost that exists is carried by
architectures with a state bottleneck, and it follows non-locality, not naturalness.
So claim (2) as usually phrased is architecture-relative: true as a *learning-speed*
statement on state-bottlenecked learners, false on attention — and testing
Kallini-strict (genuinely hard impossibles: non-bijective, counting-based, at GPT-2
scale) is beyond our toys; we state it as out of scope. Claim (3) of the tradition —
poverty of the stimulus — is untouched by anything here, deliberately.

## 7. Related work

**Mechanistic interpretability.** Induction heads and their formation schedule were
mapped by Olsson et al. (2022), within the circuits program of Elhage et al. (2021);
causal interventions on activations are that field's standard tool, with mean-ablation
and activation-patching practice codified by Wang et al. (2023) and Zhang & Nanda
(2024). We inherit the gesture and differ in the *epistemic packaging*: every
intervention here travels with a pre-registered kill criterion and a witness taxonomy
(paired shadow, symmetry control, notebook-free twin), and the claim being tested is
not a circuit description of one model but an **invariance across substrates** —
including one crossing of the implicit↔explicit divide, and one intervention applied
*during training* rather than at inference.

**Task and function vectors.** Hendel et al. (2023) and Todd et al. (2024) showed that
in-context rules condense into compact, transportable vectors. Our results refine
"compact" into a measured dimension with a validated ruler (variance = attribution
ordering, §4.4), add interventional necessity (freeze → 0.000, with witnesses), and
characterize structure their framing leaves open: separable composition, the
structured-multiset nature, and the architecture tiers.

**Belief-state geometry and computational mechanics.** Shai et al. (2024) showed
transformers linearly represent the belief simplex of a hidden process in their
residual stream — a lineage running back to computational mechanics (Crutchfield &
Young, 1989). We confirm the geometry (probe R² ≥ 0.91) and intervene on it: the
belief-notebook is causally necessary, but the naive dimensional prediction of the
geometric reading (K\* = k−1) is falsified — the predictively load-bearing dimension is
≈ k/2 (our own first fit of 2k/3 fell when the range was extended — §4.6), and only a
*declared* state (RSSM; Hafner et al., 2019) retains the full
simplex. Geometry present ≠ geometry load-bearing is, we believe, a useful corrective
for regression-based readings generally.

**Singular learning theory and developmental interpretability.** We use the local
learning coefficient (Watanabe, 2009; estimator of Lau et al., 2024) as an instrument,
in the spirit of Hoogland et al. (2024). Two contributions flow back: the freeze leaves
a matched-loss geometric imprint (a validated pre-registered prediction, §5.2), and a
caution — λ̂ is governed by architecture and does **not** read the notebook's dimension
(§5.6); studies correlating λ̂ with representational quantities across tasks should
control for shared task-complexity drivers.

**Emergent abilities.** Whether large-model capability jumps are real or
metric-induced (Wei et al., 2022; Schaeffer et al., 2023) is a question about score
curves; ours is about mechanism, and the two meet in one sentence: at the mechanism
level everything we measured is gradual (§5.1), while being causally all-or-nothing
under intervention (§3). Anderson (1972) remains the framing ancestor of the whole
question.

**Impossible languages.** Positioned in §6.3 (Chomsky, 1957; 1965; Moro, 2016;
Chomsky, Roberts & Watumull, 2023; Kallini et al., 2024): our contribution is the
mechanistic *why* and its architecture-relativity — the cost of structure follows
non-locality and is paid only through a state bottleneck.

**Slow variables.** The write-slow/reread-fast motif is synergetics' enslaving
principle (Haken, 1983), and linear notebook structure echoes the linear representation
hypothesis (Park et al., 2023). What we add to that old and good intuition is exactly
what it lacked: a falsifiable, portable gesture.

## 8. What we do not claim

The program's anti-overclaim register, verbatim in spirit:

- σ is a **candidate** slow variable designated a priori and tested by a falsifiable
  gesture — not "the" slow variable of a system, and never selected post hoc (§2.1).
- **No nontrivial formation-linked conserved charge.** The Noether machinery applies
  exactly (§5.4), but the verified charge is architectural; the symmetry origin of the
  obstruction is established, a conservation law for formation is not claimed.
- **No derivation that the freeze symmetry is the notebook's invariance group.** The
  dimension-locks-at-formation bridge (§5.5) is a measured, replicated coincidence.
- **K\* is neither universal nor a capability measure** (§4.5) — both were our own
  earlier readings, and both are retracted here. K\* is task- and notebook-specific;
  cross-task comparison of raw values is a category error (§4.3).
- **K\* is not a structure discriminator** (§6.2): matched hierarchical and local
  grammars distill notebooks of identical dimension — K\* measures payload, not
  computation; our pre-registered prediction to the contrary was falsified.
- **No net engineering gain from fine right-sizing** (§6.1): with the measurement
  honestly billed, measure-then-size loses to a sensible fixed default; the surviving
  engineering claim is the floor bound only.
- **λ̂ does not read K\*** (§5.6); no direct object↔dynamics link is claimed — the
  established relation is co-variation through task complexity.
- **The freeze does not sort storage regimes**: on a grokking substrate where σ is the
  sole route to the readout, memorized and generalized solutions die identically under
  the freeze — our pre-registered dissociation prediction was falsified (epilogue).
  With §6.2, the full bound: the gesture detects *necessity*, uniformly — not structure
  type, not upstream computation, not storage regime.
- **No generalization beyond tested substrates**: inference-side results cover models
  up to 3B parameters from four families; the real-network formation result covers one
  small architecture trained by us; hidden-state and structure-cost results are
  toy-scale. Strict impossible-language claims are explicitly out of scope (§6.3), as
  is poverty of the stimulus.

## 9. Open fronts

Stated as invitations — the instrument travels (Tier 0 runs on a laptop; §Repro):

1. **The mechanism of the K\* tiers.** What in a full-scale architecture compresses a
   notebook to K\* = 4? Norm placement and norm type are falsified on matched toys;
   the minimal toy cannot reach the low tier at all. A first depth×norm campaign on
   richer toys was disqualified by its own instrument (the whole-residual probe
   saturates on rich tasks — §4.7); the scoped next step is to *localize* the induction
   notebook in deep toys before re-running the grid. The most concrete open question
   this work produces.
2. **The formal bridge.** Derive — or refute — that the freeze symmetry is the
   invariance group whose dimension locks at formation. The program's theoretical core.
3. **What would test "the landscape reads the object" properly?** λ̂↔K\* is bounded
   (§5.6); a valid bridge needs an observable moved at fixed architecture *and* fixed
   task complexity.
4. **High-load separability.** Beyond two simultaneous notebooks, capacity — not
   separability — fails first on a 124M model; a larger model settles it.
5. **Scale.** The installed arc at 7B–72B; the formation arc on an *open-trajectory*
   full-scale model (public checkpoints make the freeze-during-formation gesture
   testable beyond our own training runs).
6. **Impossible languages, strict form.** Non-bijective, counting-based impossibles at
   GPT-2 scale — the substrate design, not compute, is the bottleneck (§6.3).

The standing offer of §1: take the gesture to a substrate we never touched, arm the
witnesses, pre-register the bar — and try to kill it.

## Reproducibility statement

Every claim maps to a command with a pinned environment, registered seeds, expected
numbers, and measured runtime (repository: `repro/`, the claim→command table). Tier 0 —
both arcs of the invariant on the toy — runs on a laptop CPU (~4 min installed arc,
~20 min formation arc) and is re-executed in CI on every commit, together with an
independent re-derivation of every verdict from the raw artifacts (no number in this
paper is hard-coded). Reproduction is bit-identical at fixed platform; verdicts are the
platform-portable claim, verified on two OS/architecture combinations. Tiers 1–2 (real
models; the training-time results) ship artifacts plus re-derivation first, retraining
scripts second.

---

*Paper v0 complete (abstract + §1–9 + reproducibility). Next passes: numbers audit
against re-derived verdicts as Tiers 1–2 land; figures F1–F9; LaTeX/PDF build.*
