# === Stage 80: Polish user-facing messages, names, and examples for consistency ===
# Project: SavingsGoal
def show_progress(goal, balance):
    """Display how close we are to the savings goal using friendly wording."""
    remaining = goal.target - balance
    if remaining < 0:
        message = f"You have overachieved by {abs(remaining)} and reached your goal."
    elif remaining == 0:
        message = "You have reached your savings goal!"
    else:
        percent = round(balance / goal.target * 100)
        message = f"You are {percent}% toward your goal of {goal.target}."
    print(message)


def celebrate_milestone(goal, balance, milestones):
    """Announce the next milestone reached with an encouraging note."""
    reached = [m for m in milestones if balance >= m]
    if reached:
        next_milestone = max(reached)
        print(f"Great work! You just hit the {next_milestone} milestone.")
    else:
        print("Keep going; the first milestone is within reach.")


def project_future(balance, monthly, months, goal):
    """Estimate the projected balance after a number of monthly contributions."""
    projected = balance + monthly * months
    if projected >= goal.target:
        print(f"In {months} months you will reach your goal.")
    else:
        print(f"In {months} months you will have {projected}.")
