# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: SavingsGoal
def dispatch(text: str):
    cmd = text.strip().lower()
    if cmd in ("help", "h"):
        print("Available commands: save, goal, milestones, project, list, quit")
    elif cmd == "save":
        print("Usage: save <amount> [label]")
    elif cmd == "goal":
        print("Usage: goal <target> [label]")
    elif cmd == "milestones":
        print("Usage: milestones <target> <amount>")
    elif cmd == "project":
        print("Usage: project <months>")
    elif cmd == "list":
        print("Current goals, contributions, and milestones:")
        for g in goals:
            print(f"  Goal: {g.target}, label: {g.label}")
        for c in contributions:
            print(f"  Contribution: {c.amount}, label: {c.label}")
        for m in milestones:
            print(f"  Milestone: {m.amount}, label: {m.label}")
    elif cmd == "quit" or cmd == "exit":
        print("Goodbye!")
        return True
    else:
        print("Unknown command. Type 'help' for a list.")
    return False
