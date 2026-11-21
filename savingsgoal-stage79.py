# === Stage 79: Add a final self-check command that runs validations and demo operations ===
# Project: SavingsGoal
def final_self_check():
    from savings_goal import SavingsGoal, Contribution, Milestone, ProjectedValue
    goal = SavingsGoal(name="Vacation", target=5000.0, start=1000.0)
    goal.add_contribution(Contribution(date="2024-01-01", amount=500.0))
    goal.add_milestone(Milestone(amount=2500.0, date="2024-03-01"))
    goal.add_projection(ProjectedValue(date="2024-06-01", value=4000.0))
    assert goal.name == "Vacation"
    assert goal.target == 5000.0
    assert goal.remaining == 4000.0
    assert goal.progress_pct == 20.0
    assert goal.status == "in_progress"
    assert len(goal.contributions) == 1
    assert goal.contributions[0].amount == 500.0
    assert len(goal.milestones) == 1
    assert goal.milestones[0].amount == 2500.0
    assert len(goal.projections) == 1
    assert goal.projections[0].value == 4000.0
    assert goal.is_target_reached() is False
    goal.target = 4000.0
    assert goal.is_target_reached() is True
    assert goal.status == "completed"
    assert goal.projected_completion_date == "2024-06-01"
    print("Self-check passed")
