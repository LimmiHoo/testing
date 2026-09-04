# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: MovieQueue
def dry_run(action, *args, **kwargs):
    """Return a dry-run result dict without mutating state.
    Works for add, update, delete, and history queries.
    """
    return {
        "mode": "dry-run",
        "action": action,
        "args": args,
        "kwargs": kwargs,
        "success": False,
        "detail": "No state to simulate; use with a real MovieQueue to see live results.",
    }
