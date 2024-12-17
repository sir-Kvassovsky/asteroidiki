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
a = math.pi * 3/2
speed = 1 

def start_move(event):
    global moving
    moving = True

def endless_window(x1, y1, x2, y2, obj):
    if x2 < 0:
        canvas.move(obj, 800 + x2 - x1, 0)
    elif x1 > 800:
        canvas.move(obj, -(x2 - x1 + 800), 0)
    elif y2 < 0:
        canvas.move(obj, 0, 600 + y2 - y1)
    elif y1 > 600:
        canvas.move(obj, 0, -(y2 - y1 + 600))

def stop_move(event):
    global moving
    moving = False

def speed_change():
    global speed
    if moving:
        speed = min(speed + 0.05, 10)
    else:
        speed = max(speed - 0.1, 0) 


def rotation(direction):
    global a
    if direction == "Left":
        i = -1
    elif direction == "Right":
        i = 1
    x1, y1, x2, y2 = canvas.coords(ship)
    a+= 0.1 * i
    x1 = cos(a) * 40 + x2
    y1 = sin(a) * 40 + y2
    canvas.coords(ship, x1, y1, x2, y2)

def rotation_left(event):
    rotation("Left")

def rotation_right(event):
    rotation("Right")

def move():
    global ship, a, moving
    x1, y1, x2, y2 = canvas.coords(ship)
    speed_change()
    canvas.move(ship, speed*cos(a), speed*sin(a))
    endless_window(x1, y1, x2, y2, ship)
    root.after(10, move)

moving = False
root.bind("<KeyPress-Up>", start_move) 
root.bind("<KeyRelease-Up>", stop_move) 
root.bind("<Left>", rotation_left)
root.bind("<Right>", rotation_right)
move()

canvas.pack()
root.mainloop()




