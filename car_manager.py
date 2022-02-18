import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
RANDOM_POSITION = [(300, random.randint(-220, 220))]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.num_cars = 20
        self.car_freq = 10
        self.hideturtle()
        self.parking_lot = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def move_car(self):
        for car in self.parking_lot:
            car.forward(self.move_distance)

    def create_car(self):
        if len(self.parking_lot) < 150:
            new_car = Turtle("square")
            new_car.hideturtle()
            new_car.pu()
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.goto((300, random.randint(-220, 220)))
            new_car.showturtle()
            self.parking_lot.append(new_car)

    def reset_car(self):
        for car in self.parking_lot:
            if car.xcor() < -320:
                car.hideturtle()
                car.goto((300, random.randint(-220, 220)))
                car.showturtle()

    def go_faster(self):
        self.move_distance += MOVE_INCREMENT
