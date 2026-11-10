# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: SavingsGoal
def bulk_delete(self, goal_ids, confirm=False):
    if not goal_ids:
        return 0
    if confirm and not self._confirm_bulk_delete(goal_ids):
        return 0
    deleted = 0
    for goal_id in goal_ids:
        goal = self._goals.get(goal_id)
        if goal is None:
            continue
        self._contributions.pop(goal_id, None)
        self._milestones.pop(goal_id, None)
        self._projections.pop(goal_id, None)
        self._goals.pop(goal_id, None)
        deleted += 1
    if deleted:
        self._dirty = True
    return deleted
