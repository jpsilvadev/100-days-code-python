"""Car Generator"""

from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    """Create car objects"""

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.create_car()
        self.drive_cars()
        self.increase_speed()

    def create_car(self):
        """Randomly generates a colored car."""
        car_spawn_rate = random.randint(1, 6)
        if car_spawn_rate == 1:
            car = Turtle()
            car.shape("square")
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.penup()
            random_num = random.randint(0, 5)
            car.color(COLORS[random_num])
            random_y = random.randint(-250, 250)
            car.goto(300, random_y)
            self.all_cars.append(car)

    def drive_cars(self):
        """Move cars forward."""
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        """Increase car speed."""
        self.car_speed += MOVE_INCREMENT
