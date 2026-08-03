# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: MovieQueue
def undo_last_action():
    """Откат последнего действия в истории MovieQueue."""
    global _history, _action_counter
    
    if not _history:
        print("Нет действий для отката.")
        return
    
    last_entry = _history.pop()
    print(f"Отменено действие: {last_entry['type']}")
    
    # Восстанавливаем состояние из предыдущего действия (если есть)
    if len(_history) > 0:
        previous_state = _history[-1].get('state', {})
        state.update(previous_state)
    else:
        print("Внимание: после отката не осталось сохранённых состояний.")
