# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: SavingsGoal
def validate_positive(value, label):
    if not isinstance(value, (int, float)) or value <= 0:
        raise ValueError(f"{label} must be a positive number, got {value}")
    return value

def validate_non_negative(value, label):
    if not isinstance(value, (int, float)) or value < 0:
        raise ValueError(f"{label} must be a non-negative number, got {value}")
    return value

def validate_identifier(value, label):
    if not value or not value.isalnum():
        raise ValueError(f"{label} must be a non-empty alphanumeric string, got '{value}'")
    return value

def validate_short_text(value, label, max_length=50):
    if not isinstance(value, str) or not value or len(value) > max_length:
        raise ValueError(f"{label} must be a non-empty string of at most {max_length} chars, got '{value}'")
    return value.strip()

def validate_date(value, label):
    if not isinstance(value, str) or len(value) != 10 or value[4] != '-' or value[7] != '-':
        raise ValueError(f"{label} must be YYYY-MM-DD, got '{value}'")
    try:
        year, month, day = int(value[:4]), int(value[5:7]), int(value[8:10])
        if not (1 <= year <= 9999 and 1 <= month <= 12 and 1 <= day <= 31):
            raise ValueError
    except ValueError:
        raise ValueError(f"{label} is not a valid date in YYYY-MM-DD format, got '{value}'")
    return value
