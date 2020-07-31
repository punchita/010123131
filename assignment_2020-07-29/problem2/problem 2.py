import pygame
import pygame.camera
from pygame.locals import *
import sys

scr_w = 1280
scr_h = 720
pygame.init()

cam = open_camera()
M = 10
N = 8
rw, rh = scr_w//M, scr_h//N
rect = []
blackclick = []
rectclick = []

if cam:
    cam.start()
else:
    print('Cannot open camera')
    sys.exit(-1)

screen = pygame.display.set_mode( (scr_w,scr_h) )
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )

class Rectangle:
    def __init__(self, left, top, rw, rh):
        self.left = left
        self.top = top
        self.rw = rw
        self.rh = rh
        self.position = (left, top, rw, rh)

    def draw(self):
        pygame.draw.rect( img, (0,255,0) ,positon.pos, 1 )
        surface.blit( img, (self.left, self.top, self.rw, self.rh), self.position )
        
list_rect = []
add_rect = []

img = None
is_running = True 

for i in range(M):
    for j in range(N):
        rect = (i*rw, j*rh, rw, rh)
        rectclick.append(rect)
        blackclick.append(rect)

while is_running:

    # try to capture the next image from the camera 
    img = cam.get_image()
    if img is None:
        continue

    # get the image size
    img_rect = img.get_rect()
    img_w, img_h = img_rect.w, img_rect.h
    
    
    # get image screenshot
    img = cam.get_image()
    
    #click to appear the image
    for event in pygame.event.get():

        if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            is_running = False
            if img:
                # save the current image into the output file
                pygame.image.save( img, 'image.jpg' )
            
     # take position input from mouse
    if(event.type == pygame.MOUSEBUTTONUP and event.button ==1):
        #global pos_start
        global pos_start_rect

        mousepositon = pygame.mouse.get_pos()
            for pos in list_rect:
                if(  (pos.left < mousepositon[0] < pos.left+pos.rw) and (pos.top < mousepositon[1] < pos.top+pos.rh)  ):
                    if(pos_start_rect.pos == pos.pos):
                        # append which position of rectangle to show camera
                        #if(pos not in theCamera):
                        print("Pop!!")
                        #theCamera.append(pos)
                    else:
                        #pos_start_rect
                        #pos

                        print((pos_start_rect.left, pos_start_rect.top, pos_start_rect.rw, pos_start_rect.rh),end='')
                        print(pos.pos,"OLD")
                        list_rect.remove(pos_start_rect)
                        list_rect.remove(pos)

                        pos.pos, pos_start_rect.pos = pos_start_rect.pos, pos.pos
                        
                        list_rect.append(pos)
                        list_rect.append(pos_start_rect)
                        print( (pos_start_rect.left, pos_start_rect.top, pos_start_rect.rw, pos_start_rect.rh),end='' )
                        print( (pos.left, pos.top, pos.rw, pos.rh),"NEW")

                    #list_rect.remove(pos) #<-- if you want grid on the screen open this code 
    
    elif(event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
        mousestart = pygame.mouse.get_pos()
        
            for pos in list_rect:
                if(  (pos.left < mousestart[0] < pos.left+pos.rw) and (pos.top < mousestart[1] < pos.top+pos.rh)  ):
                    pos_start_rect = pos
                    #print(mousestart)

    screen.blit( surface, (0,0) )
    pygame.display.update()
    
pygame.quit()

#ref by rsp
#ref by stackoverflow
#จะมาแก้เพิ่มสัปดาห์หน้าค่ะ