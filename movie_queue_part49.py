# === Stage 49: Добавь финальную самопроверку приложения и отчёт о готовности ===
# Project: MovieQueue
def self_check():
    print("=== Самопроверка MovieQueue ===")
    assert "movies" in dir() or "movies" in globals(), "movies не определён"
    assert "queue" in dir() or "queue" in globals(), "queue не определён"
    if hasattr(globals(), "movies"):
        print(f"✓ movies: {len(globals()['movies'])} фильмов в списке")
    if hasattr(globals(), "queue"):
        print(f"✓ queue: {len(globals()['queue'])} элементов в очереди")
    if hasattr(globals(), "ratings"):
        print(f"✓ ratings: {len(globals()['ratings'])} оценок записано")
    if hasattr(globals(), "history"):
        print(f"✓ history: {len(globals()['history'])} записей просмотра")
    if hasattr(globals(), "genres"):
        print(f"✓ genres: {len(globals()['genres'])} жанров")
    if hasattr(globals(), "priorities"):
        print(f"✓ priorities: {len(globals()['priorities'])} приоритетов")
    print("=== Проверка завершена успешно ===")

self_check()
