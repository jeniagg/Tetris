import pygame
from designe import *
from class_colors import *

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))


class drawBox_:
    def drawBox(boxx, boxy, color, pixelx=None, pixely=None):
        # draw a single box (each  piece has four boxes)
        if color == BLANK:
            return
        if pixelx is None and pixely is None:
            pixelx, pixely = drawBox_.convertToPixelCoords(boxx, boxy)
        pygame.draw.rect(DISPLAYSURF, COLORS[color],
                         (pixelx + 1, pixely + 1, BOXSIZE - 1, BOXSIZE - 1))
        pygame.draw.rect(DISPLAYSURF, LIGHTCOLORS[color],
                         (pixelx + 1, pixely + 1, BOXSIZE - 4, BOXSIZE - 4))

    def convertToPixelCoords(boxx, boxy):
        # Convert the given xy coordinates of the board to xy
        # coordinates of the location on the screen.
        return (XMARGIN + (boxx * BOXSIZE)), (TOPMARGIN + (boxy * BOXSIZE))
