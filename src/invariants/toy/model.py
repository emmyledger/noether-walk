"""Minimal attention-only in-context learner (2 layers, causal, no MLP) + the
pre-registered gesture. Story chapter 2; paper §2-3.

σ (the notebook, designated BY CONSTRUCTION) = the layer-1 attention contribution
to the residual stream at CONTEXT positions (every position except the final
query) — exactly what layer 2's K/V read to find "after A comes B". It is what
the fast dynamics WRITE into the context and REREAD to govern prediction: the
candidate slow variable.

Gesture = the freeze: σ_t → mean over context positions, per sequence. Mean
magnitude kept ("same ink"), context-dependent variation destroyed ("zero
information").

Shadow (paired shadow) = σ shuffled across context positions (same marginal
distribution, positional pairing destroyed).

The intervention is applied to the residual stream that layer 2 reads as K/V.
The final-position query path and the direct token path are untouched by
construction: only the written context state is touched.
"""
from __future__ import annotations

import torch
import torch.nn as nn
import torch.nn.functional as F

from .task import SEQ_LEN, VOCAB


class CausalAttention(nn.Module):
    def __init__(self, d_model: int, n_heads: int):
        super().__init__()
        self.n_heads = n_heads
        self.d_head = d_model // n_heads
        self.qkv = nn.Linear(d_model, 3 * d_model, bias=False)
        self.proj = nn.Linear(d_model, d_model, bias=False)

    def forward(self, x_q: torch.Tensor, x_kv: torch.Tensor) -> torch.Tensor:
        B, S, D = x_q.shape
        H, Dh = self.n_heads, self.d_head
        w_q, w_k, w_v = self.qkv.weight.split(D, dim=0)
        q = (x_q @ w_q.T).view(B, S, H, Dh).transpose(1, 2)
        k = (x_kv @ w_k.T).view(B, S, H, Dh).transpose(1, 2)
        v = (x_kv @ w_v.T).view(B, S, H, Dh).transpose(1, 2)
        att = (q @ k.transpose(-2, -1)) / Dh**0.5
        mask = torch.triu(torch.ones(S, S, dtype=torch.bool, device=x_q.device), 1)
        att = att.masked_fill(mask, float("-inf")).softmax(-1)
        out = (att @ v).transpose(1, 2).reshape(B, S, D)
        return self.proj(out)


class InductionToy(nn.Module):
    """tok+pos embeddings → attn1 → attn2 → unembed. Attention-only."""

    def __init__(self, d_model: int = 64, n_heads: int = 4):
        super().__init__()
        self.tok = nn.Embedding(VOCAB, d_model)
        self.pos = nn.Embedding(SEQ_LEN, d_model)
        self.attn1 = CausalAttention(d_model, n_heads)
        self.attn2 = CausalAttention(d_model, n_heads)
        self.unembed = nn.Linear(d_model, VOCAB, bias=False)

    def forward(self, toks: torch.Tensor, intervention: str = "live",
                freeze_lambda: float = 1.0) -> torch.Tensor:
        """Interventions: "live" / "freeze" / "shadow" (paired shadow) /
        "content_shadow" (σ from the neighbouring sequence). freeze_lambda gives
        the partial freeze σ_λ = (1−λ)·σ + λ·frozen(σ) for dose-response curves
        (λ=1 is the full freeze)."""
        B, S = toks.shape
        h = self.tok(toks) + self.pos(torch.arange(S, device=toks.device))
        a1 = self.attn1(h, h)  # σ = a1 at context positions [0, S-1)

        if intervention == "live":
            a1_kv = a1
        elif intervention == "freeze":
            a1_kv = a1.clone()
            frozen = a1[:, :-1].mean(dim=1, keepdim=True)
            a1_kv[:, :-1] = (1 - freeze_lambda) * a1[:, :-1] + freeze_lambda * frozen
        elif intervention == "content_shadow":
            a1_kv = a1.clone()
            a1_kv[:, :-1] = a1.roll(1, dims=0)[:, :-1]
        elif intervention == "shadow":
            a1_kv = a1.clone()
            idx = torch.argsort(torch.rand(B, S - 1, device=toks.device), dim=1)
            a1_kv[:, :-1] = torch.gather(
                a1[:, :-1], 1, idx.unsqueeze(-1).expand(-1, -1, a1.shape[-1])
            )
        else:
            raise ValueError(intervention)

        h_q = h + a1            # query path: untouched
        h_kv = h + a1_kv        # what layer 2 reads as K/V: σ intervened
        h2 = h_q + self.attn2(h_q, h_kv)
        return self.unembed(h2[:, -1])  # logits for the induced token

    def accuracy(self, toks: torch.Tensor, tgt: torch.Tensor, intervention: str) -> float:
        with torch.no_grad():
            logits = self(toks, intervention)
        return (logits.argmax(-1) == tgt).float().mean().item()

    def evaluate(self, toks: torch.Tensor, tgt: torch.Tensor, intervention: str,
                 freeze_lambda: float = 1.0) -> dict:
        """Accuracy + cross-entropy + raw predictions."""
        with torch.no_grad():
            logits = self(toks, intervention, freeze_lambda)
            loss = F.cross_entropy(logits, tgt).item()
            preds = logits.argmax(-1)
        return {
            "acc": (preds == tgt).float().mean().item(),
            "loss": loss,
            "preds": preds.numpy(),
        }


def train(model: InductionToy, sample_fn, steps: int, batch: int,
          rng, lr: float = 1e-3, log_every: int = 500,
          intervention: str = "live", eval_fn=None) -> list[tuple[int, float]]:
    """sample_fn(batch, rng) -> (toks, tgt) numpy arrays. Returns loss curve.

    intervention != "live" applies the gesture to EVERY forward pass, gradient
    included — the formation arc (the gesture's σ and mechanics are unchanged;
    only its timing moves to training). Note the toy's freeze statistic is
    intra-sequence, which is causal HERE because the loss lives at the final
    position only (the whole window is its past); for losses graded at every
    position this statistic is forbidden — see guards.causal_at_training and
    paper §2.4. eval_fn(model, step), if given, is called every log_every steps."""
    opt = torch.optim.AdamW(model.parameters(), lr=lr)
    curve = []
    for step in range(steps):
        toks_np, tgt_np = sample_fn(batch, rng)
        toks, tgt = torch.from_numpy(toks_np), torch.from_numpy(tgt_np)
        loss = F.cross_entropy(model(toks, intervention), tgt)
        opt.zero_grad()
        loss.backward()
        opt.step()
        if step % log_every == 0 or step == steps - 1:
            curve.append((step, loss.item()))
            if eval_fn is not None:
                eval_fn(model, step)
    return curve
