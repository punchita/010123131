import pygame
import pygame.camera
from pygame.locals import *
import sys

scr_w = 1280
scr_h = 720
pygame.init()


def open_camera( frame_size=(1280,720),mode='RGB'):
    pygame.camera.init()
    list_cameras = pygame.camera.list_cameras()
    print( 'Mumber of cameras found: ', len(list_cameras) )
    if list_cameras:
        # use the first camera found
        camera = pygame.camera.Camera(list_cameras[0], frame_size, mode )
        return camera 
    return None 

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
        pygame.draw.rect( img, (0,255,0) ,pos.position, 1 )
        surface.blit( img, (self.left, self.top, self.rw, self.rh), self.position )
        
list_rect = []
add_rect = []

img = None
is_running = True 

for i in range(M):
    for j in range(N):
        rect = Rectangle(i*rw, j*rh, rw, rh)
        list_rect.append(rect)
        

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

    for pos in list_rect:
        pygame.draw.rect( surface, (0,255,0) ,pos.position, 1 )

    for pos in add_rect: 
        pos.draw()  
     # take position input from mouse
    if(event.type == pygame.MOUSEBUTTONUP and event.button ==1):
        #global pos_start
        global pos_start_rect

        mousepositon = pygame.mouse.get_pos()
        for pos in list_rect:
            if(  (pos.left < mousepositon[0] < pos.left+pos.rw) and (pos.top < mousepositon[1] < pos.top+pos.rh)  ):
                if(pos_start_rect.position == pos.position):
                        # append which position of rectangle to show camera
                    if(pos not in add_rect): 
                        print('append')
                        add_rect.append(pos)
                        check = False
                elif check:
                    check = False
                    print('swap')
                    pos.position,pos_start_rect.position = pos_start_rect.position,pos.position 


                
    elif(event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
        check = True 
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
#แก้เพิ่มแล้วนะคะ