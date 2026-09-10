# === Stage 16: Add argparse support for the most common commands ===
# Project: SavingsGoal
import argparse

def build_cli():
    parser = argparse.ArgumentParser(description="SavingsGoal CLI")
    sub = parser.add_subparsers(dest="cmd")

    add = sub.add_parser("add", help="Add a contribution")
    add.add_argument("--name", required=True)
    add.add_argument("--amount", type=float, required=True)
    add.add_argument("--date", default=None)

    show = sub.add_parser("show", help="Show status")
    show.add_argument("--target", default=None, help="Filter by target")

    proj = sub.add_parser("project", help="Run projection")
    proj.add_argument("--months", type=int, default=12)
    proj.add_argument("--rate", type=float, default=0.0)

    return parser.parse_args()
