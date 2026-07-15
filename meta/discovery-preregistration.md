# The discovery experiment — pre-registration

> *A prediction made after the fact is a description.* — the rule this repository walks
> with, turned on the repository itself.

**Registered:** 2026-07-15, before the first reader.
**Status at registration:** public since 2026-07-14 13:46 UTC · 0 stars · 0 forks · 0 issues · 0 inbound links known to exist.

This page is not about the invariant. It is a small, badly-powered experiment about
*this repository's reception*, held to the same standard as the rest — because a
question worth being curious about is worth a kill criterion, and because it would be
embarrassing to run one sloppily in a repository that spends ten chapters insisting.

## The question

The work went public with no announcement, no post, no submission, no link from
anywhere. The tempting question is:

> **How long until someone finds it?**

## Why that question, as posed, is nearly worthless

Stated first, because a pre-registration that only lists an experiment's hopes is
advertising.

GitHub has no organic discovery surface. There is no feed of new repositories, search
ranks by stars, and a repository at zero stars from an account with no network is
reachable by essentially one route: an inbound link that does not exist. The honest
prior is therefore **nothing, indefinitely** — and an experiment whose outcome is known
in advance measures the measuring apparatus, not the world. What it would actually test
is "does GitHub have serendipity", and that is already answered: no.

So the silent arm is run **bounded and cheap**, as a calibration, not as a bet.

## The gesture, the signature, the kill criterion

- **Gesture** — publish, and link to it from nowhere. No post, no submission, no
  mention. The repository is left to be found or not found.
- **Signature** — if passive discovery is real, it arrives through a traceable channel:
  a referrer that is not a bot, a star, a fork, or an issue.
- **Kill criterion** — **no human arrival by 2026-10-12 (D+90)** kills the
  passive-discovery hypothesis. The silent arm ends and the link goes up.

**Ninety days, not twelve months.** Long enough that "it just needed time" is not
available as an excuse; short enough that the cost is bounded. The cost is not
hypothetical: this repository's [standing offer](../story/ch10-where-the-trail-goes-cold.md#the-standing-offer)
asks readers to *try to kill the invariant*. A falsificationist program with no readers
is a program running with its witnesses unarmed. Every day of silence is a day the work
is not being attacked, which is the only thing it has ever asked for. That is what the
ninety days buy, and it is why they are ninety.

## What counts as an arrival

Ranked by how much each would surprise the prior:

| # | event | reading |
|---|---|---|
| 1 | an issue, a discussion, or a fork | someone read it and engaged — the prior is wrong |
| 2 | a star from a human account | someone found it and marked it |
| 3 | a referrer that is not a crawler | **the interesting one** — records *how* it was reached |
| 4 | clones from outside our own machines | someone took a copy |

A referrer is the only event that answers the actual question, which was never "how
long" but **"through what channel"**. That is why the instrument records referrers and
not just counts.

Bots, crawlers, and mirrors do **not** count. They arrive within days on every public
repository and mean nothing about human discovery.

## The decision, written before the data

| outcome by 2026-10-12 | what we conclude | what we do |
|---|---|---|
| no human arrival | passive discovery is dead, as predicted; the silent arm was calibration | post the link; the promotion arm begins; this page records the null |
| any human arrival | the prior was wrong — **record the channel first**, it is the whole result | write it up here, then post the link anyway |

Note that both branches end in the same action. That is deliberate: the experiment is
allowed to be interesting, but it is **not** allowed to decide the publication strategy.
The reason to seek readers was never the outcome of this measurement — it is that the
work is built to be attacked and cannot be attacked unread. If those ninety days ever
start looking like a reason to keep waiting, the experiment has stopped being an
experiment and become an excuse, and it should be killed on the spot.

## Known weaknesses — the ones that matter

1. **n = 1, no control, unblinded, and the experimenter can end it at will.** This is an
   anecdote with a timestamp. It is registered so it is at least an *honest* anecdote.
2. **The outcome is nearly certain.** See above. Very little information is at stake.
3. **The instrument can fail silently.** GitHub keeps only 14 days of traffic data;
   miss the window and the record is gone with no error. Worse, GitHub disables
   scheduled workflows after 60 days without repository activity — on a deliberately
   silent repository, that is a live failure mode aimed straight at day 60 of a 90-day
   run. The ledger's own commits should reset that timer; this is **unverified** and is
   the first thing to check.
4. **The largest channel is invisible to this instrument.** Public GitHub is scraped
   into model training corpora. This repository will very likely be *read by machines*
   regardless of the outcome above, and that leaves no referrer, no star, and no trace
   — diffusion without attribution. The instrument cannot see it, and this experiment
   makes no claim about it.
5. **Observer effect, accepted.** This page is public, so anyone who arrives can read
   that they were being timed. Since discovery is what is being measured, and the
   measurement completes at the moment of arrival, the contamination is judged
   negligible. Recorded rather than fixed.
6. **A null result here is over-determined.** "Nobody found it" is consistent with "the
   work is uninteresting" *and* with "GitHub has no discovery surface" — and this
   experiment cannot separate them. It does not measure quality. **No conclusion about
   the worth of the work may be drawn from this page in either direction.** That is not
   modesty; it is what the design supports.

## The instrument

[`traffic_snapshot.py`](traffic_snapshot.py), run daily by
[`.github/workflows/traffic.yml`](../.github/workflows/traffic.yml), appends GitHub's
14-day rolling traffic window into `traffic/ledger.json` before it evaporates. It
records daily views and clones, referrers, popular paths, and the star/fork/watcher
counts.

It must run with a token belonging to **this repository's own account**. The traffic API
requires push access, and any other credential used against this repository — from
another account, a personal token, or a local CLI — writes a correlation into GitHub's
server-side logs that the repository's pseudonymity exists to avoid. The instrument
runs inside the repository or not at all.

## What is deliberately *not* done during the silent arm

**The Zenodo archive is prepared but not switched on.** [`CITATION.cff`](../CITATION.cff)
and [`.zenodo.json`](../.zenodo.json) are committed and ready; the DOI is not minted.
A Zenodo record is indexed (Google Scholar, OpenAIRE) — that is an inbound link, and an
inbound link is precisely the thing this arm is defined by not having. Worse, a visitor
arriving through it would produce a referrer *we manufactured*, which is the one
measurement here that matters. Minting the DOI is therefore part of the promotion arm,
on the same day the link goes up.

The cost of waiting is a weaker priority claim for ninety days: the repository's public
creation timestamp (2026-07-14 13:46 UTC) and the commit history carry the date, without
a DOI. On an unread repository that risk is small, and it is accepted knowingly rather
than traded against the experiment.

## Prior, on the record

Stated now so it cannot be revised later: **no human arrival before 2026-10-12.** The
first star, if one ever comes, arrives *after* a link is posted somewhere — not before.

---

*If you are reading this because you found this repository on your own, before any link
existed: you falsified the prediction above. Please open an issue and tell us how you
got here — that referrer is the entire result, and we would rather have it from you
than from a log. — E.L.*

## Closure — the silent arm ends by decision (2026-07-16)

The decision to publish for real — release, DOI, announcement — was taken on
2026-07-16, two days into the silent arm and well before the D+90 criterion. This is
the exit the table above wrote down in advance: the experiment was never allowed to
decide the publication strategy, and it didn't. For the record:

- **Outcome of the silent arm at closure: null, as the prior predicted.** No human
  arrival had been recorded (no issue, no fork, no non-bot referrer, no star) in the
  ~2 days the arm ran. Two days of silence contradict nothing and confirm nothing —
  weakness #6 above applies in full.
- **The instrument stays on.** Its purpose now inverts: instead of timing an arrival
  that was never coming, the ledger records **through what channels the announced
  readers arrive** — which was the actual question all along.
- Weakness #3 (scheduled workflows disabled after 60 days of silence) is moot: the
  repository is no longer silent.

*Killed on the spot, as instructed — by its own paragraph.*
