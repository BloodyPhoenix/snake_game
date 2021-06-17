# -*- coding: utf-8 -*-


import pygame
from pygame.locals import *
import time
from random import randint


SIZE = 40


def get_apple_coordinates_multiplier(display_x: int, display_y: int):
    x = display_x//40-1
    y = display_y//40-1
    return x, y


class Apple:

    def __init__(self, screen: pygame.display, multipliers):
        self.apple = pygame.image.load("resourses/apple.jpg").convert()
        self.screen = screen
        self.multipliers = multipliers
        self.x = SIZE*randint(0, self.multipliers[0])
        self.y = SIZE*randint(0, self.multipliers[1])

    def change_position(self):
        self.x = SIZE * randint(0, self.multipliers[0])
        self.y = SIZE * randint(0, self.multipliers[1])

    def draw(self):
        self.screen.blit(self.apple, (self.x, self.y))
        pygame.display.flip()


class Snake:

    def __init__(self, screen: pygame.display):
        self.block = pygame.image.load("resourses/block.jpg").convert()
        self.direction = "right"
        self.length = 6
        self.x = [SIZE]*self.length
        self.y = [SIZE]*self.length
        self.screen = screen

    def draw(self):
        for i in range(self.length):
            self.screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    def grow(self):
        self.length += 1
        self.x += [[]]
        self.y += [[]]

    def move(self):
        self.screen.fill(color=(77, 199, 64))
        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]
        if "right" == self.direction:
            self.x[0] += SIZE
        elif "left" == self.direction:
            self.x[0] -= SIZE
        elif "up" == self.direction:
            self.y[0] -= SIZE
        else:
            self.y[0] += SIZE
        self.draw()


class SnakeGame:

    def __init__(self, x=1000, y=800):
        pygame.init()
        self.x = x
        self.y = y
        self.surface = pygame.display.set_mode(size=(self.x, self.y))
        self.apple_multiplier = (get_apple_coordinates_multiplier(self.x, self.y))
        self.surface.fill(color=(77, 199, 64))
        self.snake = Snake(self.surface)
        self.apple = Apple(self.surface, self.apple_multiplier)
        self.running = True

    def play(self):
        self.snake.move()
        self.check_obstacles()
        if self.snake.x[0] == self.apple.x:
            if self.snake.y[0] == self.apple.y:
                self.apple.change_position()
                self.snake.grow()
        self.apple.draw()

    def check_obstacles(self):
        for i in range(1, self.snake.length):
            if self.snake.x[i] == self.snake.x[0]:
                if self.snake.y[i] == self.snake.y[0]:
                    self.game_over()
        if self.snake.x[0] > self.x-SIZE:
            self.game_over()
        if self.snake.y[0] > self.y-SIZE:
            self.game_over()
        if self.snake.x[0] < 0:
            self.game_over()
        if self.snake.y[0] < 0:
            self.game_over()

    def game_over(self):
        self.running = False

    def run(self):
        while self.running:
            time.sleep(0.3)
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.running = False
                    elif event.key == K_UP:
                        self.snake.direction = "up"
                    elif event.key == K_DOWN:
                        self.snake.direction = "down"
                    elif event.key == K_LEFT:
                        self.snake.direction = "left"
                    elif event.key == K_RIGHT:
                        self.snake.direction = "right"
            self.play()


if __name__ == "__main__":
    game = SnakeGame()
    game.run()



