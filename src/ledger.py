"""Public offline fixture for testing PDM delivery; no external services."""


def summarize_entries(entries):
    """Group integer cents by normalized category without changing input."""
    result = {}
    for entry in entries:
        category = entry["category"].strip().lower()
        if not category:
            continue
        summary = result.setdefault(category, {"count": 0, "total": 0})
        summary["count"] += 1
        summary["total"] += entry["cents"]
    return result


def category_totals(entries):
    """Sum integer cents by normalized category without changing input."""
    result = {}
    for entry in entries:
        category = entry["category"].strip().lower()
        if not category:
            continue
        result[category] = result.get(category, 0) + entry["cents"]
    return result
