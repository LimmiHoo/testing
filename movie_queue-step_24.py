# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: MovieQueue
def print_movie_record(record):
    """Компактный вывод одной записи: название, жанры, оценка, просмотрено."""
    title = record.get("title", "Без названия")
    genres = ", ".join(record["genres"]) if isinstance(record.get("genres"), list) else str(record.get("genres"))
    rating = f"{record['rating']:.1f}" if not record.get("rating") else ""
    status = record.get("status", "?").upper()

    lines = [f"  🎬 {title}"]
    if genres:
        lines.append(f"      Жанр(ы): {genres}")
    if rating:
        lines.append(f"      Оценка: {rating}/10")
    watched_count = record.get("watched_count", 0)
    total_episodes = record.get("total_episodes", 1)
    progress = f"{watched_count}/{total_episodes}" if total_episodes else "∞"
    lines.append(f"      Просмотрено: {progress} эпизодов [{status}]")

    print("\n".join(lines))


def demo_queue():
    """Демо-запуск: добавляем 2 записи, показываем список и детали."""
    movie1 = {"title": "Интерстеллар", "genres": ["Научная фантастика"], "rating": 8.6}
    movie2 = {"title": "Офис (US)", "genres": ["Комедия", "Драма"], "rating": 9.0, "status": "completed"}

    queue = [movie1, movie2]
    print("=== Текущий список ===")
    for rec in queue:
        print_movie_record(rec)

    print("\n=== Детальная запись (Интерстеллар) ===")
    print_movie_record(movie1)
