from graphics import *
from time import sleep
win = GraphWin('q1',300,605)
circ = Circle(Point(150,250),20)
circ.setFill('red')
circ.draw(win)
yChange = 0
grav = 0.1
while circ.getCenter().getY()<583.5:
    yChange-=grav
    circ.move(0,circ.getCenter().getY() - (circ.getCenter().getY()+yChange))
    if circ.getCenter().getY() >= 580:
        yChange*=-1
win.mainloop()
