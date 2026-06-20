# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: MovieQueue
import json, ast, sys

def load_initial_data(json_string):
    try:
        raw = json.loads(json_string)
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        return None
    
    if not isinstance(raw, dict):
        print("JSON должен содержать объект (словарь).")
        return None

    movies = raw.get('movies', [])
    history = raw.get('history', [])
    
    # Валидация и нормализация данных
    for m in movies:
        if not isinstance(m, dict):
            print("Ошибка: каждый фильм должен быть словарем.")
            return None
        for key in ['title', 'priority', 'rating']:
            if key not in m or (isinstance(m[key], str) and len(m[key]) == 0):
                print(f"Ошибка: пропущено или пустое поле '{key}' в фильме {m.get('id')}")
                return None
    
    for h in history:
        if not isinstance(h, dict):
            print("Ошибка: каждая запись истории должна быть словарем.")
            return None

    # Преобразование списков из JSON-строк (если они были сохранены как строки)
    def safe_list(s):
        if isinstance(s, str):
            try:
                return ast.literal_eval(s)
            except Exception:
                return []
        return s or []

    movies = [dict(m, genres=safe_list(m.get('genres', '[]'))) for m in movies]
    history = [dict(h, watched_at=safe_list(h.get('watched_at', '[]')), rating=int(safe_list(h.get('rating', 0)))) for h in history]

    return {
        'movies': movies,
        'history': history,
        'total_movies': len(movies),
        'total_history_entries': len(history)
    }
