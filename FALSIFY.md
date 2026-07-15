# How to try to kill this work (please do)

The most useful thing you can do with this repository is not to cite it — it is to take
the gesture to a substrate we never touched and **try to falsify the invariant**. This
page is the protocol. A clean falsification will be posted in the
[epilogue](story/epilogue-postcards.md) at full font size, above the confirmations.

## The claim you are attacking

> If a capability is carried by a notebook — a slow state the system writes and rereads
> — then freezing that notebook collapses the capability (installed arc), and freezing
> it throughout training prevents the capability from ever forming (formation arc).

Full statement with witnesses and scope: [`paper/draft.md`](paper/draft.md) §2–3.

## What counts as a kill

Any ONE of these, on a substrate where the setup below is respected:

1. **The freeze fails to collapse** a capability whose σ was designated a priori and
   whose witnesses validate the setup;
2. **The symmetry control collapses** (the pairing-preserving transformation was
   supposed to be harmless — if it kills, our taxonomy is wrong);
3. **The notebook-free twin flinches** under the freeze (the gesture would be generic
   damage, not selective ignorance);
4. **Formation arc**: the capability forms normally under a *causally clean* permanent
   freeze (see the causality guard — an anti-causal freeze invalidates the run, ours
   included; that story is chapter 4).

## The protocol (the same one we bind ourselves to)

1. **Pick a substrate** with a write-then-reread loop, and a capability that plausibly
   lives in it. The further from our substrates, the better.
2. **Designate σ BEFORE any intervention**, by a criterion you publish first. Selecting
   σ by searching for what breaks is hosting, and disqualifies the attempt — in either
   direction.
3. **Pre-register**: open an Issue with the plan *before running* — substrate, σ
   criterion, the four conditions (freeze / paired shadow / symmetry control / twin),
   the collapse bar (we use chance + 0.5·(live−chance)), and your kill criteria. The
   Issue's timestamp is your pre-registration.
4. **Implement the contract.** `src/invariants/contract.py` is substrate-agnostic:
   expose `capacity(intervention, seed)` and a `chance` level, and the verdict logic is
   done for you. `guards.py` gives you the causality check and the
   never-beats-the-living tripwire.
5. **Run, then report the verdict either way** — issue templates are provided. Include
   seeds, environment, and raw artifacts so the verdict can be re-derived.

## What does NOT count

- Ablation or noise instead of the freeze (budget/perturbation confounds — §2.2);
- σ chosen post hoc; witnesses omitted; bars moved after contact with data;
- training-time freezes that leak the future (run the causality guard);
- a capability whose live performance is not sharp (non-conclusive, not falsified).

These rules are not gatekeeping — they are the same rules that disqualified several of
*our* runs, documented in chapters 4 and 7 and in the epilogue.

## Easy mode

Not ready to build a substrate? Two lighter attacks are welcome: **replicate Tier 0 on
your platform** (`make tier0` — takes minutes; report any verdict flip), or **audit the
claim→command table** ([`repro/`](repro/)) and catch a number that doesn't reproduce.

— E.L.
