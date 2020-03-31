import random,pygame,sys,time
from pygame.locals import*
FPS=30
windowwidth=640
windowheight=480
flashspeed=500
flashdelay=200
buttonsize=200
buttongapsize=20
timeout=4

white=(255,255,255)
black=(0,0,0)
brightred=(255,0,0)
red=(155,0,0)
brightgreen=(0,255,0)
green=(0,155,0)
brightblue=(0,0,255)
blue=(0,0,155)
brightyellow=(255,255,0)
yellow=(155,155,0)
darkgray=(40,40,40)
bgColour=black

xmargin=int((windowwidth - (2*buttonsize)-buttongapsize)/2)
ymargin=int((windowheight - (2*buttonsize)-buttongapsize)/2)

yellowrect=pygame.Rect(xmargin, ymargin, buttonsize, buttonsize)
bluerect=pygame.Rect(xmargin + buttonsize + buttongapsize, ymargin, buttonsize, buttonsize)
redrect=pygame.Rect(xmargin, ymargin + buttonsize + buttongapsize, buttonsize, buttonsize)
greenrect=pygame.Rect(xmargin + buttonsize + buttongapsize, ymargin + buttonsize + buttongapsize, buttonsize, buttonsize)

def main():
    global FPSclock, displaysurf, basicfont, beep1, beep2, beep3, beep4

    pygame.init()
    FPSclock = pygame.time.Clock()
    displaysurf = pygame.display.set_mode((windowwidth,windowheight))
    pygame.display.set_caption(' Simulate ')

    basicfont = pygame.font.Font('freesansbold.ttf',16)

    infosurf = basicfont.render(' match the pattern by clicking on the T, Y, G, H keys',1,darkgray)
    inforect = infosurf.get_rect()
    inforect.topleft = (10, windowheight - 25)

    beep1 = pygame.mixer.Sound('beep1.wav')
    beep2 = pygame.mixer.Sound('beep2.wav')
    beep3 = pygame.mixer.Sound('beep3.wav')
    beep4 = pygame.mixer.Sound('beep4.wav')

    pattern = []
    currentstep = 0
    lastclicktime = 0
    score = 0

    waitingforinput= False

    while True:
        clickedbutton = None
        displaysurf.fill(bgcolour)
        drawButtons()

        scoresurf = basicfont.render(' Score :' + str(score),1,white)
        scorerect = scoresurf.get_rect()
        scorerect.topleft = (windowwidth - 100, 10)
        displaysurf.blit(scoresurf, scorerect)

        displaysurf.blit(infosurf,inforect)

        checkForQuit()
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:# this code can be removed, it is jsut so that user can play using mouse as well
                mousex, mousey = event.pos
                clickedbutton =getbuttonclicked(mosex, mousey)
            elif event.type==KEYDOWN:
                if event.key == K_t:
                    clickedbutton = yellow
                elif event.key == K_y:
                    clickedbutton = blue
                elif event.key == K_g:
                    clickedbutton = red
                elif event.key == K_h:
                    clickedbutton = green
        if not waitingforinput:
            pygame.display.update()
            pygame.time.wait(1000)
            pattern.append(random.choice((yellow,blue,red,green)))
            for button in pattern:
                flashButtonAnimation(button)
                pygame.time.wait(flashdelay)
            waitingforinput=True
        else:

            if clickedbutton and clickedbutton == pattern[currentstep]:
                flashButtonAnimation(clickedbutton)
                currentstep+=1
                lastclicktime=time.time()

                if currentStep == len(pattern):
                    changeBackgroundAnimation()
                    score += 1
                    waitingforinput = False
                    currentstep = 0
            elif (clickedbutton and clickedbutton!= pattern[currentstep]) or (currentstep!=0 and time.time() - timeout> lastclicktime):

                gameOverAnimation()

                pattern= []
                currentStep = 0
                waitingfornput = False
                score = 0
                pygame.time.wait(1000)
                changeBackgroundAnimation()

                pygame.display.update()
                FPSclock.tick(FPS)

def terminate():
    pygame.quit()
    sys.exit()

def checkForQuit():
    for event in pygame.event.get(QUIT):
        terminate()
    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            terminate()
        pygame.event.post(event)
def flashButtonAnimation(colour,animationspeed=50):
    if colour == yellow:
        sound = beep1
        flashcolour= brightyellow
        rectangle = yellowrect
    elif colour == blue:
        sound = beep2
        flashcolour= brightblue
        rectangle = bluerect
    elif colour == red:
        sound = beep3
        flashcolour= brightred
        rectangle = redrect
    elif colour == green:
        sound = beep4
        flashcolour= brightgreen
        rectangle = greenrect

    origsurf = displaysurf.copy()
    flashsurf = pyagme.Surafce((buttonsize,buttonsize))
    flashsurf= flashsurf.convert_alpha()
    r,g,b = flashcolour
    sound.play()

    for start, end , step in ((0,255,1),(255,0,-1)):
        for alpha in range(start, end, animationSpeed*step):
            checkForQuit()
            displaysurf.blit(origsurf,(0,0))
            flashsurf.fill((r,g,b,alpha))
            displaysurf.blit(flashsurf,rectangle.topleft)
            pygame.display.update()
            FPSclock.tick(FPS)
    displaysurf.blit(origsurf,(0,0))

def drawButtons():
    pygame.draw.rect(displaysurf, yellow, yellowrect)
    pygame.draw.rect(displaysurf, blue, bluerect)
    pygame.draw.rect(displaysurf, red, redrect)
    pygame.draw.rect(displaysurf, green, greenrect)

def changeBackgroundAnimation(animtionspeed = 40):
    global bgcolour
    newbgcolour = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

    newbgsurf = pygame.Surface((windowwidth,windowheight))
    newbgsurf = newbgsurf.convert_alpha()
    r,g,b = newbgcolour

    for alpha in range(0,255,animationspeed):
        checkForQuit()
        displaysurf.fill(bgcolour)

        newbgsurf.fill((r,g,b, alpha))
        displaysurf.blit(newbgsurf,(0,0))
        
        drawButtons()
        
        pygame.display.update()
        FPSclock.tick(FPS)
    bgcolour = newbgcolour

def gameOverAnimation(colour = white,animationspeed = 50):
    origsurf = displaysurf.copy()
    flashsurf = pygame.Surface(displaysurf.get_size())
    flashsurf = flashsurf.convert_aplha()
    beep1.play()
    beep2.play()
    beep3.play()
    beep4.play()
    r,g,b = colour

    for i in range(0,3):
        for alpha in range(start,end, animationspeed*step):

            checkForQuit()
            flashsurf.fill(r,g,b,alpha)
            displaysurf.blit(origsurf,(0,0))
            displaysurf.blit(flashsurf,(0,0))
            drawButtons()
            pygame.display.update()
            FPSclock.tick(FPS)

def getButtonClicked(x,y):
    if yellowrect.collidepoint((x,y)):
        return yellow
    elif bluerect.collidepoint((x,y)):
        return blue
    elif redrect.collidepoint((x,y)):
        return red
    elif greenrect.collidepoint((x,y)):
        return green
    return None

if __name__ == '__main__':
    main()

    
        














                
            
        

        
                













