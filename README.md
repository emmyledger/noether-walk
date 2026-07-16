# noether-walk

[![tier0](https://github.com/emmyledger/noether-walk/actions/workflows/ci.yml/badge.svg)](https://github.com/emmyledger/noether-walk/actions/workflows/ci.yml)
[![paper-pdf](https://github.com/emmyledger/noether-walk/actions/workflows/paper.yml/badge.svg)](https://github.com/emmyledger/noether-walk/actions/workflows/paper.yml)
[![DOI](https://zenodo.org/badge/1300545702.svg)](https://zenodo.org/badge/latestdoi/1300545702)

> *Same gesture, same signature — and a kill criterion written down before every step.*

**This is a living repository.** Calculations are still landing: corrections arrive as
dated signposts in the chapters and as postcards in the
[epilogue](story/epilogue-postcards.md) — the ones that catch us go at the top.

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

| door | for whom | start here |
|---|---|---|
| **A Walk with Emmy Noether** | anyone curious; no prerequisites; diagrams, one idea at a time, including the day we fooled ourselves | [chapter 1](story/ch01-the-graveyard-of-resemblances.md) (plan: [`story/outline.md`](story/outline.md)) |
| **Freezing the Notebook** *(formal paper)* | researchers; claims, numbers, methods, reservations | [**PDF**](https://github.com/emmyledger/noether-walk/releases/latest/download/freezing-the-notebook.pdf) (built by CI, attached to each release) · source: [`paper/draft.md`](paper/draft.md) · [references](paper/references.md) |

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

### Quickstart (Tier 0)

```bash
make setup          # venv + pinned deps (CPU-only torch is enough)
make test           # unit tests: contract, guards, toy
make tier0          # installed arc: train the toy, freeze the notebook, watch
make tier0-formation  # formation arc: freeze during training — it never forms
make verdicts       # re-derive every verdict from the raw artifacts, independently
```

`make tier0` exits 0 iff the pre-registered verdict HOLDS — the same check runs
in CI on every commit.

## Feedback — and how to try to kill this

Issues and Discussions are open — disagreement, replication reports, and "this breaks on
my machine" are all equally welcome. The most useful feedback of all: **an attempt to
falsify the invariant on a substrate we didn't test.** The protocol, what counts as a
kill, and the pre-registration template: [`FALSIFY.md`](FALSIFY.md). A clean
falsification will be posted in the epilogue louder than any confirmation.

*Even this repository's own reception runs under the walk's rules: a pre-registered
experiment, its instrument, and its honest closure live in [`meta/`](meta/). However
you got here, the referrer ledger is curious about you.*

## Cite

See [`CITATION.cff`](CITATION.cff) (GitHub's "Cite this repository" button uses it) —
and if you falsify this work, open an issue instead: that is worth more to us than the
citation. Each release is archived with a DOI on Zenodo (badge above); the paper PDF is
attached to every [release](https://github.com/emmyledger/noether-walk/releases).

## License

Code: [MIT](LICENSE). Texts and figures (story, paper): [CC BY 4.0](LICENSE-texts.md) —
share and adapt freely, with attribution.

— Emmy Ledger
