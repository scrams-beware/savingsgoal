# === Stage 51: Add unit tests for search and filter behavior ===
# Project: SavingsGoal
def test_search_by_name_contains():
    goal = SavingsGoal(name="vacation", amount=2000, contributions=[500, 300])
    results = find_goals_by_substring(goals=[goal], substring="vac")
    assert len(results) == 1
    assert results[0] is goal


def test_search_is_case_insensitive():
    goal = SavingsGoal(name="Car Trip", amount=3000)
    results = find_goals_by_substring(goals=[goal], substring="car")
    assert len(results) == 1


def test_search_no_match_returns_empty():
    goal = SavingsGoal(name="wedding", amount=10000)
    results = find_goals_by_substring(goals=[goal], substring="honeymoon")
    assert results == []


def test_filter_by_status_savings():
    active = SavingsGoal(name="a", amount=1000, contributions=[200])
    done = SavingsGoal(name="b", amount=500, contributions=[500])
    results = filter_goals_by_status(goals=[active, done], status="savings")
    assert len(results) == 1
    assert results[0] is active


def test_filter_by_min_amount():
    small = SavingsGoal(name="a", amount=500)
    big = SavingsGoal(name="b", amount=2000)
    results = filter_goals_by_min_amount(goals=[small, big], minimum=1000)
    assert len(results) == 1
    assert results[0] is big


def test_filter_by_max_amount():
    small = SavingsGoal(name="a", amount=500)
    big = SavingsGoal(name="b", amount=2000)
    results = filter_goals_by_max_amount(goals=[small, big], maximum=1000)
    assert len(results) == 1
    assert results[0] is small


def test_filter_empty_list_returns_empty():
    results = filter_goals_by_status(goals=[], status="savings")
    assert results == []
