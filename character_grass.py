from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
y = 90
center_x, center_y = 400, 300
r = 200
angle = 0
rectangle_mode = True

while True:
    while x < 790:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        x += 3
        delay(0.01)
    
    while y < 590:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y += 3
        delay(0.01)
    
    while x > 0:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x -= 3
        delay(0.01)
    
    while y > 90:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y -= 3
        delay(0.01)
    
    while x < 400:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x += 3
        delay(0.01)
    
    while angle <= 360:
        clear_canvas_now()
        grass.draw_now(400, 30)
        x = center_x + r * math.cos(math.radians(angle))
        y = center_y + r * math.sin(math.radians(angle))
        character.draw_now(x, y)
        angle += 3
        delay(0.01)
    
    angle = 0 
    rectangle_mode = not rectangle_mode
close_canvas()
