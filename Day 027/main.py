from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am  label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New text"
my_label.config(text="New text")

# Button


def button_clicked():
    print("I got clicked")
    new_text = user_input.get()
    my_label.config(text=new_text)


button = Button(text="Click me", command=button_clicked)
button.pack()

# Entry
user_input = Entry()
user_input.pack()
print(user_input.get())


window.mainloop()
