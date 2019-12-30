import pygame, sys
from ball import ball
from paddle import paddle
import tensorflow as tf
import keras

pygame.init()

size = width, height = 250, 400
color = (0,0,255)
ballColor = (255,0,0)

bG = (0,0,0)

pygame.display.set_caption('Pong')
 
boll = ball()
paddleUp = paddle(120,0)
paddleDown = paddle(100, 380)

print(paddleDown.getWidth())


screen = pygame.display.set_mode(size)
gameExit = False
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: gameExit=True
    screen.fill(bG)
    pygame.draw.rect(screen, color, [paddleUp.getWidth(), paddleUp.getHeight(), paddleUp.getwidth(), paddleUp.getheight()])
    pygame.draw.rect(screen, color, [paddleDown.getWidth(), paddleDown.getHeight(), paddleDown.getwidth(), paddleDown.getheight()])
    boll.move()
    circle1 = pygame.draw.circle(screen, ballColor, (int(boll.getWidth()), boll.getHeight()), boll.getSize(), boll.getThick())
    #odbijanie polki od scian
    if boll.getWidth() >= 240:
        boll.setSpeedxOpposite()
    elif boll.getWidth() <= 10:
        boll.setSpeedxOpposite()

    if boll.srodek() > paddleUp.srodek():
        if not paddleUp.getWidth() == 176:
            paddleUp.Right()
    elif boll.srodek() < paddleUp.srodek():
        if not paddleUp.getWidth() == 0:
            paddleUp.Left()

    #ODbijanie pilki od paletki
    if boll.getHeight() == 370 and boll.getWidth() >= paddleDown.getWidth()- 10 and boll.getWidth() <= paddleDown.getwidth() + paddleDown.getWidth() + 10:
        boll.setSpeedyOppostie()
        paddleDown.updateScore()
    if boll.getHeight() == 30 and boll.getWidth() >= paddleUp.getWidth()-10  and boll.getWidth() <= paddleUp.getwidth() + paddleUp.getWidth()+10:
        boll.setSpeedyOppostie()
    #if boll.getHeight() > 370 and boll.getWidth() <= paddleDown.getWidth() + paddleDown.getwidth() + 10 :
     #  boll.setSpeedxOpposite()


    key_pressed = pygame.key.get_pressed()


    if key_pressed[pygame.K_LEFT] and not paddleDown.getWidth() == 0:
        paddleDown.Left()

    if key_pressed[pygame.K_RIGHT] and not paddleDown.getWidth() == 176:
        paddleDown.Right()

    pygame.display.update()
    pygame.time.wait(15)
