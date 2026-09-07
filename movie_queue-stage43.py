# === Stage 43: Добавь пагинацию длинных списков ===
# Project: MovieQueue
def render_paginated_table(self, items, max_rows=20):
        if not items:
            return "Список пуст."
        total = len(items)
        if total <= max_rows:
            return self.render_table(items)
        page = items[:max_rows]
        remaining = total - max_rows
        return (
            f"Показано {max_rows} из {total} фильмов/сериалов.\n"
            f"Страница 1 из {math.ceil(total / max_rows)}.\n\n"
            f"--- Страница 1 ---\n"
            + self.render_table(page)
            + f"\n\nОсталось {remaining} записей."
        )
