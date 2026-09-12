# === Stage 22: Add favorite records and quick favorite listing ===
# Project: SavingsGoal
# Favorites for quick access to a user's top savings goals
FAVORITES_FILE = "favorites.json"

def set_favorites(user, favorite_ids):
    """Record the user's favorite goal IDs."""
    favorites = _load(FAVORITES_FILE)
    favorites[user] = favorite_ids
    _save(FAVORITES_FILE, favorites)

def get_favorites(user):
    """Return the user's favorite goal IDs, or an empty list."""
    return _load(FAVORITES_FILE).get(user, [])

def list_favorites(user):
    """Print a compact summary of the user's favorite goals."""
    fav_ids = get_favorites(user)
    if not fav_ids:
        print("No favorites yet.")
        return
    goals = _load("savings_goals.json")
    for fid in fav_ids:
        g = goals.get(fid, {})
        name = g.get("name", "Unnamed")
        target = g.get("target", "?")
        print(f"  - {name} (target: {target})")
