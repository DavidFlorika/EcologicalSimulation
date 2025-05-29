import random
import pygame
import sys
from Food import Food

class Consumer:
    width = 800
    height = 600

    # Initialize values
    def __init__(self, speed, x, y, size=5, hunger=50, quadrant=random.randint(1, 4), have_target=0, target_x=0,
                 target_y=0):
        """
        quadrant -> a direction for consumer to move when no food is targeted
        target_x, target_y -> the coordinates of the target
        """
        self.speed = speed
        self.hunger = hunger
        self.x = x
        self.y = y
        self.size = size
        self.quadrant = quadrant
        self.h_t = have_target
        self.t_x = target_x
        self.t_y = target_y

    # Draw a circle on the screen to display consumer
    def display(self, screen, color):
        pygame.draw.circle(screen, color, (self.x, self.y), self.size)

    # Eat food and increase "hunger"
    # check if any food object is within the range of eating
    def eat(self, food):
        if (abs(self.x - food.x) ** 2 + abs(self.y - food.y) ** 2) ** 0.5 <= 3:
            self.hunger += 10
            return True
        return False

    # Changing place to find food
    def go_around(self):
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

    # Moving towards the food detected
    def find_food(self, food):
        d_x = food.x - self.x
        d_y = food.y - self.y
        distance = (d_x ** 2 + d_y ** 2) ** 0.5
        if distance == 0:
            return True
        if distance <= 100:
            self.h_t = 1
            self.t_x = food.x
            self.t_y = food.y
            self.x += d_x / distance * min(distance, self.speed)
            self.y += d_y / distance * min(distance, self.speed)
            return True
        return False

    #Calculate the time needed to reach the targeted food
    def time_needed(self, food):
        distance = abs(food.x - self.x) + abs(food.y - self.y)
        time_need = round(distance / self.speed) + 5
        return time_need

    #Try to reach the food when it already has a target
    def find_food_ht(self):
        d_x = self.t_x - self.x
        d_y = self.t_y - self.y
        distance = (d_x ** 2 + d_y ** 2) ** 0.5
        if distance == 0:
            self.h_t = 0
            return True
        if distance <= 100:
            self.x += d_x / distance * min(distance, self.speed)
            self.y += d_y / distance * min(distance, self.speed)
            return True
        return False

    #Find a food near it
    def hunt(self, curent, all_food):
        for food in all_food:
            if food.targeted == 0:
                if self.find_food(food):
                    food.time_caught = curent
                    food.targeted = 1
                    food.time_needed = self.time_needed(food)
                    return True
        return False
