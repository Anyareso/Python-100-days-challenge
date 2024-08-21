from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = user_input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am  label", font=("Arial", 24, "bold"))
my_label.config(text="New text")
my_label.grid(column=0, row=0)

# Button
button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

# New Button
button1 = Button(text="New Button", command=button_clicked)
button1.grid(column=2, row=0)

# Entry
user_input = Entry()
print(user_input.get())
user_input.grid(column=4, row=4)


window.mainloop()
