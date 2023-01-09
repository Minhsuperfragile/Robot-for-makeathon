import pygame
from subprocess import call
import RPi.GPIO as GPIO          
from time import sleep

# set up pin out
in1 = 40
in2 = 38
ena = 36

in3 = 33
in4 = 35
enb = 37

in5 = 13
in6 = 15
enc = 11

in7 = 3
in8 = 5
end = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(ena,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)

GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)

GPIO.setup(in5,GPIO.OUT)
GPIO.setup(in6,GPIO.OUT)
GPIO.setup(enc,GPIO.OUT)
GPIO.output(in5,GPIO.LOW)
GPIO.output(in6,GPIO.LOW)

GPIO.setup(in7,GPIO.OUT)
GPIO.setup(in8,GPIO.OUT)
GPIO.setup(end,GPIO.OUT)
GPIO.output(in7,GPIO.LOW)
GPIO.output(in8,GPIO.LOW)

pa=GPIO.PWM(ena,1000)
pa.start(100)

pb=GPIO.PWM(enb,1000)
pb.start(100)

pc=GPIO.PWM(enc,1000)
pc.start(100)

pd=GPIO.PWM(end,1000)
pd.start(100)

# define some constant
width = 1366
heigh = 720
url = 'https://www.facebook.com/'
active = 0
run = True

# start pygame and set up display,fps,font,etc
pygame.init()
screen = pygame.display.set_mode((width,heigh))
pygame.display.set_caption('REM')
clock = pygame.time.Clock()
mainFont = pygame.font.Font('font/Pixeltype.ttf',50)
movement = 'shit'
# Locate source file for app
initialScreen = pygame.image.load('background.jpg').convert()
initialScreen = pygame.transform.scale(initialScreen, (width,heigh)) #scale the image
initialQrCode = pygame.image.load('initialQrCode.png').convert_alpha()
initialQrCode = pygame.transform.scale(initialQrCode,(500,500))

otherProjectScreen = pygame.image.load('otherProjectScreen.jpg').convert()
# otherPSRect = otherProjectScreen.get_rect(topleft=(0,0))
background = pygame.image.load('logarith.jpg').convert()
cuteFace = pygame.image.load('cuteFace.jpg').convert()
cuteFace = pygame.transform.scale(cuteFace,(width,heigh))
staffScreen1 = pygame.image.load('staff1.jpg').convert()
staffScreen1 = pygame.transform.scale(staffScreen1, (width,heigh))
staffScreen2 = pygame.image.load('staff2.jpg').convert()
staffScreen2 = pygame.transform.scale(staffScreen2, (width,heigh))
staffScreen3 = pygame.image.load('staff3.jpg').convert()
staffScreen3 = pygame.transform.scale(staffScreen3, (width,heigh))

stateList = [0,1,2,3,4,5,6]
counter = 0

def displayWebStatus(status):
    statusSurface = mainFont.render(str(status), False, (64,64,64))
    statusRectangle = statusSurface.get_rect(midtop = (456,200))
    screen.blit(statusSurface,statusRectangle)

# movement functions for robot that will be added in future
def moveForward():
    movement = 'Forward'
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)

def moveBackward():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)

def turnRight():
    GPIO.output(in5,GPIO.HIGH)
    GPIO.output(in6,GPIO.LOW)
    GPIO.output(in7,GPIO.HIGH)
    GPIO.output(in8,GPIO.LOW)

def turnLeft():
    GPIO.output(in5,GPIO.LOW)
    GPIO.output(in6,GPIO.HIGH)
    GPIO.output(in7,GPIO.LOW)
    GPIO.output(in8,GPIO.HIGH)

def stop():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    GPIO.output(in5,GPIO.LOW)
    GPIO.output(in6,GPIO.LOW)
    GPIO.output(in7,GPIO.LOW)
    GPIO.output(in8,GPIO.LOW)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
#         define key stroke for movement 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                moveForward()
            if event.key == pygame.K_DOWN:
                moveBackward()
            if event.key == pygame.K_LEFT:
                turnLeft()
            if event.key == pygame.K_RIGHT:
                turnRight()
#           define key stroke for screen change
            if event.key == pygame.K_w:
                counter += 1
                if counter >= len(stateList):
                    counter = 0
                active = stateList[counter]
            elif event.key == pygame.K_s:
                counter += -1
                if counter < 0:
                    counter = len(stateList) - 1
                active = stateList[counter]
            # cute face screen (press C)
            if event.key == pygame.K_c:
                counter = 3
                active = stateList[counter]
            # staff screen (press Z,Q,A)
            if event.key == pygame.K_z:
                counter = 4
                active = stateList[counter]
            if event.key == pygame.K_a:
                counter = 5
                active = stateList[counter]
            if event.key == pygame.K_q:
                counter = 6
                active = stateList[counter]
            # open intro video (press V)
            if event.key == pygame.K_v:
                counter = 1
                active = stateList[counter]

            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

#       define that if you are no longer hold movement key, robot will stop
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_UP,pygame.K_DOWN,pygame.K_LEFT,pygame.K_RIGHT]:
                stop()

#   which screen is displayed   
    if active == 0:
        screen.blit(initialScreen,(0,0))
        screen.blit(initialQrCode,(900,170))
    elif active == 1:
        call(["python","introVideo.py"])
        counter += 1
        active = stateList[counter]
    elif active == 2:
        screen.blit(otherProjectScreen,(0,0))
    elif active == 3:
        screen.blit(cuteFace,(0,0))
    elif active == 4:
        screen.blit(staffScreen1,(0,0))
    elif active == 5:
        screen.blit(staffScreen2,(0,0))
    elif active == 6:
        screen.blit(staffScreen3,(0,0))
        
    pygame.display.update()
#   set fps
    clock.tick(60)   