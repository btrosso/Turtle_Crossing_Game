import random
import time
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
# BOUNDARY for cars is y = -220 to y = 220

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.parking_lot = []

    def move_cars(self):
        for car in self.parking_lot:
            car.forward(STARTING_MOVE_DISTANCE)


    def create_car(self):
        if len(self.parking_lot) < 1:
            new_car = Turtle("square")
            new_car.hideturtle()
            new_car.pu()
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.goto(300, random.randint(-220, 220))
            new_car.showturtle()
            self.parking_lot.append(new_car)
        else:
            pass



