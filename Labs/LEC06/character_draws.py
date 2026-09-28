from pico2d import *
import math

open_canvas(800, 600)

character = load_image('character.png')

MOVE_DELAY = 0.02

LEFT = 50
RIGHT = 750
TOP = 550
BOTTOM = 50

TRIANGLE_LEFT = 100
TRIANGLE_RIGHT = 700
TRIANGLE_TOP = 100
TRIANGLE_BOTTOM = 500


def move_character(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(MOVE_DELAY)


def move_circle():
    center_x = 350
    center_y = 300
    radius = 200

    for degree in range(0, 360, 5):
        theta = math.radians(degree)
        x = center_x + radius * math.cos(theta)
        y = center_y + radius * math.sin(theta)
        move_character(x, y)


def move_rectangle():
    for x in range(LEFT, RIGHT + 1, 5):
        move_character(x, TOP)

    for y in range(TOP, BOTTOM - 1, -5):
        move_character(RIGHT, y)

    for x in range(RIGHT, LEFT - 1, -5):
        move_character(x, BOTTOM)

    for y in range(BOTTOM, TOP + 1, 5):
        move_character(LEFT, y)


def move_triangle():
    for x in range(TRIANGLE_LEFT, TRIANGLE_RIGHT + 1, 5):
        move_character(x, TRIANGLE_TOP)

    for x in range(TRIANGLE_RIGHT, 399, -5):
        y = TRIANGLE_TOP + (TRIANGLE_BOTTOM - TRIANGLE_TOP) * (TRIANGLE_RIGHT - x) / 300
        move_character(x, y)

    for x in range(400, TRIANGLE_LEFT - 1, -5):
        y = TRIANGLE_BOTTOM - (TRIANGLE_BOTTOM - TRIANGLE_TOP) * (400 - x) / 300
        move_character(x, y)


def main():
    while True:
        move_circle()
        move_rectangle()
        move_triangle()


main()

close_canvas()