"""
Use boolean variables to control program logic between two different code
paths.
"""
from tkinter import messagebox, Tk, simpledialog, colorchooser
if __name__ == '__main__':
    # TODO)
    #  1. Use a boolean variable to indicate if it is the weekend.
    import turtle
    Weekend = True
    Passed = True
    Over = True
    Red = True
    Square = True
    #     Display a different message to the user depending on whether it is
    #     the weekend or not.
    window = Tk()
    window.withdraw()
    if Weekend:
        print("Yay!")
    else:
        print("Do your work!")
    #  2. Use a boolean variable to indicate if a student passed an exam.
    if Passed:
        print("Congrats!")
    else:
        print("Work harder!")

    #     Display a different message to the user depending on whether they
    #     passed or not.
    #  3. Use a boolean variable to indicate if a game is over. When the game
    #     is over, tell the user.
    if Over:
        print("The game is over!")
    #  4. Use two boolean variables, one to indicate if a shape should be red,
    #     the other to indicate if the shape is to be square. When both
    #     variables are true, use a turtle to draw a red square.
    t = turtle.Turtle()
    if Red:
        t.pencolor('red')
    if Square:
        t.pendown()
        t.forward(20)
        t.right(90)
        t.forward(20)
        t.right(90)
        t.forward(20)
        t.right(90)
        t.forward(20)
        t.right(90)
    if Square and Red:
        t.pencolor('red')
        t.pendown()
        t.forward(20)
        t.right(90)
        t.forward(20)
        t.right(90)
        t.forward(20)
        t.right(90)
        t.forward(20)
        t.right(90)


    pass
