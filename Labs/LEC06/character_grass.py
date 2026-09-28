from pico2d import *

open_canvas()
character = load_image('character.png')


x = 100
y = 90

while True:
    while x < 700:
        clear_canvas()
        character.draw(x, 90)
        update_canvas()
        x += 2
        delay(0.01)

    while y < 500:
        clear_canvas()
        character.draw(700, y)
        update_canvas()
        y += 2
        delay(0.01)

    while x > 100:
        clear_canvas()
        character.draw(x, 500)
        update_canvas()
        x -= 2
        delay(0.01)

    while y > 90:
        clear_canvas()
        character.draw(100, y)
        update_canvas()
        y -= 2
        delay(0.01)

close_canvas()