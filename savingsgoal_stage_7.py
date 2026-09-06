# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: SavingsGoal
def format_goal(goal):
    name = goal.get("name", "Unnamed")
    target = goal.get("target", 0)
    current = goal.get("current", 0)
    pct = (current / target * 100) if target else 0
    bar_len = 20
    filled = int(bar_len * pct / 100)
    bar = "█" * filled + "░" * (bar_len - filled)
    return f"[{name}] {bar} {current:>10.2f}/{target:>10.2f} ({pct:.1f}%)"


def format_contribution(contrib):
    date = contrib.get("date", "?")
    amount = contrib.get("amount", 0)
    goal = contrib.get("goal", "")
    return f"[{date}] +{amount:.2f} → {goal}"


def format_milestone(m):
    label = m.get("label", "")
    date = m.get("date", "")
    amount = m.get("amount", 0)
    return f"[{label}] ({date}) → {amount:.2f}"


def format_projection(proj):
    month = proj.get("month", "")
    est_total = proj.get("total", 0)
    est_count = proj.get("count", 0)
    return f"[{month}] est. {est_count} contributions → {est_total:.2f}"
