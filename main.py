# -*- coding: utf-8 -*-


import pygame
from pygame.locals import *
import time


class Snake:

    def __init__(self, screen: pygame.display):
        self.block = pygame.image.load("resourses/block.jpg").convert()
        self.direction = "right"
        self.length = 6
        self.x = [40]*self.length
        self.y = [40]*self.length
        self.screen = screen

    def draw(self):
        self.screen.fill(color=(77, 199, 64))
        for i in range (self.length):
            self.screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    def move(self):
        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]
        if "right" == self.direction:
            self.x[0] += 40
        elif "left" == self.direction:
            self.x[0] -= 40
        elif "up" == self.direction:
            self.y[0] -= 40
        else:
            self.y[0] += 40
        self.draw()


class SnakeGame:

    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode(size=(1000, 700))
        self.surface.fill(color=(77, 199, 64))
        self.snake = Snake(self.surface)
        self.snake.draw()

    def run(self):
        running = True
        while running:
            time.sleep(0.5)
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    elif event.key == K_UP:
                        self.snake.direction = "up"
                    elif event.key == K_DOWN:
                        self.snake.direction = "down"
                    elif event.key == K_LEFT:
                        self.snake.direction = "left"
                    elif event.key == K_RIGHT:
                        self.snake.direction = "right"
            self.snake.move()


if __name__ == "__main__":
    game = SnakeGame()
    game.run()



