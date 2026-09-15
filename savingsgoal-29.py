# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: SavingsGoal
import math
from datetime import date, timedelta


def days_until(target_date: date, today: date = None) -> int:
    """Return the number of days left until *target_date* from *today*."""
    if today is None:
        today = date.today()
    delta = target_date - today
    return delta.days


def upcoming_milestones(milestones: list, today: date = None) -> list:
    """Return milestones that are still in the future, sorted by date."""
    if today is None:
        today = date.today()
    return sorted(
        [m for m in milestones if m["date"] > today],
        key=lambda m: m["date"],
    )


def upcoming_contributions(contributions: list, today: date = None) -> list:
    """Return contributions whose due date is at or after *today*."""
    if today is None:
        today = date.today()
    return sorted(
        [c for c in contributions if c["due_date"] >= today],
        key=lambda c: c["due_date"],
    )


def upcoming_reminders(goals: list, today: date = None) -> list:
    """Return a flat list of all upcoming events across all goals."""
    if today is None:
        today = date.today()
    items = []
    for g in goals:
        items.extend(
            [
                {"type": "milestone", "name": m["title"], "date": m["date"]}
                for m in g.get("milestones", [])
                if m["date"] > today
            ]
            + [
                {"type": "contribution", "name": c["name"], "date": c["due_date"]}
                for c in g.get("contributions", [])
                if c["due_date"] >= today
            ]
        )
    items.sort(key=lambda x: x["date"])
    return items
