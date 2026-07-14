"""Tier 0 — see the invariant with your own eyes, on a laptop, in minutes.

    python -m invariants.tier0 --arc installed
    python -m invariants.tier0 --arc formation
    python -m invariants.tier0 --arc both

Trains the toy from scratch (CPU), applies the freeze and its witnesses, writes
raw artifacts to --out, prints the report, and exits 0 iff the pre-registered
verdict HOLDS. Verify independently afterwards with:

    python -m invariants.verdicts artifacts/
"""
from __future__ import annotations

import argparse
import dataclasses
import json
import pathlib
import time

from .toy import formation, installed


def _jsonable(obj):
    if dataclasses.is_dataclass(obj):
        d = dataclasses.asdict(obj)
        # persist the derived bar so the artifact is self-describing
        d["collapse_bar"] = obj.collapse_bar
        return d
    return obj


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--arc", choices=("installed", "formation", "both"),
                   default="installed")
    p.add_argument("--seeds", type=int, nargs="+", default=None,
                   help="default: 0 1 2 (installed), 0 1 2 3 4 (formation)")
    p.add_argument("--train-steps", type=int, default=4000)
    p.add_argument("--out", type=pathlib.Path, default=pathlib.Path("artifacts"))
    args = p.parse_args(argv)
    args.out.mkdir(parents=True, exist_ok=True)

    ok = True
    if args.arc in ("installed", "both"):
        seeds = tuple(args.seeds) if args.seeds else (0, 1, 2)
        t0 = time.time()
        res = installed.run(seeds=seeds, train_steps=args.train_steps)
        print(f"\n=== INSTALLED ARC (freeze at inference) — {time.time()-t0:.0f}s ===")
        print(installed.report(res))
        out = {k: _jsonable(v) for k, v in res.items()}
        (args.out / "tier0_installed.json").write_text(json.dumps(out, indent=1))
        v, vt = res["notebook"], res["twin"]
        ok &= v.freeze_collapses and v.shadow_collapses and not vt.freeze_collapses

    if args.arc in ("formation", "both"):
        seeds = tuple(args.seeds) if args.seeds else (0, 1, 2, 3, 4)
        t0 = time.time()
        res = formation.run(seeds=seeds, train_steps=args.train_steps)
        print(f"\n=== FORMATION ARC (freeze during training) — {time.time()-t0:.0f}s ===")
        print(formation.report(res))
        (args.out / "tier0_formation.json").write_text(json.dumps(res, indent=1))
        m = lambda k: sum(r["final"] for r in res["conditions"][k]) / len(res["conditions"][k])
        from .contract import bar
        ok &= (m("notebook/live") >= 0.90
               and m("notebook/freeze") <= bar(m("notebook/live"), res["chance"])
               and m("twin/freeze") > bar(m("twin/live"), res["chance"]))

    print(f"\n>>> Tier 0 verdict: {'HOLDS' if ok else 'FALSIFIED / NON-CONCLUSIVE'}")
    print(">>> re-derive independently: python -m invariants.verdicts", args.out)
    return 0 if ok else 2


if __name__ == "__main__":
    raise SystemExit(main())
