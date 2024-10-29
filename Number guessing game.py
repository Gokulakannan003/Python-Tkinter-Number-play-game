# version 1
"""from tkinter import *
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
    a = ("You", gamer, "Computer", com)
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
"""
# version 2
from customtkinter import *
import random
from tkinter import messagebox

root = CTk()
root.geometry("650x300")
root.resizable(False, False)
root.configure(bg="sky blue")
root.title("Number guessing game")


main_frame = CTkFrame(root, height=250, width=600, fg_color="ivory4")
main_frame.place(x=25, y=25)



def computer():
    gamer1 = entrybox.get()
    if gamer1 == "":
        messagebox.showerror("Input error", "Enter a number")

    gamer = int(entrybox.get())
    com = random.randint(0, 9)
    a = ("You", gamer, "Computer", com)
    label2 = CTkLabel(main_frame, text="", font=("Ariel", 18, "bold"), fg_color="ivory4")
    label2.place(x=200, y=150)

    label3 = CTkLabel(main_frame, text="", font=("Ariel", 18, "bold"), fg_color="ivory4")
    label3.place(x=260, y=190)
    if 0 <= gamer <= 9:
        if com == gamer:
            label3.configure(text="Win")
            label2.configure(text=a)
        else:
            label2.configure(text=a)
            label3.configure(text="Out")


label = CTkLabel(main_frame, text="Enter a you guessed number ", font=("Ariel", 18, "bold"))
label.place(x=25, y=25)

entrybox = CTkEntry(main_frame, font=("Ariel", 18, "bold"), corner_radius=2)
entrybox.place(x=290, y=25)

submit = CTkButton(root, text="Play", command=computer, font=("Ariel", 25, "bold"), bg_color="ivory4", width=90)
submit.place(x=260, y=110)
root.mainloop()
