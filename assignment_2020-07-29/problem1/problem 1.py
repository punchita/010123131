import pygame
import pygame.camera
from pygame.locals import *
import sys

def open_camera( frame_size=(1280,720),mode='RGB'):
    pygame.camera.init()
    list_cameras = pygame.camera.list_cameras()
    print( 'Mumber of cameras found: ', len(list_cameras) )
    if list_cameras:
        # use the first camera found
        camera = pygame.camera.Camera(list_cameras[0], frame_size, mode )
        return camera 
    return None 

scr_w = 1280
scr_h = 720
pygame.init()
camera = open_camera()
# draw (MxN) tiles of the images
M = 10
N = 8
rw, rh = scr_w//M, scr_h//N
rect = []
blackclick = []
rectclick = []

if camera:
    camera.start()
else:
    print('Cannot open camera')
    sys.exit(-1)

screen = pygame.display.set_mode((scr_w, scr_h))

surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )
        
img = None
is_running = True 

for i in range(M):
    for j in range(N):
        rect = (i*rw, j*rh, rw, rh)
        rectclick.append(rect)
        blackclick.append(rect)

while is_running:

    # try to capture the next image from the camera 
    img = camera.get_image()
    if img is None:
        continue

    # get the image size
    img_rect = img.get_rect()
    img_w, img_h = img_rect.w, img_rect.h

     # draw a green frame (tile)
    rect = (i*rw, j*rh, rw, rh)
    pygame.draw.rect( img, (0,255,0), rect, 1)
    surface.blit( img, rect, rect )

    # draw black rect on the images
    for rect in rectclick:
        black = pygame.draw.rect( img, (0,0,0), rect ,1500)
        pygame.draw.rect( img, (0,255,0), rect, 1)
        blackclick.append(black)
        surface.blit( img, rect, rect)

    #click to appear the image
    for event in pygame.event.get():

        if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            is_running = False
            if img:
                # save the current image into the output file
                pygame.image.save( img, 'image.jpg' )

        if (event.type == pygame.MOUSEBUTTONUP and event.button == 1):
            mouse_position = pygame.mouse.get_pos() 

            for i in range(len(blackclick)):
                blackdrawrect = blackclick[i]       
                if ( blackdrawrect.collidepoint( mouse_position ) ):
                    rectclick.pop(0) 


    # write the surface to the screen and update the display
    
    screen.blit( surface, (0,0) )
    pygame.display.update()

# close the camera
camera.stop()

print('Done....')
###################################################################

#ref by rsp