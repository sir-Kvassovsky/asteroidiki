import tkinter as tk
import random
import math
from math import cos, sin
from classi import Ship, Asteroid
from start_screen import show_start_screen

def start_game(start_window):
    # Закрываем стартовое окно
    start_window.destroy()

    # Основные параметры окна игры
    root = tk.Tk()
    root.title("Asteroidiki")
    width = 800
    height = 600

    # Создаем холст
    canvas = tk.Canvas(root, width=width, height=height, bg="white")
    canvas.pack()

    # Центр холста
    x_center = width / 2
    y_center = height / 2

    # Длина линии корабля
    line_length = 40

    # Вычисляем начальные координаты корабля
    x1 = x_center
    y1 = y_center
    x2 = x1
    y2 = y1 - line_length

    # Создаем корабль (линия со стрелкой)
    ship = canvas.create_line(x1, y1, x2, y2, arrow='first', arrowshape=(20, 30, 10), fill="blue")

    # Создаем объект класса Ship
    ship1 = Ship(ship, x1, y1, x2, y2, canvas, root)

    # Создаем астероид (один для теста)
    astr = canvas.create_oval(0, 0, 0, 0)  # Пустой объект, который инициализируется в классе
    astr1 = Asteroid(astr, canvas, root)

    # Параметры игры
    lives = 3
    score = 0

    # Счетчики жизней и очков
    lives_counter = canvas.create_text(60, 30, text=f"lives: {lives}", fill="green", font=("Arial", 16))
    score_counter = canvas.create_text(width - 120, 30, text=f"score: {score}", fill="green", font=("Arial", 16))

    # Запускаем игру
    root.mainloop()

# Запуск стартового экрана
show_start_screen(start_game)


