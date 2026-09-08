# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: SavingsGoal
def sort_savings_goals(goals, key='title'):
    sort_keys = {
        'title': lambda g: g.title.lower(),
        'date': lambda g: g.created_date or '',
        'priority': lambda g: (g.priority or 3, g.title.lower()),
        'last_update': lambda g: g.last_updated or '',
    }
    key_func = sort_keys.get(key, sort_keys['title'])
    return sorted(goals, key=key_func)
