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

---

*Sections 4–9: see [`outline.md`](outline.md). Next to be drafted: §4 (The object).*
