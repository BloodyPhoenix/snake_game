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
        self.screen.fill(color=(77, 199, 64))
        self.screen.blit(self.apple, (self.x, self.y))
        pygame.display.flip()


class Snake:

    def __init__(self, screen: pygame.display):
        self.block = pygame.image.load("resourses/block.jpg").convert()
        self.direction = "right"
        self.length = 3
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
        self.font = pygame.font.SysFont("arial", 30)
        self.surface = pygame.display.set_mode(size=(self.x, self.y))
        self.apple_multiplier = (get_apple_coordinates_multiplier(self.x, self.y))
        self.surface.fill(color=(77, 199, 64))
        self.snake = Snake(self.surface)
        self.apple = Apple(self.surface, self.apple_multiplier)
        self.running = True

    def _play(self):
        self.apple.draw()
        self.snake.move()
        self._check_obstacles()
        if self.snake.x[0] == self.apple.x:
            if self.snake.y[0] == self.apple.y:
                self.apple.change_position()
                self.snake.grow()

    def _check_obstacles(self):
        for i in range(1, self.snake.length):
            if self.snake.x[i] == self.snake.x[0]:
                if self.snake.y[i] == self.snake.y[0]:
                    self._game_over()
        if self.snake.x[0] > self.x-SIZE:
            self._game_over()
        if self.snake.y[0] > self.y-SIZE:
            self._game_over()
        if self.snake.x[0] < 0:
            self._game_over()
        if self.snake.y[0] < 0:
            self._game_over()

    def _game_over(self):
        self.surface.fill((0, 0, 0))

        score = self.snake.length-3
        label = self.font.render(f"Игра окончена! Количество съеденных яблок - {score}!", True, (122, 122, 122))
        escape_label = self.font.render("Чтобы выйти, нажмите клавишу Esc", True, (122, 122, 122))
        enter_label = self.font.render("Чтобы сыграть ещё раз, нажмите клавишу Enter", True, (122, 122, 122))
        self.surface.blit(label, (200, 300))
        self.surface.blit(escape_label, (200, 400))
        self.surface.blit(enter_label, (200, 500))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    return
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.running = False
                        return
                    if event.key == K_RETURN:
                        self.snake = Snake(self.surface)
                        return

    def _pause(self):
        while True:
            pause_label = self.font.render("Игра на паузе", True, (0, 0, 0))
            cont_label = self.font.render("Для продолжения нажмите клавишу Enter", False, (0, 0, 0))
            self.surface.blit(pause_label, (400, 300))
            self.surface.blit(cont_label, (200, 400))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == QUIT:
                    self._game_over()
                    return
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        return

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self._game_over()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        self._pause()
                    if event.key == K_ESCAPE:
                        self._game_over()
                    elif event.key == K_UP:
                        if not self.snake.direction == "down":
                            self.snake.direction = "up"
                    elif event.key == K_DOWN:
                        if not self.snake.direction == "up":
                            self.snake.direction = "down"
                    elif event.key == K_LEFT:
                        if not self.snake.direction == "right":
                            self.snake.direction = "left"
                    elif event.key == K_RIGHT:
                        if not self.snake.direction == "left":
                            self.snake.direction = "right"
            self._play()
            time.sleep(0.3)


if __name__ == "__main__":
    game = SnakeGame()
    game.run()



