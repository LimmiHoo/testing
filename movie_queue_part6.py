# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: MovieQueue
class MovieQueue:
    def filter_movies(self, status=None, category=None, tags=None):
        filtered = self.movies.copy()
        if status is not None and status != "all":
            filtered = [m for m in filtered if m.get("status") == status]
        if category is not None and category != "all":
            filtered = [m for m in filtered if m.get("category") == category]
        if tags:
            def has_any_tag(movie):
                movie_tags = set(m.get("tags", []))
                return any(tag in movie_tags for tag in tags)
            filtered = [m for m in filtered if has_any_tag(m)]
        return filtered

    def get_movies_by_status(self, status="watching"):
        return self.filter_movies(status=status)

    def get_movies_by_category(self, category):
        return self.filter_movies(category=category)

    def get_movies_with_tags(self, tags):
        return self.filter_movies(tags=tags)
