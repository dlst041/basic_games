import time
# needed for key capture, can't use keyboard on linux
from curtsies import Input
import random

configs = {
    "board_size": 10,
}
# [x, y]
s_head_pos = [1, 1]
direction = [0, 0]
feed_pos = [3, 3]
snake = [[1, 1]]


def update_food_pos():
    """Update the food position to a new random coordinate, ensure it is not a coordinate currently occupied by the head

    :return:
    """
    global feed_pos
    new_x_pos = random.randint(0, configs['board_size']-1)
    new_y_pos = random.randint(0, configs['board_size']-1)
    if new_x_pos == s_head_pos[0] and new_y_pos == s_head_pos[1]:
        update_food_pos()
    else:
        feed_pos = [new_x_pos, new_y_pos]


def update_pos():
    """Update current coordinate position of snake head.
    Check if the next position will be the food, if so extend the snake.
    Otherwise, update the snake coord list by append the next position and remove the tail coordinate

    Check if the new snake head coordinate will "eat" a coordinate occupied by the rest of the snake
    Check if the snake has moved out of the board game bounds

    :return:
    """
    global snake, s_head_pos, direction
    # if the next position of head is the feed pos, extend snake
    # set the head to be the feed pos
    if [sum(x) for x in zip(s_head_pos, direction)] == feed_pos:
        snake.insert(0, feed_pos)
        s_head_pos = feed_pos
        update_food_pos()
    else:
        s_head_pos = [sum(x) for x in zip(s_head_pos, direction)]
        snake.pop()
        snake.insert(0, s_head_pos)

    # check if snake eats itself
    if s_head_pos in snake[1:len(snake)]:
        print('GAME OVER')
        exit(1)

    # check if out of board game bounds
    if s_head_pos[0] >= configs['board_size'] or s_head_pos[0] < 0:
        print('GAME OVER')
        exit(1)
    elif s_head_pos[1] >= configs['board_size'] or s_head_pos[1] < 0:
        print('GAME OVER')
        exit(1)


def update_direction(key_pressed):
    """Update the movement direction of the snake. Direction used when updating snake position

    :param key_pressed: key code obtained from keyboard
    :return:
    """
    global direction
    if key_pressed == 'KEY_UP':
        direction = [0, -1]
    elif key_pressed == 'KEY_DOWN':
        direction = [0, 1]
    elif key_pressed == 'KEY_LEFT':
        direction = [-1, 0]
    elif key_pressed == 'KEY_RIGHT':
        direction = [1, 0]


def check_key_press():
    """Check if an arrow key has been pressed and update direction
    :return:
    """
    with Input(keynames='curses') as input_generator:
        res = input_generator.send(timeout=1)
        if res:
            update_direction(res)


def draw():
    """Redraw the board, redraw all snake coordinates and feed coordinate
    :return:
    """
    global feed_pos, s_head_pos, snake

    for y in range(0, configs['board_size']):
        row = ''
        for x in range(0, configs['board_size']):
            if [x, y] in snake:
                row += ' X '
            elif [x, y] == feed_pos:
                row += ' O '
            else:
                row += ' _ '

        print(row)


def game():
    """Loop for main game functions

    """
    while 1:
        time.sleep(.2)
        check_key_press()
        update_pos()
        draw()


if __name__ == '__main__':
    game()



