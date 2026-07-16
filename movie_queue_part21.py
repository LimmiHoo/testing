# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: MovieQueue
def add_reminder(reminder_id, message, due_date):
    reminders = {
        "watch_movie": {"message": "Watch 'Inception' (priority 5)", "due_date": "2024-12-31"},
        "read_book": {"message": "Read Chapter 3 of Python Cookbook", "due_date": "2024-12-15"}
    }
    reminders[reminder_id] = {"message": message, "due_date": due_date}
    return reminders

def check_reminders(reminders):
    today = "2024-12-31"
    overdue = []
    for rid, r in reminders.items():
        if r["due_date"] <= today:
            overdue.append(f"[{rid}] {r['message']} — due on {r['due_date']}")
    return overdue

def get_reminders_status(reminders):
    status = {"total": len(reminders), "overdue": 0, "upcoming": 0}
    today = "2024-12-31"
    for r in reminders.values():
        if r["due_date"] <= today:
            status["overdue"] += 1
        else:
            status["upcoming"] += 1
    return status

reminders = add_reminder("watch_movie", "Watch 'Inception' (priority 5)", "2024-12-31")
print(check_reminders(reminders))
