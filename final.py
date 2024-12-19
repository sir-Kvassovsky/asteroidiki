import tkinter as tk
import random
import math
from math import cos, sin
from classi import Ship, Asteroids
from PIL import Image, ImageTk
from game_start import create_start_screen
import time
from game_over_screen import create_game_over_screen

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
        self.score_text = tk.Label(root, text=f"score: {score}", fg="green", font=("Arial", 16), bg="#0A0A32")
        lives_text.place(relx=60/800, rely=30/600, anchor="center")
        self.score_text.place(relx=680/800, rely=30/600, anchor="center")
        root.after(100, lambda: start_text.bind("<Button-1>", lambda e: self.game_start_now(root)))

    def game_start_now(self, root):
        self.root = root
        width = 800
        self.width = width
        height = 600
        self.height = height
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
        self.blow_up = Image.open('explosion.png').resize((100, 100))
        self.blow_up_image = ImageTk.PhotoImage(self.blow_up)
        self.live_pred = 3
        self.ship = Ship(x1, y1, x2, y2, canvas, root)
        self.asteroids = Asteroids(4, canvas, root)
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
        self.asteroids.create_asteroid()
        self.collision_check()
        self.game_over_check()
        try:
            self.ship_death_time -= 1
            if self.ship_death_time == 0:
                self.canvas.delete(self.ship_death)
            for i in range(4):
                self.asteroids.asteroids_deaths_times[i] -= 1
                if self.asteroids.asteroids_deaths_times[i] == 0:
                    self.canvas.delete(self.asteroids.asteroids_deaths[i])
        except AttributeError: pass
        root.after(50, lambda: self.game(root))


    def collision_check(self, n=4):
        for i in range(n):
            self.lives = self.asteroids.collision(i, self.ship, self.lives)
            if self.live_pred > self.lives:
                self.ship_death = self.canvas.create_image(self.ship.x1-70, self.ship.x2-60, image=self.blow_up_image)
                self.ship_death_time = 12
                self.canvas.coords(self.ship.typeo, self.width//2, self.height//2)
                self.ship.speed = 0
                self.live_pred -= 1
            for j in range(30):
                self.asteroids.collision(i, self.ship.bullets[j])
        self.score += self.asteroids.kill_asteroid()



    def game_over_check(self):
        if self.lives <= 0:
            self.show_game_over_screen()

    def show_game_over_screen(self):

        self.background_image = create_game_over_screen()
        self.background_image_tk = ImageTk.PhotoImage(self.background_image)

        background_label = tk.Label(self.root, image=self.background_image_tk)
        background_label.place(relwidth=1, relheight=1)

        start_font = ("Arial", 50)
        start_text = tk.Label(self.root, text="game over", font=start_font, fg="white")
        start_text.place(relx=0.5, rely=0.5, anchor="center")
        self.score_text = tk.Label(root, text=f"score: {self.score}", fg="green", font=("Arial", 16), bg="#0A0A32")
        self.score_text.place(relx=400/800, rely=200/600, anchor="center")

        def toggle_text_visibility():
            current_color = start_text.cget("fg")

            if current_color == "white":
                start_text.config(fg="#999999", bg="#0A0A32")
            else:
                start_text.config(fg="white", bg="#0A0A32")

            self.root.after(500, toggle_text_visibility)

        toggle_text_visibility()
        self.root.mainloop()

root = tk.Tk()
game = Game(root)
root.mainloop()


