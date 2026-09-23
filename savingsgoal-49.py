# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: SavingsGoal
import pytest
from savings_goal import Goal, Contribution, Milestone


def test_delete_contributions_removes_all():
    goal = Goal("Test", target=1000)
    goal.add_contribution(Contribution("Jan", 100))
    goal.add_contribution(Contribution("Feb", 200))
    goal.delete_contributions(["Jan", "Feb"])
    assert goal.contributions == []
    assert goal.total_contributions == 0


def test_delete_milestones_removes_all():
    goal = Goal("Test", target=1000)
    goal.add_milestone(Milestone("Saved 500", 500))
    goal.add_milestone(Milestone("Saved 1000", 1000))
    goal.delete_milestones(["Saved 500", "Saved 1000"])
    assert goal.milestones == []
    assert len(goal.milestones) == 0


def test_delete_nonexistent_contributions_no_error():
    goal = Goal("Test", target=1000)
    goal.add_contribution(Contribution("Jan", 100))
    goal.delete_contributions(["Feb", "Mar"])
    assert goal.contributions[0].name == "Jan"


def test_delete_nonexistent_milestones_no_error():
    goal = Goal("Test", target=1000)
    goal.add_milestone(Milestone("Saved 500", 500))
    goal.delete_milestones(["Saved 999"])
    assert goal.milestones[0].description == "Saved 500"


def test_update_contribution_changes_amount():
    goal = Goal("Test", target=1000)
    goal.add_contribution(Contribution("Jan", 100))
    goal.update_contribution("Jan", 150)
    assert goal.contributions[0].amount == 150


def test_update_milestone_changes_amount():
    goal = Goal("Test", target=1000)
    goal.add_milestone(Milestone("Saved 500", 500))
    goal.update_milestone("Saved 500", 600)
    assert goal.milestones[0].amount == 600


def test_update_nonexistent_contribution_raises():
    goal = Goal("Test", target=1000)
    goal.add_contribution(Contribution("Jan", 100))
    with pytest.raises(ValueError):
        goal.update_contribution("Feb", 200)


def test_update_nonexistent_milestone_raises():
    goal = Goal("Test", target=1000)
    goal.add_milestone(Milestone("Saved 500", 500))
    with pytest.raises(ValueError):
        goal.update_milestone("Saved 999", 1000)
