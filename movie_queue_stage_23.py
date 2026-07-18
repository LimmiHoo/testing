# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: MovieQueue
def print_movie_table(movies):
    if not movies:
        print("Нет фильмов в списке.")
        return
    width = 100
    headers = ["#", "Название", "Приоритет", "Оценка", "Жанры"]
    col_w = [width // len(headers)] * len(headers)
    for i, h in enumerate(headers):
        col_w[i] = max(col_w[i], len(h))
    row_fmt = "| {:<" + str(col_w[0]) + "} | {:<" + str(col_w[1]) + "} | {:>4} | {:>4} | {:<30} |"
    print(row_fmt.format(*headers).strip())
    for i, m in enumerate(movies):
        genres = ", ".join(m.get("genre", []))[:28] + "..." if len(genres) > 28 else genres
        row_fmt_data = (i+1, m["title"] or "", m.get("priority", "?"), m.get("rating", "?"), genres)
        print(row_fmt.format(*row_fmt_data).strip())
