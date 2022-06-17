from tkinter import *

# basically what this does is it does something upon button press

window = Tk()


def click():
    print("you cliked me lmao xD")


button = Button(window,
                text="click me!",
                command=click,
                font=("Comic Sans MS", 30),
                fg="#00FFF0")
button.pack()

window.mainloop()

# XD wala lang natripan ko lang to baket ba
