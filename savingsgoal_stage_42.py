# === Stage 42: Add CSV export without external dependencies ===
# Project: SavingsGoal
import csv, os

def export_csv(tracker, path):
    with open(path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['date', 'amount', 'category', 'balance', 'milestones', 'notes'])
        for d in tracker.history:
            w.writerow([d['date'], d['amount'], d.get('category', ''),
                         d.get('balance', 0), d.get('milestones', []), d.get('notes', '')])
        for i, m in enumerate(tracker.milestones):
            w.writerow(['milestone', i+1, m['target'], m['amount'], m['remaining'], m['date'], m.get('notes', '')])
        w.writerow(['projection', '', tracker.target, tracker.current, tracker.remaining, '', tracker.date])
