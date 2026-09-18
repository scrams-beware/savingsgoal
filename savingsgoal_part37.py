# === Stage 37: Add recommendations for the next useful action ===
# Project: SavingsGoal
def get_next_best_action(goals, contributions, milestones):
    """Suggest the most impactful next contribution based on current state."""
    if not goals:
        return {"action": "set_goal", "reason": "No savings goal defined."}

    best_goal = max(goals, key=lambda g: g["remaining"])
    remaining = best_goal["remaining"]
    target = best_goal["target"]

    if remaining <= 0:
        return {"action": "celebrate", "reason": f"Goal ${target} reached!"}

    contribution = contributions.get("monthly", 100)
    progress = remaining / target
    if progress >= 0.9 and progress < 1.0:
        return {"action": "increase_contribution", "reason": "Almost there—consider boosting your monthly deposit to finish faster."}
    elif progress < 0.3:
        return {"action": "set_milestone", "reason": "Progress is slow—set a mid-term milestone to stay motivated."}
    else:
        return {"action": "stay_on_track", "reason": "Keep saving as planned!"}
