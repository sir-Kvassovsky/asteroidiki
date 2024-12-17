import tkinter as tk
import random
import math
from math import cos, sin

class StarObj:
    def __init__(self, typeo, x1, y1, x2, y2, canvas, root, speed, a):
        self.typeo = typeo
        self.update_coords((x1, y1, x2, y2))
        self.speed = speed
        self.a = a
        self.canvas = canvas
        self.root = root
    
    def update_coords(self, cords):
        self.x1, self.y1, self.x2, self.y2 = cords

    def move(self):
        self.update_coords(self.canvas.coords(self.typeo))
        self.canvas.move(self.typeo, self.speed*cos(self.a), self.speed*sin(self.a))
        self.endless_window(self.x1, self.y1, self.x2, self.y2, self.typeo)
        self.root.after(10, self.move)

    def endless_window(self):
        if self.x2 < 0:
            self.canvas.move(self.typeo, 800 + self.x2 - self.x1, 0)
        elif self.x1 > 800:
            self.canvas.move(self.typeo, -(self.x2 - self.x1 + 800), 0)
        elif self.y2 < 0:
            self.canvas.move(self.typeo, 0, 600 + self.y2 - self.y1)
        elif self.y1 > 600:
            self.canvas.move(self.typeo, 0, -(self.y2 - self.y1 + 600))
        
class Ship(StarObj):
    def __init__(self, typeo, x1, y1, x2, y2, canvas, root, speed=1, a=math.pi * 3/2,moving=False):
        super().__init__(typeo, x1, y1, x2, y2, canvas, root, speed, a)
        self.moving = moving
        self.root.bind("<KeyPress-Up>", self.start_move) 
        self.root.bind("<KeyRelease-Up>", self.stop_move) 
        self.root.bind("<Left>", self.rotation_left)
        self.root.bind("<Right>", self.rotation_right)
        self.move()


    def move(self):
        self.update_coords(self.canvas.coords(self.typeo))
        self.speed_change()
        self.canvas.move(self.typeo, self.speed*cos(self.a), self.speed*sin(self.a))
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
        self.update_coords(self.canvas.coords(self.typeo))
        self.a+= 0.1 * i
        self.x1 = cos(self.a) * 40 + self.x2
        self.y1 = sin(self.a) * 40 + self.y2
        self.canvas.coords(self.typeo, self.x1, self.y1, self.x2, self.y2)

    def rotation_left(self, event):
        self.rotation("Left")

    def rotation_right(self, event):
        self.rotation("Right")
    
class Asteroid(StarObj):
    def __init__(self, typeo, canvas, root, x1=0, y1=0, x2=0, y2=0,  a=0, speed=0, width=800, height=600):
        super().__init__(typeo, x1, y1, x2, y2, canvas, root, speed, a)
        self.create(width, height)
        self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2)

    def create(self, width, height):
        x_0 = random.uniform(0,  width/2.1)
        y_0 = random.uniform(0,  height/2.1)
        x_1 = random.uniform(width/1.9,  width)
        y_1 = random.uniform(height/1.9,  height)
        r1, r2 = random.randint(0, 1), random.randint(0, 1)
        self.speed = random.uniform(0.1, 3)
        self.a = random.uniform(0, 2*math.pi)
        r = random.randint(25, 50)
        self.x1 = x_0 - r
        self.x2 = x_0 + r
        self.y1 = y_0 - r
        self.y2 = y_0 + r
    
