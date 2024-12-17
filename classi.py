# class Asteroid:
#     def __init__(self, ):
#         self.
import tkinter as tk
import random
import math
from math import cos, sin

class StarObj:
    def __init__(self, name, x1, y1, x2, y2, canvas, root):
        self.name = name
        self.update_coords((x1, y1, x2, y2))
        self.speed = 1
        self.a = math.pi * 3/2
        self.canvas = canvas
        self.root = root
    
    def update_coords(self, cords):
        self.x1, self.y1, self.x2, self.y2 = cords

    def move(self):
        self.update_coords(self.canvas.coords(self.name))
        self.canvas.move(self.name, self.speed*cos(self.a), self.speed*sin(self.a))
        self.endless_window(self.x1, self.y1, self.x2, self.y2, self.name)
        self.root.after(10, self.move)

    def endless_window(self):
        if self.x2 < 0:
            self.canvas.move(self.name, 800 + self.x2 - self.x1, 0)
        elif self.x1 > 800:
            self.canvas.move(self.name, -(self.x2 - self.x1 + 800), 0)
        elif self.y2 < 0:
            self.canvas.move(self.name, 0, 600 + self.y2 - self.y1)
        elif self.y1 > 600:
            self.canvas.move(self.name, 0, -(self.y2 - self.y1 + 600))
        
class Ship (StarObj):
    def __init__(self, name, x1, y1, x2, y2, canvas, root, moving=False):
        super().__init__(name, x1, y1, x2, y2, canvas, root)
        self.moving = moving
        self.root.bind("<KeyPress-Up>", self.start_move) 
        self.root.bind("<KeyRelease-Up>", self.stop_move) 
        self.root.bind("<Left>", self.rotation_left)
        self.root.bind("<Right>", self.rotation_right)
        self.move()


    def move(self):
        self.update_coords(self.canvas.coords(self.name))
        self.speed_change()
        self.canvas.move(self.name, self.speed*cos(self.a), self.speed*sin(self.a))
        self.endless_window()
        self.root.after(10, self.move)

    def speed_change(self):
        if self.moving:
            self.speed = min(self.speed + 0.03, 7)
        else:
            self.speed = max(self.speed - 0.1, 0) 

    def start_move(self, event):
        self.moving = True

    def stop_move(self, event):
        self.moving = False

    def rotation(self, direction):
        if direction == "Left":
            i = -1
        elif direction == "Right":
            i = 1
        self.update_coords(self.canvas.coords(self.name))
        self.a+= 0.1 * i
        self.x1 = cos(self.a) * 40 + self.x2
        self.y1 = sin(self.a) * 40 + self.y2
        self.canvas.coords(self.name, self.x1, self.y1, self.x2, self.y2)

    def rotation_left(self, event):
        self.rotation("Left")

    def rotation_right(self, event):
        self.rotation("Right")
    
    
