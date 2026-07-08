# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: MovieQueue
def add_tags(queue, tag):
    """Добавить тег к фильму/сериалу."""
    item = queue.find_item(tag)
    if item:
        item.tags.add(tag)
        return True
    else:
        print(f"Не найдено: {tag}")
        return False

def remove_tags(queue, tag):
    """Удалить тег из фильма/сериала."""
    item = queue.find_item(tag)
    if item and tag in item.tags:
        item.tags.discard(tag)
        return True
    else:
        print(f"Не найдено или тег {tag} уже отсутствует")
        return False

def list_tags(queue):
    """Вывести все уникальные теги."""
    seen = set()
    for item in queue.items:
        for t in item.tags:
            if t not in seen:
                print(t)
                seen.add(t)
