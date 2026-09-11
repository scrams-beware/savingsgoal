# === Stage 19: Add undo support for the last simple mutation ===
# Project: SavingsGoal
import json
from pathlib import Path
from datetime import datetime

GOAL_FILE = Path("savings_goal.json")

def load_goal():
    if not GOAL_FILE.exists():
        return {"name": "Savings Goal", "target": 0, "contributions": [], "milestones": []}
    return json.loads(GOAL_FILE.read_text())

def save_goal(goal):
    GOAL_FILE.write_text(json.dumps(goal, indent=2))

def undo_last():
    goal = load_goal()
    if not goal["contributions"]:
        return goal
    last = goal["contributions"][-1]
    goal["contributions"].pop()
    goal["target"] = max(0, goal["target"] - last["amount"])
    goal["milestones"] = [m for m in goal["milestones"] if m["month"] != last["month"]]
    save_goal(goal)
    return goal
