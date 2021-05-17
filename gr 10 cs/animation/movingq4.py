from graphics import *
import threading
from time import sleep
from random import randint
from playsound import playsound
import pygame

# pygame.mixer.init()
# pygame.mixer.music.load('holup.wav')
# pygame.mixer.music.play(999)

win = GraphWin('q4', 600, 600)
win.setBackground('blue')
char = Image(Point(300, 300), 'alex.gif')
rand1 = Image(Point(200, 200), 'steve.gif')
rand2 = Image(Point(250, 250), 'steve.gif')
counter = 0


class moveChar(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global win
        global char
        global charHitbox
        char.draw(win)
        xmove2 = 0
        ymove2 = 0
        while True:
            sleep(0.001)
            if char.getAnchor().getY() <= 25:
                char.move(0, 50)
            elif char.getAnchor().getY() >= 570:
                char.move(0, -50)
            elif char.getAnchor().getX() <= 25:
                char.move(50, 0)
            elif char.getAnchor().getX() >= 570:
                char.move(-50, 0)
            key = win.checkKey()
            if key == 'Up':
                ymove2 = -1
                xmove2 = 0
            elif key == 'Down':
                ymove2 = 1
                xmove2 = 0
            elif key == 'Left':
                xmove2 = -1
                ymove2 = 0
            elif key == 'Right':
                xmove2 = 1
                ymove2 = 0
            char.move(4 * xmove2, 4 * ymove2)


class moveRandom(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global win
        global rand1
        rand1.draw(win)
        xmove = 0
        ymove = 0
        while True:
            sleep(0.002)
            if rand1.getAnchor().getY() <= 23:
                rand1.move(0, 40)
            elif rand1.getAnchor().getY() >= 575:
                rand1.move(0, -40)
            elif rand1.getAnchor().getX() <= 23:
                rand1.move(40, 0)
            elif rand1.getAnchor().getX() >= 575:
                rand1.move(-40, 0)
            key = randint(1, 50)
            if key == 1:
                ymove = -1
                xmove = 0
            elif key == 2:
                ymove = 1
                xmove = 0
            elif key == 3:
                xmove = -1
                ymove = 0
            elif key == 4:
                xmove = 1
                ymove = 0
            rand1.move(2 * xmove, 2 * ymove)


class moveRandom2(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global win
        global rand2
        rand2.draw(win)
        xmove = 0
        ymove = 0
        while True:
            sleep(0.002)
            if rand2.getAnchor().getY() <= 23:
                rand2.move(0, 40)
            elif rand2.getAnchor().getY() >= 575:
                rand2.move(0, -40)
            elif rand2.getAnchor().getX() <= 23:
                rand2.move(40, 0)
            elif rand2.getAnchor().getX() >= 575:
                rand2.move(-40, 0)
            key = randint(1, 50)
            if key == 1:
                ymove = -1
                xmove = 0
            elif key == 2:
                ymove = 1
                xmove = 0
            elif key == 3:
                xmove = -1
                ymove = 0
            elif key == 4:
                xmove = 1
                ymove = 0
            rand2.move(2 * xmove, 2 * ymove)


class collision(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global win
        global rand1
        global rand2
        global char
        global counter
        while True:
            sleep(0.002)
            if abs(char.getAnchor().getX() - rand1.getAnchor().getX()) <= 65 and abs(
                    char.getAnchor().getY() - rand1.getAnchor().getY()) <= 95:
                counter = -1
                playsound('fafa.wav', False)
                win.setBackground('red')
                text = Text(Point(300, 300), 'get gud')
                text.setSize(36)
                text.draw(win)
                sleep(2)
                text.undraw()
                win.setBackground('blue')
            elif abs(char.getAnchor().getX() - rand2.getAnchor().getX()) <= 65 and abs(
                    char.getAnchor().getY() - rand2.getAnchor().getY()) <= 95:
                counter = -1
                playsound('fafa.wav', False)
                win.setBackground('red')
                text = Text(Point(300, 300), 'get gud')
                text.setSize(36)
                text.draw(win)
                sleep(2)
                text.undraw()
                win.setBackground('blue')


class counterFunc(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global win
        global counter
        text = Text(Point(300, 100), 'your score is ' + str(counter))
        text.setSize(30)
        text.draw(win)
        while True:
            sleep(1)
            counter += 1
            text.setText('your score is ' + str(counter))


thread1 = moveRandom()
thread3 = moveRandom2()
thread2 = moveChar()
thread4 = collision()
thread5 = counterFunc()
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
win.mainloop()
