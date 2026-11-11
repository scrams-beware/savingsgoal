# === Stage 61: Add performance timing for core list and search operations ===
# Project: SavingsGoal
import time


def _timeit(func, iterations=1000):
    """Return average execution time in seconds for func over iterations."""
    start = time.perf_counter()
    for _ in range(iterations):
        func()
    return (time.perf_counter() - start) / iterations


def time_operations(contributions, goals):
    """Benchmark core list and search operations on contributions and goals."""
    results = {}
    results["list_contributions"] = _timeit(lambda: list(contributions))
    results["list_goals"] = _timeit(lambda: list(goals))
    results["search_by_amount_in_contributions"] = _timeit(
        lambda: [c for c in contributions if c.amount >= 50]
    )
    results["search_by_name_in_goals"] = _timeit(
        lambda: [g for g in goals if "goal" in g.name.lower()]
    )
    results["search_by_target_in_goals"] = _timeit(
        lambda: [g for g in goals if g.target >= 1000]
    )
    return results


def print_timing_report(report):
    """Print a formatted timing report for benchmark results."""
    print("Performance Timing Report (seconds):")
    for key, value in report.items():
        print(f"  {key}: {value:.6f}")
