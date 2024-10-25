from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
french_words = data.to_dict(orient="records")


def next_card():
    current_card = random.choice(french_words)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])


window = Tk()
window.title("French Flash-Cards")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
cancel_btn = Button(image=wrong_img, highlightthickness=0, command=next_card)
cancel_btn.grid(column=0, row=1)

right_img = PhotoImage(file="images/right.png")
cancel_btn = Button(image=right_img, highlightthickness=0, command=next_card)
cancel_btn.grid(column=1, row=1)

next_card()

window.mainloop()
