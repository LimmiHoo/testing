# === Stage 17: Добавь группировку записей по категориям ===
# Project: MovieQueue
from collections import defaultdict

def group_by_category(records):
    grouped = defaultdict(list)
    for record in records:
        category = record.get('category', 'Other') or 'Other'
        grouped[category].append(record)
    return dict(sorted(grouped.items(), key=lambda x: len(x), reverse=True))
