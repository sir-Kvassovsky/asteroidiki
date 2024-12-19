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
        try: self.x1, self.y1 = cords
        except ValueError: 
            self.x1 = 0 
            self.y2 = 0 
    
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
        self.name = 'Ship'
        self.bullets = [0]*30
        self.image = Image.open("ship.png").resize((70, 60))
        self.image2 = Image.open('enginefire.png').resize((30,30)).rotate(180)
        self.ship_image = ImageTk.PhotoImage(self.image)
        self.engine_image = ImageTk.PhotoImage(self.image2)
        self.typeo = self.canvas.create_image(self.x1, self.y1, image=self.ship_image)
        self.moving = moving
        self.root.bind("<KeyPress-Up>", self.start_move) 
        self.root.bind("<KeyRelease-Up>", self.stop_move) 
        self.root.bind("<Left>", lambda event: self.rotation_left())
        self.root.bind("<Right>",lambda event: self.rotation_right())
        self.root.bind("<KeyPress-space>",lambda event: self.spawn_bullet())
        self.move()
        self.i = 0

    def update_coords1(self):
        self.x2 = self.x1
        self.y2 = self.y1

    def move(self):
        self.update_coords(self.canvas.coords(self.typeo))
        self.update_coords1()
        self.speed_change()
        self.canvas.move(self.typeo, self.speed*cos(self.a), self.speed*sin(self.a))
        self.move_fire()
        self.endless_window()
        self.bullet_dying()
        self.kill_bullet()
        self.root.after(10, self.move)

    def speed_change(self):
        if self.moving:
            self.speed = min(self.speed + 0.02, 5)
        else:
            self.speed = max(self.speed - 0.03, 0) 

    def start_move(self, event):
        self.moving = True
        self.typet = self.canvas.create_image(self.x1, self.y1+45, image=self.engine_image)
        self.move_fire()
        
    def stop_move(self, event):
        self.moving = False
        self.canvas.delete(self.typet)

    def rotation(self, direction):
        if direction == "Left":
            i = -1
        elif direction == "Right":
            i = 1
        self.a += 0.15 * i 
        self.move_fire()
        self.ship_image = ImageTk.PhotoImage(self.image.rotate(-57*self.a - 90, expand=True))
        self.engine_image = ImageTk.PhotoImage(self.image2.rotate(-57*self.a - 90, expand=True))
        self.canvas.itemconfig(self.typeo, image=self.ship_image)
        try: 
            self.canvas.itemconfig(self.typet, image=self.engine_image) 
        except AttributeError: pass
        
    def rotation_left(self):
        self.rotation("Left")

    def rotation_right(self):
        self.rotation("Right")

    def move_fire(self):
        try:
            self.update_coords(self.canvas.coords(self.typeo))
            self.update_coords1()
            x = cos(self.a - math.pi)*45 + self.x1
            y = sin(self.a - math.pi)*45 + self.y1
            self.canvas.coords(self.typet, x, y)
        except AttributeError:
            pass

    def spawn_bullet(self):
        self.i += 1
        if self.i == 29:
            self.i = 0
        self.bullets[self.i] = Bullet(self.canvas, self.root, self.x1, self.y1,self.a, speed=5)

    def kill_bullet(self):
        for i in range(30):
            try:
                if not self.bullets[i].alive:
                    self.canvas.delete(self.bullets[i].typeo)
                    self.bullets[i] = 0
            except AttributeError: pass

    def bullet_dying(self):
        for i in range(30):
            try:
                self.bullets[i].life_time -= 1
                if self.bullets[i].life_time <= 0:
                    self.bullets[i].alive = False
            except AttributeError: pass



class Asteroid(StarObj):
    def __init__(self, canvas, root, x1=0, y1=0, x2=0, y2=0,  a=0, speed=0, width=800, height=600):
        super().__init__(x1, y1, x2, y2, canvas, root, speed, a)
        self.name = 'Asteroid'
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
        self.r = r
        self.x1 = x_0 * r1 
        self.y1 = y_0 * r2
        self.x2 = self.x1
        self.y2 = self.y1
        self.blow_up = Image.open('explosion.png').resize((int(r), int(r)))
        self.blow_up_image = ImageTk.PhotoImage(self.blow_up)
        self.image = Image.open("asteroid.png").resize((int(r), int(r)))

    def destroy(self, space_obj, lives):
        live = lives
        try:
            if ((space_obj.x2 - self.x2)**2 + (space_obj.y2 - self.y2)**2)**0.5 <= self.r/2 + 5:
                if space_obj.name == 'Ship':
                    live -= 1
                    self.alive = False
                    return live 
                if space_obj.name == 'Bullet':
                    self.alive = False
                    space_obj.alive = False
        except AttributeError: pass
        return live

    
class Asteroids:
    def __init__(self, n, canvas, root):
        self.n = n
        self.canvas = canvas
        self.root = root
        self.asteroids = [0]*n
        self.asteroids_deaths = [0]*n
        self.asteroids_deaths_times = [0]*n
    
    def create_asteroid(self):
        for i in range(self.n):
            if self.asteroids[i] == 0:
                self.asteroids[i] = Asteroid(self.canvas, self.root)
    
    def collision(self, i, space_obj, lives=0):
        return self.asteroids[i].destroy(space_obj, lives)

    def kill_asteroid(self):
        killed = 0
        for i in range(self.n):
            # try:
                if not self.asteroids[i].alive:
                    # self.asteroids_deaths[i] = self.canvas.create_image(self.asteroids[i].x1, self.asteroids[i].x2-300, image=self.asteroids[i].blow_up_image)
                    # self.asteroids_deaths_times[i] = 12 
                    self.canvas.delete(self.asteroids[i].typeo)
                    self.asteroids[i] = 0
                    killed += 1
            # except AttributeError: pass
        return killed



class Bullet(StarObj):
    def __init__(self, canvas, root, x1, y1, a, speed, x2=0, y2=0):
        super().__init__(x1, y1, x2, y2, canvas, root, speed, a)
        self.name = 'Bullet'
        self.life_time = 300
        self.alive = True
        self.image = Image.open("fire.png").resize((10, 5))
        self.astr_image = ImageTk.PhotoImage(self.image)
        self.typeo = self.canvas.create_image(self.x1, self.y1, image=self.astr_image)
        self.move()

    def endless_window(self):
        pass
        



        

    
