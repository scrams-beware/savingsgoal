# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: SavingsGoal
#!/usr/bin/env python3
"""demo.py - compact end-to-end demonstration of SavingsGoal."""

from savings_goal import SavingsGoal


def main() -> None:
    # --- 1. Create a goal ---
    goal = SavingsGoal(
        name="New Laptop",
        target=2500.0,
        currency="USD",
    )

    # --- 2. Add milestones ---
    goal.add_milestone("Saved $500", 500.0)
    goal.add_milestone("Saved $1000", 1000.0)
    goal.add_milestone("Saved $2000", 2000.0)

    # --- 3. Make contributions ---
    goal.contribute(100.0, "First paycheck")
    goal.contribute(200.0, "Birthday gift")
    goal.contribute(150.0, "Tax refund")

    # --- 4. Project future savings ---
    projected = goal.project_months(6, monthly_contribution=100.0)

    # --- 5. Print summary ---
    print(f"Goal: {goal.name}")
    print(f"Current savings: ${goal.total_contributions:.2f}")
    print(f"Projected in 6 months: ${projected:.2f}")
    print(f"Remaining to target: ${goal.target - goal.total_contributions:.2f}")
    print(f"Milestones reached: {goal.n_milestones_reached}/{goal.n_milestones}")


if __name__ == "__main__":
    main()
