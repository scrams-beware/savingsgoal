# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: SavingsGoal
def build_changelog(activity_log):
    """Summarize activity_log into a compact changelog string."""
    entries = activity_log.get("entries", [])
    if not entries:
        return "No changes recorded yet."
    lines = []
    for idx, item in enumerate(entries, start=1):
        date = item.get("date", "unknown")
        message = item.get("message", "no message")
        lines.append(f"{idx}. [{date}] {message}")
    header = "SavingsGoal Changelog"
    width = max(len(header), len(lines[0].split(". ", 1)[0]))
    separator = "=" * (width + 4)
    changelog = f"{separator}\n{header}\n{separator}\n"
    changelog += "\n".join(lines) + "\n"
    return changelog
