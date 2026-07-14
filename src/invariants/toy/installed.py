"""Installed arc on the toy (claim C1, paper §3.2; story chapters 2-3).

Two systems enter the interventional contract:
- the NOTEBOOK system : fresh-pair recall — the association is written into
                        context by the fast dynamics and reread (carried state);
- the TWIN system     : same architecture, same surface form, association fixed
                        in the weights (no carried state).

Same gesture on both. The kill criterion is evaluated against FreezeVerdict,
with the bar posed before any run (chance + 0.5·(live − chance)).
"""
from __future__ import annotations

import numpy as np
import torch

from ..contract import FreezeVerdict, Intervention, measure
from . import model as M
from . import task as T

TRAIN_STEPS = 4000
BATCH = 128
EVAL_BATCH = 2048


class ToySystem:
    """Trains one model per seed (lazily, cached), measures capability under the
    contract's interventions on held-out sequences."""

    chance = T.CHANCE

    def __init__(self, twin: bool, train_steps: int = TRAIN_STEPS):
        self.twin = twin
        self.train_steps = train_steps
        self._models: dict[int, M.InductionToy] = {}

    def _sampler(self, rng: np.random.Generator):
        if self.twin:
            perm = T.fixed_permutation(np.random.default_rng(0))  # pi fixed for ALL
            return lambda b, r: T.sample_twin(b, perm, r)
        return T.sample_induction

    def _get(self, seed: int) -> M.InductionToy:
        if seed not in self._models:
            torch.manual_seed(seed)
            rng = np.random.default_rng(seed)
            net = M.InductionToy()
            M.train(net, self._sampler(rng), self.train_steps, BATCH, rng)
            self._models[seed] = net
        return self._models[seed]

    def capacity(self, intervention: Intervention, seed: int) -> float:
        net = self._get(seed)
        rng = np.random.default_rng(10_000 + seed)  # held-out eval stream
        toks_np, tgt_np = self._sampler(rng)(EVAL_BATCH, rng)
        torch.manual_seed(20_000 + seed)  # shadow shuffle reproducible
        return net.accuracy(torch.from_numpy(toks_np), torch.from_numpy(tgt_np), intervention)


def run(seeds: tuple[int, ...] = (0, 1, 2), train_steps: int = TRAIN_STEPS) -> dict:
    notebook = ToySystem(twin=False, train_steps=train_steps)
    twin = ToySystem(twin=True, train_steps=train_steps)
    v_nb = measure(notebook, seeds)
    v_tw = measure(twin, seeds)

    per_seed = {
        name: {iv: [sys.capacity(iv, s) for s in seeds] for iv in ("live", "freeze", "shadow")}
        for name, sys in (("notebook", notebook), ("twin", twin))
    }
    return {
        "seeds": list(seeds),
        "train_steps": train_steps,
        "chance": T.CHANCE,
        "notebook": v_nb,
        "twin": v_tw,
        "per_seed": per_seed,
    }


def report(res: dict) -> str:
    v: FreezeVerdict = res["notebook"]
    vt: FreezeVerdict = res["twin"]
    lines = [
        f"chance = {res['chance']:.4f}   seeds = {res['seeds']}",
        "",
        f"{'':14}{'live':>8}{'freeze':>8}{'shadow':>8}{'bar':>8}",
        f"{'notebook':14}{v.live:8.3f}{v.freeze:8.3f}{v.shadow:8.3f}{v.collapse_bar:8.3f}",
        f"{'twin':14}{vt.live:8.3f}{vt.freeze:8.3f}{vt.shadow:8.3f}{vt.collapse_bar:8.3f}",
        "",
        f"freeze collapses the notebook system : {v.freeze_collapses}   (must be True)",
        f"shadow collapses the notebook system : {v.shadow_collapses}   (must be True)",
        f"freeze collapses the twin            : {vt.freeze_collapses}   (must be False)",
    ]
    return "\n".join(lines)
