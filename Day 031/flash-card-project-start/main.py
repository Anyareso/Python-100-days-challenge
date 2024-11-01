from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
french_words = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    french_words = original_data.to_dict(orient="records")
else:
    french_words = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(french_words)
    canvas.itemconfig(card_title, text="French", fill="Black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="Black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="White")
    canvas.itemconfig(card_word, text=current_card["English"], fill="White")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    french_words.remove(current_card)
    new_data = pandas.DataFrame(french_words)
    new_data.to_csv("data/words_to_learn", index=False)
    next_card()


window = Tk()
window.title("French Flash-Cards")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
cancel_btn = Button(image=wrong_img, highlightthickness=0, command=next_card)
cancel_btn.grid(column=0, row=1)

right_img = PhotoImage(file="images/right.png")
accept_btn = Button(image=right_img, highlightthickness=0, command=is_known)
accept_btn.grid(column=1, row=1)

next_card()

window.mainloop()
