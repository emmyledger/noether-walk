# Reproduction — the spine of this repository

> Rule: **no claim without a command.** Every number in the paper is re-derived by code
> from raw artifacts (never hard-coded), and every figure regenerates from a script.

## Tiers

| tier | what you see | hardware | time | status |
|---|---|---|---|---|
| **0** | freeze the notebook of a small in-context learner → capability collapses; twin-without-notebook and paired-shadow witnesses behave as predicted; both arcs (installed + formation) | laptop CPU | ~4 min (installed) / ~20 min (formation) | **✅ shipped & CI-checked** |
| **1** | freeze + K\* measurements on real models (GPT-2, Pythia, Qwen2.5-0.5B, OLMo-2-1B); architecture tiers; metrology check | 1 GPU or patient CPU | hours | ☐ to package |
| **2** | formation arc on a real network (0/3 frozen runs form at 16× the living formation point); K\*(k) law on hidden-state tracking; LLC at matched loss | 1 GPU, longer runs | documented per-claim | ☐ artifacts + re-derivation first, retraining optional |

## Quickstart

```bash
make setup            # venv + deps (CPU torch is enough)
make test             # 14 unit tests: contract, guards, toy
make tier0            # installed arc  (~4 min on a laptop CPU)
make tier0-formation  # formation arc  (~20 min)
make verdicts         # independent re-derivation from the raw artifacts
```

`python -m invariants.tier0` exits 0 iff the pre-registered verdict HOLDS.

## Claim → command map

| claim | paper § | command | seeds | runtime* | expected |
|---|---|---|---|---|---|
| **C1** installed arc (toy): freeze/shadow collapse the notebook system, the twin doesn't flinch | §3.2 | `python -m invariants.tier0 --arc installed` | 0 1 2 | ~4 min | live 1.000 → freeze **0.119**, shadow **0.093** (bar 0.515); twin 1.000 under freeze — verdict HOLDS |
| **C1-r** same, fresh seeds (replication) | §2.5 | `python -m invariants.tier0 --arc installed --seeds 100 101 102` | 100 101 102 | ~4 min | freeze **0.126**, shadow **0.088**; twin 1.000 — verdict HOLDS |
| **C1b** formation arc (toy): permanent freeze → never forms; twin learns under the same freeze | §3.3 | `python -m invariants.tier0 --arc formation` | 0 1 2 3 4 | ~20 min | notebook/live 1.000; notebook/freeze **0.121** (bar 0.516, never forms); twin/freeze **1.000** — verdict HOLDS |
| C2 installed arc, real models ×4 | §3.2 | *(Tier 1, to package)* | — | — | — |
| C3 formation arc, real network 0/3 | §3.3 | *(Tier 2)* | — | — | — |
| C4 K\* metrology (variance = attribution) | §4.4 | *(Tier 1)* | — | — | — |
| C5 architecture tiers 4/16/32 | §4.5 | *(Tier 1)* | — | — | — |
| C6 K\*(k) ≈ k/2 (8 values of k; first fit 2k/3 corrected), k−1 falsified | §4.6 | *(Tier 2)* | — | — | — |
| C7 implicit↔explicit same signature | §3.4 | *(Tier 2)* | — | — | — |
| C8 LLC results (incl. the λ̂/K\* decoupling) | §5 | *(Tier 2)* | — | — | — |
| C9 latent floor (right-sizing tempered vs fair baseline; K\* blind to structure) | §6 | *(Tier 2)* | — | — | — |

\* measured on an Apple-silicon laptop CPU; CI (ubuntu) re-runs C1 on every commit.

## What "reproduces" means here

- **Bit-identical reproduction**: same seeds + same environment → byte-identical
  artifact JSON (we verified run-vs-run equality before shipping).
- **Replication**: fresh seeds → same verdict under the frozen criteria (C1-r).
- **Platform note**: exact third-decimal numbers are guaranteed only for a given
  platform + torch build; the *verdicts* are what must hold everywhere, and CI
  asserts exactly that.
- Reference artifacts from the runs above are committed in [`expected/`](expected/);
  the environment used is pinned in [`requirements.lock`](requirements.lock)
  (python 3.14 / torch 2.13.0 / numpy 2.5.1 at ship time).
- Verdicts are re-derived from raw artifacts by [`invariants/verdicts.py`](../src/invariants/verdicts.py),
  which shares no logic with the runners beyond the published bar formula.

## Porting checklist (Tier 1-2)

- [x] Interventional contract (gesture taxonomy + guards + verdict re-derivation)
- [x] Tier 0 toy: installed + formation arcs, CLI, tests, CI
- [ ] Tier 1: real-model freeze + K\* runners (GPT-2 / Pythia / Qwen / OLMo)
- [ ] Tier 2: formation-arc artifacts + re-derivation; HMM K\*(k) + LLC runners
- [ ] Seed registry; figure-regeneration scripts wired to claims
