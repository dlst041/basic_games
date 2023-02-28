import time
import random
from curtsies import Input


class Snake:
    def __init__(self):
        self.board_size = 10
        self.snake = [[1, 1]]
        self.feed_pos = [3, 3]
        self.direction = [1, 0]
        self.timeout = 0.5
        self.start_game()

    def update_pos(self):

        new_pos = [sum(x) for x in zip(self.snake[0], self.direction)]

        if new_pos == self.feed_pos:
            self.snake.insert(0, new_pos)
            self.feed_pos = [random.randint(0, self.board_size), random.randint(0, self.board_size)]
        else:
            self.snake.insert(0, new_pos)
            self.snake.pop()

        if self.snake[0][0] >= self.board_size or self.snake[0][0] < 0:
            print('GAME OVER')
            exit(1)
        elif self.snake[0][1] >= self.board_size or self.snake[0][1] < 0:
            print('GAME OVER')
            exit(1)

    def draw(self):
        print('\n')
        for y in range(0, self.board_size):
            row = ""
            for x in range(0, self.board_size):
                if [x, y] in self.snake:
                    row += " X "
                elif [x, y] == self.feed_pos:
                    row += " O "
                else:
                    row += " _ "

            print(row)

    def update_direction(self):
        with Input(keynames="curses") as key_input:
            res = key_input.send(timeout=1)
            if res == 'KEY_UP':
                self.direction = [0, -1]
            elif res == 'KEY_DOWN':
                self.direction = [0, 1]
            elif res == 'KEY_LEFT':
                self.direction = [-1, 0]
            elif res == 'KEY_RIGHT':
                self.direction = [1, 0]

    def start_game(self):
        while 1:
            time.sleep(1)
            self.update_pos()
            self.update_direction()
            self.draw()


if __name__ == '__main__':
    s = Snake()
