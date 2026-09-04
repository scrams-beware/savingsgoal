# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: SavingsGoal
import random
from datetime import date, timedelta

class SavingsGoal:
    def __init__(self, name, target_amount, start_date=None):
        self.name = name
        self.target_amount = target_amount
        self.start_date = start_date or date.today()
        self.contributions = []
        self.milestones = []

    def add_contribution(self, amount, note=""):
        self.contributions.append({
            "amount": amount,
            "date": date.today(),
            "note": note
        })

    def add_milestone(self, amount_achieved, note=""):
        self.milestones.append({
            "amount_achieved": amount_achieved,
            "date": date.today(),
            "note": note
        })

    def get_progress(self):
        total_contributed = sum(c["amount"] for c in self.contributions)
        return {
            "total_contributed": total_contributed,
            "target": self.target_amount,
            "remaining": self.target_amount - total_contributed,
            "progress_pct": (total_contributed / self.target_amount * 100) if self.target_amount > 0 else 0
        }

goals = [
    SavingsGoal("Emergency Fund", 10000),
    SavingsGoal("New Laptop", 2500),
    SavingsGoal("Vacation", 5000)
]

for goal in goals:
    for _ in range(random.randint(3, 8)):
        goal.add_contribution(random.randint(100, 500))
        if goal.get_progress()["progress_pct"] >= 25:
            goal.add_milestone(goal.target_amount * 0.25, "Quarterly goal")
