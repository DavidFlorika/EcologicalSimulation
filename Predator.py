import random
import pygame
import sys
from Consumer import Consumer

class Predator:
    width = 800
    height = 600

    def __init__(self, speed, x, y, hunger=50, size=10, quadrant=random.randint(1, 4)):
        """
        quadrant -> the direction of predator going when nothing is targeted
        """
        self.speed = speed
        self.x = random.randint(0, 800)
        self.y = random.randint(0, 600)
        self.hunger = hunger
        self.size = size
        self.quadrant = quadrant

    def display(self, screen, color):
        pygame.draw.circle(screen, color, (self.x, self.y), self.size)

    def eat(self, consumer):
        if (abs(self.x - consumer.x) ** 2 + abs(self.y - consumer.y) ** 2) ** 0.5 <= 5:
            self.hunger += 10
            return True
        return False

    def go_around(self):
        """
        See Consumer.go_around function
        """
        choice_one = [1, 3]
        choice_two = [2, 4]
        if self.quadrant == 1 or self.quadrant == 2:
            self.y += random.randint(0, self.speed)
        else:
            self.y -= random.randint(0, self.speed)
        if self.quadrant == 1 or self.quadrant == 4:
            self.x += random.randint(0, self.speed)
        else:
            self.x -= random.randint(0, self.speed)
        if self.x >= 800 or self.x <= 0 or self.y >= 600 or self.y <= 0:
            if self.quadrant == 1:
                self.quadrant = random.choice(choice_two)
            elif self.quadrant == 2:
                self.quadrant = random.choice(choice_one)
            elif self.quadrant == 3:
                self.quadrant = random.choice(choice_two)
            elif self.quadrant == 4:
                self.quadrant = random.choice(choice_one)

    def find_consumer(self, consumer):
        """
        See Consumer.find_food function
        """
        d_x = consumer.x - self.x
        d_y = consumer.y - self.y
        distance = (d_x ** 2 + d_y ** 2) ** 0.5
        if distance == 0:
            return True
        if distance <= 150:
            self.x += d_x / distance * min(distance, self.speed)
            self.y += d_y / distance * min(distance, self.speed)
            return True
        return False

    def hunt(self, all_consumer):
        for consumer in all_consumer:
            if self.find_consumer(consumer):
                return True
        return False
