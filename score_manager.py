## score_manager.py
import curses

class ScoreManager:
    def __init__(self):
        self.score = 0

    def get_score(self) -> int:
        return self.score

    def update_score(self, points: int):
        self.score += points

class GameManager:
    def __init__(self):
        self.game = Game()
        self.input_manager = InputManager()
        self.score_manager = ScoreManager()

    def start_game(self):
        self.game.start()

    def restart_game(self):
        self.game.restart()

class Game:
    def __init__(self):
        self.score_manager = ScoreManager()

    def start(self):
        self.score_manager.update_score(10)
        print(f"Score: {self.score_manager.get_score()}")

    def restart(self):
        self.score_manager.update_score(0)
        print(f"Score: {self.score_manager.get_score()}")

class InputManager:
    def get_key(self) -> int:
        return curses.getch()
