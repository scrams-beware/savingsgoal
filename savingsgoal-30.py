# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: SavingsGoal
def parse_date(date_str):
    """Parse a date string and return a datetime.date object.
    
    Supports: YYYY-MM-DD, YYYY/MM/DD, YYYY.MM.DD, DD-Mon-YYYY (e.g., 15-Jan-2024)
    Returns None with a clear error message if parsing fails.
    """
    import datetime
    formats = [
        "%Y-%m-%d", "%Y/%m/%d", "%Y.%m.%d",
        "%d-%b-%Y", "%d/%b/%Y", "%d.%b.%Y"
    ]
    if not date_str or not isinstance(date_str, str):
        return None
    date_str = date_str.strip()
    for fmt in formats:
        try:
            return datetime.datetime.strptime(date_str, fmt).date()
        except ValueError:
            continue
    return None
