# === Stage 36: Add templates for quickly creating common records ===
# Project: SavingsGoal
class RecordTemplates:
    """Quick templates for common SavingsGoal records."""
    @staticmethod
    def monthly_contribution(goal, amount, month_label):
        return {
            "goal": goal,
            "type": "monthly_contribution",
            "amount": amount,
            "month": month_label,
            "date": None,
            "note": f"Regular monthly contribution of ${amount:.2f} toward {goal}.",
        }

    @staticmethod
    def one_time_deposit(goal, amount, date, note=""):
        return {
            "goal": goal,
            "type": "one_time_deposit",
            "amount": amount,
            "date": date,
            "note": note or f"One-time deposit of ${amount:.2f} toward {goal}.",
        }

    @staticmethod
    def milestone(goal, target_amount, achieved_date, note=""):
        return {
            "goal": goal,
            "type": "milestone",
            "target_amount": target_amount,
            "achieved_date": achieved_date,
            "note": note or f"Milestone reached for {goal}: ${target_amount:.2f}!",
        }

    @staticmethod
    def projection(goal, start_date, rate, months, note=""):
        return {
            "goal": goal,
            "type": "projection",
            "start_date": start_date,
            "monthly_rate": rate,
            "months": months,
            "note": note or f"Projected growth for {goal} over {months} months at {rate*100:.1f}% monthly.",
        }

    @staticmethod
    def withdrawal(goal, amount, date, note=""):
        return {
            "goal": goal,
            "type": "withdrawal",
            "amount": amount,
            "date": date,
            "note": note or f"Withdrew ${amount:.2f} from {goal} on {date}.",
        }
