"""The task pair of the Tier-0 toy — fresh-pair recall, and its twin.

Fresh pairs (the notebook task): [a1 b1 a2 b2 ... aK bK aq] with aq = one of the
ai, target = the matching bi. The pairs are drawn FRESH per sequence: the
association lives only in the context — it must be written by the fast dynamics
and reread. Memorization is impossible by construction.

Twin (the discriminant control): same surface form, but bi = pi(ai) for ONE fixed
permutation pi shared by all sequences. The association lives in the weights:
prediction can read the query token directly, no carried context state needed.
The same gesture applied here must NOT collapse the capability.

chance = 1/VOCAB, posed before any run.
"""
from __future__ import annotations

import numpy as np

VOCAB = 32
K_PAIRS = 8
SEQ_LEN = 2 * K_PAIRS + 1  # a1 b1 ... aK bK aq
CHANCE = 1.0 / VOCAB


def sample_induction(batch: int, rng: np.random.Generator) -> tuple[np.ndarray, np.ndarray]:
    """Fresh random pairs per sequence; returns (tokens[B,S], target[B])."""
    toks = np.empty((batch, SEQ_LEN), dtype=np.int64)
    tgt = np.empty(batch, dtype=np.int64)
    for i in range(batch):
        a = rng.choice(VOCAB, size=K_PAIRS, replace=False)
        b = rng.choice(VOCAB, size=K_PAIRS, replace=False)
        q = rng.integers(K_PAIRS)
        toks[i, 0:2 * K_PAIRS:2] = a
        toks[i, 1:2 * K_PAIRS:2] = b
        toks[i, -1] = a[q]
        tgt[i] = b[q]
    return toks, tgt


def fixed_permutation(rng: np.random.Generator) -> np.ndarray:
    return rng.permutation(VOCAB)


def sample_twin(batch: int, perm: np.ndarray, rng: np.random.Generator) -> tuple[np.ndarray, np.ndarray]:
    """Same surface form, but b = pi(a) with pi fixed across ALL sequences."""
    toks = np.empty((batch, SEQ_LEN), dtype=np.int64)
    tgt = np.empty(batch, dtype=np.int64)
    for i in range(batch):
        a = rng.choice(VOCAB, size=K_PAIRS, replace=False)
        q = rng.integers(K_PAIRS)
        toks[i, 0:2 * K_PAIRS:2] = a
        toks[i, 1:2 * K_PAIRS:2] = perm[a]
        toks[i, -1] = a[q]
        tgt[i] = perm[a[q]]
    return toks, tgt
