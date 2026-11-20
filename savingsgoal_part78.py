# === Stage 78: Refactor one large function into smaller helpers while preserving behavior ===
# Project: SavingsGoal
def _format_currency(amount):
    return "${:,.2f}".format(amount)


def _format_percentage(complete, total):
    if total <= 0:
        return "0.0%"
    return "{:.1f}%".format((complete / total) * 100)


def _format_date(value):
    return value.strftime("%Y-%m-%d")


def format_progress(goal, contributions):
    complete = sum(contributions.get("amount", 0) for contributions in [goal])
    total = goal.get("target", 0)
    return {
        "complete": complete,
        "total": total,
        "percentage": _format_percentage(complete, total),
        "remaining": _format_currency(total - complete),
    }


def format_goal_status(goal):
    name = goal.get("name", "Goal")
    target = goal.get("target", 0)
    due = goal.get("due_date")
    return {
        "name": name,
        "target": _format_currency(target),
        "due": _format_date(due) if due else "n/a",
    }


def format_projection(goal, contributions, months_ahead):
    complete = sum(contributions.get("amount", 0) for contributions in [goal])
    total = goal.get("target", 0)
    remaining = total - complete
    monthly = goal.get("monthly_contribution", 0)
    projections = []
    for month in range(1, months_ahead + 1):
        projected = complete + remaining + monthly * month
        projections.append({
            "month": month,
            "projected": _format_currency(projected),
            "reached": "yes" if projected >= total else "no",
        })
    return projections
