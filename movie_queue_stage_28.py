# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: MovieQueue
def print_metrics(movies, watched_history):
    total = len(movies)
    watched_ids = {w["id"] for w in watched_history}
    watched_count = sum(1 for m in movies if m["id"] in watched_ids)
    avg_rating = (sum(m.get("rating", 0) for m in movies) / total) if total else 0.0
    genre_counts = {}
    priority_counts = {"high": 0, "medium": 0, "low": 0}
    for m in movies:
        g = m.get("genre", "Unknown")
        genre_counts[g] = genre_counts.get(g, 0) + 1
        p = m.get("priority", "medium")
        priority_counts[p] += 1
    print(f"Total titles: {total}")
    print(f"Watched: {watched_count} / {total}")
    print(f"Avg rating: {avg_rating:.2f}")
    print(f"Genre distribution:")
    for g, c in sorted(genre_counts.items(), key=lambda x: -x[1]):
        print(f"  {g}: {c}")
    print("Priority distribution:")
    for p, c in priority_counts.items():
        print(f"  {p}: {c}")
