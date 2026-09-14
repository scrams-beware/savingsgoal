# === Stage 27: Add monthly summary calculations ===
# Project: SavingsGoal
def monthly_summary(goals, months=12):
    """Return a dict of monthly summaries with totals and progress."""
    summaries = []
    for g in goals:
        if g["target"] <= 0:
            continue
        monthly_contrib = g["monthly_contribution"] or g["target"] / months
        for i in range(1, months + 1):
            balance = (monthly_contrib * i) + g["initial_balance"] or 0
            progress = balance / g["target"]
            summaries.append({
                "month": i,
                "balance": round(balance, 2),
                "target": g["target"],
                "progress_pct": round(progress * 100, 1),
                "goal_name": g.get("name", "Unnamed"),
            })
    if not summaries:
        return []
    total_balance = sum(s["balance"] for s in summaries)
    return {
        "monthly": summaries,
        "total_balance": round(total_balance, 2),
        "months": months,
    }
