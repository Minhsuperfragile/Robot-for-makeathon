import pygame
import requests
from subprocess import call

# define some constant
width = 1920
heigh = 1080
url = 'https://www.facebook.com/'
active = 'initialScreen'
run = True

# start pygame and set up display,fps,font,etc
pygame.init()
screen = pygame.display.set_mode((width,heigh))
pygame.display.set_caption('REM')
clock = pygame.time.Clock()
mainFont = pygame.font.Font('font/Pixeltype.ttf',50)

# Locate source file for app
initialScreen = pygame.image.load('assets/background.jpg').convert()
# initialScreen = pygame.transform.scale(initialScreen, (1440,720)) #scale the image
initialQrCode = pygame.image.load('assets/initialQrCode.png').convert_alpha()
initialQrCode = pygame.transform.scale(initialQrCode,(700,700))

otherProjectScreen = pygame.image.load('assets/otherProjectScreen.jpg').convert()
# otherPSRect = otherProjectScreen.get_rect(topleft=(0,0))
background = pygame.image.load('assets/logarith.jpg').convert()

stateList = ['initialScreen','introVideo','otherProjectScreen']
counter = 0

def displayWebStatus(status):
    statusSurface = mainFont.render(str(status), False, (64,64,64))
    statusRectangle = statusSurface.get_rect(midtop = (456,200))
    screen.blit(statusSurface,statusRectangle)

# movement functions for robot that will be added in future
def moveForward():
    print('motherfuck you are moving forward')

def moveBackward():
    print("sike, I'm moving backward now")

def turnRight():
    print("only me or that guy is turning right?")

def turnLeft():
    print('your dad has been left for 10 years')

def stop():
    print('Ikuuuuu')
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
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
#       define that if you are no longer hold movement key, robot will stop
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_UP,pygame.K_DOWN,pygame.K_LEFT,pygame.K_RIGHT]:
                stop()
#   which screen is displayed   
    if active == 'initialScreen':
        screen.blit(initialScreen,(0,0))
        screen.blit(initialQrCode,(900,170))
        # web_response = requests.get(url)
        # displayWebStatus(web_response.status_code)
    elif active == 'otherProjectScreen':
        screen.blit(otherProjectScreen,(0,0))
    elif active == 'introVideo':
        call(['python','introVideo.py'])
        counter += 1
        active = stateList[counter]
    
    pygame.display.update()
#   set fps
    clock.tick(60)
