# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: MovieQueue
def remove_item(item_id: int) -> bool:
    if not movies and not series:
        return False
    removed = None
    for collection in [movies, series]:
        for i, item in enumerate(collection):
            if item['id'] == item_id:
                removed = collection.pop(i)
                break
        if removed is not None:
            break
    else:
        return False
    print(f"Удалён: {removed.get('title')}")
    return True

def handle_missing_id(item_id: int, default_collection=None):
    if item_id < 1 or (default_collection and len(default_collection) == 0):
        print("ID отсутствует или коллекция пуста.")
        return None
    for collection in [movies, series]:
        for i, item in enumerate(collection):
            if item['id'] == item_id:
                return item
    return None
