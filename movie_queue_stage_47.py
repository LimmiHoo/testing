# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: MovieQueue
def demo():
    print("=" * 50)
    print("MovieQueue — Демо: основной сценарий")
    print("=" * 50)

    # --- Создание каталога с фильмами ---
    catalog = MovieCatalog()
    catalog.add("Inception", genre="Sci-Fi", priority=3, rating=4.8, watched=False)
    catalog.add("The Godfather", genre="Crime", priority=2, rating=4.9, watched=False)
    catalog.add("Spirited Away", genre="Animation", priority=1, rating=4.7, watched=True)
    catalog.add("Interstellar", genre="Sci-Fi", priority=2, rating=4.6, watched=False)
    catalog.add("The Dark Knight", genre="Action", priority=3, rating=4.8, watched=True)
    catalog.add("Parasite", genre="Thriller", priority=1, rating=4.7, watched=False)

    print(f"\n[1] Всего фильмов: {len(catalog)}")
    print(f"    Жанры: {sorted(set(f.genre for f in catalog.values()))}")

    # --- Фильтрация по жанру ---
    sci_fi = [f for f in catalog.values() if f.genre == "Sci-Fi"]
    print(f"\n[2] Фильмы жанра 'Sci-Fi': {len(sci_fi)}")
    for f in sci_fi:
        print(f"    — {f.title} (приоритет={f.priority}, оценка={f.rating})")

    # --- Получение списка на просмотр (не просмотренные, с приоритетом >= 2) ---
    to_watch = [f for f in catalog.values() if not f.watched and f.priority >= 2]
    to_watch.sort(key=lambda f: f.priority, reverse=True)
    print(f"\n[3] Список на просмотр (приоритет >= 2):")
    for i, f in enumerate(to_watch, 1):
        print(f"    {i}. {f.title} [{f.genre}] — оценка {f.rating}")

    # --- Просмотр фильма и обновление статуса ---
    chosen = to_watch[0]
    print(f"\n[4] Выбираю: {chosen.title}")
    chosen.watched = True
    chosen.rating = 5.0
    chosen.history.append(f"Просмотр {chosen.title} — оценка 5.0")
    print(f"    Статус: просмотрен, оценка обновлена до {chosen.rating}")
    print(f"    История: {chosen.history}")

    # --- Статистика ---
    total = len(catalog)
    watched_count = sum(1 for f in catalog.values() if f.watched)
    avg_rating = sum(f.rating for f in catalog.values() if f.watched) / max(watched_count, 1)
    print(f"\n[5] Статистика:")
    print(f"    Просмотрено: {watched_count}/{total}")
    print(f"    Средняя оценка просмотренных: {avg_rating:.2f}")

    # --- Поиск по ключевому слову ---
    search_term = "Sci"
    results = [f for f in catalog.values() if search_term.lower() in f.title.lower() or search_term.lower() in f.genre.lower()]
    print(f"\n[6] Поиск по '{search_term}': найдено {len(results)}")
    for f in results:
        print(f"    — {f.title} ({f.genre})")

    # --- Топ-3 фильма по оценке ---
    top3 = sorted(catalog.values(), key=lambda f: f.rating, reverse=True)[:3]
    print(f"\n[7] Топ-3 по оценке:")
    for i, f in enumerate(top3, 1):
        print(f"    {i}. {f.title} — {f.rating}")

    print("\n" + "=" * 50)
    print("Демо завершена успешно! ✅")
    print("=" * 50)
