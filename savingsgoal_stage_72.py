# === Stage 72: Add Markdown report export ===
# Project: SavingsGoal
def export_markdown_report(savings_goal, report_path="savings_goal_report.md"):
    lines = []
    lines.append("# Savings Goal Report")
    lines.append("")
    lines.append(f"Target: {savings_goal.target_currency} {savings_goal.target_amount:,.2f}")
    lines.append(f"Current:  {savings_goal.current_balance:,.2f}")
    lines.append(f"Progress: {savings_goal.progress_percentage:.1f}%")
    lines.append("")
    if savings_goal.contributions:
        lines.append("Recent Contributions")
        lines.append("")
        lines.append("| Date       | Amount    |")
        lines.append("|------------|-----------|")
        for c in savings_goal.contributions[-10:]:
            lines.append(f"| {c.date} | {c.amount:,.2f} |")
        lines.append("")
    if savings_goal.milestones:
        lines.append("Milestones")
        lines.append("")
        for m in savings_goal.milestones:
            status = "Reached" if m.achieved else "Upcoming"
            lines.append(f"- {status}: {m.description} at {m.amount:,.2f}")
        lines.append("")
    projection = savings_goal.projected_balance()
    lines.append(f"Projected Balance: {projection:,.2f}")
    lines.append("")
    with open(report_path, "w") as f:
        f.write("\n".join(lines))
    return report_path
