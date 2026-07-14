"""Formation arc on the toy (claim C1b, paper §3.3; story chapter 2's bold half).

Same toy, same σ, same gesture as the installed arc; only the TIMING moves: the
intervention runs during the WHOLE training. Predicted signature: the notebook
capability never forms under the permanent freeze, while the twin (weight-carried)
learns fine under the very same gesture — the freeze obstructs the capability,
not optimization.

Note on causality: the toy's intra-sequence freeze is causal here because the
loss lives at the final position only. See model.train's docstring and paper §2.4.
"""
from __future__ import annotations

import numpy as np
import torch

from . import model as M
from . import task as T

SEEDS = (0, 1, 2, 3, 4)
TRAIN_STEPS = 4000
BATCH = 128
EVAL_BATCH = 2048
CURVE_EVERY = 250

# (system, training intervention) — the pre-registered conditions
CONDITIONS = [
    ("notebook", "live"),
    ("notebook", "freeze"),
    ("notebook", "shadow"),
    ("twin", "live"),
    ("twin", "freeze"),
]


def _sampler(system: str):
    if system == "twin":
        perm = T.fixed_permutation(np.random.default_rng(0))  # same pi as installed
        return lambda b, r: T.sample_twin(b, perm, r)
    return T.sample_induction


def _eval(net, system: str, seed: int, intervention: str) -> float:
    rng = np.random.default_rng(10_000 + seed)
    toks_np, tgt_np = _sampler(system)(EVAL_BATCH, rng)
    torch.manual_seed(20_000 + seed)
    return net.accuracy(torch.from_numpy(toks_np), torch.from_numpy(tgt_np), intervention)


def run(seeds=SEEDS, train_steps: int = TRAIN_STEPS) -> dict:
    out = {"seeds": list(seeds), "train_steps": train_steps, "chance": T.CHANCE,
           "conditions": {}}
    for system, iv in CONDITIONS:
        key = f"{system}/{iv}"
        rows = []
        for seed in seeds:
            torch.manual_seed(seed)
            rng = np.random.default_rng(seed)
            net = M.InductionToy()
            curve = []
            M.train(net, _sampler(system), train_steps, BATCH, rng,
                    log_every=CURVE_EVERY, intervention=iv,
                    eval_fn=lambda m, s: curve.append((s, _eval(m, system, seed, iv))))
            # verdict metric: final accuracy UNDER the training condition
            final = _eval(net, system, seed, iv)
            # pre-registered post-hoc characterization: the other regime
            other = "live" if iv != "live" else "freeze"
            final_other = _eval(net, system, seed, other)
            rows.append({"seed": seed, "final": final,
                         f"final_{other}": final_other, "curve": curve})
        out["conditions"][key] = rows
    return out


def report(res: dict) -> str:
    from ..contract import bar
    m = lambda k: sum(r["final"] for r in res["conditions"][k]) / len(res["conditions"][k])
    bar_nb = bar(m("notebook/live"), res["chance"])
    bar_tw = bar(m("twin/live"), res["chance"])
    lines = [
        f"chance = {res['chance']:.4f}   seeds = {res['seeds']}",
        "",
        f"{'condition':18}{'final acc':>10}",
    ]
    for key in res["conditions"]:
        lines.append(f"{key:18}{m(key):10.3f}")
    lines += [
        "",
        f"notebook/live reference sharp (>= 0.90)      : {m('notebook/live') >= 0.90}",
        f"permanent freeze never forms (<= bar {bar_nb:.3f}) : {m('notebook/freeze') <= bar_nb}",
        f"permanent shadow never forms (<= bar {bar_nb:.3f})  : {m('notebook/shadow') <= bar_nb}",
        f"twin LEARNS under the same freeze (> bar {bar_tw:.3f}): {m('twin/freeze') > bar_tw}",
    ]
    return "\n".join(lines)
