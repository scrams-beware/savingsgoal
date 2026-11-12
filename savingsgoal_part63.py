# === Stage 63: Add relationships between records where useful ===
# Project: SavingsGoal
def link_records(records):
    linked = []
    for i, r in enumerate(records):
        for j, s in enumerate(records):
            if i == j:
                continue
            if r.get('goal') == s.get('goal'):
                if not r.get('related'):
                    r['related'] = [s['id']]
                else:
                    r['related'].append(s['id'])
                if not s.get('related'):
                    s['related'] = [r['id']]
                else:
                    s['related'].append(r['id'])
            linked.append((r['id'], s['id']))
    return linked

def display_relationships(records):
    print("Relationships:")
    for r in records:
        rel = r.get('related')
        if rel:
            print(f"{r['id']} -> {rel}")
        else:
            print(f"{r['id']} -> None")
