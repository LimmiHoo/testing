# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: MovieQueue
import sys

def _colorize(text, code):
    return f"\033[{code}m{text}\033[0m"

def _set_color(enabled):
    """Toggle ANSI support for the current terminal."""
    if not sys.stdout.isatty():
        return False
    try:
        import curses
        curses.setupterm()
        return True
    except Exception:
        return False

def _init_colors():
    """Initialize color constants for terminal output."""
    global _COLORS
    _COLORS = {
        "red": _colorize,
        "green": _colorize,
        "yellow": _colorize,
        "blue": _colorize,
        "magenta": _colorize,
        "cyan": _colorize,
        "white": _colorize,
        "black": _colorize,
    }
    return _COLORS

def _reset_color():
    """Reset terminal color to default."""
    return "\033[0m"

def _set_color_fg(color):
    """Set foreground color."""
    return f"\033[3{color}m"

def _set_color_bg(color):
    """Set background color."""
    return f"\033[4{color}m"

def _set_bold():
    """Enable bold text."""
    return "\033[1m"

def _set_italic():
    """Enable italic text."""
    return "\033[3m"

def _set_underline():
    """Enable underline."""
    return "\033[4m"

def _set_dim():
    """Enable dim text."""
    return "\033[2m"

def _set_hidden():
    """Enable hidden text."""
    return "\033[8m"

def _set_strikethrough():
    """Enable strikethrough."""
    return "\033[9m"

def _set_reset():
    """Reset all text formatting."""
    return "\033[0m"

def _set_default():
    """Set default text color."""
    return "\033[39m"
