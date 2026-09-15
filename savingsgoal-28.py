# === Stage 28: Add overdue item detection based on due dates ===
# Project: SavingsGoal
def check_overdue(self):
        """Mark items past their due date as overdue."""
        overdue = []
        now = datetime.now()
        for item in self.items:
            if item.due_date and item.due_date < now:
                if item.status != "completed":
                    item.status = "overdue"
                    overdue.append(item)
        return overdue
