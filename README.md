# noether-walk

> *Same gesture, same signature — and a kill criterion written down before every step.*

This repository is a walk. Not a hunt for "emergence" — a walk guided by Emmy Noether's
oldest lesson: **if you want to understand a system, look for what stays the same while
everything else changes.** We went looking for an *interventional invariant* of how
capabilities form in learning systems: one gesture (freeze the slow variable — the
"notebook" a system writes and rereads), one predicted signature (the capability
collapses), and, before every experiment, a written criterion that would kill the
hypothesis.

Across toy physics, purpose-built mini-networks, and real transformers (GPT-2, Pythia,
Qwen, OLMo), through seven types of capability and one crossing of the implicit↔explicit
divide, **the invariant has never been falsified**. Plenty of other things were — this
repository keeps the dead ends on the map, because a walk without wrong turns is a walk
someone else took for you.

## Two doors

| door | for whom | where |
|---|---|---|
| **A Walk with Emmy Noether** | anyone curious; no prerequisites; diagrams, one idea at a time, including the day we fooled ourselves | [`story/`](story/) |
| **Freezing the Notebook** *(formal paper)* | researchers; claims, numbers, methods, reservations | [`paper/`](paper/) |

## Reproducibility is the spine, not an appendix

Every claim in the paper maps to a runnable command with a pinned environment, a
registered seed, an expected runtime, and expected numbers. Reproduction comes in tiers:

- **Tier 0 — see it with your own eyes.** One command, laptop CPU, minutes: freeze the
  notebook of a small in-context learner and watch the capability collapse (and the
  controls survive).
- **Tier 1 — the real models.** Hours, one GPU (or a patient CPU): the freeze and the
  notebook-dimension measurements on GPT-2 / Pythia / Qwen / OLMo.
- **Tier 2 — formation.** Freezing during training of a real network (the costliest and
  strongest result). Compute documented honestly; raw artifacts provided so verdicts can
  be re-derived without retraining.

Details and the claim→command table: [`repro/`](repro/).

## Feedback

Issues and Discussions are open — disagreement, replication reports, and "this breaks on
my machine" are all equally welcome. The most useful feedback of all: **an attempt to
falsify the invariant on a substrate we didn't test.**

— Emmy Ledger
