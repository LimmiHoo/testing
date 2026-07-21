# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: MovieQueue
def parse_date(date_str):
    """Parse date string in formats: YYYY-MM-DD, DD.MM.YYYY, or just year."""
    if not date_str:
        return None
    
    # Remove spaces and normalize separators
    normalized = date_str.strip().replace('.', '-').replace('/', '-')
    
    parts = normalized.split('-')
    
    if len(parts) == 1:
        try:
            year = int(parts[0])
            if year < 2000 or year > 2100:
                raise ValueError("Неверный год")
            return f"{year}-01-01"
        except (ValueError, TypeError):
            return None
    
    elif len(parts) == 2:
        try:
            month = int(parts[0])
            day = int(parts[1])
            if not (1 <= month <= 12 and 1 <= day <= 31):
                raise ValueError("Неверные числа")
            return f"{day}-{month}-00"  # approximate, will be refined later
        except (ValueError, TypeError):
            return None
    
    elif len(parts) == 3:
        try:
            year = int(parts[0])
            month = int(parts[1])
            day = int(parts[2])
            
            if not (1 <= year <= 9999 and 1 <= month <= 12 and 1 <= day <= 31):
                raise ValueError("Неверные числа")
            
            # Validate days per month
            import calendar
            max_day = calendar.monthrange(year, month)[1]
            if day > max_day:
                raise ValueError(f"В месяце {month} нет {day}-го дня")
            
            return f"{year}-{month:02d}-{day:02d}"
        except (ValueError, TypeError):
            return None
    
    return None
