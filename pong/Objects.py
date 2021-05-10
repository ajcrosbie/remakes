import pygame
import random


class Paddle():
    def __init__(self, pos, player):
        self.pos = pos
        self.player = player
        self.size = (30, 100)
        self.colour = (255, 255, 255)

    def move(self, keys):
        change = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        if keys[pygame.K_UP]:
            change = -10
        elif keys[pygame.K_DOWN]:
            change = 10
        elif keys[pygame.K_w]:
            change = -10
        elif keys[pygame.K_s]:
            change = 10
        self.pos = (self.pos[0], self.pos[1] + change)
        self.change = change

    def draw(self, win):
        pygame.draw_rect(win, self.colour, (self.pos, self.size))


class Ball():
    def __init__(self, pos):
        self.pos = pos
        self.colour = (255, 255, 255)
        self.size = 10
        self.dir1 = 10
        self.dir = 0

    def move(self):
        self.pos = (self.pos[0] + self.dir, self.pos[1] + self.dir1)

    def bounce(self, paddle):
        if paddle == 0:
            self.dir1 = self.dir * -1
            self.dir = self.dir * -1
        else:
            self.dir = self.dir * -1
            self.dir1 = self.dir1 + paddle.change

    def draw(self, win):
        pygame.draw.circle(win, self.colour, self.pos, self.size)
