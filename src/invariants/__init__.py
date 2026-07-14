"""Interventional invariants — the contract, the guards, and the Tier-0 toy.

A capability is characterized not by what it looks like but by what happens to it
under a NAMED intervention on its pre-registered slow variable σ (the "notebook").
See the paper (paper/draft.md) for the method, and repro/README.md for the
claim → command map.
"""
from .contract import (  # noqa: F401
    INTERVENTIONS,
    TAXONOMY,
    FreezeVerdict,
    Intervention,
    InterventionalSystem,
    Verdict,
    bar,
    measure,
)

__version__ = "0.1.0"
