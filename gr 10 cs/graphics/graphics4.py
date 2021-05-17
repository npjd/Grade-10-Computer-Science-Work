from graphics import *

win = GraphWin('q4',400,400)
c1 = Circle(Point(240,160),25)
c1.setFill('green')
c1.setWidth(3)
c1.setOutline('blue')
c1.draw(win)
c2 = Circle(Point(240,110),25)
c2.setFill('gray')
c2.setOutline('blue')
c2.setWidth(3)
c2.draw(win)
win.mainloop()