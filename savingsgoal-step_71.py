# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: SavingsGoal
def seed_demo_data(account):
    account.name = "Vacation Fund"
    account.target_amount = 5000.0
    account.contributions = [
        {"date": "2024-01-01", "amount": 100.0, "note": "First deposit"},
        {"date": "2024-02-01", "amount": 150.0, "note": "Monthly habit"},
        {"date": "2024-03-01", "amount": 200.0, "note": "Bonus saved"},
    ]
    account.milestones = [
        {"amount": 1000.0, "date": "2024-04-01", "note": "Quarter one"},
        {"amount": 2500.0, "date": "2024-07-01", "note": "Halfway point"},
    ]
    account.monthly_contribution = 150.0
    account.annual_interest_rate = 0.03
    account.start_date = "2024-01-01"
