# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: MovieQueue
def _compute_viewed_avg(item):
    """Return the average rating of an item's viewed entries, or None if none viewed."""
    if item["viewed"] == 0:
        return None
    return sum(item["ratings"][:item["viewed"]]) / item["viewed"]

def _get_next_priority():
    """Return the next auto-incremented priority number."""
    return _priority_counter + 1

def _reset_counters():
    """Reset the priority and ID counters to their initial values."""
    global _priority_counter, _id_counter
    _priority_counter = 0
    _id_counter = 0
