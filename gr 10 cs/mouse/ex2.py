from graphics import *
from random import randint
import threading
from time import sleep

win = GraphWin('q2', 400, 400)


class rect(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        last_color = color_rgb(randint(0, 255), randint(0, 255), randint(0, 255))
        while True:
            sleep(0.001)
            p1 = win.getMouse()
            p1.draw(win)
            p2 = win.getMouse()
            rect = Rectangle(p1, p2)
            color = color_rgb(randint(0, 255), randint(0, 255), randint(0, 255))
            rect.setFill(color)
            rect.setOutline(last_color)
            rect.draw(win)
            last_color = color

class delete(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        erase = Rectangle(Point(0,0),Point(400,400))
        erase.setFill('white')
        while True:
            sleep(0.001)
            key = win.checkKey()
            if key =='c':
                erase.undraw()
                erase.draw(win)

thread1 = rect()
thread2 = delete()
thread1.start()
thread2.start()
win.mainloop()