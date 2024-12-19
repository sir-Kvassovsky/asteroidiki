import tkinter as tk
import random
import math
from math import cos, sin
from classi import Ship, Asteroid
# from start_screen import show_start_screen
from PIL import Image, ImageTk

def start_game(root):
    # start_window.destroy()
    # root = tk.Tk()
    # root.title("Asteroidiki")
    for l in root.winfo_children():
        l.destroy()
    width = 800
    height = 600
    canvas = tk.Canvas(root, width=width, height=height, bg="white")
    canvas.pack()

    x1 = width // 2
    y1 = height // 2
    x2 = x1 - 70
    y2 = y1 - 60

    img = Image.open("ship.png")
    ship_image = img.resize((70, 60))
    ship_image = ImageTk.PhotoImage(ship_image)
    ship = canvas.create_image(x1, y1, image=ship_image)

    ship1 = Ship(ship, x1, y1, x2, y2, canvas, root)
    astr = canvas.create_oval(0, 0, 0, 0)  
    astr1 = Asteroid(astr, canvas, root)

    lives = 3
    score = 0

    lives_counter = canvas.create_text(60, 30, text=f"lives: {lives}", fill="green", font=("Arial", 16))
    score_counter = canvas.create_text(width - 120, 30, text=f"score: {score}", fill="green", font=("Arial", 16))


    root.mainloop()




