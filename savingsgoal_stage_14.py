# === Stage 14: Add file load support with fallback demo data ===
# Project: SavingsGoal
def load_data():
    """Load SavingsGoal data from a JSON file; fall back to demo data."""
    import json
    import os

    file_path = os.path.join(os.path.dirname(__file__), "savings_data.json")
    if os.path.exists(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {
        "goal_name": "New Laptop",
        "target_amount": 1200.0,
        "contributions": [
            {"date": "2024-01-01", "amount": 100.0},
            {"date": "2024-02-01", "amount": 150.0},
            {"date": "2024-03-01", "amount": 200.0},
        ],
        "milestones": [
            {"date": "2024-04-01", "amount": 500.0, "note": "Halfway there!"},
        ],
    }
