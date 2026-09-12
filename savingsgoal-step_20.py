# === Stage 20: Add duplicate detection for newly created records ===
# Project: SavingsGoal
def detect_duplicates(records, new_record):
    """Check if a new record already exists in the list of records."""
    for r in records:
        if r['target'] == new_record['target'] and r['goal_name'] == new_record['goal_name']:
            return True
    return False
