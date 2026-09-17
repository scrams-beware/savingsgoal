# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: SavingsGoal
DEFAULT_SETTINGS = {
    "currency": "$",
    "interest_rate": 0.05,
    "compound_frequency": "monthly",
    "notification_days": 7,
    "max_contribution": None,
    "goal_name": "General Savings",
}

def get_settings():
    return DEFAULT_SETTINGS.copy()

def update_settings(**kwargs):
    settings = get_settings()
    for key, value in kwargs.items():
        if key in DEFAULT_SETTINGS and value is not None:
            settings[key] = value
        else:
            raise ValueError(f"Invalid setting key: {key}")
    return settings

def set_default_settings():
    return DEFAULT_SETTINGS.copy()
