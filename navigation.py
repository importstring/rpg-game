from random import randint, choice

# Handle key presses for navigation
class _Getch:
    def __init__(self):
        try:
            self.impl = _GetchUnix()
        except ImportError:
            self.impl = _GetchWindows()

    def __call__(self):
        return self.impl()

class _GetchUnix:
    def __init__(self):
        import tty, sys, termios

    def __call__(self):
        import sys, tty, termios

        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
            if ch == "\x1b":  # Start of escape sequence
                ch += sys.stdin.read(2)  # Read the next two characters for the escape sequence
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt

        ch = msvcrt.getch()
        if ch == b"\xe0":  # Special key prefix for Windows
            ch += msvcrt.getch()  # Get the actual key code
        return ch

getch = _Getch()

def get_user_input(prompt):
    print(prompt, end='', flush=True)  # Ensure prompt is displayed
    return getch()  # Read and return a single character input
