# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: SavingsGoal
CONFIRM = False

def ask_clear(prompt):
    global CONFIRM
    CONFIRM = input(prompt).strip().lower() == "yes"

def clear_state():
    if not CONFIRM:
        print("Aborted: type 'yes' to confirm clearing all data.")
        return
    goals.clear()
    milestones.clear()
    contributions.clear()
    print("All savings data cleared.")

def load_data():
    with open("savings_data.json", "w") as f:
        json.dump({"goals": goals, "milestones": milestones, "contributions": contributions}, f, indent=2)

def save_data():
    load_data()
    print("Data saved.")
