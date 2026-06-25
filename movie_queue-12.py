# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: MovieQueue
def load_from_json(filepath):
    try:
        import json
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list):
            queue.extend(data)
            print(f"Загружено {len(data)} элементов из '{filepath}'")
        else:
            raise ValueError("Формат JSON должен быть списком объектов.")
    except FileNotFoundError:
        print(f"Ошибка: файл '{filepath}' не найден.")
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON в '{filepath}': {e}")
    except Exception as e:
        print(f"Неожиданная ошибка при загрузке файла: {type(e).__name__}: {e}")
