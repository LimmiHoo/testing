# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: MovieQueue
import json
from datetime import datetime

class Movie:
    def __init__(self, title, genre, priority=0, rating=None):
        self.title = title
        self.genre = genre
        self.priority = priority
        self.rating = rating
        self.history = []

    def watch(self, duration_minutes):
        self.history.append({
            "date": datetime.now().isoformat(),
            "duration_minutes": duration_minutes
        })

    def rate(self, score):
        if 1 <= score <= 5:
            self.rating = score

class MovieQueue:
    def __init__(self):
        self.movies = []
        self.load_data()

    def add_movie(self, title, genre, priority=0, rating=None):
        movie = Movie(title, genre, priority, rating)
        self.movies.append(movie)
        return movie

    def sort_movies(self):
        self.movies.sort(key=lambda m: m.priority, reverse=True)

    def save_data(self):
        data = {m.title: {"genre": m.genre, "priority": m.priority, "rating": m.rating, "history": m.history} for m in self.movies}
        with open("movie_queue.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load_data(self):
        try:
            with open("movie_queue.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                for title, info in data.items():
                    movie = Movie(title, info["genre"], info["priority"], info.get("rating"))
                    movie.history = info.get("history", [])
                    self.movies.append(movie)
        except FileNotFoundError:
            pass

    def list_movies(self):
        return [f"{i+1}. {m.title} ({m.genre}) - Приоритет: {m.priority}, Оценка: {m.rating}" for i, m in enumerate(self.movies)]

if __name__ == "__main__":
    queue = MovieQueue()
    queue.add_movie("Дюна", "Фантастика", priority=10)
    queue.add_movie("Интерстеллар", "Фантастика", priority=5)
    queue.add_movie("Криминальное чтиво", "Драма", priority=3)
    queue.sort_movies()
    print("Список фильмов:")
    for line in queue.list_movies():
        print(line)
