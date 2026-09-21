# === Stage 45: Add restore from backup with validation ===
# Project: SavingsGoal
import json, os

def restore_from_backup(backup_path, target_file, validate=True):
    """Restore a JSON backup into target_file, optionally validating it."""
    if not os.path.isfile(backup_path):
        raise FileNotFoundError(f"Backup file not found: {backup_path}")
    with open(backup_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if validate:
        if not isinstance(data, dict):
            raise ValueError("Backup must be a JSON object")
        for key in ('goal_name', 'target_amount', 'contributions', 'milestones'):
            if key not in data:
                raise ValueError(f"Missing required key: {key}")
    with open(target_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Restored from {backup_path} to {target_file}")
