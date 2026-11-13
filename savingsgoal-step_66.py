# === Stage 66: Add export of a short status dashboard ===
# Project: SavingsGoal
def show_dashboard(goals):
    total_target = 0
    total_saved = 0
    for g in goals:
        total_target += g["target"]
        total_saved += g["saved"]
    pct = (total_saved / total_target * 100) if total_target else 0
    print("=" * 30)
    print("Savings Dashboard")
    print("Total Target: {}".format(total_target))
    print("Total Saved:  {}".format(total_saved))
    print("Progress:     {:.1f}%".format(pct))
    print("=" * 30)
    for g in goals:
        bar = "#" * int(pct / 100 * 20)
        print("{} {:.0f}/{:.0f} ({:.0f}%) {}".format(bar, g["saved"], g["target"], g["saved"] / g["target"] * 100, g["name"]))
    next_milestone = None
    for g in goals:
        if g["saved"] < g["target"]:
            gap = g["target"] - g["saved"]
            if next_milestone is None or gap < next_milestone["gap"]:
                next_milestone = {"name": g["name"], "gap": gap}
    if next_milestone:
        print("Next goal: {} (need {:.0f} more)".format(next_milestone["name"], next_milestone["gap"]))
