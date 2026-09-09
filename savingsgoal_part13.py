# === Stage 13: Add file save support using a configurable path ===
# Project: SavingsGoal
import os
import json
import datetime

def save_goal_data(goal, filepath=None):
    """Save the goal data to a JSON file.

    Args:
        goal (dict): The goal data to save.
        filepath (str, optional): The file path to save to. If None, uses a default path.

    Returns:
        str: The file path where the data was saved.
    """
    if filepath is None:
        filepath = "savings_goal.json"

    # Ensure the file path ends with .json
    if not filepath.endswith(".json"):
        filepath += ".json"

    # Create the directory if it doesn't exist
    directory = os.path.dirname(filepath)
    if directory:
        os.makedirs(directory, exist_ok=True)

    # Save the goal data to the file
    with open(filepath, "w") as f:
        json.dump(goal, f, indent=2)

    return filepath
