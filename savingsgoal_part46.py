# === Stage 46: Add a schema version field and migration helper ===
# Project: SavingsGoal
SCHEMA_VERSION = 2


def migrate_to_v2(db):
    """Apply schema v1 -> v2 migration: add audit log table and reset counters."""
    cur = db.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS audit_log (id INTEGER PRIMARY KEY AUTOINCREMENT, action TEXT, record_id INTEGER, timestamp TEXT DEFAULT CURRENT_TIMESTAMP)")
    cur.execute("SELECT COUNT(*) FROM audit_log")
    if cur.fetchone()[0] == 0:
        cur.execute("INSERT INTO audit_log (action, record_id) VALUES ('schema_migrate', 0)")
    cur.close()
