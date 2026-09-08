# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: SavingsGoal
import json

def load_json_safe(path):
    """Load a JSON file and return its parsed content.
    
    If the file does not exist or contains malformed data,
    a clear exception is raised with a helpful message.
    """
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"JSON file not found: {path}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Malformed JSON in '{path}' at line {e.lineno}, column {e.colno}: {e.msg}")
    except PermissionError:
        raise PermissionError(f"No permission to read '{path}'")
