import pygame


class Paddle():
    def __init__(self, pos, player):
        self.pos = pos
        self.player = player
        self.size = (30, 100)
        self.colour = (255, 255, 255)
        self.opos = pos

    def move(self, keys):
        change = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        if keys[pygame.K_UP] and self.player == 0:
            change = -10
        elif keys[pygame.K_DOWN] and self.player == 0:
            change = 10
        elif keys[pygame.K_w] and self.player == 1:
            change = -10
        elif keys[pygame.K_s] and self.player == 1:
            change = 10
        self.pos = (self.pos[0], self.pos[1] + change)
        self.change = change

    def draw(self, win):
        pygame.draw.rect(win, self.colour, (self.pos, self.size))


class Ball():
    def __init__(self, pos):
        self.opos = pos
        self.pos = pos
        self.colour = (255, 255, 255)
        self.size = 10
        self.dir = 10
        self.dir1 = 0

    def move(self):
        self.pos = (self.pos[0] + self.dir, self.pos[1] + self.dir1)

    def bounce(self, paddle):
        if paddle == 0:
            self.dir1 = self.dir1 * -1
        else:
            self.dir = self.dir * -1
            self.dir1 = self.dir1 + paddle.change

    def draw(self, win):
        pygame.draw.circle(win, self.colour, self.pos, self.size)
