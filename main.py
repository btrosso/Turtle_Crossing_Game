import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

tim = Player()
car_manager = CarManager()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
screen.onkey(fun=tim.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # TODO: may need to rethink how to create the cars
    # Detect car crossing left boundary
    # for car in car_manager.parking_lot:
    #     if car.xcor() < -280:
    #         car_manager.reset()

    # Detect crossing finish line
    if tim.ycor() > 280:
        tim.reset()



screen.exitonclick()