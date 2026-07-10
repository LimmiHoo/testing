# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: MovieQueue
def archive_movies(archive_date=None):
    if archive_date is None:
        archive_date = datetime.now().date()
    archived = []
    for movie in movies:
        completed = movie.get('completed', False) or movie.get('watched', False)
        added = (archive_date - movie.get('added_date', datetime.now().date())).days > 90
        if completed or added:
            movie['archived'] = True
            archived.append(movie)
    movies = [m for m in movies if not m.get('archived', False)]
    return archived
