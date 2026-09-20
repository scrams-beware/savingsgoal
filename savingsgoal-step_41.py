# === Stage 41: Add plain text import for a simple line-based format ===
# Project: SavingsGoal
def parse_csv(lines):
    """Parse a simple CSV string with headers into a list of dicts."""
    records = []
    for line in lines.strip().splitlines():
        if not line.strip():
            continue
        parts = [f.strip() for f in line.split(",")]
        records.append(dict(zip(parts, parts)))
    return records

def parse_tsv(lines):
    """Parse a simple TSV string with headers into a list of dicts."""
    records = []
    for line in lines.strip().splitlines():
        if not line.strip():
            continue
        parts = line.split("\t")
        records.append(dict(zip(parts, parts)))
    return records

def parse_plain(lines):
    """Parse a simple key=value per line into a list of dicts."""
    records = []
    for line in lines.strip().splitlines():
        if not line.strip():
            continue
        if "=" in line:
            key, value = line.split("=", 1)
            records.append({key.strip(): value.strip()})
    return records
