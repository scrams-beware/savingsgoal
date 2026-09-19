# === Stage 38: Add data integrity checks for broken references ===
# Project: SavingsGoal
def check_integrity(data):
    """Validate that all cross-references in the savings data are consistent."""
    errors = []
    contributions = data.get("contributions", [])
    milestones = data.get("milestones", [])
    targets = data.get("targets", [])

    contrib_ids = {c["id"] for c in contributions}
    milestone_contrib_ids = {m["contribution_id"] for m in milestones if "contribution_id" in m}
    errors += [f"Orphan milestone: {m['id']} references non-existent contribution {m['contribution_id']}" for m in milestones if m["contribution_id"] not in contrib_ids]

    target_ids = {t["id"] for t in targets}
    milestone_target_ids = {m["target_id"] for m in milestones if "target_id" in m}
    errors += [f"Orphan milestone: {m['id']} references non-existent target {m['target_id']}" for m in milestones if m["target_id"] not in target_ids]

    for t in targets:
        if t.get("goal_id") and t["goal_id"] not in contrib_ids:
            errors.append(f"Orphan target: {t['id']} references non-existent goal {t['goal_id']}")

    return len(errors) == 0, errors
