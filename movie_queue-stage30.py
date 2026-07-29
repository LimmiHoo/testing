# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: MovieQueue
class User:
    def __init__(self, name):
        self.name = name
        self.queue = []
        self.history = []

def add_user(name):
    return User(name)
