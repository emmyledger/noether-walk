"""Independent verdict re-derivation (paper §2.4, "no number is hard-coded").

Reads ONLY the raw JSON artifacts written by the runners and re-derives every
clause and verdict from them. Shares no logic with the runners beyond the
published bar formula. Usage:

    python -m invariants.verdicts [artifacts_dir]
"""
from __future__ import annotations

import json
import pathlib
import sys

CHANCE_TOY = 1 / 32
COLLAPSE_FRACTION = 0.5


def _bar(live: float, chance: float) -> float:
    return chance + COLLAPSE_FRACTION * (live - chance)


def installed(art: pathlib.Path) -> dict:
    d = json.loads((art / "tier0_installed.json").read_text())
    nb, tw = d["notebook"], d["twin"]
    bar_nb, bar_tw = _bar(nb["live"], d["chance"]), _bar(tw["live"], d["chance"])
    clauses = {
        "freeze collapses the notebook system": nb["freeze"] <= bar_nb,
        "shadow collapses the notebook system": nb["shadow"] <= bar_nb,
        "freeze spares the twin": tw["freeze"] > bar_tw,
    }
    return {
        "claim": "C1 (toy, installed arc)",
        "clauses": clauses,
        "verdict": "HOLDS" if all(clauses.values()) else "FALSIFIED",
    }


def formation(art: pathlib.Path) -> dict:
    d = json.loads((art / "tier0_formation.json").read_text())
    m = lambda k: sum(r["final"] for r in d["conditions"][k]) / len(d["conditions"][k])
    bar_nb = _bar(m("notebook/live"), CHANCE_TOY)
    bar_tw = _bar(m("twin/live"), CHANCE_TOY)
    clauses = {
        "live reference sharp (>= 0.90)": m("notebook/live") >= 0.90,
        "permanent freeze under bar (never formed)": m("notebook/freeze") <= bar_nb,
        "twin learns under the same freeze": m("twin/freeze") > bar_tw,
    }
    return {
        "claim": "C1b (toy, formation arc)",
        "clauses": clauses,
        "verdict": "HOLDS" if all(clauses.values()) else "FALSIFIED/NON-CONCLUSIVE",
    }


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    art = pathlib.Path(args[0]) if args else pathlib.Path("artifacts")
    ok = True
    for name, fn in (("installed", installed), ("formation", formation)):
        path = art / f"tier0_{name}.json"
        if not path.exists():
            print(f"[skip] {path} not found")
            continue
        res = fn(art)
        print(f"\n== {res['claim']} ==")
        for clause, val in res["clauses"].items():
            print(f"  {'PASS' if val else 'FAIL'}  {clause}")
        print(f"  verdict: {res['verdict']}")
        ok = ok and res["verdict"] == "HOLDS"
    return 0 if ok else 2


if __name__ == "__main__":
    raise SystemExit(main())
