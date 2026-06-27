# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: MovieQueue
class MovieQueue:
    def __init__(self):
        self.movies = []

    def add_movie(self, title, genre, priority=0, rating=None, watched=False, history=""):
        movie = {
            "title": title.lower(),
            "genre": genre.lower(),
            "priority": int(priority),
            "rating": float(rating) if rating else None,
            "watched": bool(watched),
            "history": history
        }
        self.movies.append(movie)

    def search_movies(self, query):
        query = query.lower()
        results = []
        for movie in self.movies:
            match_title = query in movie["title"]
            match_genre = query in movie["genre"]
            if match_title or match_genre:
                result_movie = {k: v for k, v in movie.items() if k != "title"}
                result_movie["title"] = movie["title"].replace(query, query.capitalize())
                results.append(result_movie)
        return results

    def get_movies(self):
        sorted_movies = sorted(
            self.movies,
            key=lambda m: (m["priority"], m.get("rating", 0)),
            reverse=True
        )
        for i, movie in enumerate(sorted_movies, 1):
            print(f"{i}. {movie['title']} [{movie['genre']}] | Приоритет: {movie['priority']}")
