# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: MovieQueue
class MovieQueue:
    def __init__(self):
        self.movies = []

    def add_movie(self, title, genre, priority, rating=None, watched=False):
        movie = {
            "title": title,
            "genre": genre,
            "priority": priority,
            "rating": rating,
            "watched": watched,
            "added_at": self._get_timestamp()
        }
        self.movies.append(movie)
        return movie

    def _get_timestamp(self):
        import datetime
        return datetime.datetime.now().isoformat()

    def get_next_movie(self):
        if not self.movies:
            return None
        sorted_movies = sorted(
            self.movies,
            key=lambda m: (not m["watched"], m["priority"]),
            reverse=True
        )
        next_movie = sorted_movies[0]
        next_movie["watched"] = True
        next_movie["rating"] = next_movie.get("rating") or 5
        return next_movie
