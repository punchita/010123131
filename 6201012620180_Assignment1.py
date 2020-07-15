#6201012620180 Assignment I
import pygame 
import random
import math
# initialize PyGame
pygame.init()

# show PyGame version
print( 'PyGame version: {}'.format( pygame.version.ver ) ) 


# set window caption
pygame.display.set_caption('PyGame Demo 1') 

# create a clock
clock = pygame.time.Clock()

# Set up the drawing window (500 x 500 pixels)
scr_w, scr_h = 800, 600
screen  = pygame.display.set_mode((scr_w, scr_h))

# create a new surface 
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )

# Run until the user asks to quit
running = True
while running:

    # This limits the while loop to a max of 10 times per second.
    clock.tick( 10 ) 

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # randomize an integer value between 5..40 for the radius
    r = random.randint(10,20)
    # randomize an integer value between 50..255 for alpha level
    # create a blue color with alpha level (RGBA)

    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb = [(r,g,b),(r,g,b),(r,g,b)]

    
    def random_color():
        return random.choice(rgb)
    # randomize a position (x,y)
    x,y = random.randint(r,scr_w-r), random.randint(r,scr_h-r)
    # draw a circle filled with the blue color on the surface
    pygame.draw.circle( surface, random_color(), (x,y), r ) 
    
    # fill the screen with the white color
    screen.fill((200,200,200))
    # draw the surface on the screen
    screen.blit(surface, (0,0))
    # update the screen display
    pygame.display.update()

pygame.quit() 
