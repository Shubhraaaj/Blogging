__author__ = 'Shubhraj'

def guessGame():
    y = 8
    x = input("Enter a number between 1 to 10 - ")
    if int(x) == y:
        print("Congratulations you won the game")
    else:
        print("Sorry, You guessed the wrong number {s}".format(s=x))

guessGame()