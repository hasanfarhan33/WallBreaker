from Paddle import Paddle
from Ball import Ball
from Brick import Brick
import pygame
from pygame import gfxdraw
import sys
import random

#Setting up the display
windowSize = windowWidth, windowHeight = 900, 500
FPS = 60
clock = pygame.time.Clock()

LIVES = 3

#INSTANTIATING CLASSES HERE
paddle = Paddle()
ball = Ball()
brick = Brick()

#TESTING BRICKS HERE
brick.brickX = 100
brick.brickY = 100


def drawingWindow():
    pygame.display.set_caption("Wallbreaker")
    window = pygame.display.set_mode(windowSize)
    return window

def drawStuff(window):
    # Drawing the paddle
    pygame.draw.rect(window, paddle.paddleColor,
                     (paddle.paddleX, paddle.paddleY, paddle.paddleWidth, paddle.paddleHeight), border_radius=5)
    # Drawing the ball (might change the ball to a rect)
    pygame.draw.circle(window, ball.ballColor, (ball.ballX, ball.ballY), ball.ballRadius)

    # Drawing bricks here
    # TODO: Add random colors to the brick or pick a random color from an array of colors
    pygame.draw.rect(window, (255, 255, 255), (brick.brickX, brick.brickY, brick.brickWidth, brick.brickHeight))

def handleBrickCollisions(ball, brick):
    #Bottom of the brick
    if ball.ballX + ball.ballRadius < brick.brickX + brick.brickWidth and ball.ballX + ball.ballRadius > brick.brickX:
        if ball.ballY + ball.ballRadius <= brick.brickY + brick.brickHeight and ball.ballY + ball.ballRadius > brick.brickY:
            print("THE BALL IS INSIDE THE BRICK")


def handleBallMovement(ball):
    ball.ballX += ball.ballXSpeed
    ball.ballY += ball.ballYSpeed

    if ball.ballX + ball.ballRadius >= windowWidth or ball.ballX - ball.ballRadius <= 0:
        ball.ballXSpeed *= -1
    if ball.ballY - ball.ballRadius <= 0:
        ball.ballYSpeed *= -1
    if ball.ballY > windowHeight:
        ball.ballLaunched = False
        ball.ballXSpeed = 0
        ball.ballYSpeed = 0
        ball.ballX = paddle.paddleX + paddle.paddleWidth / 2 - ball.ballRadius / 2
        ball.ballY = paddle.paddleY - paddle.paddleHeight + 1
        #TODO: decrement lives here


    #Detecting ball's collision with the paddle
    if ball.ballX >= paddle.paddleX and ball.ballX <= paddle.paddleX + paddle.paddleWidth and ball.ballY + ball.ballRadius >= paddle.paddleY and ball.ballY + ball.ballRadius >= paddle.paddleY:
        ball.ballYSpeed *= -1

        #Change the XSpeed of the ball based on where the ball lands on the paddle
        if ball.ballX < paddle.paddleX + paddle.paddleWidth / 2: #The ball is on the left side of the paddle
            if ball.ballXSpeed > 0:
                ball.ballXSpeed *= -1
        if ball.ballX >= paddle.paddleX + paddle.paddleWidth/2: #The ball is on the right side of the paddle
            if ball.ballXSpeed < 0:
                ball.ballXSpeed *= -1



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
            if not ball.ballLaunched:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #TODO: If the paddle is on the right side of the screen the ball should go left
                    ball.ballYSpeed = random.randint(-3, -2)
                    ball.ballXSpeed = -random.randint(-3, -2)
                    ball.ballLaunched = True


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
        handleBrickCollisions(ball, brick)
        drawStuff(WINDOW)
        pygame.display.update()


if __name__ == "__main__":
    main()