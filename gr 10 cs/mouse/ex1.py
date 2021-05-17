from graphics import *
from random import randint
win = GraphWin('ex1',400,400)

last = Point(0,400)
while True:
    mouse = win.getMouse()
    line = Line(last,mouse)
    line.setOutline("")
    line.setFill(color_rgb(randint(0,255),randint(0,255),randint(0,255)))
    line.draw(win)
    last = mouse

