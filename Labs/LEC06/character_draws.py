from pico2d import *

open_canvas(800, 600)

character = load_image('character.png')


def move_character(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.05)


def move_circle():
    print('CIRCLE')

    for degree in range(0, 360, 5):
        print(degree)


move_circle()

close_canvas()