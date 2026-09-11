# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: SavingsGoal
def dry_run(*args, **kwargs):
    """Simulate a mutating command without actually changing state."""
    print(f"[DRY RUN] Would execute: {args[0]} with kwargs={kwargs}")
