# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: SavingsGoal
def recommend_priority(goals):
    scored = []
    for goal in goals:
        score = 0
        if goal['deadline']:
            days_left = (goal['deadline'] - date.today()).days
            if days_left <= 0:
                score += 100
            else:
                score += (30 - days_left // 30)
        if goal['remaining'] < 500:
            score += 50
        if goal['remaining'] <= 0:
            score += 200
        if goal['milestones']:
            score += 20
        scored.append((score, goal))
    scored.sort(reverse=True)
    return [goal for _, goal in scored]

def suggest_contribution(goal, monthly_income):
    if goal['deadline']:
        days_left = (goal['deadline'] - date.today()).days
        if days_left <= 0:
            return 0
        needed = goal['remaining'] / days_left * 30
        return min(int(needed), monthly_income)
    return int(goal['target'] * 0.05)
