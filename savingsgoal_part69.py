# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: SavingsGoal
def reset_demo_data(savings_goal):
    savings_goal.targets = [
        SavingsTarget(name="Emergency Fund", amount=10000.0, date_created=datetime.date(2024, 1, 1))
    ]
    savings_goal.contributions = [
        Contribution(amount=500.0, date=datetime.date(2024, 1, 15), target=savings_goal.targets[0]),
        Contribution(amount=500.0, date=datetime.date(2024, 2, 15), target=savings_goal.targets[0]),
        Contribution(amount=500.0, date=datetime.date(2024, 3, 15), target=savings_goal.targets[0]),
    ]
    savings_goal.milestones = [
        Milestone(target=savings_goal.targets[0], date=datetime.date(2024, 3, 15), percentage=15.0),
    ]
    savings_goal.projections = [
        Projection(date=datetime.date(2024, 6, 1), amount=1500.0, target=savings_goal.targets[0]),
        Projection(date=datetime.date(2024, 9, 1), amount=2500.0, target=savings_goal.targets[0]),
        Projection(date=datetime.date(2024, 12, 1), amount=3500.0, target=savings_goal.targets[0]),
    ]
    return savings_goal
