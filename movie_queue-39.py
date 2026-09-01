# === Stage 39: Добавь документационную строку с описанием сценариев использования ===
# Project: MovieQueue
def usage_scenarios():
    """
    Демонстрация сценариев использования MovieQueue.
    """
    from movie_queue import MovieQueue

    queue = MovieQueue()

    # Сценарий 1: Добавление и удаление фильмов по приоритету
    queue.add_movie("Interstellar", genre="Sci-Fi", priority="high", rating=4.5)
    queue.add_movie("The Godfather", genre="Crime", priority="medium", rating=5.0)
    queue.add_movie("Paddington 2", genre="Family", priority="low", rating=4.0)
    print("Очередь:", queue.get_queue())

    # Сценарий 2: Просмотр фильма и обновление истории
    movie = queue.get_movie("Interstellar")
    queue.add_to_history(movie, rating=4.0, watched=True)
    print("История:", queue.get_history())

    # Сценарий 3: Фильтрация по жанру
    filtered = queue.get_movies_by_genre("Sci-Fi")
    print("Sci-Fi фильмы:", filtered)

    # Сценарий 4: Поиск по названию
    found = queue.search_movie("Godfather")
    print("Поиск:", found)

    # Сценарий 5: Статистика
    stats = queue.get_stats()
    print("Статистика:", stats)

    # Сценарий 6: Удаление фильма
    queue.remove_movie("Paddington 2")
    print("После удаления:", queue.get_queue())

    # Сценарий 7: Экспорт/импорт
    json_data = queue.to_json()
    queue2 = MovieQueue.from_json(json_data)
    print("Восстановленная очередь:", queue2.get_queue())
