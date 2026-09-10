# === Stage 45: Добавь восстановление из резервной копии ===
# Project: MovieQueue
def restore_from_backup(self, backup_path: str) -> None:
        """Восстановить данные из JSON-резервной копии.

        Формат: [{"id": int, "title": str, "genre": str, "priority": int,
                  "rating": float, "watched": bool, "watch_date": str|None}]
        """
        try:
            with open(backup_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            print(f"[!] Резервная копия не найдена или повреждена: {backup_path}")
            return

        if not data or not isinstance(data, list):
            print("[!] Ошибка: резервная копия должна содержать список фильмов.")
            return

        movies = []
        for item in data:
            if not isinstance(item, dict) or "id" not in item:
                print(f"[!] Пропущена невалидная запись: {item}")
                continue
            movies.append(Movie(id=item["id"], title=item.get("title", ""),
                                genre=item.get("genre", ""), priority=item.get("priority", 0),
                                rating=item.get("rating", 0.0), watched=item.get("watched", False),
                                watch_date=item.get("watch_date", None)))

        self.movies = movies
        self._sort()
        print(f"[+] Восстановлено {len(movies)} фильмов из {backup_path}.")
