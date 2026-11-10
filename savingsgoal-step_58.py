# === Stage 58: Add bulk update behavior for selected records ===
# Project: SavingsGoal
def bulk_update_records(records, updates, where):
    """Apply bulk updates to selected records.

    Args:
        records: dict mapping primary key to record dict.
        updates: dict of field -> new value to apply.
        where: dict of field -> value used to select records.

    Returns:
        int number of records updated.
    """
    selected = {
        key: rec for key, rec in records.items() if all(rec.get(field) == value for field, value in where.items())
    }
    updated = 0
    for rec in selected.values():
        for field, value in updates.items():
            rec[field] = value
        updated += 1
    return updated
