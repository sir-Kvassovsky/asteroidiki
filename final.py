import tkinter as tk
import random
import math


root = tk.Tk()
root.title("Asteroidiki")
width = 800
height = 600
canvas = tk.Canvas(root, width=width, height=height, bg="white")

ship = canvas.create_line(400, 280, 400, 320, arrow='first', arrowshape=(40, 50, 15))
angle = 0  
speed = 5 


def start_move(direction):
    global moving
    moving = True
    move(direction)

def stop_move():
    global moving
    moving = False

def move(direction):
    if moving:
        x1, y1, x2, y2 = canvas.coords(ship)
        if x2 < 0:
            canvas.move(ship, 800 + x2 - x1, 0)
        elif x1 > 800:
            canvas.move(ship, -(x2 - x1 + 800), 0)
        elif y2 < 0:
            canvas.move(ship, 0, 600 + y2 - y1)
        elif y1 > 600:
            canvas.move(ship, 0, -(y2 - y1 + 600))
        elif direction == "Up":
            canvas.move(ship, 0, -5)
        elif direction == "Down":
            canvas.move(ship, 0, 5)
        elif direction == "Left":
            canvas.move(ship, -5, 0)
        elif direction == "Right":
            canvas.move(ship, 5, 0)
        root.after(50, lambda: move(direction))  


moving = False 
root.bind("<KeyPress-Up>", lambda e: start_move("Up"))
root.bind("<KeyRelease-Up>", lambda e: stop_move())
root.bind("<KeyPress-Down>", lambda e: start_move("Down"))
root.bind("<KeyRelease-Down>", lambda e: stop_move())
root.bind("<KeyPress-Left>", lambda e: start_move("Left"))
root.bind("<KeyRelease-Left>", lambda e: stop_move())
root.bind("<KeyPress-Right>", lambda e: start_move("Right"))
root.bind("<KeyRelease-Right>", lambda e: stop_move())




canvas.pack()
root.mainloop()




