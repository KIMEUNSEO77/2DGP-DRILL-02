from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def move_rectangle():
    for x in range(365, 790 + 1, 2):
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, 90)
        update_canvas()
        delay(0.01)

    for y in range(90, 560 + 1, 2):
        clear_canvas()
        grass.draw(400, 30)
        character.draw(780, y)
        update_canvas()
        delay(0.01)

    for x in range(790, 0 - 1, -2):
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, 560)
        update_canvas()
        delay(0.01)

    for y in range(560, 90 - 1, -2):
        clear_canvas()
        grass.draw(400, 30)
        character.draw(10, y)
        update_canvas()
        delay(0.01)

    for x in range(0, 365 + 1, 2):
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, 90)
        update_canvas()
        delay(0.01)


def move_circle():
    r = 220
    for deg in range(360, 0, -1):
        x = r * math.cos(math.radians(deg)) + 400
        y = r * math.sin(math.radians(deg)) + 330
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, y)
        update_canvas()
        delay(0.01)


while True:
    move_rectangle()
    move_circle()



close_canvas()