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

# import tkinter as tk
# import random
# import math
# from math import cos, sin
#
#
# class StarObj:
#     def __init__(self, typeo, x1, y1, x2, y2, canvas, root, speed, a):
#         self.typeo = typeo
#         self.update_coords((x1, y1, x2, y2))
#         self.speed = speed
#         self.a = a
#         self.canvas = canvas
#         self.root = root
#
#     def update_coords(self, cords):
#         self.x1, self.y1, self.x2, self.y2 = cords
#
#     def move(self):
#         self.update_coords(self.canvas.coords(self.typeo))
#         self.canvas.move(self.typeo, self.speed * cos(self.a), self.speed * sin(self.a))
#         self.endless_window(self.x1, self.y1, self.x2, self.y2, self.typeo)
#         self.root.after(10, self.move)
#
#     def endless_window(self):
#         if self.x2 < 0:
#             self.canvas.move(self.typeo, 800 + self.x2 - self.x1, 0)
#         elif self.x1 > 800:
#             self.canvas.move(self.typeo, -(self.x2 - self.x1 + 800), 0)
#         elif self.y2 < 0:
#             self.canvas.move(self.typeo, 0, 600 + self.y2 - self.y1)
#         elif self.y1 > 600:
#             self.canvas.move(self.typeo, 0, -(self.y2 - self.y1 + 600))
#
#
# class Ship(StarObj):
#     def __init__(self, typeo, x1, y1, x2, y2, canvas, root, speed=1, a=math.pi * 3 / 2, moving=False):
#         super().__init__(typeo, x1, y1, x2, y2, canvas, root, speed, a)
#         self.moving = moving
#         self.root.bind("<KeyPress-Up>", self.start_move)
#         self.root.bind("<KeyRelease-Up>", self.stop_move)
#         self.root.bind("<Left>", self.rotation_left)
#         self.root.bind("<Right>", self.rotation_right)
#         self.move()
#
#     def move(self):
#         self.update_coords(self.canvas.coords(self.typeo))
#         self.speed_change()
#         self.canvas.move(self.typeo, self.speed * cos(self.a), self.speed * sin(self.a))
#         self.endless_window()
#         self.root.after(10, self.move)
#
#     def speed_change(self):
#         if self.moving:
#             self.speed = min(self.speed + 0.03, 7)
#         else:
#             self.speed = max(self.speed - 0.1, 0)
#
#     def start_move(self, event):
#         self.moving = True
#
#     def stop_move(self, event):
#         self.moving = False
#
#     def rotation(self, direction):
#         if direction == "Left":
#             i = -1
#         elif direction == "Right":
#             i = 1
#
#         # Изменение угла поворота
#         self.a += 0.1 * i
#
#         # Длина линии корабля
#         line_length = 40
#
#         # Пересчет координат корабля
#         self.x2 = self.x1 + cos(self.a) * line_length
#         self.y2 = self.y1 + sin(self.a) * line_length
#
#         # Обновляем координаты на холсте
#         self.canvas.coords(self.typeo, self.x1, self.y1, self.x2, self.y2)
#
#     def rotation_left(self, event):
#         self.rotation("Left")
#
#     def rotation_right(self, event):
#         self.rotation("Right")
#
#
# class Asteroid(StarObj):
#     def __init__(self, typeo, canvas, root, x1=0, y1=0, x2=0, y2=0, a=0, speed=0, width=800, height=600):
#         super().__init__(typeo, x1, y1, x2, y2, canvas, root, speed, a)
#         self.create(width, height)
#         self.typeo = self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill="gray")
#
#     def create(self, width, height):
#         x_0 = random.uniform(0, width / 2.1)
#         y_0 = random.uniform(0, height / 2.1)
#         r = random.randint(25, 50)
#         self.speed = random.uniform(0.1, 3)
#         self.a = random.uniform(0, 2 * math.pi)
#         self.x1 = x_0 - r
#         self.x2 = x_0 + r
#         self.y1 = y_0 - r
#         self.y2 = y_0 + r
#         self.typeo = self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill="gray")
#





