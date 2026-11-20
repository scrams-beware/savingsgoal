# === Stage 77: Add type hints to older helper functions that are missing them ===
# Project: SavingsGoal
def format_currency(amount):
    return f"${amount:,.2f}"

def calculate_progress(current, target):
    if target == 0:
        return 0.0
    return max(0.0, min(100.0, (current / target) * 100))

def average_monthly_contribution(contributions):
    if not contributions:
        return 0.0
    return sum(contributions) / len(contributions)

def remaining_months_to_reach(target, current, monthly_rate):
    if monthly_rate == 0:
        return None
    remaining = target - current
    if remaining <= 0:
        return 0
    return math.ceil(remaining / monthly_rate)

def project_future(current, monthly_rate, months):
    return current + monthly_rate * months

def summarize_goal(target, current, contributions):
    avg = average_monthly_contribution(contributions)
    months = remaining_months_to_reach(target, current, avg)
    return {
        "raised": current,
        "target": target,
        "percent": calculate_progress(current, target),
        "avg_monthly": avg,
        "months_left": months,
    }
