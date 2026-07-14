from invariants.contract import FreezeVerdict, Verdict, bar, measure


def test_bar():
    assert bar(1.0, 0.0) == 0.5
    assert abs(bar(1.0, 1 / 32) - (1 / 32 + 0.5 * (1 - 1 / 32))) < 1e-12


def test_freeze_verdict_collapse_logic():
    v = FreezeVerdict(live=1.0, freeze=0.12, shadow=0.10, chance=1 / 32)
    assert v.freeze_collapses and v.shadow_collapses
    survivor = FreezeVerdict(live=1.0, freeze=0.95, shadow=0.10, chance=1 / 32)
    assert not survivor.freeze_collapses


def test_verdict_holds_requires_all_witnesses():
    base = dict(chance=0.0, discriminant_live=0.9, discriminant_frozen=0.85)
    good = Verdict(notebook={"live": 1.0, "freeze": 0.1, "shadow": 0.1,
                             "symmetry_control": 0.9}, **base)
    assert good.holds
    # symmetry control collapsing must falsify
    sym_dead = Verdict(notebook={"live": 1.0, "freeze": 0.1, "shadow": 0.1,
                                 "symmetry_control": 0.1}, **base)
    assert not sym_dead.holds
    # freeze surviving must falsify
    freeze_alive = Verdict(notebook={"live": 1.0, "freeze": 0.9, "shadow": 0.1}, **base)
    assert not freeze_alive.holds
    # dull live capability is non-conclusive, never a hold
    dull = Verdict(notebook={"live": 0.2, "freeze": 0.0, "shadow": 0.0}, **base)
    assert dull.non_conclusive and not dull.holds


def test_verdict_calibrated_discriminant():
    v = Verdict(notebook={"live": 1.0, "freeze": 0.1, "shadow": 0.1}, chance=0.0,
                discriminant_live=0.9, discriminant_frozen=0.7,
                discriminant_ceiling=0.25)
    assert v.discriminant_survives  # 0.7 >= 0.9 - 0.25
    tight = Verdict(notebook={"live": 1.0, "freeze": 0.1, "shadow": 0.1}, chance=0.0,
                    discriminant_live=0.9, discriminant_frozen=0.6,
                    discriminant_ceiling=0.25)
    assert not tight.discriminant_survives


def test_measure_averages_over_seeds():
    class Fake:
        chance = 0.0

        def capacity(self, iv, seed):
            return {"live": 1.0, "freeze": 0.0, "shadow": 0.5}[iv] + seed * 0.0

    v = measure(Fake(), seeds=(0, 1))
    assert v.live == 1.0 and v.freeze == 0.0 and v.shadow == 0.5
