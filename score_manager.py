## score_manager.py
class ScoreManager:
    def __init__(self):
        self.score = 0

    def get_score(self) -> int:
        return self.score

    def update_score(self, points: int):
        self.score += points
