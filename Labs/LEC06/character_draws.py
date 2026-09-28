from pico2d import *
import math

open_canvas(800, 600)

character = load_image('character.png')

MOVE_DELAY = 0.03

LEFT = 50
RIGHT = 750
TOP = 550
BOTTOM = 50


def move_character(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(MOVE_DELAY)


def move_circle():
    print('CIRCLE')

    center_x = 400
    center_y = 300
    radius = 200

    for degree in range(0, 360, 5):
        theta = math.radians(degree)

        x = center_x + radius * math.cos(theta)
        y = center_y + radius * math.sin(theta)

        move_character(x, y)


def move_top():
    print('TOP')

    for x in range(LEFT, RIGHT + 1, 5):
        move_character(x, TOP)


def move_right():
    print('RIGHT')

    for y in range(TOP, BOTTOM - 1, -5):
        move_character(RIGHT, y)


def move_bottom():
    print('BOTTOM')

    for x in range(RIGHT, LEFT - 1, -5):
        move_character(x, BOTTOM)


def move_left():
    print('LEFT')

    for y in range(BOTTOM, TOP + 1, 5):
        move_character(LEFT, y)


def move_rectangle():
    print('RECTANGLE')

    move_top()
    move_right()
    move_bottom()
    move_left()


def move_triangle():
    print('TRIANGLE')

    for x in range(100, 701, 5):
        y = 100
        move_character(x, y)

    for x in range(700, 399, -5):
        y = 100 + (700 - x) * 400 / 300
        move_character(x, y)

    for x in range(400, 99, -5):
        y = 500 - (400 - x) * 400 / 300
        move_character(x, y)


move_circle()
move_rectangle()
move_triangle()

close_canvas()