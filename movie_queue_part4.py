# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: MovieQueue
def edit_movie_queue_item(movie_id: int, updates: dict) -> bool:
    if not isinstance(updates, dict):
        raise ValueError("Updates must be a dictionary")
    
    for key in ["title", "genre", "rating", "priority"]:
        if key in updates and updates[key] is None:
            del updates[key]

    try:
        index = next((i for i, item in enumerate(movie_queue) if item["id"] == movie_id), -1)
        if index < 0:
            raise ValueError(f"Movie with id {movie_id} not found")
        
        updated_item = dict(movie_queue[index])
        updated_item.update({k: v for k, v in updates.items() if k in updated_item})
        movie_queue[index] = updated_item
        
        history_entry = {"action": "edit", "id": movie_id, "timestamp": datetime.now(), "changes": list(updates.keys())}
        watch_history.append(history_entry)
        
        return True
    except Exception as e:
        print(f"Error editing item {movie_id}: {e}")
        return False
