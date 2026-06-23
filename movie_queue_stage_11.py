# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: MovieQueue
import json, os

DATA_FILE = "movie_queue.json"

def save_to_json(data):
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except IOError as e:
        print(f"[Ошибка сохранения] {e}")

def load_from_json():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data.get("movies", [])
    except (json.JSONDecodeError, IOError):
        print("[Ошибка чтения] Файл повреждён или недоступен")
        return []

def get_or_create_data():
    existing = load_from_json()
    if not existing:
        save_to_json({"movies": [], "history": []})
    return {"movies": existing, "history": []}
