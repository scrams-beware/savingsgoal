# === Stage 56: Add compact error classes for domain failures ===
# Project: SavingsGoal
class SavingsGoalError(Exception):
    pass


class TargetError(SavingsGoalError):
    def __init__(self, target, message):
        self.target = target
        self.message = message
        super().__init__(f"Target {target}: {message}")


class ContributionError(SavingsGoalError):
    def __init__(self, amount, message):
        self.amount = amount
        self.message = message
        super().__init__(f"Contribution {amount}: {message}")


class MilestoneError(SavingsGoalError):
    def __init__(self, milestone, message):
        self.milestone = milestone
        self.message = message
        super().__init__(f"Milestone {milestone}: {message}")


class ProjectionError(SavingsGoalError):
    def __init__(self, message):
        self.message = message
        super().__init__(f"Projection: {message}")
