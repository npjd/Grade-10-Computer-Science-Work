# Name: Nima Dehkordi
# Date: December 18th 2020

# import libraries
from graphics import *
from random import randint

# draw window
win = GraphWin("HANGMAN", 1400, 700)

# opening screen
titleText = Text(Point(700, 150), "Hangman by Chef Pourjafar ")
titleText.setSize(30)
titleText.draw(win)
titleButtonText = Text(Point(700, 375), 'CLICK TO START')
titleButtonText.setSize(30)
titleButtonText.draw(win)
# waits for user to click to start
check = win.getMouse()

# clears screen
clear = Rectangle(Point(0, 0), Point(1400, 700))
clear.setFill('white')
clear.draw(win)

# word list makes picking a word easy, for we can pick a random word with a random index
wordList = ['variable', 'strings', 'graphics', 'python', 'programming', 'data', 'julian', 'hangman', 'lol', 'bruh',
            'alexander', 'fortnite']
word = wordList[randint(0, len(wordList) - 1)]

# Button for resetting game
newGame = Rectangle(Point(1100, 600), Point(1390, 690))
newGame.draw(win)
newGameText = Text(Point(1245, 645), "New Game")
newGameText.setSize(30)
newGameText.draw(win)

# Button for exiting game
exitBut = Rectangle(Point(10, 600), Point(300, 690))
exitBut.draw(win)
exitText = Text(Point(155, 645), "Exit")
exitText.setSize(30)
exitText.draw(win)
# Initializing guess entry box w/ text
guessing = Rectangle(Point(725, 450), Point(900, 500))
guessing.draw(win)
guessHeader = Text(Point(800, 480), "Enter a Guess")
guessHeader.setSize(20)
guessHeader.draw(win)
guessBox = Entry(Point(850, 505), 35)
guessBox.draw(win)
# Draws the noose
nooseBase = Line(Point(400, 350), Point(600, 350))
nooseBase.draw(win)
noosePole = Line(Point(500, 350), Point(500, 100))
noosePole.draw(win)
nooseHori = Line(Point(500, 100), Point(600, 100))
nooseHori.draw(win)
# the hangman's shapes are stored in a list so we can draw them 1 by 1
person = [Circle(Point(600, 150), 50), Line(Point(600, 200), Point(600, 270)), Line(Point(600, 225), Point(570, 240)),
          Line(Point(600, 225), Point(630, 240))
    , Line(Point(600, 270), Point(570, 290)), Line(Point(600, 270), Point(630, 290)), Circle(Point(580, 150), 10)
    , Circle(Point(620, 150), 10), Oval(Point(590, 155), Point(610, 165)), Oval(Point(580, 165), Point(620, 185))]
# alphabet list to draw alphabet text later
alpText = ["A", "B", "C", "D", "E", "F", "G", "H", 'I', "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z"]
# list used to draw the underscores on the game. We use a list since we can modify each text shape when the user gets
# a letter right
underscores = []
# list for alphabet buttons on screen
alp = []
# list for text elements in the buttons
alpTextDraw = []
# the loops help draw the buttons more efficiently, we append each rectangle to the alp list for later uses.
# starting position of the buttons
x = 10
# 1st row
for _ in range(17):
    rect = Rectangle(Point(x, 370), Point(x + 70, 440))
    rect.draw(win)
    alp.append(rect)
    x += 80
# re-initialize x
x = 10
# 2nd row
for _ in range(9):
    rect = Rectangle(Point(x, 450), Point(x + 70, 520))
    rect.draw(win)
    alp.append(rect)
    x += 80
# loop that draw the text inside the buttons
for i in range(len(alp)):
    # picks which letter to draw from alphabet text list, since the len(alp) is the same as the len of the alphabet, the letters will be in the rright spot.
    letterText = alpText[i]
    # gets the button with the respected letter
    rect = alp[i]
    # draws the text inside the rect
    text = Text(Point(rect.getP1().getX() + 35, rect.getP1().getY() + 35), letterText)
    text.setSize(20)
    # adds the text element to the list
    alpTextDraw.append(text)
    text.draw(win)
x = 60
# draws underscores. The amount of underscores match the length of the word
for _ in range(len(word)):
    underscore = Text(Point(x, 250), "_")
    underscore.setSize(32)
    # appends the text to the list
    underscores.append(underscore)
    underscore.draw(win)
    x += 40
# hangman counter
hangman = 0

# main game loop
while True:
    # sets reset variable back to false so we can pass our conditional statements
    reset = False
    # finds where user clicks
    mouse = win.getMouse()
    # variables for mouse coordinates
    x = mouse.getX()
    y = mouse.getY()
    guess = ""
    # while loop that checks if the users mouse click is in a button
    i = 0
    while i != len(alp):
        rect = alp[i]
        # checks to see if user clicked in a alphabet button by iterating through each one and checking
        if rect.getP1().getX() < x < rect.getP2().getX() and rect.getP1().getY() < y < rect.getP2().getY():
            # gets the letter that button represents
            letter = alpText[i]
            # checks to see if letter is in the word
            if letter.lower() in word:
                # array to store the positions the letter is in the word
                positions = []
                # loop that checks positions and appends them to the positions list
                for j in range(len(word)):
                    if word[j] == letter.lower():
                        positions.append(j)
                # loop that changes the text in the underscores list to the correclty guessed letter
                for k in range(len(positions)):
                    pos = positions[k]
                    underscores[pos].setText(letter.lower())
                # gets rid of the button pressed and the text so the program doesn't check them again
                alp[i].undraw()
                alpTextDraw[i].undraw()
                alp.pop(i)
                alpTextDraw.pop(i)
                alpText.pop(i)
            # checks to see if user used up all their guesses
            elif hangman == 10:
                # clears screen
                guessBox.undraw()
                clear = Rectangle(Point(0, 0), Point(1400, 700))
                clear.setFill('white')
                clear.draw(win)
                # displays losing screen
                loseTitle = Text(Point(700, 150), 'lol git gud')
                loseTitle.setSize(30)
                loseTitle.draw(win)
                continueBox = Rectangle(Point(150, 350), Point(400, 450))
                continueBox.draw(win)
                continueText = Text(Point(275, 400), "Play Again")
                continueText.setSize(28)
                continueText.draw(win)
                quitBox = Rectangle(Point(1050, 350), Point(1300, 450))
                quitBox.draw(win)
                quitText = Text(Point(1175, 400), "Quit")
                quitText.setSize(28)
                quitText.draw(win)
                clicked = False
                # waits until user clicks a button
                while not clicked:
                    mouse2 = win.getMouse()
                    x2 = mouse2.getX()
                    y2 = mouse2.getY()
                    # button for new game
                    if 150 < x2 < 400 and 350 < y2 < 450:
                        # redraws game and restores original values to lists
                        clear = Rectangle(Point(0, 0), Point(1400, 700))
                        clear.setFill('white')
                        clear.draw(win)
                        word = wordList[randint(0, len(wordList) - 1)]
                        newGame = Rectangle(Point(1100, 600), Point(1390, 690))
                        newGame.draw(win)
                        newGameText = Text(Point(1245, 645), "New Game")
                        newGameText.setSize(30)
                        newGameText.draw(win)
                        exitBut = Rectangle(Point(10, 600), Point(300, 690))
                        exitBut.draw(win)
                        exitText = Text(Point(155, 645), "Exit")
                        exitText.setSize(30)
                        exitText.draw(win)
                        guessHeader = Text(Point(790, 465), "Enter a Guess")
                        guessHeader.setSize(20)
                        guessHeader.draw(win)
                        guessing = Rectangle(Point(725, 450), Point(900, 500))
                        guessing.draw(win)
                        guessBox = Entry(Point(850, 505), 35)
                        guessBox.draw(win)
                        nooseBase = Line(Point(400, 350), Point(600, 350))
                        nooseBase.draw(win)
                        noosePole = Line(Point(500, 350), Point(500, 100))
                        noosePole.draw(win)
                        nooseHori = Line(Point(500, 100), Point(600, 100))
                        nooseHori.draw(win)
                        person = [Circle(Point(600, 150), 50), Line(Point(600, 200), Point(600, 270)),
                                  Line(Point(600, 225), Point(570, 240)),
                                  Line(Point(600, 225), Point(630, 240))
                            , Line(Point(600, 270), Point(570, 290)), Line(Point(600, 270), Point(630, 290)),
                                  Circle(Point(580, 150), 10)
                            , Circle(Point(620, 150), 10), Oval(Point(590, 155), Point(610, 165)),
                                  Oval(Point(580, 165), Point(620, 185))]
                        alpText = ["A", "B", "C", "D", "E", "F", "G", "H", 'I', "J", "K", "L", "M", "N", "O", "P",
                                   "Q", "R", "S", "T",
                                   "U", "V",
                                   "W", "X", "Y", "Z"]
                        underscores = []
                        alp = []
                        alpTextDraw = []
                        x = 10
                        for _ in range(17):
                            rect = Rectangle(Point(x, 370), Point(x + 70, 440))
                            rect.draw(win)
                            alp.append(rect)
                            x += 80
                        x = 10
                        for _ in range(9):
                            rect = Rectangle(Point(x, 450), Point(x + 70, 520))
                            rect.draw(win)
                            alp.append(rect)
                            x += 80
                        for i in range(len(alp)):
                            letterText = alpText[i]
                            rect = alp[i]
                            text = Text(Point(rect.getP1().getX() + 35, rect.getP1().getY() + 35), letterText)
                            text.setSize(20)
                            alpTextDraw.append(text)
                            text.draw(win)
                        x = 60
                        for _ in range(len(word)):
                            underscore = Text(Point(x, 250), "_")
                            underscore.setSize(32)
                            underscores.append(underscore)
                            underscore.draw(win)
                            x += 40
                        hangman = 0
                        clicked = True
                        # reset variable to ingore the last conditional statement, since hangman is set back to 10
                        reset = True
                    # quits game
                    elif 1050 < x2 < 1300 and 350 < y2 < 450:
                        clicked = True
                        quit()
            # if hangman is not 10 and the user did not correctly guess a letter, they pass this conditional statement
            elif not reset and hangman != 10:
                reset = False
                # draws hangman element and increases hangman by 1
                person[hangman].draw(win)
                hangman += 1
                # gets rid of button clicked from list so the program doesn't check it
                alp[i].undraw()
                alpTextDraw[i].undraw()
                alp.pop(i)
                alpTextDraw.pop(i)
                alpText.pop(i)
                break
        else:
            # interation thru list
            i += 1

    if 1100 < x < 1390 and 600 < y < 690:
        # reset button, resets game and clears page
        clear = Rectangle(Point(0, 0), Point(1400, 700))
        clear.setFill('white')
        clear.draw(win)
        word = wordList[randint(0, len(wordList) - 1)]
        newGame = Rectangle(Point(1100, 600), Point(1390, 690))
        newGame.draw(win)
        newGameText = Text(Point(1245, 645), "New Game")
        newGameText.setSize(30)
        newGameText.draw(win)
        exitBut = Rectangle(Point(10, 600), Point(300, 690))
        exitBut.draw(win)
        exitText = Text(Point(155, 645), "Exit")
        exitText.setSize(30)
        exitText.draw(win)
        guessing = Rectangle(Point(725, 450), Point(900, 500))
        guessing.draw(win)
        guessHeader = Text(Point(790, 465), "Enter a Guess")
        guessHeader.setSize(20)
        guessHeader.draw(win)
        guessBox = Entry(Point(850, 505), 35)
        guessBox.draw(win)
        nooseBase = Line(Point(400, 350), Point(600, 350))
        nooseBase.draw(win)
        noosePole = Line(Point(500, 350), Point(500, 100))
        noosePole.draw(win)
        nooseHori = Line(Point(500, 100), Point(600, 100))
        nooseHori.draw(win)
        person = [Circle(Point(600, 150), 50), Line(Point(600, 200), Point(600, 270)),
                  Line(Point(600, 225), Point(570, 240)),
                  Line(Point(600, 225), Point(630, 240))
            , Line(Point(600, 270), Point(570, 290)), Line(Point(600, 270), Point(630, 290)),
                  Circle(Point(580, 150), 10)
            , Circle(Point(620, 150), 10), Oval(Point(590, 155), Point(610, 165)),
                  Oval(Point(580, 165), Point(620, 185))]
        alpText = ["A", "B", "C", "D", "E", "F", "G", "H", 'I', "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                   "U", "V",
                   "W", "X", "Y", "Z"]
        underscores = []
        alp = []
        alpTextDraw = []
        x = 10
        for _ in range(17):
            rect = Rectangle(Point(x, 370), Point(x + 70, 440))
            rect.draw(win)
            alp.append(rect)
            x += 80
        x = 10
        for _ in range(9):
            rect = Rectangle(Point(x, 450), Point(x + 70, 520))
            rect.draw(win)
            alp.append(rect)
            x += 80
        for i in range(len(alp)):
            letterText = alpText[i]
            rect = alp[i]
            text = Text(Point(rect.getP1().getX() + 35, rect.getP1().getY() + 35), letterText)
            text.setSize(20)
            alpTextDraw.append(text)
            text.draw(win)
        x = 60
        for _ in range(len(word)):
            underscore = Text(Point(x, 250), "_")
            underscore.setSize(32)
            underscores.append(underscore)
            underscore.draw(win)
            x += 40
        hangman = 0
    # Guess button
    elif 725 < x < 900 and 450 < y < 500:
        # makes the guess variable the text in entry box
        guess = guessBox.getText()
        # entry guesses take up 1 guess so we draw the hangman element
        person[hangman].draw(win)
        hangman += 1
    # quit button
    elif 10 < x < 300 and 600 < y < 690:
        quit()
    # creates guess variable, which is essenitally the underscore list. The underscore list includes all the players correct guesses.
    else:
        for i in range(len(underscores)):
            guess += underscores[i].getText()
    # checks to see if the player sucessfully guessed the word
    if guess == word:
        # displays winning screen
        guessBox.undraw()
        clear = Rectangle(Point(0, 0), Point(1400, 700))
        clear.setFill('white')
        clear.draw(win)
        loseTitle = Text(Point(700, 150), 'GJ Loser')
        loseTitle.setSize(30)
        loseTitle.draw(win)
        continueBox = Rectangle(Point(150, 350), Point(400, 450))
        continueBox.draw(win)
        continueText = Text(Point(275, 400), "Play Again")
        continueText.setSize(28)
        continueText.draw(win)
        quitBox = Rectangle(Point(1050, 350), Point(1300, 450))
        quitBox.draw(win)
        quitText = Text(Point(1175, 400), "Quit")
        quitText.setSize(28)
        quitText.draw(win)
        clicked = False
        # loops until user clicks a button
        while not clicked:
            mouse2 = win.getMouse()
            x2 = mouse2.getX()
            y2 = mouse2.getY()
            if 150 < x2 < 400 and 350 < y2 < 450:
                # resets to original game with original variable values
                clear = Rectangle(Point(0, 0), Point(1400, 700))
                clear.setFill('white')
                clear.draw(win)
                word = wordList[randint(0, len(wordList) - 1)]
                newGame = Rectangle(Point(1100, 600), Point(1390, 690))
                newGame.draw(win)
                newGameText = Text(Point(1245, 645), "New Game")
                newGameText.setSize(30)
                newGameText.draw(win)
                exitBut = Rectangle(Point(10, 600), Point(300, 690))
                exitBut.draw(win)
                exitText = Text(Point(155, 645), "Exit")
                exitText.setSize(30)
                exitText.draw(win)
                guessHeader = Text(Point(790, 465), "Enter a Guess")
                guessHeader.setSize(20)
                guessHeader.draw(win)
                guessing = Rectangle(Point(725, 450), Point(900, 500))
                guessing.draw(win)
                guessBox = Entry(Point(850, 505), 35)
                guessBox.draw(win)
                nooseBase = Line(Point(400, 350), Point(600, 350))
                nooseBase.draw(win)
                noosePole = Line(Point(500, 350), Point(500, 100))
                noosePole.draw(win)
                nooseHori = Line(Point(500, 100), Point(600, 100))
                nooseHori.draw(win)
                person = [Circle(Point(600, 150), 50), Line(Point(600, 200), Point(600, 270)),
                          Line(Point(600, 225), Point(570, 240)),
                          Line(Point(600, 225), Point(630, 240))
                    , Line(Point(600, 270), Point(570, 290)), Line(Point(600, 270), Point(630, 290)),
                          Circle(Point(580, 150), 10)
                    , Circle(Point(620, 150), 10), Oval(Point(590, 155), Point(610, 165)),
                          Oval(Point(580, 165), Point(620, 185))]
                alpText = ["A", "B", "C", "D", "E", "F", "G", "H", 'I', "J", "K", "L", "M", "N", "O", "P",
                           "Q", "R", "S", "T",
                           "U", "V",
                           "W", "X", "Y", "Z"]
                underscores = []
                alp = []
                alpTextDraw = []
                x = 10
                for _ in range(17):
                    rect = Rectangle(Point(x, 370), Point(x + 70, 440))
                    rect.draw(win)
                    alp.append(rect)
                    x += 80
                x = 10
                for _ in range(9):
                    rect = Rectangle(Point(x, 450), Point(x + 70, 520))
                    rect.draw(win)
                    alp.append(rect)
                    x += 80
                for i in range(len(alp)):
                    letterText = alpText[i]
                    rect = alp[i]
                    text = Text(Point(rect.getP1().getX() + 35, rect.getP1().getY() + 35), letterText)
                    text.setSize(20)
                    alpTextDraw.append(text)
                    text.draw(win)
                x = 60
                for _ in range(len(word)):
                    underscore = Text(Point(x, 250), "_")
                    underscore.setSize(32)
                    underscores.append(underscore)
                    underscore.draw(win)
                    x += 40
                hangman = 0
                clicked = True
                reset = True
            # quits game
            elif 1050 < x2 < 1300 and 350 < y2 < 450:
                clicked = True
                quit()

win.mainloop()
