"""Margin check for the demo bracket."""

FACTORS = {"ultimate": 1.4, "yield": 1.25}  # NASA-STD-5001B Table 1
FITTING = 1.15  # bolts only, NASA-STD-5020B


def margin(allowable, load, factor=FACTORS["ultimate"]):
    """Margin of safety: allowable / (load x factor) - 1."""
    return allowable / (load * factor) - 1


def check(cases, parts):
    """Every part under every load case; returns what needs a redesign."""
    failed = []
    for case in cases:
        for part in parts:
            factor = FACTORS["ultimate"] * (FITTING if part.is_bolt else 1)
            ms = margin(part.allowable, case.load * part.share, factor)
            if ms < 0:
                failed.append((case.name, part.name, ms))
    return failed
