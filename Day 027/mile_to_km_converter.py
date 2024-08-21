from tkinter import *


def miles_converter():
    n = float(user_input.get())
    result = round(n * 1.609)
    answer_label.config(text=str(result))


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# user_input
user_input = Entry(width=7)
user_input.grid(column=2, row=0)

# Miles text
miles_label = Label(text="Miles")
miles_label.grid(column=3, row=0)

# is equal to text
equal_to_label = Label(text="is equal to")
equal_to_label.grid(column=0, row=1)

# solution
answer_label = Label(text="0")
answer_label.grid(column=2, row=1)

# km text
km_label = Label(text="Km")
km_label.grid(column=3, row=1)

# Button
button = Button(text="Calculate", command=miles_converter)
button.grid(column=2, row=2)

window.mainloop()
