from graphics import *
win = GraphWin('q7',300,300)
hex1 = Polygon(Point(15,15), Point(45,15), Point(55,35), Point(45, 55), Point(15,55), Point(5,35))
hex1.setFill('orange')
hex1.draw(win)
i1 = Text(Point(30,35),"N")
i1.draw(win)

hex2 = Polygon(Point(69,69), Point(207,69), Point(253,161), Point(207, 253), Point(69,253), Point(23,161))
hex2.setFill('blue')
i2 = Text(Point(149,161),"P")
hex2.draw(win)
i2.draw(win)
win.mainloop()