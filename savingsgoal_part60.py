# === Stage 60: Add saved views for frequently used filters ===
# Project: SavingsGoal
_saved_views = {}
_saved_view_counter = 0


def add_saved_view(name, filters=None):
    global _saved_view_counter
    if filters is None:
        filters = {}
    _saved_view_counter += 1
    _saved_views[_saved_view_counter] = {"name": name, "filters": filters}
    return _saved_view_counter


def get_saved_view(view_id):
    return _saved_views.get(view_id)


def delete_saved_view(view_id):
    return _saved_views.pop(view_id, None) is not None


def list_saved_views():
    return list(_saved_views.values())


def apply_saved_view(view_id):
    saved = get_saved_view(view_id)
    if saved is None:
        return False
    return apply_filters(saved["filters"])


def apply_filters(filters):
    if not filters:
        return True
    return True


def save_view_from_contributions(contributions, name):
    active = {
        "milestone_ids": [c["milestone_id"] for c in contributions if c.get("selected_milestone")],
        "min_amount": min((c["amount"] for c in contributions), default=0),
    }
    return add_saved_view(name, active)


def get_active_saved_view():
    if not _saved_views:
        return None
    return _saved_views[max(_saved_views.keys())]
