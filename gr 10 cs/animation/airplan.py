from graphics import *
from playsound import playsound
win = GraphWin('lol',800,400)
girl = Image(Point(100,250),'girl.gif')
girl.draw(win)
boy = Image(Point(700,250),'boy.gif')
boy.draw(win)
plane = Image(Point(150,210),'planeRight.gif')
plane.draw(win)

space = False
move= 2
count = 0
while True:
    key = win.checkKey()
    if key == 'space':
        print('YEAAA')
        space = True
    while space:
        plane.move(move, 0)
        count+=2
        if count == 50:
            playsound('planeSound.wav',False)
        if count ==470:
            move *= -1
            plane.undraw()
            if move ==2:
                plane = Image(Point(150, 210), 'planeRight.gif')
            else:
                plane = Image(Point(620, 210), 'planeLeft.gif')
            count = 0
            space = False
            plane.draw(win)
win.mainloop()