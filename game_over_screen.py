import tkinter as tk
from PIL import Image, ImageTk
import random


def create_game_over_screen():
    width, height = 800, 600

    background = Image.new("RGB", (width, height), (10, 10, 50))
    asteroid_image = Image.open("asteroid.png")

    asteroid_data = [
        {"position": (100, 50), "size": (120, 120)},
        {"position": (300, 150), "size": (80, 80)},
        {"position": (500, 250), "size": (200, 200)},
        {"position": (600, 450), "size": (150, 150)},
        {"position": (200, 475), "size": (100, 100)},
        {"position": (600, 45), "size": (150, 150)},
        {"position": (0, 275), "size": (130, 130)}
    ]

    # астероиды
    for asteroid in asteroid_data:
        asteroid_image_resized = asteroid_image.resize(asteroid["size"])
        background.paste(asteroid_image_resized, asteroid["position"],
                         asteroid_image_resized)

    # звездочки
    for _ in range(100):
        star_x = random.randint(0, width - 1)
        star_y = random.randint(0, height - 1)
        background.putpixel((star_x, star_y), (255, 255, 255))

    return background


def show_game_over_screen():
    game_over_window = tk.Tk()
    game_over_window.title("Asteroidiki")
    game_over_window.geometry("800x600")

    background_image = create_game_over_screen()
    background_image_tk = ImageTk.PhotoImage(background_image)

    background_label = tk.Label(game_over_window, image=background_image_tk)
    background_label.place(relwidth=1, relheight=1)

    start_font = ("Arial", 50)
    start_text = tk.Label(game_over_window, text="game over", font=start_font, fg="white")
    start_text.place(relx=0.5, rely=0.5, anchor="center")

    def toggle_text_visibility():
        current_color = start_text.cget("fg")

        if current_color == "white":
            start_text.config(fg="#999999", bg="#0A0A32")
        else:
            start_text.config(fg="white", bg="#0A0A32")

        game_over_window.after(500, toggle_text_visibility)

    toggle_text_visibility()
    game_over_window.mainloop()


show_game_over_screen()
