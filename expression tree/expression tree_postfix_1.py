import pygame, sys
from pygame.locals import *

pygame.init()

class infix_to_prefix:
    def __init__(self):
        self.items=[]
        self.top=-1
        self.precedence={'+':3,'&':3,'(':2,')':1}
    def push(self,el):
        self.items.append(el)
        self.top+=1
    def pop(self): 
        if not self.isempty(): 
            self.top -= 1
            return self.items.pop() 
        else: 
            return empty
    def isempty(self):
        if(self.top==-1):
            return True
        else:
            return False
    def peek(self): 
        return self.items[-1] 
    def seek(self): 
        if self.isempty():
            return False
        else:
            return self.items[self.top]
    def isOperant(self,i): 
        if(i != '+' and i != '&' and i != '(' and i != ')'):
            return True
        else:
            return False
    def notGreater(self, i): 
        try: 
            b = self.precedence[i] 
            c = self.precedence[self.peek()] 
            return True if b <= c else False
        except KeyError:  
            return False
    def reverse(self,exp): 
        rev=[]
        for i in exp:
            if i == '(':
                i=')'
            elif i == ')':
                i='('
            rev.insert(0,i)
        return rev
    def infix_to_postfix (self,exp):
        postfix=""
        for i in exp:
            if(self.isOperant(i)): 
                postfix +=i
            elif(i == '&' or i =='+'): 
                while(not self.isempty() and self.notGreater(i)):
                    postfix += i
                self.push(i) 
            elif i == '(':
                self.push(i)
            elif i == ')':
                o=self.pop() 
                while( (not self.isempty()) and o!= '('): 
                    postfix+=o 
                    o=self.pop() 
        #pop all the operator from the stack
        while len(self.items):
            if(self.seek()=='('):
                self.pop()
            else:
                postfix += self.pop()
        return postfix


obj=infix_to_prefix() 
exp = "!(I0&I1)+!(I1+I2)"
rev = ''
rev=obj.reverse(exp)
out=obj.infix_to_postfix(rev) 


postfix=obj.reverse(out)
print(postfix)


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

prefix = ['&','+','i0','i1','!','i1','i2']
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
    pygame.draw.line(screen, green, (column_pos[0],row_pos[1]), (column_pos[0]-100,row_pos[2]),8)
    pygame.draw.line(screen, green, (column_pos[0],row_pos[1]), (column_pos[0]+100,row_pos[2]),8)


    text = '+'
    label = font.render(text,True,black)
    pygame.draw.circle(screen, powderblue, (400, 50), 40, 0)
    screen.blit(label,(380,20))

    text = '&'
    label = font.render(text,True,black)
    pygame.draw.circle(screen, powderblue, (220, 200), 40, 0)
    screen.blit(label,(190,180))

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