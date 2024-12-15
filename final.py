import tkinter as tk
import random
import math
from math import cos, sin


root = tk.Tk()
root.title("Asteroidiki")
width = 800
height = 600
canvas = tk.Canvas(root, width=width, height=height, bg="white")

ship = canvas.create_line(400, 280, 400, 320, arrow='first', arrowshape=(40, 50, 15))
a = 3.14 * 3/2
speed = 1 

def start_move(direction):
    global moving
    moving = True
    move(direction)

def endless_window(x1, y1, x2, y2, obj):
    if x2 < 0:
        canvas.move(obj, 800 + x2 - x1, 0)
    elif x1 > 800:
        canvas.move(obj, -(x2 - x1 + 800), 0)
    elif y2 < 0:
        canvas.move(obj, 0, 600 + y2 - y1)
    elif y1 > 600:
        canvas.move(obj, 0, -(y2 - y1 + 600))

def stop_move(direction):
    global moving, speed
    moving = False
    speed = 1

def speed_change():
    global speed
    speed *= 1.003

def rotation(x1, y1, x2, y2, direction):
    global ship, a
    canvas.delete(ship)
    if direction == "Left":
        i = -1
    elif direction == "Right":
        i = 1
    a+= 0.01 * i
    x1 = cos(a) * 40 + x2
    y1 = sin(a) * 40 + y2
    ship = canvas.create_line(x1, y1, x2, y2, arrow='first', arrowshape=(40, 50, 15))

def move(direction):
    global ship, a, speed
    x1, y1, x2, y2 = canvas.coords(ship)
    speed_change()
    if direction != "Up":
        rotation(x1, y1, x2, y2, direction)
    elif direction == "Up":
        canvas.move(ship, speed*speed*cos(a), speed*speed*sin(a))
    endless_window(x1, y1, x2, y2, ship)
    root.after(20, lambda: move(direction))  


moving = False 
root.bind("<KeyPress-Up>", lambda e: start_move("Up"))
root.bind("<KeyRelease-Up>", lambda e: stop_move("Up"))
root.bind("<KeyPress-Left>", lambda e: start_move("Left"))
root.bind("<KeyRelease-Left>", lambda e: stop_move("notUp"))
root.bind("<KeyPress-Right>", lambda e: start_move("Right"))
root.bind("<KeyRelease-Right>", lambda e: stop_move("notUp"))


canvas.pack()
root.mainloop()




