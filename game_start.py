import tkinter as tk
from PIL import Image, ImageTk
import random

def create_start_screen():
    width, height = 800, 600
    background = Image.new("RGB", (width, height), (10, 10, 50))

    ship_image = Image.open("ship.png")
    asteroid_image = Image.open("asteroid.png")

    ship_image = ship_image.resize((400, 400))
    ship_image = ship_image.rotate(-25, expand=True)
    ship_x = -200
    ship_y = 200
    for _ in range(100):
        star_x = random.randint(0, width - 1)
        star_y = random.randint(0, height - 1)
        background.putpixel((star_x, star_y), (255, 255, 255))

    background.paste(ship_image, (ship_x, ship_y), ship_image)

    asteroid_data = [
        {"position": (-100, 70), "size": (200, 200)},
        {"position": (200, -30), "size": (100, 100)},
        {"position": (400, 100), "size": (150, 150)},
        {"position": (500, 400), "size": (80, 80)},
        {"position": (650, 150), "size": (55, 55)},
        {"position": (500, 450), "size": (300, 300)},
        {"position": (300, 350), "size": (65, 65)},
        {"position": (375, 480), "size": (80, 80)}
    ]

    for asteroid in asteroid_data:
        asteroid_image_resized = asteroid_image.resize(asteroid["size"])
        background.paste(asteroid_image_resized, asteroid["position"],
                         asteroid_image_resized)



    return background


