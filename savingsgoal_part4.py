# === Stage 4: Implement create operations for the primary records ===
# Project: SavingsGoal
def create_savings_goal(name, target_amount, description=""):
    goal = SavingsGoal(name=name, target_amount=target_amount, description=description)
    db.insert(goal)
    return goal

def create_contribution(goal_id, amount, date=None):
    if date is None:
        date = datetime.date.today()
    contribution = Contribution(goal_id=goal_id, amount=amount, date=date)
    db.insert(contribution)
    return contribution

def create_milestone(goal_id, amount, date=None, label=""):
    if date is None:
        date = datetime.date.today()
    milestone = Milestone(goal_id=goal_id, amount=amount, date=date, label=label)
    db.insert(milestone)
    return milestone

def create_projection(goal_id, months_ahead, monthly_contribution, start_date=None):
    if start_date is None:
        start_date = datetime.date.today()
    projection = Projection(goal_id=goal_id, months_ahead=months_ahead,
                            monthly_contribution=monthly_contribution, start_date=start_date)
    db.insert(projection)
    return projection
