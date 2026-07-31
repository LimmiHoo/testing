# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: MovieQueue
def switch_user():
    """Переключение активного пользователя."""
    global active_user, user_profiles
    
    if not user_profiles:
        print("Нет сохранённых профилей.")
        return
    
    if not active_user:
        print("Выберите профиль:")
        for i, name in enumerate(user_profiles):
            print(f"  {i+1}. {name}")
        
        choice = input("> ")
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(user_profiles):
                active_user = user_profiles[idx]
                print(f"\nПрофиль '{active_user}' активен.")
            else:
                print("Неверный выбор.")
        except ValueError:
            print("Введите номер профиля.")
    
    elif active_user:
        print(f"Текущий профиль: {active_user}")
        print("\nВыберите другой профиль:")
        for i, name in enumerate(user_profiles):
            if name != active_user:
                print(f"  {i+1}. {name}")
        
        choice = input("> ")
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(user_profiles):
                active_user = user_profiles[idx]
                print(f"\nПереключено на '{active_user}'.")
            else:
                print("Неверный выбор.")
        except ValueError:
            print("Введите номер профиля.")
