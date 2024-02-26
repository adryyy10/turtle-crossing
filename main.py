import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move_up, "w")
screen.onkey(player.move_down, "s")

game_is_on = True
loop = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # Detect player has arrived at the top
    if player.ycor() >= player.finish_line:
        player.update_player_position()
        scoreboard.increase_point()
        car_manager.increase_speed_all_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if player.distance(car) < 30:
            game_is_on = False

    loop += 1


scoreboard.game_over()
screen.exitonclick()

