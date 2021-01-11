from random import randint
from tkinter import Tk, Button, Label
from PIL import Image, ImageTk

BACKGROUND = "#fcf8e8"
FONT_NAME  = "Courier"


def generate_dice_image():
    load_image    =  Image.open(f"{randint(1, 6)}.PNG")
    render_image  =  ImageTk.PhotoImage(load_image)
    img           =  Label(image=render_image, bg=BACKGROUND)
    img.image     =  render_image
    img.grid(column=2, row=2)


# Creating a window
window = Tk()
window.title("Dice App")
window.config(padx=20, pady=10, bg=BACKGROUND)

# Creating a label
dice_app = Label()
dice_app.config(text="Python Dice App", font=("Arial", 30, "bold"), fg="#0f0f0f", bg=BACKGROUND)
dice_app.grid(column=2, row=0)


# Calling this function to generate a dice image when app started
generate_dice_image()

# Creating a button
button = Button()
button.config(text="Click Me", width=10, command=generate_dice_image, font=(FONT_NAME, 20, "bold"))
button.grid(column=2, row=3)


window.mainloop()
