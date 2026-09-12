# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: MovieQueue
class DataMigration:
    """Handles versioned schema migrations for MovieQueue data structures."""

    SCHEMA_VERSION = 46

    @classmethod
    def migrate(cls, data):
        if cls.SCHEMA_VERSION not in data:
            data[cls.SCHEMA_VERSION] = cls.SCHEMA_VERSION
        return data
