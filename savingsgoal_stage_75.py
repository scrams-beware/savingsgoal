# === Stage 75: Add a validation report that lists warnings and errors ===
# Project: SavingsGoal
def validate_savings_goal(goal):
    warnings = []
    errors = []
    if not goal.name:
        errors.append("Goal name is empty.")
    if goal.target <= 0:
        errors.append("Target amount must be positive.")
    total_contributed = sum(c.amount for c in goal.contributions)
    if total_contributed > goal.target:
        warnings.append(f"Contributions ({total_contributed}) exceed target ({goal.target}).")
    if goal.start_date and goal.end_date and goal.end_date < goal.start_date:
        warnings.append("End date is before start date.")
    if goal.start_date and goal.end_date:
        months = (goal.end_date.year - goal.start_date.year) * 12 + (goal.end_date.month - goal.start_date.month)
        if months <= 0:
            warnings.append("Savings period is not positive.")
        if goal.target > 0:
            monthly_rate = goal.target / months if months > 0 else 0
            if monthly_rate > 0:
                avg_contribution = total_contributed / len(goal.contributions) if goal.contributions else 0
                if avg_contribution < monthly_rate:
                    warnings.append("Average contribution is below the projected monthly rate needed to reach the target.")
    if goal.contributions and not goal.milestones:
        warnings.append("Goal has contributions but no milestones defined.")
    if errors:
        raise ValueError("Validation failed: " + "; ".join(errors))
    return warnings, errors
