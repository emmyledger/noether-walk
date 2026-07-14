# Reproduction — the spine of this repository

> Rule: **no claim without a command.** Every number in the paper is re-derived by code
> from raw artifacts (never hard-coded), and every figure regenerates from a script.

## Tiers

| tier | what you see | hardware | time | status |
|---|---|---|---|---|
| **0** | freeze the notebook of a small in-context learner → capability collapses; twin-without-notebook and symmetry control survive | laptop CPU | minutes | ☐ to package |
| **1** | freeze + K\* measurements on real models (GPT-2, Pythia, Qwen2.5-0.5B, OLMo-2-1B); architecture tiers; metrology check | 1 GPU or patient CPU | hours | ☐ to package |
| **2** | formation arc: freezing during training prevents induction heads from forming (0/3 at 16× the living formation point); K\*(k) law on hidden-state tracking; LLC at matched loss | 1 GPU, longer runs | documented per-claim | ☐ artifacts + re-derivation first, retraining optional |

Environment: pinned lockfile (exact torch / transformer-lens versions), registered seeds,
committed expected outputs. Tier 0 runs in CI on every commit.

## Claim → command map (to fill as code lands)

| claim ID | paper § | command | seed(s) | runtime | expected |
|---|---|---|---|---|---|
| C1 installed-arc collapse (toy) | §3 | `make tier0` | — | ~min | live ≈ 1.0 → frozen ≈ chance; controls survive |
| C2 installed-arc collapse (real models ×4) | §3 | — | — | — | — |
| C3 formation arc 0/3 | §3 | — | — | — | — |
| C4 K\* metrology (variance = attribution) | §4 | — | — | — | — |
| C5 architecture tiers 4/16/32 | §4 | — | — | — | — |
| C6 K\*(k) ≈ 2k/3, k−1 falsified | §4 | — | — | — | — |
| C7 implicit↔explicit same signature | §3 | — | — | — | — |
| C8 LLC live > frozen at matched loss | §5 | — | — | — | — |
| C9 latent floor / cost trough | §6 | — | — | — | — |

## Porting checklist (from the private research tree)

- [ ] Extract the interventional contract (gesture taxonomy + guards + verdict
      re-derivation) as the package core.
- [ ] One runner per claim family; one `make`/CLI entry point per tier.
- [ ] Sweep names/paths/comments for research-tree vocabulary; keep the public lexicon
      (notebook, slow variable, freeze, invariant, formation).
- [ ] Registry of seeds; commit raw verdict artifacts for Tier 2 claims.
- [ ] CI: Tier 0 on every push; lockfile install from scratch.
