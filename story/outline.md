# A Walk with Emmy Noether — chapter plan

> Working outline. Tone: progressive, honest about detours, one idea per chapter, one
> hand-drawn SVG figure minimum per chapter. No prerequisites beyond curiosity. The
> narrator is a walker, not a lecturer.

## 1. The graveyard of resemblances
Why "this curve looks like that curve" proves nothing, and why grand theories built on
resemblance die there. The rule of the walk: we only compare **experiments** — a gesture
you can perform identically in two unrelated systems, with the outcome that would kill
the idea written down *first*. Introduce Emmy Noether in three sentences: the woman who
taught physics that what *stays the same* is what explains what *changes*.
**Figure:** two lookalike curves from unrelated systems (the trap), vs. one gesture
applied to both (the method).

## 2. The notebook
The central image: fast activity *writes* slow notes, then *rereads* them to steer. The
slow variable σ. The gesture: freeze the notebook — replace its content by its "average
scribble" (same ink, zero information) while everything else keeps running. The invariant
candidate: if a capability lives in the notebook, freezing kills it — in *any* substrate.
**Figure:** the write→reread loop; the freeze as a grey smear.

## 3. A ladder of worlds
The same gesture climbed across substrates: a toy physics cascade → a mini-network built
on purpose (pairs A→B, fresh every time, impossible to memorize) → real language models
nobody tuned for us. Same freeze, same collapse. The witnesses that make it non-trivial:
the twin without a notebook (doesn't flinch), the paired shuffle (collapses the same),
the symmetry control (must survive — and does).
**Figure:** the ladder; the four-outcomes table (kill / kill / survive / survive).

## 4. The day we fooled ourselves
The anti-causal defect: our freeze leaked the future into training, and the network
*learned to exploit the leak*. How we caught it, why we threw away weeks of results,
what we rebuilt (automatic guards with teeth: "an intervention never beats the living
run"). The chapter that makes the rest believable.
**Figure:** the leak (an arrow from the future), and the guard that now bites.

## 5. How big is a notebook?
The puzzle: neither the notebook's average nor its deviations carry the rule (both
falsified!) — yet in a clean basis it compresses to a few dozen coordinates out of
hundreds. K\*, the notebook's dimension. The metrology chapter: how we checked the ruler
itself before trusting the number.
**Figure:** 768 dials, ~32 that matter; the wrong bases vs. the clean one.

## 6. Not all notebooks are alike
Measure K\* across model families: it clusters by **architecture, not size** (a model 6×
bigger, same K\*; a differently-built model, K\* four times smaller). The candidate
explanations we falsified on purpose-built toys (norm placement, norm type) — the cause
is still open, and we say so.
**Figure:** the tiers (4 ≪ 16 < 32) with model logos as hikers on different paths.

## 7. A law at last — but not the one we wanted
Give the network a world with k hidden states; theory whispers the notebook should have
dimension k−1. Four rounds of pre-registered discipline (a beautiful motif held at arm's
length until a test could *conclusively* speak) — and the verdict: there **is** a law,
monotone, nearly linear… with slope ~2/3, not 1. The discovered notebook compresses the
geometry it carries; the predictive dimension is smaller than the geometric one.
**Figure:** K\*(k) data points against the two candidate lines (k−1 dashed, falsified;
k/2 solid — with the 2k/3 first-fit shown falling; see the post-publication signpost).

## 8. The declared and the discovered
Two architectures that share nothing: a transformer whose notebook we had to *find*, and
a world model whose state is *declared by construction*. Same freeze, same death. The
invariant crosses the implicit↔explicit divide — and the dimensions differ exactly as
chapter 7 predicts (declared state keeps the full geometry k−1; discovered notebook
compresses to ~k/2).
**Coda — the pair that killed a bridge.** The same two machines, reused as an
instrument: they move the notebook's dimension at fixed task complexity, and thereby
falsified our own freshly-supported prediction that the loss landscape's complexity
(the local learning coefficient) *reads* the notebook's size. Built in the morning,
bounded by evening: λ̂ belongs to the architecture, K\* to the task; they only travel
together when the task drags both. The walk's fastest full cycle of
conjecture → support → falsification, and proof that a matched pair of substrates is
worth more than any single one.
**Figure:** the two machines side by side, one gesture, one signature; inset: K\*
tripling while λ̂ stays flat.

## 9. What structure costs
The Chomsky question, made mechanistic: are "impossible" languages harder for a learning
machine? Build matched grammars — agreement with the *hierarchically correct* subject
across nested clauses, versus the *nearest* noun — and race architectures on them. For
**attention**, hierarchy is free: any position is one hop away, structured = local, even
for a tiny model. For a **recurrent state bottleneck**, hierarchy has a real price —
~3× slower to learn at matched configuration — because carrying the subject across the
distractors must squeeze through the small state. And the twist: an *unnatural* counting
rule forms as fast as the local one — **the cost follows non-locality, not
"naturalness"**. The price of structure is paid in learning speed, and the architecture
decides who pays. Plus what the dimension measurement buys in engineering: K\* predicts
the floor of a world model's latent size (undersize it and the target is never reached;
the sweet spot sits near ~1.4×K\*).
**Figure:** two racers on the same grammar — attention strolling, the recurrent
bottleneck climbing; the cost table; the latent-size floor curve.

## 10. Where the trail goes cold
What this walk does **not** claim (small models, one self-trained formation run, the
formal bridge unproven). The open fronts, stated as invitations. And the standing offer:
the gesture is packaged — take it to a substrate we never touched, and try to kill it.
**Figure:** the map so far, with the blank regions drawn honestly blank.

## Epilogue. Postcards from after the walk (LIVING)
The page where post-publication verdicts land, newest first, the ones that catch us at
the top: the slope corrected (2k/3 → k/2, the proof row) then DERIVED (spectral gap), the saturated tiers probe
(instrument, not verdict), the structure-blind ruler, the tempered right-sizing — and
the one that held (three seeds, two machines). When a postcard corrects a chapter, the
chapter gets a dated signpost (chapter 7 wears the first); this page keeps the "before"
honest. **Figure:** the signposts on the trail.

---

### Running motifs
- Every chapter ends with *"what would have killed this, and didn't"* (or **did** — ch. 4, 7).
- Noether appears at chapter heads via one-line epigraphs connecting her two legacies
  (invariant theory; the 1918 theorem) to the walk.
- Numbers stay out of the prose; each figure caption links to the paper section and the
  repro command that regenerates it.
