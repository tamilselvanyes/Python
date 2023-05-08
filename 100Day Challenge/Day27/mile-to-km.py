from tkinter import *

window = Tk()
window.minsize(width=300, height=150)
window.title("Mile to Km Converter")
window.config(padx=30, pady=20)

input_mile = Entry()
input_mile.config(width=10)
input_mile.grid(row=0, column=2)

mile_label = Label()
mile_label.config(text="Miles", font="Arial", padx=5)
mile_label.grid(row=0, column=3)

equal_label = Label()
equal_label.config(text="is equal to", font="Arial")
equal_label.grid(row=1, column=1)

value_label = Label()
value_label.config(text="0", font="Arial")
value_label.grid(row=1, column=2)

km_label = Label()
km_label.config(text="Km", font="Arial")
km_label.grid(row=1, column=3)


def calculate_km():
    value_label.config(text=format(float(input_mile.get()) * 1.6, ".2f"))


button = Button()
button.config(text="Calculate", command=calculate_km)
button.grid(row=2, column=2)

window.mainloop()
