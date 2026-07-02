# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: MovieQueue
def get_monthly_stats(queue: list[dict]) -> dict[str, int]:
    stats = {}
    for item in queue:
        date_str = item.get("watched_at") or item.get("added_at", "")
        if not date_str:
            continue
        try:
            year, month = map(int, date_str[:7].split("-"))
            key = f"{year}-{month}"
            stats[key] = stats.get(key, 0) + 1
        except (ValueError, TypeError):
            pass
    return stats

def print_monthly_summary(stats: dict[str, int]) -> None:
    if not stats:
        print("Статистика за месяц отсутствует.")
        return
    for month in sorted(stats.keys()):
        count = stats[month]
        print(f"{month}: {count} просмотрено")
