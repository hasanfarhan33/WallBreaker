from Paddle import Paddle
from Ball import Ball
import pygame
from pygame import gfxdraw
import sys

#Setting up the display
windowSize = windowWidth, windowHeight = 900, 500
FPS = 60
clock = pygame.time.Clock()

LIVES = 3

#INSTANTIATING CLASSES HERE
paddle = Paddle()
ball = Ball()


def drawingWindow():
    pygame.display.set_caption("Wallbreaker")
    window = pygame.display.set_mode(windowSize)
    return window

def handleBallMovement(ball):
    ball.ballX += ball.ballXSpeed
    ball.ballY += ball.ballYSpeed

    if ball.ballX + ball.ballRadius >= windowWidth or ball.ballX - ball.ballRadius <= 0:
        ball.ballXSpeed *= -1
    if ball.ballY - ball.ballRadius <= 0:
        ball.ballYSpeed *= -1

    #Detecting ball's collision with the paddle
    if ball.ballX >= paddle.paddleX and ball.ballX <= paddle.paddleX + paddle.paddleWidth and ball.ballY + ball.ballRadius >= paddle.paddleY and ball.ballY + ball.ballRadius >= paddle.paddleY:
        ball.ballYSpeed *= -1
        #Change the XSpeed of the ball based on where the ball lands on the paddle




def main():
    pygame.init()
    WINDOW = drawingWindow()

    running = True
    while running:
        clock.tick(FPS)
        pygame.mouse.set_visible(False)
        mouseX, mouseY = pygame.mouse.get_pos()
        #Handling events here
        for event in pygame.event.get():
            #Closing the game when press x
            if event.type == pygame.QUIT:
                running = False

            #Detect mouse click to start the game
            if event.type == pygame.MOUSEBUTTONDOWN:
                ball.ballYSpeed = -1
                ball.ballXSpeed = -3

            #Assigning the location of the paddle to the X Position of the mouse
            paddle.paddleX = mouseX - paddle.paddleWidth/2
            paddle.paddleY = windowHeight - paddle.paddleHeight - 5

            #Keeping the ball on the paddle in the beginning of the game
            if ball.ballXSpeed == 0 and ball.ballYSpeed == 0:
                ball.ballX = paddle.paddleX + paddle.paddleWidth/2 - ball.ballRadius/2
                ball.ballY = paddle.paddleY - paddle.paddleHeight + 1

        #Drawing things here (TURN THIS INTO A FUNCTION LATER)
        #Window background
        WINDOW.fill((0, 0, 0))
        handleBallMovement(ball)

        # Drawing the paddle
        pygame.draw.rect(WINDOW, paddle.paddleColor, (paddle.paddleX, paddle.paddleY, paddle.paddleWidth, paddle.paddleHeight), border_radius=5)
        pygame.draw.circle(WINDOW, ball.ballColor, (ball.ballX, ball.ballY), ball.ballRadius)
        pygame.display.update()


if __name__ == "__main__":
    main()