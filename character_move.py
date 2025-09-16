from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

while True:
    for x in range(0, 800 + 1, 2):
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, 90)
        update_canvas()
        delay(0.01)

    for y in range(30, 600 + 1, 2):
        clear_canvas()
        grass.draw(400, 30)
        character.draw(800, y)
        update_canvas()
        delay(0.01)

    for x in range(800, 0 - 1, -2):
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, 600)
        update_canvas()
        delay(0.01)

    for y in range(600, 30 - 1, -2):
        clear_canvas()
        grass.draw(400, 30)
        character.draw(800, y)
        update_canvas()
        delay(0.01)

close_canvas()