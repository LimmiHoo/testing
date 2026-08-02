# === Stage 32: Добавь журнал действий пользователя ===
# Project: MovieQueue
class HistoryLog:
    def __init__(self):
        self._log = []
    
    def add(self, action_type, details=None):
        entry = {"time": datetime.now().strftime("%H:%M:%S"), "type": action_type}
        if details:
            entry["details"] = details
        self._log.append(entry)

    def get_history(self):
        return list(self._log)

history_log = HistoryLog()
