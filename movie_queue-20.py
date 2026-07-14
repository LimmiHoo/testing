# === Stage 20: Добавь восстановление записей из архива ===
# Project: MovieQueue
def restore_from_archive(filename):
    records = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = line.split(';')
            record = {
                'title': parts[0],
                'priority': int(parts[1]),
                'rating': float(parts[2]),
                'genre': parts[3],
                'watched': parts[4].lower() == 'true',
                'history': json.loads(parts[5]) if len(parts) > 5 else [],
            }
            records.append(record)
    return records

if __name__ == '__main__':
    print("Restore from archive feature implemented.")
