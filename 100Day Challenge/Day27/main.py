from tkinter import *

window = Tk()
window.title("My First GUI program")

window.minsize(width=500, height=300)


my_label = Label(text= "I am Label",font=("Arial", 24, "bold"))

my_label.pack()


def button_click_handler():
    my_label.config(text= input_entry.get())


button = Button(text="Click me", command=button_click_handler)
button.pack()

input_entry = Entry()
input_entry.pack()

window.mainloop()
