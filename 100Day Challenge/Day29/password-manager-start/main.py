from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0,column=1)

website_label = Label()
website_label.config(text="Website:")
website_label.grid(row=1, column=0)

website_input = Entry()
website_input.config(width=35)
website_input.grid(row=1, column=1, columnspan=2)

email_label = Label()
email_label.config(text="Email/Username:")
email_label.grid(row=2, column=0)

email_input = Entry()
email_input.config(width=35)
email_input.grid(row=2, column=1, columnspan=2)

password_label = Label()
password_label.config(text="Password")
password_label.grid(row=3, column=0)

password_input = Entry()
password_input.config(width=21)
password_input.grid(row=3, column=1)

generate_password_btn = Button()
generate_password_btn.config(text="Generate Password")
generate_password_btn.grid(row=3, column=2,)

add_btn = Button()
add_btn.config(text="Add", width=36)
add_btn.grid(row=4, column=1, columnspan=2)


window.mainloop()
