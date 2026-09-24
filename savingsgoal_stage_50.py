# === Stage 50: Add unit tests for import and export behavior ===
# Project: SavingsGoal
import json, os, tempfile
from pathlib import Path

TEST_DIR = Path(tempfile.gettempdir()) / "savings_goal_tests"
TEST_DIR.mkdir(parents=True, exist_ok=True)

from savings_goal import SavingsGoal, Contribution, Milestone, GoalTarget, Projector
from savings_goal_export import export_json, export_csv, export_html

def test_export_roundtrip():
    goal = SavingsGoal("Vacation", 5000, "USD", "2025-12-31")
    goal.add_contribution(100, "2025-01-01", "Salary")
    goal.add_contribution(200, "2025-02-01", "Freelance")
    goal.add_milestone(2500, "2025-06-01")
    goal.add_target(1000, "2025-03-01")

    json_path = TEST_DIR / "vacation.json"
    csv_path = TEST_DIR / "vacation.csv"
    html_path = TEST_DIR / "vacation.html"

    export_json(goal, json_path)
    export_csv(goal, csv_path)
    export_html(goal, html_path)

    assert json_path.exists() and csv_path.exists() and html_path.exists()

    loaded = json.loads(json_path.read_text())
    assert loaded["name"] == "Vacation"
    assert len(loaded["contributions"]) == 2
    assert len(loaded["milestones"]) == 1
    assert len(loaded["targets"]) == 1
