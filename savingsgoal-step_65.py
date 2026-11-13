# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: SavingsGoal
import re


def merge_imports(existing, new_code):
    """Merge new imports into existing block, avoiding obvious duplicates."""
    if not existing:
        return new_code
    existing_lines = existing.strip().splitlines()
    merged = list(existing_lines)
    new_lines = []
    for line in new_code.strip().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            new_lines.append(line)
            continue
        if not line.startswith("import ") and not line.startswith("from "):
            new_lines.append(line)
            continue
        new_lines.append(line)
    for new_line in new_lines:
        if not new_line:
            continue
        if not new_line.startswith("import ") and not new_line.startswith("from "):
            continue
        if _is_duplicate(merged, new_line):
            continue
        merged.append(new_line)
        if new_line.startswith("from "):
            merged = _dedupe_from_imports(merged)
    return "\n".join(merged)


def _is_duplicate(existing_lines, new_line):
    new_name = _extract_name(new_line)
    if not new_name:
        return False
    for line in existing_lines:
        if line.strip() == new_line:
            return True
        existing_name = _extract_name(line)
        if existing_name and existing_name == new_name:
            return True
    return False


def _extract_name(line):
    line = line.strip()
    if line.startswith("import "):
        rest = line[len("import "):].strip()
        return rest.split()[0] if rest else None
    if line.startswith("from "):
        rest = line[len("from "):].strip()
        module = rest.split()[0] if rest else None
        return module.split(".")[0] if module else None
    return None


def _dedupe_from_imports(existing_lines):
    by_module = {}
    for line in existing_lines:
        module = _extract_name(line)
        if not module:
            continue
        if module not in by_module:
            by_module[module] = []
        by_module[module].append(line)
    result = []
    for module, lines in by_module.items():
        result.extend(lines)
    return result
