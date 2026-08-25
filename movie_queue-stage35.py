# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: MovieQueue
def next_action(queue):
    if not queue:
        return {"action": "none", "message": "Список пуст. Добавьте контент."}
    top = queue[0]
    if top["priority"] == "watched":
        return {"action": "review", "message": f"Подошел к просмотру: {top['title']}. Оцените и отметьте."}
    elif top["priority"] == "high":
        return {"action": "watch", "message": f"Высокий приоритет: {top['title']}. Начните просмотр."}
    elif top["priority"] == "medium":
        return {"action": "plan", "message": f"Средний приоритет: {top['title']}. Занесите в план на вечер."}
    else:
        return {"action": "browse", "message": f"Низкий приоритет: {top['title']}. Оставите на потом."}
