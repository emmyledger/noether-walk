import numpy as np

from invariants.guards import (
    causal_at_training,
    causal_violation,
    in_window,
    intervention_never_better_than_live,
)


def test_never_better_than_live_bites_on_leak():
    # the poisoned-battery symptom: intervention loss far below living loss
    assert intervention_never_better_than_live(10.6, 2.59) is not None
    # normal case: intervention worse than live -> no alert
    assert intervention_never_better_than_live(2.0, 3.5) is None
    # within eps -> no alert
    assert intervention_never_better_than_live(2.0, 1.95) is None


def test_in_window():
    assert in_window(0.75, 0.60, 0.95) is None
    assert in_window(0.99, 0.60, 0.95) is not None


def test_causal_guard_detects_future_dependence():
    rng = np.random.default_rng(0)
    ref = rng.normal(size=(2, 8, 5))
    # causal twin: identical logits at positions <= t
    alt = ref.copy()
    alt[:, 5:, :] += 1.0  # only the tail differs
    assert causal_violation(ref, alt, t=4) < 1e-12
    assert causal_at_training(ref, alt, t=4) is None
    # anti-causal: a position <= t depends on the randomized tail
    leaky = ref.copy()
    leaky[:, 2, :] += 0.5
    assert causal_at_training(ref, leaky, t=4) is not None
