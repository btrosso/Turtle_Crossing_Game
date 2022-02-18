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
screen.onkeypress(fun=tim.move, key="Up")

scoreboard = Scoreboard()


sleep_time = .1
loop_run = 1
game_is_on = True

while game_is_on:
    time.sleep(sleep_time)
    screen.update()

    if len(car_manager.parking_lot) < car_manager.num_cars:
        if loop_run % car_manager.car_freq == 0:
            car_manager.create_car()

    car_manager.move_car()
    car_manager.reset_car()

    # Detect crossing finish line
    if tim.ycor() > 280:
        tim.reset()
        car_manager.go_faster()
        scoreboard.level_up()

    # Detect collision with car - best yet - (still having a bit of trouble visualizing the logic with the car turtles)
    for car in car_manager.parking_lot:
        if (car.distance(tim) < 30 and car.ycor() < 10) or (car.distance(tim) < 30 and car.xcor() < 5):
            game_is_on = False
            scoreboard.game_over()

    # This block works but i think i can do better
    # for car in car_manager.parking_lot:
    #     if tim.distance(car) < 20:
    #         game_is_on = False

    loop_run += 1

screen.exitonclick()
