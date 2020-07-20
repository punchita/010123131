import pygame
from pygame.locals import *
#import random,math,sys
import random, math, sys
pygame.init()

pygame.display.set_caption('moving circles')
Surface = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
Circles = []

class Circle:
    def __init__(self,radius,x,y,speedx,speedy): 
##        self.radius = int(random.random()*50) + 1
        self.radius = radius
        self.x = x
        self.y = y
        self.speedx = speedx
        self.speedy = speedy

##        self.mass = math.sqrt(self.radius)
for x in range(20):
    radius = random.randint(10,20)
    x = random.randint(radius, 800-radius)
    y = random.randint(radius, 600-radius)
    speedx = 0.5*(random.random()+1.0)
    speedy = 0.5*(random.random()+1.0)
    Circles.append(Circle(radius,x,y,speedx,speedy))
    #Circles.append(Circle(random.randint(10,20)),(random.randint(self.radius, 800-self.radius)),(random.randint(self.radius, 600-self.radius)),(1*(random.random()+1.0)),(1*(random.random()+1.0))

def CircleCollide(C1,C2):
    C1Speed = math.sqrt((C1.speedx**2)+(C1.speedy**2))
    XDiff = -(C1.x-C2.x)
    YDiff = -(C1.y-C2.y)
    if XDiff > 0:
        if YDiff > 0:
            Angle = math.degrees(math.atan(YDiff/XDiff))
            XSpeed = -C1Speed*math.cos(math.radians(Angle))
            YSpeed = -C1Speed*math.sin(math.radians(Angle))
        elif YDiff < 0:
            Angle = math.degrees(math.atan(YDiff/XDiff))
            XSpeed = -C1Speed*math.cos(math.radians(Angle))
            YSpeed = -C1Speed*math.sin(math.radians(Angle))
    elif XDiff < 0:
        if YDiff > 0:
            Angle = 180 + math.degrees(math.atan(YDiff/XDiff))
            XSpeed = -C1Speed*math.cos(math.radians(Angle))
            YSpeed = -C1Speed*math.sin(math.radians(Angle))
        elif YDiff < 0:
            Angle = -180 + math.degrees(math.atan(YDiff/XDiff))
            XSpeed = -C1Speed*math.cos(math.radians(Angle))
            YSpeed = -C1Speed*math.sin(math.radians(Angle))
    elif XDiff == 0:
        if YDiff > 0:
            Angle = -90
        else:
            Angle = 90
        XSpeed = C1Speed*math.cos(math.radians(Angle))
        YSpeed = C1Speed*math.sin(math.radians(Angle))
    elif YDiff == 0:
        if XDiff < 0:
            Angle = 0
        else:
            Angle = 180
        XSpeed = C1Speed*math.cos(math.radians(Angle))
        YSpeed = C1Speed*math.sin(math.radians(Angle))
    C1.speedx = XSpeed
    C1.speedy = YSpeed
def Move():
    for Circle in Circles:
        Circle.x += Circle.speedx
        Circle.y += Circle.speedy
def CollisionDetect():
    for Circle in Circles:
        if Circle.x < Circle.radius or Circle.x > 800-Circle.radius:    Circle.speedx *= -1
        if Circle.y < Circle.radius or Circle.y > 600-Circle.radius:    Circle.speedy *= -1
    for Circle in Circles:
        for Circle2 in Circles:
            if Circle != Circle2:
                if math.sqrt(  ((Circle.x-Circle2.x)**2)  +  ((Circle.y-Circle2.y)**2)  ) <= (Circle.radius+Circle2.radius):
                    CircleCollide(Circle,Circle2)
def Draw():
    Surface.fill(black)
    for Circle in Circles:
        pygame.draw.circle(Surface,random_color(),(int(Circle.x),int(600-Circle.y)),Circle.radius)
    pygame.display.flip()

    rr = random.randint(10,20)
        # randomize an integer value between 50..255 for alpha level
        # create a blue color with alpha level (RGBA)

black = 0,0,0

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
def GetInput():
    keystate = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT or keystate[K_ESCAPE]:
            pygame.quit(); sys.exit()
def main():
    while True:
        clock.tick( 30 )
        GetInput()
        Move()
        CollisionDetect()
        Draw()
if __name__ == '__main__': main()
