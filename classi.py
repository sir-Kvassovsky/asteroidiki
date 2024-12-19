import tkinter as tk
import random
import math
from math import cos, sin
from PIL import Image, ImageTk

class StarObj:
    def __init__(self, x1, y1, x2, y2, canvas, root, speed, a):
        self.typeo = None
        self.update_coords((x1, y1))
        self.update_coords1()
        self.speed = speed
        self.a = a
        self.canvas = canvas
        self.root = root
    
    def update_coords(self, cords):
        self.x1, self.y1 = cords
    
    def update_coords1(self):
        self.x2, self.y2 = self.x1, self.y1

    def move(self):
        self.update_coords(self.canvas.coords(self.typeo))
        self.update_coords1()
        self.canvas.move(self.typeo, self.speed*cos(self.a), self.speed*sin(self.a))
        self.endless_window()
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
    def __init__(self, x1, y1, x2, y2, canvas, root, speed=1, a=math.pi * 3/2,moving=False):
        super().__init__(x1, y1, x2, y2, canvas, root, speed, a)
        self.image = Image.open("ship.png").resize((70, 60))
        self.ship_image = ImageTk.PhotoImage(self.image)
        self.typeo = self.canvas.create_image(self.x1, self.y1, image=self.ship_image)
        self.moving = moving
        self.root.bind("<KeyPress-Up>", self.start_move) 
        self.root.bind("<KeyRelease-Up>", self.stop_move) 
        self.root.bind("<Left>", self.rotation_left)
        self.root.bind("<Right>", self.rotation_right)
        self.move()

    def update_coords1(self):
        self.x2 = self.x1 + 70
        self.y2 = self.y1 + 60

    def move(self):
        self.update_coords(self.canvas.coords(self.typeo))
        self.update_coords1()
        self.speed_change()
        self.canvas.move(self.typeo, self.speed*cos(self.a), self.speed*sin(self.a))
        self.endless_window()
        self.root.after(10, self.move)

    def speed_change(self):
        if self.moving:
            self.speed = min(self.speed + 0.03, 6)
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
        self.a += 0.15 * i 
        self.ship_image = ImageTk.PhotoImage(self.image.rotate(-57*self.a - 90, expand=True))
        self.canvas.itemconfig(self.typeo, image=self.ship_image) 
        
    def rotation_left(self, event):
        self.rotation("Left")

    def rotation_right(self, event):
        self.rotation("Right")
    
class Asteroid(StarObj):
    def __init__(self, canvas, root, x1=0, y1=0, x2=0, y2=0,  a=0, speed=0, width=800, height=600):
        super().__init__(x1, y1, x2, y2, canvas, root, speed, a)
        self.alive = True
        self.create(width, height)
        self.astr_image = ImageTk.PhotoImage(self.image)
        self.typeo = self.canvas.create_image(self.x1, self.y1, image=self.astr_image)
        self.move()

    def create(self, width, height):
        x_0 = random.uniform(0,  width)
        y_0 = random.uniform(0,  height)
        r1 = random.randint(0, 1)
        r2 = 1 - r1
        self.speed = random.uniform(0.1, 3)
        self.a = random.uniform(0, 2*math.pi)
        r = random.randint(50, 200)
        self.x1 = x_0 * r1 
        self.y1 = y_0 * r2
        self.x2 = x_0 + r
        self.y2 = y_0 + r
        self.image = Image.open("asteroid.png").resize((int(r), int(r)))
    
class Asteroids:
    def __init__(self, n, canvas, root):
        self.n = n
        self.canvas = canvas
        self.root = root
        self.asteroids = [0]*n
        self.i = 0
        self.create_asteroid(self.i)
    
    def create_asteroid(self, i):
        if self.asteroids[i] == 0:
                self.asteroids[i] = Asteroid(self.canvas, self.root)

class Bullet(StarObj):
    def __init__(self, canvas, root, x1, y1, a, speed, x2=0, y2=0):
        super().__init__(x1, y1, x2, y2, canvas, root, speed, a)
        self.alive = True


        

    
