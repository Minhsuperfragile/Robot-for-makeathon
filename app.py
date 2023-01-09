import pygame
import subprocess

# define some constant
width = 1440
heigh = 720
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
initialScreen = pygame.transform.scale(initialScreen, (width,heigh)) #scale the image
initialQrCode = pygame.image.load('assets/initialQrCode.png').convert_alpha()
initialQrCode = pygame.transform.scale(initialQrCode,(500,500))

otherProjectScreen = pygame.image.load('assets/otherProjectScreen.jpg').convert()
# otherPSRect = otherProjectScreen.get_rect(topleft=(0,0))
background = pygame.image.load('assets/logarith.jpg').convert()
cuteFace = pygame.image.load('assets/cuteFace.jpg').convert()
cuteFace = pygame.transform.scale(cuteFace,(width,heigh))
staffScreen1 = pygame.image.load('assets/staff1.jpg').convert()
staffScreen2 = pygame.image.load('assets/staff2.jpg').convert()
staffScreen3 = pygame.image.load('assets/staff3.jpg').convert()

stateList = ['initialScreen','introVideo','otherProjectScreen','cuteFace','staffScreen1','staffScreen2','staffScreen3']
counter = 0
move = False

def displayWebStatus(status):
    statusSurface = mainFont.render(str(status), False, (64,64,64))
    statusRectangle = statusSurface.get_rect(midtop = (456,200))
    screen.blit(statusSurface,statusRectangle)

# movement functions for robot that will be added in future
def moveForward():
    movement = 'Forward'

def moveBackward():
    movement = 'Backward'

def turnRight():
    movement = 'Right'

def turnLeft():
    movement = 'Left'

def stop():
    movement = 'Stop'

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
#         define key stroke for movement 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                moveForward()
                move = True
            if event.key == pygame.K_DOWN:
                moveBackward()
                move = True
            if event.key == pygame.K_LEFT:
                turnLeft()
                move = True
            if event.key == pygame.K_RIGHT:
                turnRight()
                move = True
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
                move = False
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
    elif active == 'cuteFace':
        screen.blit(cuteFace,(0,0))
    elif active == 'staffScreen1':
        screen.blit(staffScreen1,(0,0))
    elif active == 'staffScreen2':
        screen.blit(staffScreen2,(0,0))
    elif active == 'staffScreen3':
        screen.blit(staffScreen3,(0,0))
    if move:
        displayWebStatus(movement)
    pygame.display.update()
#   set fps
    clock.tick(60)
