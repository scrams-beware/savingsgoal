# === Stage 64: Add validation for relationship references ===
# Project: SavingsGoal
def validate_references(goals):
    goal_ids = {g['id'] for g in goals}
    errors = []
    for goal in goals:
        goal_id = goal.get('id')
        if goal_id not in goal_ids:
            errors.append(f"Goal {goal_id} has an unknown id")
        for field in ['target_id', 'milestone_ids']:
            if field in goal and goal[field] is not None:
                ref = goal[field]
                if isinstance(ref, str):
                    ref = [ref]
                for item in ref:
                    if item not in goal_ids:
                        errors.append(f"Goal {goal_id} references unknown {field} {item}")
    return errors
