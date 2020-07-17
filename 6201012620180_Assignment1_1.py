#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pygame
import random
import math
pygame.init()

screen = pygame.display.set_mode([800,600])
pygame.display.set_caption('non-overlapping circles')

clock = pygame.time.Clock()

black = 0,0,0
white = 255,255,255

createcircle = []
namelist = []
radius = []


rr = random.randint(10,20)
        # randomize an integer value between 50..255 for alpha level
        # create a blue color with alpha level (RGBA)

r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)
r1 = random.randint(0,255)
g1 = random.randint(0,255)
b1 = random.randint(0,255)
r2 = random.randint(0,255)
g2 = random.randint(0,255)
b2 = random.randint(0,255)

rgb = [(r,g,b),(r1,g1,b1),(r2,g2,b2)]

    
def random_color():
        return random.choice(rgb)
# make 10 circles
def make_Circle():
    for num in range(10):
        xr = random.randint(10,20)
        x = random.randint(20,780)
        y = random.randint(20,580) 
        color = random_color()
        
        out = pygame.draw.circle(screen, color, (x,y), xr ,0)
        namelist.append(out)
        createcircle.append((x,y,xr))
        radius.append(xr)
    return 0

# find circle to remove that choose from the circle with the most radius
def get_cir_rm():
    max_r = max(radius)
    for x,y,xr in createcircle :
        if xr == max_r: 
            c = createcircle[createcircle.index((x,y,xr))]   # Let c = circle with the most radius
            index = createcircle.index((x,y,xr))          # find index of circle with the most radius
            circle = namelist[index]                      # Let circle = out of  circle 
            print("The largest circle is ", circle)
            return circle

# get the most radius
def get_r_rm():
    max_r = max(radius)
    for x,y,xr in createcircle :
        if xr == max_r: 
            return xr 


def  del_data():
    circle = get_cir_rm()                     # circle = วงกลมที่จะลบ
    index = namelist.index(circle)                # fin dindex of data about circle
    namelist.remove(namelist[index])                  # Remove out from Namelist
    createcircle.remove(createcircle[index])        # Remove position from createcircle
    radius.remove(radius[index])              # Remove radius from radius
    return 0    

# Draw
make_Circle()

running = True

while running :

    clock.tick(10)
    
    ev = pygame.event.get()

    for event in ev:
        if event.type == pygame.QUIT:
            running = False

    for event in ev:
        if ( event.type == pygame.MOUSEBUTTONUP ):         # When click mouse 
            mouse_pos = pygame.mouse.get_pos()             # Location of the mouse-click
            circle_remove = get_cir_rm()                   # Select circle to remove 
            xr = get_r_rm()
            if ( circle_remove.collidepoint( mouse_pos ) ):   # click inside circle 
                pygame.draw.circle(screen, black, mouse_pos, xr*2 ,0)    # Draw another circle over selected circle (color is same background)
                del_data()                                  # delete data about removed circle from every list
   
    pygame.display.update()

pygame.quit()

 
   



