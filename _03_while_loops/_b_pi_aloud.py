"""
Use a while loop to recite the digits of pi
"""
from tkinter import messagebox, simpledialog, Tk


if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    # TODO) Place the first 20 digits of pi into a variable as a string
    #  3.1415926535897932384
    PI = "3.1415926535897932384"
    # TODO) Print out the first 3 digits of pi. For example,
    #  pi_str[0]   # first digit
    #  pi_str[1]   # second digit
    stage = True
    num = 0
    print(PI[0])
    print(PI[1])
    print(PI[2])
    # TODO) Use a while loop to keep asking for the next digit of pi
    pi = ""
    while stage:
        pi = simpledialog.askstring(None, prompt="What is the next digit of pi?")

        if pi == PI[3+num]:
            print("correct")
            print(pi)
            num += 1
        else:
            print("incorrect")
            break

        # TODO) If they are correct, print "correct".
        #  If they are not, print "incorrect" and break out of the while loop


    # TODO) Print out how many digits of pi the user was able to recite
    #  in a row
    print("You were able to recite "+str(num)+" digits of pi in a row!")