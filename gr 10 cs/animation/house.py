from graphics import *
win = GraphWin('lol',800,800)
house = Image(Point(400,400),'house.gif')
house.draw(win)
pika = Image(Point(100,750),'pikachu.gif')
pika.draw(win)
jiggle = Image(Point(750,750),'jigglypuff.gif')
jiggle.draw(win)
pikx = 3
piky = -3
jigx = -5
jigy= -5
while True:
    pika.move(pikx,piky)
    jiggle.move(jigx,jigy)
    if jiggle.getAnchor().getX() <= 100 or jiggle.getAnchor().getX() >= 755:
        jigx *= -1
        jigy *= -1
    elif pika.getAnchor().getX() >= 720 or pika.getAnchor().getX() <= 100:
        piky*=-1
        pikx*=-1
win.mainloop()