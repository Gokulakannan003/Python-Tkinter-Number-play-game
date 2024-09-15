from tkinter import *
import random

root = Tk()
root.geometry("650x300")
root.resizable(False, False)
root.configure(bg="sky blue")
root.title("Number guessing game")

label2 = Label(root, text="", font=("Ariel", 18, "bold"), bg="sky blue")
label2.grid(row=2, column=0, columnspan=3, padx=5, pady=20)

label3 = Label(root, text="", font=("Ariel", 18, "bold"), bg="sky blue")
label3.grid(row=3, column=0, columnspan=3, padx=5, pady=20)


def computer():
    gamer = int(entrybox.get())
    com = random.randint(0, 9)
    a = ("You ", gamer, "Computer ", com)
    if 0 <= gamer <= 9:
        if com == gamer:
            label3.configure(text="Win")
            label2.configure(text=a)
        else:
            label2.configure(text=a)
            label3.configure(text="Out")


label = Label(root, text="Enter a you guessed number ", font=("Ariel", 18, "bold"), bg="sky blue")
label.grid(row=0, column=0, pady=15, padx=7)

entrybox = Entry(root, font=("Ariel", 18, "bold"))
entrybox.grid(row=0, column=1, padx=10, pady=15)

submit = Button(root, text="Play", command=computer, font=("Ariel", 25, "bold"), background="brown", width=23)
submit.grid(row=1, column=0, columnspan=4, padx=10)
root.mainloop()
