# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: MovieQueue
def generate_summary(queue):
    if not queue:
        return "Список пуст."
    
    total = len(queue)
    watched_count = sum(1 for item in queue if item.get('watched'))
    avg_rating = sum(item.get('rating', 0) for item in queue if item.get('rating')) / max(sum(1 for i in queue if i.get('rating')), 1) or 0
    
    genres_counts = {}
    priority_items = []
    
    for item in queue:
        genre = item.get('genre', 'Неизвестно')
        genres_counts[genre] = genres_counts.get(genre, 0) + 1
        
        if not item.get('watched'):
            priority_items.append(f"{item['title']} (Приоритет: {item.get('priority', 'Низкий')})")
    
    summary_lines = [
        f"Всего записей: {total}",
        f"Просмотрено: {watched_count}/{total}",
        f"Средняя оценка: {avg_rating:.1f}/5",
        "",
        "Жанры:",
    ]
    
    for genre, count in sorted(genres_counts.items(), key=lambda x: x[1], reverse=True):
        summary_lines.append(f"  - {genre}: {count}")
    
    if priority_items:
        summary_lines.extend(["", "В приоритете (не просмотрено):"])
        for item in priority_items[:5]:
            summary_lines.append(f"  * {item}")
        
        if len(priority_items) > 5:
            summary_lines.append(f"  ... и еще {len(priority_items) - 5} записей")
    
    return "\n".join(summary_lines)
