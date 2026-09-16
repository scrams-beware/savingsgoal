# === Stage 31: Add compact table rendering for long lists ===
# Project: SavingsGoal
def compact_table(rows, headers, max_height=12):
    if not headers:
        return ""
    if not rows:
        return f"{' | '.join(headers)}"
    if len(rows) <= max_height:
        header = " | ".join(str(h).ljust(max(wlen(h), len(str(h)))) for h, wlen in zip(headers, [len(str(h)) for h in headers]))
        return header + "\n" + "\n".join(" | ".join(str(c).ljust(max(wlen(h), len(str(c)))) for c, h, wlen in zip(row, headers, [len(str(h)) for h in headers])) for row in rows)
    lines = [header]
    for i, row in enumerate(rows):
        lines.append(" | ".join(str(c).ljust(max(wlen(h), len(str(c)))) for c, h, wlen in zip(row, headers, [len(str(h)) for h in headers])))
        if i >= max_height - 1:
            lines.append(f"... ({len(rows) - i} more rows)")
            break
    return "\n".join(lines)
