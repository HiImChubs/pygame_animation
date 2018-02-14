# Computer Programming 1
# Unit 11 - Graphics
#
# A scene that uses loops to make stars and make a picket fence.


#Imports-------------------------------------------------------------------------------
import pygame
import random

#Initialize game engine----------------------------------------------------------------
pygame.init()

#Window-------------------------------------------------------------------------------
SIZE = (800, 600)
TITLE = "Sunny Day"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer-----------------------------------------------------------------------------
clock = pygame.time.Clock()
refresh_rate = 60

#Images-------------------------------------------------------------------------------
bunny = pygame.image.load('img/bunny-still.png')


#Colors-------------------------------------------------------------------------- 
GREEN = (65, 130, 66)
WHITE = (255, 255, 255)
CLOUD_WHITE = (209, 209, 209)
FAR_CLOUD_WHITE = (153, 153, 153)
BLUE = (75, 200, 255)
YELLOW = (255, 255, 175)
BLACK = (0, 0, 0)
MOON_WHITE = (255, 250, 216)
GREY = (135, 135, 135)
RAIN_BLUE = (148, 162, 183)
DARK_GRAY = (94, 94, 94)
BROWN = (99, 57, 15)
LIGHT_GREY = (90, 90, 90)
DARK_GREEN = (0, 104, 0)
YELLOW = (255, 255, 140)

#Lightning Timers----------------------------------------------------------------------
lightning_prob = 300 # (higher is less frequent)
lightning_timer = 0
#Draw Functions----------------------------------------------------------------------
def draw_cloud(x, y, color):
    pygame.draw.ellipse(screen, color, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, color, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, color, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, color, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, color, [x + 20, y + 20, 60, 40])
''' Make Stars'''
stars = []
for i in range(400):
    x = random.randrange(0, 800)
    y = random.randrange(0, 800)
    r = random.randrange(1, 5)
    s = [x, y, r, r]
    stars.append(s)
    
''' make clouds '''
num_clouds = 30
near_clouds = []

for i in range(num_clouds):
    x = random.randrange(0, 1600)
    y = random.randrange(-50, 100)
    loc = [x, y]
    near_clouds.append(loc)

num_clouds = 50
far_clouds = []

for i in range(num_clouds):
    x = random.randrange(0, 1600)
    y = random.randrange(-50, 300)
    loc = [x, y]
    far_clouds.append(loc)


daytime = True
lights_on = False
bunnyx = 200
bunnyy = 400
vel = [0,0]
speed = 5
acceleration = 20
#Sound Effects-------------------------------------------------------------------------------
pygame.mixer.music.load("sounds/rainy_music.ogg")
light = pygame.mixer.Sound("sounds/light.ogg")
thunder = pygame.mixer.Sound("sounds/thunder.ogg")

# Game Loop---------------------------------------------------------------------------
pygame.mixer.music.play(-1)
done = False

while not done:
#Event Processing--------------------------------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                daytime = not daytime
            elif event.key == pygame.K_l:
                lights_on = not lights_on
                light.play()
            elif event.key == pygame.K_t:
                thunder.play()
                
#Bunny Movement--------------------------------------------------------------
            elif event.key == pygame.K_RIGHT:
                vel[0] = 1 * speed
            elif event.key == pygame.K_LEFT:
                vel[0] = -1 * speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                vel[0] = 0
            elif event.key == pygame.K_RIGHT:
                vel[0] = 0
            # google 'pygame key constants' for more keys
                
#Game Logic-----------------------------------------------------------------------
    ''' move clouds '''
    for c in far_clouds:
        c[0] -= 1

        if c[0] < -100:
            c[0] = random.randrange(800, 1600)
            c[1] = random.randrange(-50, 200)

    for c in near_clouds:
        c[0] -= 2

        if c[0] < -100:
            c[0] = random.randrange(800, 1600)
            c[1] = random.randrange(-50, 200)


            
    for s in stars:
        s[1] += 2
        s[0] += 1

        if s[1] > 600:
           s[1] = random.randrange(-150, 0)
           s[0] = random.randrange(-300, 800)
           

    ''' set sky color '''
    if daytime:
        sky = RAIN_BLUE
    else:
        sky = BLACK

    ''' set window color (if there was a house)'''
    if lights_on:
        window_color = YELLOW
    else:
        window_color = WHITE
        
    ''' flash lighting '''
    if random.randrange(0, 300) == 0:
        lightning_timer = 5
        thunder.play()
    else:
        lightning_timer -= 1
    

#Drawing Code---------------------------------------------------------------------
    ''' sky '''
    if lightning_timer > 0:
        screen.fill(YELLOW)
    else:
        screen.fill(sky)



 
    
    ''' sun '''
    if daytime:
        pygame.draw.ellipse(screen, YELLOW, [575, 75, 100, 100])
    else:
        pygame.draw.ellipse(screen, MOON_WHITE, [575, 75, 100, 100])
        pygame.draw.ellipse(screen, BLACK, [595, 75, 100, 100])
        
    ''' grass '''
    pygame.draw.rect(screen, GREEN, [0, 400, 800, 200])


         
    ''' clouds '''
    if daytime:
        for c in far_clouds:
            draw_cloud (c[0], c[1], GREY)
    else:
        for c in far_clouds:
            draw_cloud(c[0], c[1], CLOUD_WHITE)



    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, WHITE, [[x+5, y], [x+10, y+5],
                                            [x+10, y+40], [x, y+40],
                                            [x, y+5]])
    pygame.draw.line(screen, WHITE, [0, 390], [800, 390], 5)
    pygame.draw.line(screen, WHITE, [0, 410], [800, 410], 5)

   
    
    '''draw house'''
    pygame.draw.rect(screen, BROWN, [550, 300, 200, 150])
    pygame.draw.polygon(screen, LIGHT_GREY, [[650, 220], [530, 300], [770, 300]])
    pygame.draw.rect(screen, BLACK, [623, 400, 50, 50])
    if lights_on:
        pygame.draw.rect(screen, YELLOW, [575, 325, 35, 35])
        pygame.draw.rect(screen, YELLOW, [690, 325, 35, 35])
    else:
        pygame.draw.rect(screen, WHITE, [575, 325, 35, 35])
        pygame.draw.rect(screen, WHITE, [690, 325, 35, 35])


    '''rain'''
    if daytime:
        for s in stars:
            pygame.draw.ellipse(screen, WHITE, s)
    else:
        for s in stars:
            pygame.draw.ellipse(screen, BLUE, s)
            

    ''' clouds '''
    if daytime:
        for c in near_clouds:
            draw_cloud(c[0], c[1], DARK_GRAY)
    else:
        for c in near_clouds:
            draw_cloud(c[0], c[1], FAR_CLOUD_WHITE)

    '''bunny'''
    bunnyx += vel[0]
    bunnyy += vel[1]

    screen.blit(bunny, (bunnyx, bunnyy))
    
    '''draw tree'''
    pygame.draw.rect(screen, BROWN, [227, 300, 20, 200])
    pygame.draw.ellipse(screen, DARK_GREEN, [200, 295, 75, 150])
    

    #Update Screen-------------------------------------------------------------------
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit--------------------------------------------------------------
pygame.quit()
