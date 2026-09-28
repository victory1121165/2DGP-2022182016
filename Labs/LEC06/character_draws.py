from pico2d import *

open_canvas(800, 600)

character = load_image('character.png')


def move_character(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.05)


move_character(400, 300)

delay(2)

close_canvas()