# === Stage 32: Add pagination helpers for long console output ===
# Project: SavingsGoal
def paginate(lines, per_page=20):
    """Yield chunks of lines for console paging."""
    total = len(lines)
    if total <= per_page:
        yield lines
        return
    chunk_size = per_page - 1
    chunk = []
    for line in lines:
        chunk.append(line)
        if len(chunk) >= chunk_size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk
