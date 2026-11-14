# === Stage 67: Add a function that returns key project metrics ===
# Project: SavingsGoal
def project_metrics(savings_data):
    total_target = sum(item['target'] for item in savings_data['targets'])
    total_contributed = sum(
        sum(contribution['amount'] for contribution in item['contributions'])
        for item in savings_data['targets']
    )
    total_contributors = sum(len(item['contributions']) for item in savings_data['targets'])
    total_milestones = sum(len(item['milestones']) for item in savings_data['targets'])
    total_contributed_per_month = total_contributed / 12
    total_target_per_month = total_target / 12
    total_projected_months = total_target_per_month / total_contributed_per_month
    total_projected = total_contributed_per_month * total_projected_months
    total_remaining = total_target - total_contributed
    total_percentage = (total_contributed / total_target * 100) if total_target > 0 else 0
    return {
        'total_target': total_target,
        'total_contributed': total_contributed,
        'total_remaining': total_remaining,
        'total_contributors': total_contributors,
        'total_milestones': total_milestones,
        'total_contributed_per_month': total_contributed_per_month,
        'total_target_per_month': total_target_per_month,
        'total_projected_months': total_projected_months,
        'total_projected': total_projected,
        'total_percentage': total_percentage,
    }
