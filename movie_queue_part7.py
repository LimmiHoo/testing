# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: MovieQueue
def sort_queue(records, by='date'):
    if not records: return []
    reverse = {'priority': True}.get(by, False)
    key_map = {
        'date': lambda r: (r.get('watched_at') or '').split('T')[0] if isinstance(r.get('watched_at'), str) else 0,
        'priority': lambda r: -r.get('priority', 0),
        'title': lambda r: r.get('title', '')
    }
    key = key_map.get(by, key_map['date'])
    return sorted(records, key=key, reverse=reverse)
