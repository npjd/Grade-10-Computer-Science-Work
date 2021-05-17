from graphics import *

win = GraphWin('q5',300,300)

rect = Rectangle(Point(90,40),Point(160,110))
rect.setFill('magenta')
rect.setOutline('magenta')
rect.draw(win)

circle = Circle(Point(125,75),35)
circle.setOutline('green')
circle.setFill('green')
circle.draw(win)

win.mainloop()