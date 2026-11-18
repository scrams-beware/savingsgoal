# === Stage 74: Add a snapshot comparison helper for before/after states ===
# Project: SavingsGoal
def compare_snapshots(before, after, goal_id=None):
    def _pick(state, key):
        if isinstance(state, dict):
            return state.get(key)
        return getattr(state, key, None)

    before_savings = _pick(before, "savings")
    after_savings = _pick(after, "savings")
    before_target = _pick(before, "target")
    after_target = _pick(after, "target")

    before_progress = (before_savings / before_target * 100) if before_target else 0.0
    after_progress = (after_savings / after_target * 100) if after_target else 0.0

    delta = after_savings - before_savings
    target_delta = after_target - before_target
    progress_delta = after_progress - before_progress

    def _fmt(value):
        return round(value, 2)

    return {
        "savings_delta": _fmt(delta),
        "target_delta": _fmt(target_delta),
        "progress_delta": _fmt(progress_delta),
        "before_progress": _fmt(before_progress),
        "after_progress": _fmt(after_progress),
        "goal_id": goal_id,
    }
