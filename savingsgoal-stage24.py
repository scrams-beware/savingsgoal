# === Stage 24: Add grouped summaries by category or status ===
# Project: SavingsGoal
def grouped_summary(goals, group_by="category"):
    """Summarize goals grouped by category or status."""
    groups = {}
    for g in goals:
        key = g.get(group_by, "Uncategorized")
        groups.setdefault(key, {"count": 0, "target": 0, "saved": 0, "goals": []})
        groups[key]["count"] += 1
        groups[key]["target"] += g.get("target", 0)
        groups[key]["saved"] += g.get("saved", 0)
        groups[key]["goals"].append(g)
    return groups
