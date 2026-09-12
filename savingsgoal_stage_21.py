# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: SavingsGoal
def archive_record(record, cutoff_date=None):
    if cutoff_date is None:
        cutoff_date = datetime.now()
    if record.completed_at and record.completed_at >= cutoff_date:
        return record.copy()
    return None

def restore_record(archive, cutoff_date=None):
    if cutoff_date is None:
        cutoff_date = datetime.now()
    return archive.copy() if archive else None
