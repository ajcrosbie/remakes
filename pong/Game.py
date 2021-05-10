import pygame
import Objects


def redrawWindow(win, ball, paddle, paddle1):
    win.fill((0, 0, 0))
    ball.draw(win)
    paddle.draw(win)
    paddle1.draw(win)
    pygame.display.update()


def reset(ball, paddle, paddle1):
    ball.pos = ball.opos
    ball.dir1 = 0
    ball.dir = 10
    paddle.pos = paddle.opos
    paddle1.pos = paddle1.opos


def touching(ball, paddle):
    if ball.pos[0] > paddle.pos[0]:
        if ball.pos[0] < paddle.pos[0] + paddle.size[0]:
            if ball.pos[1] < paddle.pos[1] + paddle.size[1]:
                if ball.pos[1] > paddle.pos[1]:
                    ball.bounce(paddle)


def main():
    width = 750
    height = 500
    win = pygame.display.set_mode((width, height))
    paddle = Objects.Paddle((10, height/2 - 50), 1)
    paddle1 = Objects.Paddle((width - paddle.size[0] - 10, height/2 - 50), 0)
    ball = Objects.Ball((width//2, height//2))
    running = True
    clock = pygame.time.Clock()
    while running:
        pygame.time.delay(60)
        clock.tick(10)
        keys = pygame.key.get_pressed()
        paddle.move(keys)
        paddle1.move(keys)
        ball.move()
        touching(ball, paddle)
        touching(ball, paddle1)
        redrawWindow(win, ball, paddle, paddle1)
        if ball.pos[1] < 0 or ball.pos[1] > height:
            ball.bounce(0)
        if ball.pos[0] < 0 or ball.pos[0] > width:
            reset(ball, paddle, paddle1)


if __name__ == "__main__":
    main()
