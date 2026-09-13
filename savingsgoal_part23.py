# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: SavingsGoal
def add_tag(self, goal, tag):
    if goal.tags is None:
        goal.tags = []
    if tag not in goal.tags:
        goal.tags.append(tag)
        goal._updated = True
    return goal

def remove_tag(self, goal, tag):
    if goal.tags and tag in goal.tags:
        goal.tags.remove(tag)
        goal._updated = True
    return goal

def tag_summary(self, goals, tag):
    if not goals:
        return 0.0, 0
    total, count = 0.0, 0
    for g in goals:
        if g.tags and tag in g.tags:
            total += g.amount
            count += 1
    if count == 0:
        return 0.0, 0
    return total, count
