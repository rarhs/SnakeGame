## input_manager.py
import curses

class InputManager:
    def get_key(self) -> int:
        return curses.getch()
