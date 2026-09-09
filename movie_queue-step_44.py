# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: MovieQueue
def backup_data_file(path: str, backup_dir: str = "backups") -> str:
    import os, shutil
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"moviequeue_backup_{timestamp}.json")
    shutil.copy2(path, backup_path)
    return backup_path
