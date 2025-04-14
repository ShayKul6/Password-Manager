from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

FONT = ("Ariel", 10)
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    password_letters = [choice(LETTERS) for _ in range(randint(8, 10))]
    password_symbols = [choice(SYMBOLS) for _ in range(randint(2, 4))]
    password_numbers = [choice(NUMBERS) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = ''.join(password_list)
    password_entry.insert(index=END, string=password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_pass():
    website = website_entry.get().capitalize()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Try Again!", message="Some fields are empty...")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                              f"\nPassword: {password}\n Is it ok to save?")
        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"{website} | {email} | {password}\n")

        # delete website and password entries
        website_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# --- Window --- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# --- Canvas for logo --- #
canvas = Canvas(width=200, height=190, highlightthickness=0)
logo_image = PhotoImage(file="logo.png")  # PhotoImage object of the image itself
canvas.create_image(100, 100, image=logo_image)  # set location + image
canvas.grid(column=2, row=1)

# --- Labels --- #
website_label = Label(text="Website:", font=FONT)
website_label.grid(column=1, row=2)

email_label = Label(text="Email/Username:", font=FONT)
email_label.grid(column=1, row=3)

password_label = Label(text="Password:", font=FONT)
password_label.grid(column=1, row=4)

# --- Entries --- #
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=2, row=2, columnspan=2)

email_entry = Entry(width=35)
email_entry.insert(index=END, string="shaykul6@gmail.com")
email_entry.grid(column=2, row=3, columnspan=2)

password_entry = Entry(width=21)
password_entry.insert(index=END, string="")
password_entry.grid(column=2, row=4)

# --- Buttons --- #
generate_btn = Button(text="Generate Password", command=generate_pass)
generate_btn.grid(column=3, row=4)

add_btn = Button(text="Add", width=36, command=add_pass)
add_btn.grid(column=2, row=5, columnspan=2)

window.mainloop()