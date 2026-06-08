# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: MovieQueue
class Movie:
    def __init__(self, title, genre, priority=1, rating=None):
        self.title = title
        self.genre = genre
        self.priority = priority
        self.rating = rating
        self.history = []

    def add_view(self, date, duration_minutes):
        self.history.append({"date": date, "duration_minutes": duration_minutes})

def validate_input(title, genre, priority, rating):
    if not title or len(title.strip()) < 2:
        raise ValueError("Название фильма должно быть не пустым и содержать минимум 2 символа.")
    if not isinstance(genre, str) or len(genre.strip()) == 0:
        raise ValueError("Жанр должен быть непустой строкой.")
    if not isinstance(priority, int) or priority < 1 or priority > 10:
        raise ValueError("Приоритет должен быть целым числом от 1 до 10.")
    if rating is not None and (not isinstance(rating, (int, float)) or rating < 0 or rating > 10):
        raise ValueError("Оценка должна быть числом от 0 до 10 или None.")
    return Movie(title.strip(), genre.strip(), priority, rating)
