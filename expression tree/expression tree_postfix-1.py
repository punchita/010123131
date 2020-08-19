import pygame, sys
from pygame.locals import *

pygame.init()

class infix_to_prefix:
    precedence={'+':3,'&':3,'(':2,')':1} 
    def __init__(self):
        self.items=[]
        self.top=-1
    def push(self,value):
        self.items.append(value)
        self.top+=1
    def pop(self):
        if self.isempty():
            return empty('list is empty')
        else:
            self.top-=1
            return self.items.pop()
    def isempty(self):
        if(self.top==-1):
            return True
        else:
            return False
    def seek(self):
        if self.isempty():
            return False
        else:
            return self.items[self.top]
    def is0perand(self,i): 
        List_op = []
        for a in range(1000):
            List_op.append('I'+str(a))
        if i in List_op:
            return True
        else:
            return False
    def reverse(self,expresstion): 
        rev=[]
        for i in expresstion:
            if i == '(':
                i=')'
            elif i == ')':
                i='('
            rev.insert(0,i)
        return rev
    def infix_to_postfix (self,expresstion):
        prefix=""
        for i in expresstion:
            if(self.is0perand(i)): 
                prefix +=i
            elif(i == '!'): 
                prefix+=i
            elif(i == '&' or i =='+'): 
                while(len(self.items)and self.precedence[i] < self.precedence[self.seek()]): 
                    prefix+=self.pop() 
                self.push(i)
            elif i == '(':
                self.push(i)
            elif i == ')':
                o=self.pop()
                while ( (not self.isEmpty()) and self.seek() != '('): 
                    self.output.append(o) 
                    self.pop()
        # pop all the operator from the stack             
        while not self.isEmpty(): 
            self.output.append(self.pop()) 
        return prefix


solve=infix_to_prefix() 
expresstion = "!(I1+I0)"
rev = ''
rev=solve.reverse(rev)
result=solve.infix_to_postfix(rev) 




prefix=solve.reverse(result)
print(prefix)


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
