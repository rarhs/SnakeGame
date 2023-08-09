## game.py
import curses
import random

class Game:
    def __init__(self, width: int, height: int):
        self.score = 0
        self.width = width
        self.height = height
        self.snake_x = width // 2
        self.snake_y = height // 2
        self.food_x = random.randint(1, width - 2)
        self.food_y = random.randint(1, height - 2)
        self.direction_x = 0
        self.direction_y = 0
        self.snake_body = []
        self.game_over = False
        self.game_window = curses.newwin(height, width, 0, 0)
        self.game_window.timeout(100)

    def init_game(self):
        curses.initscr()
        curses.curs_set(0)
        curses.start_color()
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        self.game_window.keypad(1)
        self.game_window.border(0)
        self.game_window.nodelay(1)

    def draw_border(self):
        self.game_window.border(0)

    def draw_snake(self):
        self.game_window.addch(self.snake_y, self.snake_x, curses.ACS_CKBOARD)

    def draw_food(self):
        self.game_window.addch(self.food_y, self.food_x, curses.ACS_DIAMOND)

    def update_snake(self):
        self.snake_x += self.direction_x
        self.snake_y += self.direction_y
        self.snake_body.insert(0, [self.snake_x, self.snake_y])

        if self.snake_x == self.food_x and self.snake_y == self.food_y:
            self.score += 1
            self.food_x = random.randint(1, self.width - 2)
            self.food_y = random.randint(1, self.height - 2)
        else:
            self.snake_body.pop()

    def check_collision(self):
        if (
            self.snake_x == 0
            or self.snake_x == self.width - 1
            or self.snake_y == 0
            or self.snake_y == self.height - 1
            or [self.snake_x, self.snake_y] in self.snake_body[1:]
        ):
            self.game_over = True

    def update_score(self):
        self.game_window.addstr(0, 2, f"Score: {self.score}")

    def game_loop(self):
        while not self.game_over:
            key = self.game_window.getch()
            if key == curses.KEY_UP:
                self.direction_x = 0
                self.direction_y = -1
            elif key == curses.KEY_DOWN:
                self.direction_x = 0
                self.direction_y = 1
            elif key == curses.KEY_LEFT:
                self.direction_x = -1
                self.direction_y = 0
            elif key == curses.KEY_RIGHT:
                self.direction_x = 1
                self.direction_y = 0

            self.update_snake()
            self.check_collision()

            self.game_window.erase()
            self.draw_border()
            self.draw_snake()
            self.draw_food()
            self.update_score()

            self.game_window.refresh()

    def start(self):
        self.init_game()
        self.game_loop()
