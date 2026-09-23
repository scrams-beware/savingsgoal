# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: SavingsGoal
import pytest
from savings_goal import create_goal, validate_goal, calculate_projection

def test_create_goal():
    goal = create_goal("Vacation", 5000, 12, 100)
    assert goal["name"] == "Vacation"
    assert goal["target_amount"] == 5000
    assert goal["monthly_contribution"] == 100
    assert goal["months"] == 12

def test_validate_goal():
    goal = {"name": "Test", "target_amount": 1000, "monthly_contribution": 50, "months": 20}
    assert validate_goal(goal) is True

def test_validate_goal_invalid():
    goal = {"name": "Test", "target_amount": 1000, "monthly_contribution": 0, "months": 20}
    assert validate_goal(goal) is False

def test_calculate_projection():
    goal = {"target_amount": 5000, "monthly_contribution": 100, "months": 12, "annual_rate": 0.05}
    projection = calculate_projection(goal)
    assert projection["months"] == 12
    assert projection["total_contributed"] == 1200
    assert projection["projected_value"] == 1200 * (1 + 0.05) ** (12 / 12)
