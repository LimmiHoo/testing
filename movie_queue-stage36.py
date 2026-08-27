# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: MovieQueue
def verify_integrity(data):
    if not isinstance(data, dict):
        raise ValueError("Data must be a dictionary")
    if 'movies' not in data or 'series' not in data:
        raise ValueError("Missing 'movies' or 'series' keys")
    if not isinstance(data['movies'], list) or not isinstance(data['series'], list):
        raise ValueError("'movies' and 'series' must be lists")
    for entry in data['movies'] + data['series']:
        if not isinstance(entry, dict):
            raise ValueError("Each entry must be a dictionary")
        for key in ['title', 'priority', 'rating', 'genre']:
            if key not in entry:
                raise ValueError(f"Missing required field: {key}")
        if not isinstance(entry['priority'], (int, float)):
            raise ValueError(f"'priority' must be numeric, got {type(entry['priority'])}")
        if not isinstance(entry['rating'], (int, float)):
            raise ValueError(f"'rating' must be numeric, got {type(entry['rating'])}")
        if not isinstance(entry['genre'], str):
            raise ValueError(f"'genre' must be string, got {type(entry['genre'])}")
        if entry['priority'] < 0 or entry['rating'] < 0:
            raise ValueError("Priority and rating must be non-negative")
    if 'history' not in data:
        data['history'] = []
    if not isinstance(data['history'], list):
        raise ValueError("'history' must be a list")
    return data

def repair_simple_issues(data):
    repaired = {'movies': [], 'series': [], 'history': data.get('history', [])}
    for entry in data.get('movies', []) + data.get('series', []):
        repaired_entry = {'title': entry.get('title', 'Unknown'), 'priority': 0, 'rating': 0, 'genre': 'Uncategorized'}
        if 'priority' in entry:
            repaired_entry['priority'] = max(0, min(entry['priority'], 10))
        if 'rating' in entry:
            repaired_entry['rating'] = max(0, min(entry['rating'], 10))
        if 'genre' in entry:
            repaired_entry['genre'] = str(entry['genre']).strip() or 'Uncategorized'
        repaired_entry['genre'] = repaired_entry['genre'][:100]
        repaired_entry['priority'] = float(repaired_entry['priority'])
        repaired_entry['rating'] = float(repaired_entry['rating'])
        repaired_entry['title'] = str(repaired_entry['title']).strip()
        repaired.append(repaired_entry)
    repaired['movies'] = [e for e in repaired if e['priority'] == 0]
    repaired['series'] = [e for e in repaired if e['priority'] > 0]
    return repaired
