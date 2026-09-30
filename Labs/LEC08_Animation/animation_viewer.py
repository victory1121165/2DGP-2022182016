from pico2d import *


CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
SPRITE_SHEET_FILE = 'mario.png'
FRAME_INTERVAL = 0.12
FRAMES_PER_ANIMATION = 5
REST_SECONDS = 1.0

# 프레임 좌표는 (왼쪽, 위쪽, 너비, 높이) 순서입니다.
ANIMATIONS = {
    '걷기': [
        (0, 0, 64, 100), (68, 0, 64, 100), (136, 0, 64, 100),
        (204, 0, 64, 100), (272, 0, 64, 100), (340, 0, 64, 100),
    ],
    '점프': [
        (448, 0, 88, 102), (544, 0, 88, 102), (640, 0, 88, 102),
        (736, 0, 88, 102), (832, 0, 88, 102), (928, 0, 88, 102),
    ],
    '공격': [
        (12, 205, 72, 122), (88, 205, 72, 122), (164, 205, 104, 122),
        (274, 205, 112, 122), (392, 205, 112, 122),
    ],
    '도구 사용': [
        (510, 448, 86, 112), (604, 448, 86, 112), (698, 448, 86, 112),
        (792, 448, 86, 112), (886, 448, 86, 112), (980, 448, 44, 112),
    ],
}


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
