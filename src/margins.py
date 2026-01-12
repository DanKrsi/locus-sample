"""Margin check for the demo bracket."""

FACTOR = 1.4  # ultimate design factor, NASA-STD-5001B Table 1


def margin(allowable, load, factor=FACTOR):
    """Margin of safety: allowable / (load x factor) - 1."""
    return allowable / (load * factor) - 1


def check(cases, parts):
    """Every part under every load case; returns what needs a redesign."""
    failed = []
    for case in cases:
        for part in parts:
            ms = margin(part.allowable, case.load * part.share)
            if ms < 0:
                failed.append((case.name, part.name, ms))
    return failed
