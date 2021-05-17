from graphics import *

win = GraphWin('ex3', 600, 400)
but1 = Rectangle(Point(400, 50), Point(500, 100))
but1.setFill('yellow')
but1t = Text(Point(450, 75), 'Happy')
but1.draw(win)
but1t.draw(win)
but2 = Rectangle(Point(400, 150), Point(500, 200))
but2.setFill('blue')
but2t = Text(Point(450, 175), 'Sad')
but2.draw(win)
but2t.draw(win)
but3 = Rectangle(Point(400, 250), Point(500, 300))
but3.setFill('red')
but3t = Text(Point(450, 275), 'Angry')
but3.draw(win)
but3t.draw(win)
head = Circle(Point(200, 200), 150)
head.setWidth(8)
head.draw(win)
eye1 = Oval(Point(125, 125), Point(150, 175))
eye1.setFill('black')
eye1.draw(win)
eye2 = Oval(Point(250, 125), Point(275, 175))
eye2.setFill('black')
eye2.draw(win)
smile = Polygon(Point(150, 250), Point(200, 300), Point(250, 250))
smile.setFill('black')
smile.draw(win)
frown = Polygon(Point(150, 300), Point(200, 250), Point(250, 300))
frown.setFill('black')
brow = Polygon(Point(125, 100), Point(125, 115), Point(200, 125), Point(275, 115), Point(275, 100), Point(200, 110))
brow.setFill('black')
Smile = True
Frown = False
Brow = False
while True:
    click = win.getMouse()
    if 400 <= click.getX() <= 500 and 50 <= click.getY() <= 100:
        Smile = True
        Frown = False
        Brow = False
    elif 400 <= click.getX() <= 500 and 150 <= click.getY() <= 200:
        Smile = False
        Frown = True
        Brow = False
    elif 400 <= click.getX() <= 500 and 250 <= click.getY() <= 300:
        Smile = False
        Frown = True
        Brow = True
    smile.undraw()
    frown.undraw()
    brow.undraw()
    if Smile:
        smile.draw(win)
    if Frown:
        frown.draw(win)
    if Brow:
        brow.draw(win)

win.mainloop()
