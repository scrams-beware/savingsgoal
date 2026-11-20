# === Stage 76: Add graceful keyboard interrupt handling in the CLI entry point ===
# Project: SavingsGoal
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nSavingsGoal interrupted. Goodbye!")
        sys.exit(0)
