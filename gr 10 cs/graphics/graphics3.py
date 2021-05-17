from graphics import *

win = GraphWin('q3', 300,250)
oval = Oval(Point(220,80),Point(180,20))
oval.setFill('cyan')
oval.draw(win)
# oval.getCenter()
# print(oval.getCenter())
win.mainloop()
