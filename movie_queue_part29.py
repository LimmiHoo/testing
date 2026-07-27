# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: MovieQueue
APP_CONFIG = {
    "app_name": "MovieQueue",
    "version": "1.0.29",
    "default_priority": 5,
    "max_history_entries": 100,
    "genres": [
        "action", "comedy", "drama", "horror", "sci-fi", "thriller",
        "romance", "fantasy", "adventure", "documentary"
    ],
    "rating_scale": (1.0, 5.0),
    "language": "ru"
}


def get_config(key=None):
    if key is None:
        return APP_CONFIG.copy()
    return APP_CONFIG.get(key, APP_CONFIG["genres"] if isinstance(key, str) and not any(c.isdigit() for c in key) else None)


def set_config(**kwargs):
    """Update APP_CONFIG with new values; returns the updated config."""
    global APP_CONFIG
    APP_CONFIG.update(kwargs)
    return APP_CONFIG.copy()
