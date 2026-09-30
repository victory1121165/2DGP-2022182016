from pico2d import *


CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
SPRITE_SHEET_FILE = 'mario.png'
FRAME_INTERVAL = 0.12
FRAMES_PER_ANIMATION = 5
REST_SECONDS = 1.0


open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

running = True
while running:
    clear_canvas()
    update_canvas()

    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

close_canvas()
