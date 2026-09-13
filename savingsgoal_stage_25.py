# === Stage 25: Add daily summary calculations ===
# Project: SavingsGoal
def daily_summary(goals):
    """Return a dictionary with today's summary for each goal."""
    summary = {}
    for goal in goals:
        today = goal['target_date']
        if isinstance(today, str) and today == '':
            today = goal.get('contribution_date')
        if not isinstance(today, datetime.date):
            today = datetime.date.today()
        days_left = (today - goal['target_date']).days if isinstance(goal['target_date'], datetime.date) else 0
        remaining = goal['target_amount'] - goal['contributed_amount']
        if remaining < 0:
            remaining = 0
        days_contributed = goal['contribution_count'] if isinstance(goal['contribution_count'], int) else 0
        if goal['target_date'] and days_left > 0:
            daily_rate = goal['target_amount'] / days_left
        else:
            daily_rate = remaining / max(days_contributed, 1)
        summary[goal['name']] = {
            'target_date': goal['target_date'].isoformat() if isinstance(goal['target_date'], datetime.date) else '',
            'remaining': remaining,
            'daily_rate': round(daily_rate, 2),
            'days_left': days_left,
            'contributions': days_contributed
        }
    return summary
