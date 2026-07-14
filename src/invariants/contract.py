"""The interventional contract — substrate-agnostic core of the method (paper §2).

A capability enters the contract by exposing `capacity(intervention, seed)` and a
`chance` level; the core below decides the verdict. Every threshold is posed BEFORE
any run; the verdict is read only against it.

## The gesture and its witnesses (paper §2.2)

- **freeze** — replace σ (the notebook) by its mean over σ's AXIS OF VARIATION
  (time / positions / batch, depending on the substrate). Mean magnitude kept,
  information destroyed. Applied at TRAINING time, the statistic must be CAUSAL
  w.r.t. the loss (paper §2.4): no mean or permutation that lets a position see
  its own future.
- **shadow** (the paired shadow) — break the pairing between what the reader looks
  up and what it reads back, marginals preserved. A JOINT permutation of
  (key, value) entries is not a shadow but a symmetry — see below.
- **symmetry_control** — a σ-transformation that PRESERVES the pairing,
  pre-registered to NOT collapse. It is what makes a collapse *specific* rather
  than "any big perturbation kills".
- **content_shadow** — σ taken from a neighbouring sequence: positional marginal
  kept, content wrong.

## The discriminant (the twin without a notebook)

A matched system whose capability lives in the WEIGHTS, pre-registered to SURVIVE
the same gesture — posed at a non-saturated operating point, and where possible
CALIBRATED: its allowed degradation is a ceiling measured on the live model, not a
guessed threshold.

## The verdict

The invariant HOLDS on a substrate iff freeze / shadow / content_shadow collapse
the notebook capability below the bar, the symmetry_control does not, and the
discriminant survives. It is FALSIFIED as soon as one of those fails; and
NON-CONCLUSIVE if the live capability is not itself sharp (the substrate was
mis-posed; the invariant was not tested).
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, Protocol

__all__ = [
    "Intervention", "INTERVENTIONS", "TAXONOMY", "InterventionalSystem",
    "FreezeVerdict", "Verdict", "measure", "bar",
]

# The full taxonomy as a TYPE. "live" is the untouched system; the rest are the
# gesture and its matched shadows/controls. A substrate implements whichever
# conditions its plan pre-registers.
Intervention = Literal[
    "live", "freeze", "shadow", "symmetry_control", "content_shadow"
]
#: the minimal battery (live / freeze / paired shadow)
INTERVENTIONS: tuple[Intervention, ...] = ("live", "freeze", "shadow")
#: the full taxonomy (adds the symmetry control and the content shadow)
TAXONOMY: tuple[Intervention, ...] = (
    "live", "freeze", "shadow", "symmetry_control", "content_shadow",
)

COLLAPSE_FRACTION = 0.5  # bar = chance + COLLAPSE_FRACTION·(live − chance)


class InterventionalSystem(Protocol):
    """A substrate exposing the gesture on its pre-registered σ."""

    #: capability level of pure chance, posed BEFORE any run
    chance: float

    def capacity(self, intervention: Intervention, seed: int) -> float:
        """Measure the capability carried by σ under one intervention."""
        ...


def bar(live: float, chance: float, collapse_fraction: float = COLLAPSE_FRACTION) -> float:
    """The collapse bar: capability at or below it counts as collapsed."""
    return chance + collapse_fraction * (live - chance)


@dataclass(frozen=True)
class FreezeVerdict:
    """Outcome of the minimal battery (live / freeze / shadow). `Verdict` below is
    the general, calibrated form."""

    live: float
    freeze: float
    shadow: float
    chance: float
    collapse_fraction: float = COLLAPSE_FRACTION

    @property
    def collapse_bar(self) -> float:
        return bar(self.live, self.chance, self.collapse_fraction)

    @property
    def freeze_collapses(self) -> bool:
        return self.freeze <= self.collapse_bar

    @property
    def shadow_collapses(self) -> bool:
        return self.shadow <= self.collapse_bar


@dataclass(frozen=True)
class Verdict:
    """The general verdict, with the discriminant optionally CALIBRATED.

    `notebook` maps each pre-registered intervention to the notebook system's
    capability. `discriminant_live` / `discriminant_frozen` are the matched
    weight-carried twin (expected to survive). `discriminant_ceiling`, if given,
    is the allowed degradation measured on the live model (a calibrated cap);
    without it, the twin must simply stay above its own bar.
    """

    notebook: dict[str, float]
    chance: float
    live_floor: float = 0.30                    # sharpness floor for NON-CONCLUSIVE
    discriminant_live: float | None = None
    discriminant_frozen: float | None = None
    discriminant_ceiling: float | None = None
    collapse_fraction: float = COLLAPSE_FRACTION
    _expected_collapse: tuple[str, ...] = ("freeze", "shadow", "content_shadow")

    @property
    def notebook_bar(self) -> float:
        return bar(self.notebook["live"], self.chance, self.collapse_fraction)

    def collapses(self, name: str) -> bool:
        return self.notebook.get(name, float("inf")) <= self.notebook_bar

    @property
    def non_conclusive(self) -> bool:
        return self.notebook["live"] < self.live_floor

    @property
    def discriminant_survives(self) -> bool:
        if self.discriminant_live is None:
            return True
        if self.discriminant_ceiling is not None:      # calibrated form
            return (self.discriminant_frozen or 0.0) >= self.discriminant_live - self.discriminant_ceiling
        dbar = bar(self.discriminant_live, self.chance, self.collapse_fraction)
        return (self.discriminant_frozen or 0.0) > dbar

    @property
    def holds(self) -> bool:
        if self.non_conclusive:
            return False
        expected_dead = all(self.collapses(n) for n in self._expected_collapse if n in self.notebook)
        symmetry_alive = ("symmetry_control" not in self.notebook) or not self.collapses("symmetry_control")
        return expected_dead and symmetry_alive and self.discriminant_survives


def measure(system: InterventionalSystem, seeds: tuple[int, ...],
            interventions: tuple[Intervention, ...] = INTERVENTIONS) -> FreezeVerdict:
    """Run the minimal gesture battery, averaged over seeds."""
    m = {iv: sum(system.capacity(iv, s) for s in seeds) / len(seeds) for iv in interventions}
    return FreezeVerdict(live=m["live"], freeze=m["freeze"],
                         shadow=m["shadow"], chance=system.chance)
