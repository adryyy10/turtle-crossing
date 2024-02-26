import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(1, 3)
            new_car.goto(random.randint(300, 400), random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            new_x = car.xcor() - self.car_speed
            car.goto(new_x, car.ycor())

    def increase_speed_all_cars(self):
        self.car_speed += MOVE_INCREMENT
