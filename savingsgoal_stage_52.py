# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: SavingsGoal
def calculate_total_contributions(contributions):
    """Sum all monetary contributions across the provided list.

    Args:
        contributions: A list of numbers representing saved amounts.

    Returns:
        The total of all contributions as a float.
    """
    total = 0.0
    for amount in contributions:
        total += amount
    return total


def calculate_savings_rate(monthly_contribution, monthly_income):
    """Compute the fraction of monthly income saved each month.

    Args:
        monthly_contribution: Amount saved per month.
        monthly_income: Total income received per month.

    Returns:
        The savings rate rounded to four decimal places.
    """
    if monthly_income <= 0:
        return 0.0
    return round(monthly_contribution / monthly_income, 4)


def format_currency(amount):
    """Render a monetary amount as a locale-free currency string.

    Args:
        amount: The numeric value to display.

    Returns:
        A string formatted to two decimal places with a dollar sign.
    """
    return "${:,.2f}".format(amount)


def find_nearest_milestone(target, current):
    """Identify the closest milestone below the current savings level.

    Args:
        target: A list of milestone threshold values in ascending order.
        current: The amount already saved.

    Returns:
        The milestone value just below the current amount, or None if no
        milestone qualifies.
    """
    nearest = None
    for milestone in target:
        if milestone <= current:
            nearest = milestone
        else:
            break
    return nearest


def project_future_value(current, monthly_contribution, months, monthly_rate):
    """Estimate savings after a number of months with simple interest.

    Args:
        current: The amount saved at the start.
        monthly_contribution: Amount added each month.
        months: Number of months to project.
        monthly_rate: Interest rate applied per month.

    Returns:
        The projected savings after the given number of months.
    """
    interest = current * monthly_rate * months
    added = monthly_contribution * months
    return current + added + interest
