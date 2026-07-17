# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: MovieQueue
def check_overdue_reminders(queue):
    overdue = []
    for item in queue:
        if item.get('reminder_date') and datetime.now().date() > datetime.strptime(item['reminder_date'], '%Y-%m-%d').date():
            overdue.append({'item': item, 'days_overdue': (datetime.now() - datetime.strptime(item['reminder_date'], '%Y-%m-%d')).days})
    return overdue

if __name__ == '__main__':
    test_queue = [
        {'title': 'Film A', 'reminder_date': '2023-12-01'},
        {'title': 'Series B', 'reminder_date': '2024-06-15'},
        {'title': 'Movie C', 'reminder_date': None},
    ]
    overdue_items = check_overdue_reminders(test_queue)
    if overdue_items:
        print(f"⚠️  Просрочено напоминаний: {len(overdue_items)}")
        for o in overdue_items:
            print(f"   - {o['item']['title']} (просрочено на {o['days_overdue']} дней)")
    else:
        print("✅ Все напоминания в норме или не установлены.")
