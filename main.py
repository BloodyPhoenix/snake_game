# -*- coding: utf-8 -*-


import pygame
from pygame.locals import *
import time


class Snake:

    def __init__(self, screen: pygame.display):
        self.block = pygame.image.load("resourses/block.jpg").convert()
        self.x = 100
        self.y = 100
        self.screen = screen

    def draw(self):
        self.screen.fill(color=(77, 199, 64))
        self.screen.blit(self.block, (self.x, self.y))
        pygame.display.flip()


class SnakeGame:

    def __init__(self):
        pygame.init()
        self.direction = "right"
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
                        self.direction = "up"
                    elif event.key == K_DOWN:
                        self.direction = "down"
                    elif event.key == K_LEFT:
                        self.direction = "left"
                    elif event.key == K_RIGHT:
                        self.direction = "right"
            if "right" == self.direction:
                self.snake.x += 10
            elif "left" == self.direction:
                self.snake.x -= 10
            elif "up" == self.direction:
                self.snake.y -= 10
            else:
                self.snake.y += 10
            self.snake.draw()


if __name__ == "__main__":
    game = SnakeGame()
    game.run()



