# === Stage 18: Add an activity log with timestamps and action names ===
# Project: SavingsGoal
class ActivityLog:
    def __init__(self):
        self.entries = []

    def log(self, action, details=""):
        self.entries.append({
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "details": details
        })

    def get_log(self):
        return self.entries
