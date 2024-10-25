from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)
    password_user_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website_input = website_user_input.get()
    email_input = email_user_input.get()
    password_input = password_user_input.get()
    new_data = {
        website_input: {
            "email": email_input,
            "password": password_input
        }
    }

    if len(website_input) == 0 or len(email_input) == 0 or len(password_input) == 0:
        messagebox.showerror(title="Oops", message="Please do not leave any of the fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_user_input.delete(0, END)
            password_user_input.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website_find = website_user_input.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website_find in data:
            email_find = data[website_find]["email"]
            password_find = data[website_find]["password"]
            messagebox.showinfo(title=website_find, message=f"Email: {email_find}\nPassword: {password_find}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website_find} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
password_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website: ", font=20)
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username: ", font=20)
email_label.grid(column=0, row=2)

password_label = Label(text="Password: ", font=20)
password_label.grid(column=0, row=3)

website_user_input = Entry(width=33)
website_user_input.grid(column=1, row=1)
website_user_input.focus()

email_user_input = Entry(width=52)
email_user_input.grid(column=1, row=2, columnspan=2)
email_user_input.insert(0, "agnesnyareso3@gmail.com")

password_user_input = Entry(width=33)
password_user_input.grid(column=1, row=3)

generate_pass_btn = Button(text="Generate Password", command=generate_password)
generate_pass_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=44, command=save_password)
add_btn.grid(column=1, row=4, columnspan=2)

search_btn = Button(text="Search", width=14, command=find_password)
search_btn.grid(column=2, row=1)

window.mainloop()
