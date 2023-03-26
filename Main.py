from pygame import *

window = display.set_mode((700,500))
display.set_caption('ping-pong')
back = (255,255,200)
window.fill(back)



run = True

while run:

    for e in event.get():
        if e.type == QUIT:
            run = False
        


    display.update()