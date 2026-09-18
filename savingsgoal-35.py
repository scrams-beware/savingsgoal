# === Stage 35: Add active user switching and user-specific records ===
# Project: SavingsGoal
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.contributions = []

    def add_contribution(self, amount, label=""):
        self.contributions.append(Contribution(amount, label))

    def __repr__(self):
        return f"User({self.name}, {self.email}, {len(self.contributions)} contributions)"
