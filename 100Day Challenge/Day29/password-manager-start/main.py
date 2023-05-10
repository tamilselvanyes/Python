from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(numbers) for _ in range(randint(2, 4))]
    password_numbers = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if website == "" or password == "":
        messagebox.showinfo(title="Oops!", message="Please don't leave any fields empty")

    else:
        try:
            with open("passwords.json", mode="r") as file:
                # Reading old data
                data = json.load(file)
        except FileNotFoundError:
            # if file is not found just create a new one
            with open("passwords.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # updating the data with the new data
            data.update(new_data)
            with open("passwords.json", mode="w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label()
website_label.config(text="Website:")
website_label.grid(row=1, column=0)

website_input = Entry()
website_input.config(width=35)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

email_label = Label()
email_label.config(text="Email/Username:")
email_label.grid(row=2, column=0)

email_input = Entry()
email_input.config(width=35)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "tamilselvanyes@gmail.com")

password_label = Label()
password_label.config(text="Password")
password_label.grid(row=3, column=0)

password_input = Entry()
password_input.config(width=21)
password_input.grid(row=3, column=1)

generate_password_btn = Button()
generate_password_btn.config(text="Generate Password", command=password_generator)
generate_password_btn.grid(row=3, column=2, )

add_btn = Button()
add_btn.config(text="Add", width=36, command=save)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
