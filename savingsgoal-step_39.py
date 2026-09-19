# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: SavingsGoal
def repair(self):
    """Fix common data integrity issues in place."""
    if not self.contributions:
        return
    total = sum(c.amount for c in self.contributions)
    if abs(total - self.current) > 1e-6:
        self.current = round(total, 2)
    if self.current > self.target:
        self.current = self.target
    if self.current < 0:
        self.current = 0.0
    if self.frozen and self.current < self.target:
        self.current = self.target
