import math
from pico2d import *

open_canvas()
character = load_image('character.png')

cx, cy = 400, 300
r = 200

angle = 0

while True:
    clear_canvas()

    x = cx + r * math.cos(angle)
    y = cy + r * math.sin(angle)

    character.draw(x, y)
    update_canvas()

    angle += 0.02
    delay(0.01)

close_canvas()