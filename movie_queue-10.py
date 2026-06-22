# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: MovieQueue
def export_to_json(queue_data):
    import json
    return json.dumps(queue_data, ensure_ascii=False, indent=2)
