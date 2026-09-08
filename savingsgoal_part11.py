# === Stage 11: Add JSON export for the current application state ===
# Project: SavingsGoal
def export_state_as_json(goal, contributions, milestones, projections):
    """Export the full SavingsGoal state to a compact JSON string."""
    import json
    state = {
        "goal": {
            "name": goal.get("name", ""),
            "target_amount": goal.get("target_amount", 0),
            "current_amount": goal.get("current_amount", 0),
            "currency": goal.get("currency", "USD"),
            "created_at": goal.get("created_at", ""),
        },
        "contributions": [
            {
                "date": c.get("date", ""),
                "amount": c.get("amount", 0),
                "note": c.get("note", ""),
            }
            for c in contributions
        ],
        "milestones": [
            {
                "label": m.get("label", ""),
                "amount": m.get("amount", 0),
                "reached_at": m.get("reached_at", ""),
            }
            for m in milestones
        ],
        "projections": [
            {
                "label": p.get("label", ""),
                "projected_amount": p.get("projected_amount", 0),
                "projected_date": p.get("projected_date", ""),
            }
            for p in projections
        ],
    }
    return json.dumps(state, indent=2)
