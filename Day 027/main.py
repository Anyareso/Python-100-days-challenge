from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am  label", font=("Arial", 24, "bold"))
my_label.pack(side="left")

my_label["text"] = "New text"
my_label.config(text="New text")

# Button
button = Button()


window.mainloop()
