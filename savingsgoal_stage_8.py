# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: SavingsGoal
def filter_contributions(contributions, **kwargs):
    """Filter contributions by status, category, owner, or tag.
    
    Any combination of kwargs filters the list.
    """
    filtered = contributions
    for key, value in kwargs.items():
        if value is None:
            continue
        filtered = [c for c in filtered if getattr(c, key) == value]
    return filtered
