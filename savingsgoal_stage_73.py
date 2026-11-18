# === Stage 73: Add a lightweight HTML report export ===
# Project: SavingsGoal
def export_html_report(path, goals):
    with open(path, 'w', encoding='utf-8') as f:
        f.write('<!DOCTYPE html>\n<html><head><meta charset="utf-8">\n<title>SavingsGoal Report</title>\n')
        f.write('<style>body{font-family:Arial,sans-serif;margin:24px}table{border-collapse:collapse;width:100%}th,td{border:1px solid #ccc;padding:8px;text-align:left}th{background:#f0f0f0}</style>\n')
        f.write('</head><body><h1>SavingsGoal Report</h1>')
        for g in goals:
            f.write('<h2>%s</h2>\n' % g.name)
            f.write('<p>Target: %.2f | Saved: %.2f | Progress: %.0f%% | Remaining: %.2f</p>\n' % (
                g.target, g.saved, 100.0 * g.saved / g.target if g.target else 0.0, g.target - g.saved))
            if g.milestones:
                f.write('<h3>Milestones</h3><ul>')
                for m in g.milestones:
                    done = 'yes' if m.done else 'no'
                    f.write('<li>%s [%s]</li>\n' % (m.description, done))
                f.write('</ul>\n')
            if g.projections:
                f.write('<h3>Projections</h3><table><tr><th>Months</th><th>Contributions</th><th>Balance</th></table>')
                for p in g.projections:
                    f.write('<tr><td>%d</td><td>%.2f</td><td>%.2f</td></tr>\n' % (p.months, p.contribution, p.balance))
        f.write('</body></html>\n')
