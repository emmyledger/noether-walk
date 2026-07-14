# Freezing the Notebook: An Interventional Invariant of Capability Formation Across Substrates

**Emmy Ledger**
*Draft v0.1 — abstract and introduction only. Outline for the remaining sections:
[`outline.md`](outline.md). Every quantitative claim will link to a reproduction
command; see [`../repro/`](../repro/).*

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
tracking tasks: K\*(k) is monotone and near-linear but ≈ 2k/3, falsifying the naive
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
*notebook*. In a transformer solving an in-context task, σ is the residual-stream
content that downstream heads reread; in a recurrent world model, σ is the latent state
by construction; in our toy cascade, σ is a slow memory that gates a second instability.
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
  object: monotone, near-linear, **≈ 2k/3 rather than the k−1** the belief-simplex
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
- **The price of structure, and what the measurement buys** (§6). K\* predicts the
  floor of a world model's latent size (with a cost trough near ~1.4×K\*), and the cost
  of maintaining non-local structure is paid only by architectures that bottleneck
  state — a mechanistic refinement of the impossible-languages debate.

### 1.4 Relation to the emergence literature

We use the word once, deliberately. A lively debate asks whether "emergent abilities"
of large models are real discontinuities or artifacts of metric choice. We take no side
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
   obvious causal candidates falsified on matched toys), and the law K\*(k) ≈ 2k/3
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
  models.
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
with perturbation. The frozen page is the calmest object in the system; the only thing
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
us; and one small transformer we trained from scratch on real code — across seven
capability types: fresh-pair recall, induction, in-context rules (task vectors),
rule composition, hidden-state tracking, syntactic agreement, and explicit world-model
state maintenance.

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
induction heads form abruptly at 145–195M tokens (the onset has the documented shape).
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
- **Explicit** — a recurrent world model (RSSM) on the *same* process, whose state z is
  σ **by construction** (R²(z→belief) 0.93–0.98). Freeze z: capability ≈ 0, shadow
  negative — the **same signature**.

One gesture, two architectures that share neither mechanism, training objective, nor
even whether σ is an emergent object or a declared one — and the same death. This is
the result that carries the trans-substrate thesis, and it sets up a quantitative twist
(§4.6): the *declared* state retains the full belief geometry (K\* ≈ k−1), while the
*discovered* notebook compresses it (K\* ≈ 2k/3).

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
~O(20–32); a one-bit syntactic-agreement notebook measures ~2; a k-state belief notebook
measures ~2k/3 (§4.6). These are different objects; comparing their K\* across tasks is
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

### 4.6 The first functional law: K\*(k) ≈ 2k/3, and the falsification of k−1

The tiers are categorical. A *law* needs a substrate where theory predicts K\* as a
function of a dial we control. Hidden-state tracking provides one: a k-state hidden
process with ambiguous emissions forces the system to carry a belief over states;
belief-state geometry predicts that belief lives on the (k−1)-simplex, so the naive
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
   strictly increasing, undershooting k−1 by a growing gap (k=18 → 11 vs 17); the slope
   is ≈ 2/3. Replicated on a fresh seed ({5, 7, 9} at k = 9, 12, 15).

The resolution of the apparent paradox is itself a result: the belief **is**
geometrically (k−1)-dimensional (that is what the high R² says), but its predictive
weight is front-loaded. K\* measures the *predictively load-bearing* dimension, not the
geometric one. The control that clinches it is the explicit world model (§3.4): its
*declared* state z gives K\* = {6, 11, 16, 16} against k−1 = {5, 11, 14, 17} — the
declared state keeps the whole simplex; the discovered notebook compresses it. Both laws
replicate across seeds, with explicit > implicit at every k.

This is the first *functional* dependence of K\* we know of (versus the categorical
tiers of §4.5), and it was reached by falsifying the beautiful prediction rather than
hosting it.

### 4.7 Mechanistic byproducts

Two facts any reuser of the instrument needs. **Carried vs. reread**: for hidden-state
tracking, σ is carried *forward* along the computation at the current position — not
reread from past context as induction and rules are; freezing the reading path alone is
not sufficient, and the correct gesture (freeze both routes) was pre-registered once
this was understood. **Layer migration**: σ lives at layer 1 in a 2-layer model but at
the belief-complete layer in deeper ones. Notebooks have addresses, and the addresses
depend on architecture and depth.

---

*Sections 5–9: see [`outline.md`](outline.md). Next to be drafted: §5 (The dynamics).*
