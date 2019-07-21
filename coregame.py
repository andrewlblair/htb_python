import pygame
import time
import random
import RPi.GPIO as GPIO
 
def play():

    def textObjects(text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()
 
    def messageDisplay(text,fSize=150,hDivide=1.5):
        largeText = pygame.font.Font('LCD-N___.TTF',fSize)
        TextSurf, TextRect = textObjects(text, largeText)
        TextRect = ((display_width/2.2),(display_height/hDivide))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
       
    def setupPins():
        a=(26,19,13,6,5)
        b=(22,27,17,4,18)
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(True)
        GPIO.setup(a, GPIO.OUT)
        GPIO.setup(b, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.output(a, GPIO.LOW)
        return a,b
 
    def switchDetect(a,b,c):
        d=0
        for i in range(5):
            if c == a[i]:
                d = b[i]
                break
        print(i)
        while True:
            if GPIO.input(d) == False:
                time.sleep(0.01)
                return a[i]

    pygame.init()
    black = (0,0,0)
    display_width = 1600
    display_height = 1000
    gameDisplay=pygame.display.set_mode ((display_width,display_height))
    pygame.display.set_caption('Hit the Button')
    background_colour=(0,150,150)
    gameDisplay.fill(background_colour)
    pygame.display.update()
 
            
    display_width=600
    display_height = 550
    messageDisplay("Hit The Button !")    
    display_width=1600
    display_height = 1000
    out,detect=setupPins()
    
    start=time.time()
    e=-1
    for i in range (0,20):
        while True:
            c=random.choice(out)
            if c!=e:
                break
        GPIO.output(c, GPIO.HIGH)
        #call button function
        e=switchDetect(out,detect,c)
        GPIO.output(c, GPIO.LOW)
       
    GPIO.cleanup()
    end=time.time()
    total=end-start
    result = '{:0>.3f}'.format(round(total,3))
 
    gameDisplay.fill(background_colour)
    pygame.display.update()
    messageDisplay(str(result)+"  sec",110,4.5)
    messageDisplay("Great Time !")
