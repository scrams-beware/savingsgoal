# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: SavingsGoal
def update_record(records, record_id, updates):
    """Update an existing record by ID; returns (updated_record, status).
    
    Args:
        records: list of dict objects in the database.
        record_id: int or string identifier of the record to update.
        updates: dict of field_name -> new_value to apply.
    
    Returns:
        (updated_record, status) where status is 'updated', 'not_found', or 'unknown_fields'.
    """
    found = None
    for r in records:
        if r.get('id') == record_id:
            found = r
            break
    
    if found is None:
        return {'id': record_id, 'status': 'not_found', 'data': None}
    
    unknown = [k for k in updates if k not in found and k != 'id']
    if unknown:
        return {'id': record_id, 'status': 'unknown_fields', 'data': found, 'unknown': unknown}
    
    for key, value in updates.items():
        found[key] = value
    
    return {'id': record_id, 'status': 'updated', 'data': found}
