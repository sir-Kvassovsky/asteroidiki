import tkinter as tk
import random
import math
from math import cos, sin
from classi import Ship, Asteroids
from PIL import Image, ImageTk
from game_start import create_start_screen
import time
class Game:
    def __init__(self, root):
        self.root = root
        root.title("Asteroidiki")
        root.geometry("800x600")
        self.asteroids = None
        self.lives = 3
        self.score = 0
        self.i = 0

        self.background_image = create_start_screen()
        self.background_image_tk = ImageTk.PhotoImage(self.background_image)
        background_label = tk.Label(root, image=self.background_image_tk)
        background_label.place(relwidth=1, relheight=1)

        start_font = ("Arial", 40)

        start_text = tk.Label(root, text="click to start", font=start_font, fg="white", bg="#0A0A32")
        start_text.place(relx=0.5, rely=0.5, anchor="center")
        lives = 3
        score = 0
        lives_text = tk.Label(root, text=f"lives: {lives}", fg="green", font=("Arial", 16), bg="#0A0A32")
        score_text = tk.Label(root, text=f"score: {score}", fg="green", font=("Arial", 16), bg="#0A0A32")
        lives_text.place(relx=60/800, rely=30/600, anchor="center")
        score_text.place(relx=680/800, rely=30/600, anchor="center")
        root.after(100, lambda: start_text.bind("<Button-1>", lambda e: self.game_start_now(root)))

    def game_start_now(self, root):
        self.root = root
        width = 800
        self.width = width
        height = 600
        canvas = tk.Canvas(root, width=width, height=height, bg="#0A0A32")
        self.canvas = canvas
        canvas.pack()
        for _ in range(100):
            star_x = random.randint(0, width - 1)
            star_y = random.randint(0, height - 1)
            canvas.create_oval(star_x, star_y, star_x, star_y, fill="white", outline="white")
        x1 = width // 2
        y1 = height // 2
        x2 = x1 - 70
        y2 = y1 - 60
        self.ship = Ship(x1, y1, x2, y2, canvas, root)
        self.asteroids = Asteroids(10, canvas, root)
        self.lives_counter = canvas.create_text(60, 30, text=f"lives: {self.lives}", fill="green", font=("Arial", 16))
        self.score_counter = canvas.create_text(width - 120, 30, text=f"score: {self.score}", fill="green", font=("Arial", 16))

        self.game(root)


    def li_sc_update(self, canvas, width):
        canvas.delete(self.lives_counter)
        canvas.delete(self.score_counter)
        self.lives_counter = canvas.create_text(60, 30, text=f"lives: {self.lives}", fill="green", font=("Arial", 16))
        self.score_counter = canvas.create_text(width - 120, 30, text=f"score: {self.score}", fill="green", font=("Arial", 16))

    def game(self, root):
        self.li_sc_update(self.canvas, self.width)
        self.spawn_asteroid(root)
        root.after(500, lambda: self.game(root))

    def spawn_asteroid(self, root, n=4):
        for i in range(n):
                if self.i == n-1:
                    self.i = 0
                else:
                    self.i += 1
                self.asteroids.create_asteroid(self.i)

root = tk.Tk()
game = Game(root)
root.mainloop()


