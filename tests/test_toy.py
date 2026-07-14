import numpy as np
import torch

from invariants.toy import model as M
from invariants.toy import task as T


def _fresh_model(seed=0):
    torch.manual_seed(seed)
    return M.InductionToy()


def test_task_pairs_are_fresh_each_sequence():
    rng = np.random.default_rng(0)
    toks1, _ = T.sample_induction(8, rng)
    toks2, _ = T.sample_induction(8, rng)
    assert toks1.shape == (8, T.SEQ_LEN)
    assert not np.array_equal(toks1, toks2)


def test_twin_association_is_fixed_across_sequences():
    perm = T.fixed_permutation(np.random.default_rng(0))
    rng = np.random.default_rng(1)
    toks, tgt = T.sample_twin(64, perm, rng)
    a, b = toks[:, 0:2 * T.K_PAIRS:2], toks[:, 1:2 * T.K_PAIRS:2]
    assert np.array_equal(perm[a], b)          # b = pi(a) everywhere
    assert np.array_equal(perm[toks[:, -1]], tgt)


def test_model_is_deterministic_given_seed():
    m1, m2 = _fresh_model(7), _fresh_model(7)
    for p1, p2 in zip(m1.parameters(), m2.parameters()):
        assert torch.equal(p1, p2)
    rng = np.random.default_rng(3)
    toks, _ = T.sample_induction(16, rng)
    toks = torch.from_numpy(toks)
    with torch.no_grad():
        assert torch.equal(m1(toks), m2(toks))


def test_freeze_touches_only_the_kv_path():
    """The freeze changes the logits (it acts) but leaves the model weights and the
    live forward untouched (it is an inference-time gesture, not a lesion)."""
    m = _fresh_model(0)
    rng = np.random.default_rng(3)
    toks, _ = T.sample_induction(16, rng)
    toks = torch.from_numpy(toks)
    with torch.no_grad():
        live1 = m(toks, "live")
        frozen = m(toks, "freeze")
        live2 = m(toks, "live")
    assert not torch.equal(live1, frozen)
    assert torch.equal(live1, live2)


def test_unknown_intervention_raises():
    m = _fresh_model(0)
    toks = torch.zeros((2, T.SEQ_LEN), dtype=torch.long)
    try:
        m(toks, "ablate")
    except ValueError:
        return
    raise AssertionError("unknown intervention must raise")


def test_short_training_lifts_notebook_capability_above_chance():
    """Smoke: a short run must already pull fresh-pair recall well above chance
    (full 4000-step runs are exercised by tier0, not unit tests)."""
    torch.manual_seed(0)
    rng = np.random.default_rng(0)
    net = M.InductionToy()
    M.train(net, T.sample_induction, steps=800, batch=128, rng=rng)
    ev_rng = np.random.default_rng(10_000)
    toks, tgt = T.sample_induction(1024, ev_rng)
    acc = net.accuracy(torch.from_numpy(toks), torch.from_numpy(tgt), "live")
    assert acc > 3 * T.CHANCE, f"acc={acc} not above 3x chance after 800 steps"
