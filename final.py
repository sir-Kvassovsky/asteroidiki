import tkinter as tk
import random
import math
from math import cos, sin
from classi import Ship, Asteroid

root = tk.Tk()
root.title("Asteroidiki")
width = 800
height = 600
canvas = tk.Canvas(root, width=width, height=height, bg="white")
ship = canvas.create_line(400, 280, 400, 320, arrow='first', arrowshape=(40, 50, 15))
ship1 = Ship(ship, 400, 280, 400, 320, canvas, root)
astr = canvas.create_oval(0,0,0,0)
astr1 = Asteroid(astr, canvas, root)
lives = 3
score = 0
lives_counter = canvas.create_text(60, 30, text=f"lives: {lives}", fill="green" )
score_counter = canvas.create_text(width-120, 30, text=f"score: {score}", fill="green" )

canvas.pack()
root.mainloop()




