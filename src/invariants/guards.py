"""Automatic guards — lessons converted into tripwires (paper §2.4).

Each returns an alert string (or None), so a runner can log the moment a
pre-registered assumption is violated, rather than discovering it at the verdict.
"""
from __future__ import annotations


def intervention_never_better_than_live(live_loss: float, intervention_loss: float,
                                        eps: float = 0.10) -> str | None:
    """At matched budget, an intervention may never beat the living run by more
    than eps. A violation means the intervention leaks information — this is the
    tripwire that catches the training-time causality leak of paper §2.4 within
    the first few million tokens."""
    if intervention_loss < live_loss - eps:
        return (f"intervention BEATS the living run: {intervention_loss:.3f} "
                f"< {live_loss:.3f} - {eps} (leak?)")
    return None


def in_window(value: float, lo: float, hi: float) -> str | None:
    """A discriminant control must sit inside its pre-registered operating window;
    outside it, the control is NON-EXECUTABLE (not 'roughly fine')."""
    if not (lo <= value <= hi):
        return f"discriminant control out of window [{lo}, {hi}]: {value:.3f} — NON-EXECUTABLE"
    return None


def causal_violation(logits_ref, logits_alt, t: int) -> float:
    """Max |Δlogits| at positions ≤ t between a forward and its TAIL-RANDOMIZED
    twin (same tokens up to t, random beyond). Works with numpy or torch arrays."""
    d = logits_ref[..., :t + 1, :] - logits_alt[..., :t + 1, :]
    d = d.abs() if hasattr(d, "abs") else abs(d)
    return float(d.max())


def causal_at_training(logits_ref, logits_alt, t: int, atol: float = 1e-4) -> str | None:
    """An intervention applied at TRAINING must respect the causal structure of
    the loss: the output at position ≤ t must be invariant to tokens at positions
    > t. The caller runs the intervened forward twice (identical up to t,
    randomized tail) and passes both logit arrays. Returns an alert if the
    property is violated beyond atol — exactly what would have caught the
    anti-causal freeze of paper §2.4 before a single run was trained."""
    v = causal_violation(logits_ref, logits_alt, t)
    return None if v < atol else f"causality violated at t={t}: dlogits={v:.2e}"
