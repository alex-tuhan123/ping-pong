from pygame import *

FPS = 60

back = (200, 250, 250)

width = 600
height = 500

window = display.set_mode((width,height))
window.fill(back)

clock = time.Clock()

game = True
finish = False

''''
....
....
....

'''

while game:

    for e in event.get():
        if e.type == QUIT:
            game = False


    display.update()
    clock.tick()
