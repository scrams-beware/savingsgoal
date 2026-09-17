# === Stage 34: Add support for multiple local user profiles ===
# Project: SavingsGoal
class ProfileConfig:
    def __init__(self, name, balance, monthly_contribution, monthly_inflation, monthly_interest, monthly_tax, monthly_fee):
        self.name = name
        self.balance = balance
        self.monthly_contribution = monthly_contribution
        self.monthly_inflation = monthly_inflation
        self.monthly_interest = monthly_interest
        self.monthly_tax = monthly_tax
        self.monthly_fee = monthly_fee

    def to_dict(self):
        return {
            "name": self.name,
            "balance": self.balance,
            "monthly_contribution": self.monthly_contribution,
            "monthly_inflation": self.monthly_inflation,
            "monthly_interest": self.monthly_interest,
            "monthly_tax": self.monthly_tax,
            "monthly_fee": self.monthly_fee,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data["name"],
            balance=data["balance"],
            monthly_contribution=data["monthly_contribution"],
            monthly_inflation=data["monthly_inflation"],
            monthly_interest=data["monthly_interest"],
            monthly_tax=data["monthly_tax"],
            monthly_fee=data["monthly_fee"],
        )
