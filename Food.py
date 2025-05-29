import random
import pygame
import sys

class Food:
    # setting up screen size and color
    width = 800
    height = 600
    green = (0, 128, 0)

    # customize variables, (x, y) are coordinates
    def __init__(self, x, y, size=3, hunger=0, targeted=0, time_caught=0, time_needed = 0):
        """
        targeted -> for determine whether a food is targeted, which prevents multiple consumers targeting one food
        time_needed -> a variable in calculating time for consumer to reach itself
        time_caught -> for determing how long has it been targeted
        """
        self.x = x
        self.y = y
        self.size = size
        self.hunger = hunger
        self.targeted = targeted
        self.time_caught = time_caught
        self.time_needed = time_needed

    # draw a circle of food
    def display(self, screen, color):
        pygame.draw.circle(screen, color, (self.x, self.y), self.size)
