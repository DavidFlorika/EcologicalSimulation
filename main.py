import sys
import random
import pygame
import math
from Consumer import Consumer
from Food import Food
from Predator import Predator

class main:
    X = 800
    Y = 600
    def __init__(self):
        pass

    def run(self):
        # default setting
        time_past = 0
        screen = pygame.display.set_mode((self.X, self.Y))
        pygame.init()
        pygame.font.init()

        # Set screen
        pygame.display.set_caption('Ecological simulation')
        white = (255, 255, 255)
        green = (0, 255, 0)
        red = (255, 0, 0)
        purple = (255, 0, 255)
        black = (0, 0, 0)
        clock = pygame.time.Clock()
        fps = 15
        font = pygame.font.Font('freesansbold.ttf', 15)

        # ask for user input
        num_consumer = int(input("Number of consumers: "))
        speed_consumer = int(input("Speed of consumer: "))
        num_predator = int(input("Number of predators: "))
        num_food = int(input('Enter Number of food:'))

        # Build arrays for consumer & food
        # including two random x, y coordinates
        all_consumer = [Consumer(speed_consumer, random.randint(0, 800), random.randint(0, 600)) for _ in range(num_consumer)]
        all_predator = [Predator(speed_consumer + 3, random.randint(0, 800), random.randint(0, 600)) for _ in
                        range(num_predator)]
        all_food = [Food(random.randint(0, 800), random.randint(0, 600)) for _ in range(num_food)]

        # Body
        while True:
            time_past += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Reproduction, and consumer seeking for food
            for consumer in all_consumer:
                # Hunger examining and changing
                if consumer.hunger >= 100:
                    consumer.hunger = 50
                    new_consumer = Consumer(speed_consumer, consumer.x + random.randint(-30, 30),
                                            consumer.y + random.randint(-30, 30))
                    new_consumer.x = max(0, min(new_consumer.x, consumer.width))
                    new_consumer.y = max(0, min(new_consumer.y, consumer.height))
                    all_consumer.append(new_consumer)
                elif consumer.hunger <= 0:
                    all_consumer.remove(consumer)
                consumer.hunger -= 1
                # Consumer going toward the targeted food, and eat() function determines whether a food is eaten
                if consumer.h_t == 1:
                    if consumer.find_food_ht():
                        for food in all_food:
                            if consumer.eat(food):
                                consumer.h_t = 0
                                all_food.remove(food)
                                consumer.hunger += 8
                                break
                else:
                    if consumer.hunt(time_past, all_food):
                        for food in all_food:
                            if consumer.eat(food):
                                all_food.remove(food)
                                consumer.hunger += 8
                                break
                    else:
                        # going around randomly but within a limited direction
                        consumer.go_around()
            
            # food reproduction
            for food in all_food:
                # Prevent from continuously being targeted even the consumer is dead
                if time_past - food.time_caught >= food.time_needed:
                    food.targeted = 0
                food.hunger += 1.2
                # split food
                if food.hunger >= random.randint(50, 100):
                    food.hunger = 0
                    new_food = Food(food.x + random.randint(-100, 100), food.y + random.randint(-100, 100))
                    new_food.x = max(0, min(new_food.x, food.width))
                    new_food.y = max(0, min(new_food.y, food.height))
                    all_food.append(new_food)
            
            # Predator reproduction and seeking for food
            for predator in all_predator:
                # Hunger examining and changing
                if predator.hunger >= 150:
                    predator.hunger = 50
                    new_predator = Predator(speed_consumer + 3, predator.x + random.randint(-30, 30),
                                            predator.y + random.randint(-30, 30))
                    new_predator.x = max(0, min(new_predator.x, predator.width))
                    new_predator.y = max(0, min(new_predator.y, predator.height))
                    all_predator.append(new_predator)
                elif predator.hunger <= 0:
                    all_predator.remove(predator)

                predator.hunger -= 0.3

                if predator.hunt(all_consumer):
                    for consumer in all_consumer:
                        if predator.eat(consumer):
                            all_consumer.remove(consumer)
                            break
                else:
                    predator.go_around()
            
            # Refresh screen
            screen.fill(white)
            for consumer in all_consumer:
                consumer.display(screen, red)
            for food in all_food:
                food.display(screen, green)
            for predator in all_predator:
                predator.display(screen, purple)
            
            # Display living creatures
            data_food = font.render(f'Number of food:{len(all_food)}', True, black)
            data_consumer = font.render(f'Number of consumer:{len(all_consumer)}', True, black)
            data_predator = font.render(f'Number of predator:{len(all_predator)}', True, black)
            
            rectFood = data_food.get_rect()
            rectConsumer = data_consumer.get_rect()
            rectPredator = data_predator.get_rect()
            # Set all texts at the left bottom corner
            rectFood.topleft = (45, 545)
            rectConsumer.topleft = (45, 560)
            rectPredator.topleft = (45, 575)
            
            screen.blit(data_food, rectFood)
            screen.blit(data_consumer, rectConsumer)
            screen.blit(data_predator, rectPredator)

            pygame.display.update()
            clock.tick(fps)

if __name__ == "__main__":
    main().run()
# This code is the main entry point for the ecological simulation game.