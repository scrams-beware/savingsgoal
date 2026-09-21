# === Stage 44: Add backup creation for the data file ===
# Project: SavingsGoal
import json, os

def save_backup(data_file, backup_dir="."):
    if not os.path.exists(data_file):
        return
    os.makedirs(backup_dir, exist_ok=True)
    backup_path = os.path.join(backup_dir, "backup_" + os.path.basename(data_file))
    with open(data_file, "r") as f:
        data = f.read()
    with open(backup_path, "w") as f:
        f.write(data)
    print(f"Backup saved to {backup_path}")
