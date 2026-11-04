# === Stage 53: Add command help text and usage examples ===
# Project: SavingsGoal
def print_help():
    help_text = (
        "SavingsGoal - Track savings toward your goals.\n"
        "Usage:\n"
        "  python savings_goal.py <command> [options]\n\n"
        "Commands:\n"
        "  add-goal    Add a new savings goal with a target amount.\n"
        "  add-contribution   Contribute money toward an existing goal.\n"
        "  add-milestone      Record a milestone reached within a goal.\n"
        "  show-goal    Display details of a specific goal.\n"
        "  list-goals   List all saved goals.\n"
        "  project      Show projected growth until the goal is met.\n"
        "  help         Show this help message.\n"
        "  exit         Exit the program.\n\n"
        "Examples:\n"
        "  python savings_goal.py add-goal vacation --target 2000\n"
        "  python savings_goal.py add-contribution vacation --amount 250\n"
        "  python savings_goal.py show-goal vacation\n"
        "  python savings_goal.py project vacation --months 6\n"
        "  python savings_goal.py list-goals\n"
    )
    print(help_text)


if __name__ == "__main__":
    print_help()
