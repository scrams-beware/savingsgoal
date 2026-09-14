# === Stage 26: Add weekly summary calculations ===
# Project: SavingsGoal
def weekly_summary(goals, contributions):
    """Compute weekly summaries across all goals.

    Returns a dict of goal_name -> {
        'total_saved': float,
        'total_contributed': float,
        'balance': float,
        'weekly_avg_contribution': float,
        'remaining': float,
        'weekly_progress_pct': float,
    }
    """
    summaries = {}
    for g in goals:
        name = g['name']
        total_saved = sum(c['amount'] for c in contributions if c['goal'] == name)
        total_contributed = sum(c['amount'] for c in contributions if c['goal'] == name)
        balance = g['target'] - total_saved
        weekly_avg = total_contributed / max(len(contributions) / 7.0, 1)
        remaining = g['target'] - total_saved
        progress_pct = (total_saved / g['target']) * 100 if g['target'] else 0
        summaries[name] = {
            'total_saved': total_saved,
            'total_contributed': total_contributed,
            'balance': balance,
            'weekly_avg_contribution': weekly_avg,
            'remaining': remaining,
            'weekly_progress_pct': progress_pct,
        }
    return summaries
