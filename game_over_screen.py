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

    for asteroid in asteroid_data:
        asteroid_image_resized = asteroid_image.resize(asteroid["size"])
        background.paste(asteroid_image_resized, asteroid["position"],
                         asteroid_image_resized)

    for _ in range(100):
        star_x = random.randint(0, width - 1)
        star_y = random.randint(0, height - 1)
        background.putpixel((star_x, star_y), (255, 255, 255))

    return background






