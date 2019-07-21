import pygame
import time
import random
import RPi.GPIO as GPIO
import coregame as cg
 
def textObjects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
 
def messageDisplay(text,fSize=110,hDivide=4.5):
    largeText = pygame.font.Font('LCD-N___.TTF',fSize)
    TextSurf, TextRect = textObjects(text, largeText)
    TextRect = ((display_width/2.2),(display_height/hDivide))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

def animate():
    firstImg=pygame.image.load("Yoshi.png")
    buttonImg=pygame.image.load("redbutton.png")
    pygame.display.update()
    
    x=100
    z=180
    step=12
    k=0
    for i in range (0,5):
        for y in range (k,z,step):
            gameDisplay.fill(background_colour)
            gameDisplay.blit(buttonImg, (20,480))
            gameDisplay.blit(firstImg, (x,y))
            if i==1 or i==2:
                messageDisplay("Hit")
            elif i==3 or i==4:
                messageDisplay("Hit The")    
            gameDisplay.blit(buttonImg, (20,480))
            gameDisplay.blit(firstImg, (x,y))
            pygame.display.update()
        temp=k
        k=z
        z=temp
        step=-(step)
    messageDisplay("Hit The Button !")
    pygame.display.update()
 
def ledFlash(a):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(a, GPIO.OUT)
    for i in range (0,3):
        GPIO.output(a, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(a, GPIO.HIGH)
        time.sleep(0.5)
 
def anySwitch():
    switchdetect=(22,27,17,4,18)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(switchdetect, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setwarnings(True)
    while True:
        for i in range(5):
            input_state = GPIO.input(switchdetect[i])
            if input_state == False:
                time.sleep(0.01)
                return

def countDown():
    for i in range(5,0,-1):
        gameDisplay.fill(background_colour)
        gameDisplay.blit(buttonImg, (20,480))
        gameDisplay.blit(firstImg, (x,y))
        messageDisplay("Get Ready  "+str(i))
        pygame.display.update()
        if i==0:
            return
        time.sleep(1)


##MAIN

pygame.init()
pygame.mixer.music.load('bensound-jazzyfrenchy.wav')
pygame.mixer.music.play(-1)
 
black = (0,0,0)
out=(26,19,13,6,5)
display_width = 1600
display_height = 1000
gameDisplay=pygame.display.set_mode ((display_width,display_height))
pygame.display.set_caption('Hit the Button')
background_colour=(0,150,150)
gameDisplay.fill(background_colour)
pygame.display.update()
 
animate()
 
ledFlash()
messageDisplay("Press to Continue",80,1.5)
pygame.display.update()
anySwitch()
GPIO.output(out, GPIO.LOW)
time.sleep(0.1)
 
countDown()
cg.play()

gameDisplay.blit(buttonImg, (20,480))
gameDisplay.blit(firstImg, (x,y))
pygame.display.update()
 
exit()
