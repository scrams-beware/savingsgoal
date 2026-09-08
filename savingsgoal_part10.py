# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: SavingsGoal
def case_insensitive_search(self, field, value, limit=20):
    """Search contributions by field with case-insensitive matching."""
    if not value:
        return []
    results = []
    for c in self.contributions:
        val = getattr(c, field, None)
        if val is None:
            continue
        if isinstance(val, str) and value.lower() in val.lower():
            results.append(c)
        elif isinstance(val, (int, float)) and val == value:
            results.append(c)
    return results[:limit]
