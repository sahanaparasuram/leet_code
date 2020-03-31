
import pygame
import random
from random import randint

#Define Colors - RGB
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)

brinda =(0,238,238)
pink =(255,130,171)
green=(0,238,118)
orange =(255,128,0)
violet=(171,130,255)
maroon=(255,52,179)
limegreen=(50,205,50)
blue=(30,144,255)
yellow=(255,215,0)
pretty=(255,106,106)

colours=[brinda,pink,green,orange,violet,maroon,limegreen,blue,yellow,pretty]
colour = colours[random.randint(0,9)]

pygame.init()

#Screen Size
size = 700,500
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Flappy Bird by parasu and ashok")

done = False
clock = pygame.time.Clock()

def ball(x,y):
    #Radius of 20 px
    pygame.draw.circle(screen,black,[x,y],20)

def gameover():
    font = pygame.font.SysFont(None,55)
    text = font.render("Game Over!Enter to Try Again",False,white)
    screen.blit(text, [150,250])
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                x = 350
                y = 250
                x_speed = 0
                y_speed = 0
                ground = 477
                xloc = 700
                yloc = 0
                xsize = 70
                ysize = randint(0,350)
                #Size of space between 2 blocks
                space = 170
                obspeed = 2
                score = 0




        
    
    

def obstacle(xloc,yloc,xsize,ysize):
    pygame.draw.rect(screen,black,[xloc,yloc,xsize,ysize])
    pygame.draw.rect(screen,black,[xloc,int(yloc+ysize+space),xsize,ysize+500])

#If the ball is between 2 points on the screen, increment score
def Score(score):
    font = pygame.font.SysFont(None,55)
    text = font.render("Score: "+str(score),True,white)
    screen.blit(text, [0,0])

x = 350
y = 250
x_speed = 0
y_speed = 0
ground = 477
xloc = 700
yloc = 0
xsize = 70
ysize = randint(0,350)
#Size of space between 2 blocks
space = 170
obspeed = 2
score = 0


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                y_speed = 10

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                y_speed = -3
                        

    screen.fill(colour)
    obstacle(xloc,yloc,xsize,ysize)
    ball(x,y)
    Score(score)

    y += y_speed
    xloc -= obspeed

    if y > ground:
        
        y_speed = 0
        obspeed = 0
        gameover()

    if x+20 > xloc and y-20 < ysize and x-15 < xsize+xloc:
        
        y_speed = 0
        obspeed = 0
        gameover()

    

    if x+20 > xloc and y-20 > ysize+space and x-15 < xsize+xloc:
        gameover()
        y_speed = 0
        obspeed = 0

    if x+20 > xloc and y+20 > ysize+space and x-15 < xsize+xloc:
        
        y_speed = 0
        obspeed = 0
        gameover()

    if xloc < -80:
        xloc = 700
        ysize = randint(0,350)

    if x > xloc and x < xloc+3:
        score = score + 1

    pygame.display.flip()
    clock.tick(100)


import pygame
import random
from random import randint

#Define Colors - RGB
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)

brinda =(0,238,238)
pink =(255,130,171)
green=(0,238,118)
orange =(255,128,0)
violet=(171,130,255)
maroon=(255,52,179)
limegreen=(50,205,50)
blue=(30,144,255)
yellow=(255,215,0)
pretty=(255,106,106)

colours=[brinda,pink,green,orange,violet,maroon,limegreen,blue,yellow,pretty]
colour = colours[random.randint(0,9)]

pygame.init()

#Screen Size
size = 700,500
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Flappy Bird by parasu and ashok")

done = False
clock = pygame.time.Clock()

def ball(x,y):
    #Radius of 20 px
    pygame.draw.circle(screen,black,[x,y],20)

def gameover():
    font = pygame.font.SysFont(None,55)
    text = font.render("Game Over! Try Again",True,white)
    screen.blit(text, [150,250])

def obstacle(xloc,yloc,xsize,ysize):
    pygame.draw.rect(screen,black,[xloc,yloc,xsize,ysize])
    pygame.draw.rect(screen,black,[xloc,int(yloc+ysize+space),xsize,ysize+500])

#If the ball is between 2 points on the screen, increment score
def Score(score):
    font = pygame.font.SysFont(None,55)
    text = font.render("Score: "+str(score),True,white)
    screen.blit(text, [0,0])

x = 350
y = 250
x_speed = 0
y_speed = 0
ground = 477
xloc = 700
yloc = 0
xsize = 70
ysize = randint(0,350)
#Size of space between 2 blocks
space = 170
obspeed = 2
score = 0


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                y_speed = 10

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                y_speed = -3
                        

    screen.fill(colour)
    obstacle(xloc,yloc,xsize,ysize)
    ball(x,y)
    Score(score)

    y += y_speed
    xloc -= obspeed

    if y > ground:
        gameover()
        y_speed = 0
        obspeed = 0
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    x = 350
                    y = 250
                    x_speed = 0
                    y_speed = 0
                    ground = 477
                    xloc = 700
                    yloc = 0
                    xsize = 70
                    ysize = randint(0,350)
                    #Size of space between 2 blocks
                    space = 170
                    obspeed = 2
                    score = 0

    if x+20 > xloc and y-20 < ysize and x-15 < xsize+xloc:
        gameover()
        y_speed = 0
        obspeed = 0
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    x = 350
                    y = 250
                    x_speed = 0
                    y_speed = 0
                    ground = 477
                    xloc = 700
                    yloc = 0
                    xsize = 70
                    ysize = randint(0,350)
                    #Size of space between 2 blocks
                    space = 170
                    obspeed = 2
                    score = 0

    

    if x+20 > xloc and y-20 > ysize+space and x-15 < xsize+xloc:
        gameover()
        y_speed = 0
        obspeed = 0
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    x = 350
                    y = 250
                    x_speed = 0
                    y_speed = 0
                    ground = 477
                    xloc = 700
                    yloc = 0
                    xsize = 70
                    ysize = randint(0,350)
                    #Size of space between 2 blocks
                    space = 170
                    obspeed = 2
                    score = 0

    if x+20 > xloc and y+20 > ysize+space and x-15 < xsize+xloc:
        gameover()
        y_speed = 0
        obspeed = 0
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    x = 350
                    y = 250
                    x_speed = 0
                    y_speed = 0
                    ground = 477
                    xloc = 700
                    yloc = 0
                    xsize = 70
                    ysize = randint(0,350)
                    #Size of space between 2 blocks
                    space = 170
                    obspeed = 2
                    score = 0

    if xloc < -80:
        xloc = 700
        ysize = randint(0,350)

    if x > xloc and x < xloc+3:
        score = score + 1

    pygame.display.flip()
    clock.tick(100)



