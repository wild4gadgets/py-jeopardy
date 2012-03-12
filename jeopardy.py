# Jeopardy Game
# By Emil Hemdal emil.hemdal.em@gmail.com and Alexander Jacques castlebravo@gmail.com
# For PA Computer Fair
# Released under ... GPL at the moment

import pygame, sys
from pygame.locals import *

FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
BOXSIZE = 40
GAPSIZE = 10



# COLORS
#            R    G    B
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)

def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    mousex = 0
    mousey = 0
    pygame.display.set_caption('py-jeopardy')
    
    categories = ('Expressions 1', 'Stuff 2', 'Letters 3', '4', '5', '6')
    questions = (('Cool? 1', 'Awesome? 2', 'Wierd? 3', 'Happy? 4', 'Sad? 5'),
                 ('Food? 1', 'Animal? 2', 'Country? 3', '4', '5'),
                 ('A? 1', 'B? 2', 'C? 3', 'D? 4', 'E? 5'),
                 ('1','2','3','4','5'),
                 ('1','2','3','4','5'),
                 ('1','2','3','4','5'))

    while True:
        mouseClicked = False
        DISPLAYSURF.fill(GRAY)
        drawBoard(questions, revealedBoxes)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True

        boxx,boxy = getBoxAtPixel(mousex, mousey)
        if boxx != None and boxy != None:
            if not revealedBoxes[boxx][boxy]:
                drawHighlightBox(boxx, boxy)
            if not revealedBoxes[boxx][boxy] and mouseClicked:
                revealBoxesAnimation(questions,[(boxx, boxy)])
                revealedBoxes[boxx][boxy] = True

    pygame.display.update()
    FPSCLOCK.tick(FPS)



def drawHighlightBox(boxx, boxy):
    left, top = leftTopCoordsOfBox(boxx, boxy)
    pygame.draw.rect(DISPLAYSURF, HIGHLIGHTCOLOR, (left - 5, top - 5, BOXSIZE + 10, BOXSIZE + 10), 4)

if __name__ == '__main__':
    main()
