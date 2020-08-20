import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30 
fpsClock = pygame.time.Clock()
font = pygame.font.Font(None, 100)

#set up the window
screen_w = 800
screen_h = 600
screen = pygame.display.set_mode((screen_w,screen_h), 0, 32)
pygame.display.set_caption('expressiontree')


#set up the colors
white = (255, 255, 255)
green = (0, 255, 0)
powderblue = (176,224,230)
black = (0,0,0)

prefix = ['*','+','i0','i1','!','i1','i2']
column_pos =[]
row_pos =[]

row_h = int(screen_h/4)
col_w = int(screen_w/4)

for i in range(4):
    row_pos.append(int(row_h*(i+1)-100))
for i in range(4):
    column_pos.append(int(col_w*(i+1)))
running = True
while True: # the main game loop
    screen.fill(white)

    # draw some green lines onto the surface
    
    pygame.draw.line(screen, green, (column_pos[1],row_pos[0]), (column_pos[0],row_pos[1]),8)
    pygame.draw.line(screen, green, (column_pos[1],row_pos[0]), (column_pos[2],row_pos[1]),8)
    pygame.draw.line(screen, green, (column_pos[0],row_pos[1]), (column_pos[0]-100,row_pos[2]),8)
    pygame.draw.line(screen, green, (column_pos[0],row_pos[1]), (column_pos[0]+100,row_pos[2]),8)
    pygame.draw.line(screen, green, (column_pos[2],row_pos[1]), (column_pos[2],row_pos[2]),8)
    pygame.draw.line(screen, green, (column_pos[2],row_pos[2]), (column_pos[2]-100,row_pos[3]),8)
    pygame.draw.line(screen, green, (column_pos[2],row_pos[2]), (column_pos[2]+100,row_pos[3]),8)
  
    text = '+'
    label = font.render(text,True,black)
    pygame.draw.circle(screen, powderblue, (400, 50), 40, 0)
    screen.blit(label,(380,20))

    text = '*'
    label = font.render(text,True,black)
    pygame.draw.circle(screen, powderblue, (200, 200), 40, 0)
    screen.blit(label,(190,180))

    text = '*'
    label = font.render(text,True,black)
    pygame.draw.circle(screen, powderblue, (600, 350), 40, 0)
    screen.blit(label,(580,330))

    text = 'i1'
    label = font.render(text,True,black)
    pygame.draw.circle(screen, powderblue, (500, 500), 40, 0)
    screen.blit(label,(485,480))

    text = 'i2'
    label = font.render(text,True,black)
    pygame.draw.circle(screen, powderblue, (700, 500), 40, 0)
    screen.blit(label,(685,480))

    text = '!'
    label = font.render(text,True,black)
    pygame.draw.circle(screen, powderblue, (600, 200), 40, 0)
    screen.blit(label,(590,180))

    text = 'i0'
    label = font.render(text,True,black)
    pygame.draw.circle(screen, powderblue, (100, 350), 40, 0)
    screen.blit(label,(85,330))

    text = 'i1'
    label = font.render(text,True,black)
    pygame.draw.circle(screen, powderblue, (300, 350), 40, 0)
    screen.blit(label,(285,330))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
