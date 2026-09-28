from pico2d import *
import math

open_canvas(800, 600)

character = load_image('character.png')


def move_character(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.03)


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


def move_rectangle():
    print('RECTANGLE')


move_circle()
move_rectangle()

close_canvas()