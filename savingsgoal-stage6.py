# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: SavingsGoal
def delete_goal(goal_id: int, confirm: bool = True) -> Optional[Goal]:
    """Delete a goal by ID; `confirm` must be True to proceed."""
    goals = load_goals()
    if goal_id not in goals:
        raise ValueError(f"Goal {goal_id} not found")
    if confirm:
        print(f"Goal #{goal_id} will be permanently deleted. Type 'yes' to confirm:")
        reply = input().strip().lower()
        if reply != "yes":
            print("Deletion cancelled.")
            return None
    goals.pop(goal_id)
    save_goals(goals)
    return goals[goal_id] if goal_id in goals else None
