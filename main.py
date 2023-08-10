
import curses
import random

def game(stdscr):
    curses.curs_set(0)
    height, width = 20, 80
    snake_x, snake_y = width // 2, height // 2
    food_x, food_y = random.randint(1, width - 2), random.randint(1, height - 2)
    snake_body = [[snake_x, snake_y]]
    direction_x, direction_y = 0, 0
    score = 0

    # Create a new window
    win = curses.newwin(height, width, 0, 0)
    win.keypad(1)
    win.timeout(100)
    win.border(0)

    # Game loop
    while True:
        key = win.getch()

        if key == curses.KEY_UP:
            direction_x, direction_y = 0, -1
        elif key == curses.KEY_DOWN:
            direction_x, direction_y = 0, 1
        elif key == curses.KEY_LEFT:
            direction_x, direction_y = -1, 0
        elif key == curses.KEY_RIGHT:
            direction_x, direction_y = 1, 0

        snake_x += direction_x
        snake_y += direction_y

        # Collision with food
        if snake_x == food_x and snake_y == food_y:
            food_x, food_y = random.randint(1, width - 2), random.randint(1, height - 2)
            score += 1
        else:
            snake_body.pop()

        # Insert new head segment
        snake_body.insert(0, [snake_x, snake_y])

        # Draw the snake
        win.clear()
        win.border(0)
        for segment in snake_body:
            win.addch(segment[1], segment[0], curses.ACS_CKBOARD)
        win.addch(food_y, food_x, curses.ACS_DIAMOND)

        # Collision with wall or self
        if (snake_x < 1 or snake_x >= width - 1 or
            snake_y < 1 or snake_y >= height - 1 or
            [snake_x, snake_y] in snake_body[1:]):
            break

        win.refresh()

if __name__ == "__main__":
    curses.wrapper(game)
