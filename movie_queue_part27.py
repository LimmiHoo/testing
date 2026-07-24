# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: MovieQueue
def reset_demo_data():
    """Заполняет MovieQueue демо-данными для обучения."""
    queue = []
    for item in [
        {"title": "Inception", "type": "movie", "priority": 3, "rating": None, "genres": ["Sci-Fi"], "watched": False},
        {"title": "Breaking Bad", "type": "series", "priority": 2, "rating": None, "genres": ["Drama"], "watched": False},
        {"title": "The Matrix", "type": "movie", "priority": 1, "rating": None, "genres": ["Sci-Fi", "Action"], "watched": False},
    ]:
        queue.append(item)
    return queue

def clear_state():
    """Полностью очищает MovieQueue и историю просмотра."""
    return {"queue": [], "history": []}
