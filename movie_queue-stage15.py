# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: MovieQueue
def get_weekly_stats(history: list[dict]) -> dict[str, int]:
    from datetime import date, timedelta
    stats = {}
    today = date.today()
    for entry in history:
        d = date.fromisoformat(entry['date'])
        week_start = (d - timedelta(days=d.weekday())).isoformat()
        key = f"{entry.get('title', 'unknown')}:{week_start}"
        stats[key] = stats.get(key, 0) + entry.get('minutes', 0)
    return stats
