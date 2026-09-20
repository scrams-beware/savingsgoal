# === Stage 43: Add CSV import for the primary record type ===
# Project: SavingsGoal
class CsvRecord:
    def __init__(self, goal_id, amount, contribution, milestone, date):
        self.goal_id = goal_id
        self.amount = amount
        self.contribution = contribution
        self.milestone = milestone
        self.date = date

    def __repr__(self):
        return f"CsvRecord(goal={self.goal_id}, amount={self.amount}, contribution={self.contribution}, milestone={self.milestone}, date={self.date})"
