"""Turtle Crossing Game!"""

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Create keybinds
screen.listen()
screen.onkey(key="Up", fun=player.move_up)
screen.onkey(key="Down", fun=player.move_down)
screen.onkey(key="Left", fun=player.move_left)
screen.onkey(key="Right", fun=player.move_right)


GAME_ON = True
while GAME_ON:
    scoreboard.set_level()
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.drive_cars()

    # Detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            GAME_ON = False
            scoreboard.player_loss()

    # Detect succesful crossing --> Start new level
    if player.level_complete():
        player.go_start()
        scoreboard.update_level()
        car_manager.increase_speed()


screen.exitonclick()
