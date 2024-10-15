from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("French Flash-Cards")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
cancel_btn = Button(image=wrong_img, highlightthickness=0)
cancel_btn.grid(column=0, row=1)

right_img = PhotoImage(file="images/right.png")
cancel_btn = Button(image=right_img, highlightthickness=0)
cancel_btn.grid(column=1, row=1)

window.mainloop()
