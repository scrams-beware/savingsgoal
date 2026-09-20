# === Stage 40: Add plain text report export ===
# Project: SavingsGoal
def export_report(self, path=None):
    """Export current savings report as plain text."""
    lines = []
    lines.append("=== Savings Goal Report ===")
    lines.append(f"Goal: {self.goal_name}")
    lines.append(f"Target: ${self.target_amount:,.2f}")
    lines.append(f"Current: ${self.current_amount:,.2f}")
    lines.append(f"Progress: {self.current_amount / self.target_amount * 100:.1f}%")
    lines.append(f"Remaining: ${self.target_amount - self.current_amount:,.2f}")
    if self.contributions:
        lines.append("\n--- Contributions ---")
        for c in self.contributions:
            lines.append(f"  {c.date}: ${c.amount:,.2f}")
    if self.milestones:
        lines.append("\n--- Milestones ---")
        for m in self.milestones:
            lines.append(f"  {m.description} (at ${m.amount:,.2f})")
    if self.projections:
        lines.append("\n--- Projections ---")
        for p in self.projections:
            lines.append(f"  {p.months_left} months: ${p.amount:,.2f}")
    text = "\n".join(lines)
    if path:
        with open(path, "w") as f:
            f.write(text)
    return text
