import time
from turtle import Screen
from player import PLayer
from cars import CarManager
from Scoreboard import Scoreboard





screen = Screen()
screen.setup(width=480, height=680)
screen.tracer(0)


player = PLayer()
car_manager =CarManager()
Scoreboard =Scoreboard()


screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on =True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
         if car.distance(player) < 20:
             game_is_on = False
             Scoreboard.game_over()


    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        Scoreboard.increase_level()




screen.exitonclick()