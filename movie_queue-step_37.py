# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: MovieQueue
import unittest


class TestMovieQueue(unittest.TestCase):
    def test_add_movie(self):
        from movie_queue import MovieQueue
        mq = MovieQueue()
        mq.add_movie("Interstellar", genre="Sci-Fi", priority=10, rating=9.0)
        self.assertEqual(mq.movies[0]["title"], "Interstellar")
        self.assertEqual(mq.movies[0]["priority"], 10)
        self.assertEqual(mq.movies[0]["rating"], 9.0)
        self.assertEqual(mq.movies[0]["genre"], "Sci-Fi")

    def test_add_multiple_movies(self):
        from movie_queue import MovieQueue
        mq = MovieQueue()
        mq.add_movie("Inception", genre="Sci-Fi", priority=5, rating=8.5)
        mq.add_movie("The Matrix", genre="Action", priority=8, rating=8.0)
        mq.add_movie("Titanic", genre="Drama", priority=3, rating=7.5)
        self.assertEqual(len(mq.movies), 3)
        self.assertEqual(mq.movies[0]["title"], "Inception")
        self.assertEqual(mq.movies[2]["title"], "Titanic")

    def test_add_series(self):
        from movie_queue import MovieQueue
        mq = MovieQueue()
        mq.add_series("Breaking Bad", genre="Drama", priority=9, rating=9.5)
        self.assertEqual(mq.series[0]["title"], "Breaking Bad")
        self.assertEqual(mq.series[0]["priority"], 9)
        self.assertEqual(mq.series[0]["rating"], 9.5)

    def test_add_multiple_series(self):
        from movie_queue import MovieQueue
        mq = MovieQueue()
        mq.add_series("Game of Thrones", genre="Fantasy", priority=7, rating=8.8)
        mq.add_series("Stranger Things", genre="Sci-Fi", priority=8, rating=8.7)
        self.assertEqual(len(mq.series), 2)
        self.assertEqual(mq.series[0]["title"], "Game of Thrones")
        self.assertEqual(mq.series[1]["title"], "Stranger Things")

    def test_get_movie_by_title(self):
        from movie_queue import MovieQueue
        mq = MovieQueue()
        mq.add_movie("Interstellar", genre="Sci-Fi", priority=10, rating=9.0)
        movie = mq.get_movie("Interstellar")
        self.assertIsNotNone(movie)
        self.assertEqual(movie["title"], "Interstellar")

    def test_get_movie_not_found(self):
        from movie_queue import MovieQueue
        mq = MovieQueue()
        movie = mq.get_movie("NonExistentMovie")
        self.assertIsNone(movie)

    def test_get_series_by_title(self):
        from movie_queue import MovieQueue
        mq = MovieQueue()
        mq.add_series("Breaking Bad", genre="Drama", priority=9, rating=9.5)
        series = mq.get_series("Breaking Bad")
        self.assertIsNotNone(series)
        self.assertEqual(series["title"], "Breaking Bad")

    def test_get_series_not_found(self):
        from movie_queue import MovieQueue
