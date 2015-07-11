import random
import time
import sys
from pygame.locals import *
from class_drawBox import *
from Menu import *
from collections import OrderedDict


class Game:
    def __init__(self, level=1):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        self.fullscreen = False
        self.clock = pygame.time.Clock()
        self.FPS = FPS
        self.level = level
        self.game_over = False
        self.is_running = True
        self.is_completed = False
        self.is_multiplayer = False
        self.is_restarted = False

    def events(self):
        pygame.display.flip()
        self.clock.tick(self.fps)
        self.screen.fill(colors.WHITE)
        if pygame.event.get(pygame.QUIT):
            terminate()
        self.event = pygame.event.get()

    def runGame():
        """ Here is the main loop for the game, first set up variables,
        then check if there is falling piece and if it don't start 
        a new piece at the top (thit is done with while), move the piece sideaways
        and let the piece fall if its time to fall and draw everything on the screen"""
        
        # setup variables for the start of the game
        board = aboutBoard_.getBlankBoard()
        lastMoveDownTime = time.time()
        lastMoveSidewaysTime = time.time()
        lastFallTime = time.time()
        movingLeft = False
        movingRight = False
        movingDown = False
        score = 0
        level, fallFreq = calculateLevelAndFallFreq(score)
        fallingPiece = aboutPieces.getNewPiece()
        nextPiece = aboutPieces.getNewPiece()

        while True:  # game loop
            if fallingPiece is None:
                # No falling piece in play, so start a new piece at the top
                fallingPiece = nextPiece
                nextPiece = aboutPieces.getNewPiece()
                lastFallTime = time.time()  # reset lastFallTime
                if not Lines.isValidPosition(board, fallingPiece):
                    return  # can't fit a new piece on the board, so game over
            checks.checkForQuit()

            for event in pygame.event.get():  # event handling loop
                if event.type == KEYUP:
                    if event.key == K_p:
                        # Pausing the game
                        DISPLAYSURF.fill(BGCOLOR)
                        Sound.pause(object)
                        lastFallTime = time.time()
                        lastMoveDownTime = time.time()
                        lastMoveSidewaysTime = time.time()
                    elif event.key == K_LEFT:
                        movingLeft = False
                    elif event.key == K_RIGHT:
                        movingRight = False
                    elif event.key == K_DOWN:
                        movingDown = False

                elif event.type == KEYDOWN:
                    # moving the piece sideways
                    if event.key == K_LEFT and Lines.isValidPosition(board, fallingPiece, adjX=-1):
                        fallingPiece['x'] -= 1
                        movingLeft = True
                        movingRight = False
                        lastMoveSidewaysTime = time.time()
                    elif event.key == K_RIGHT and Lines.isValidPosition(board, fallingPiece, adjX=1):
                        fallingPiece['x'] += 1
                        movingRight = True
                        movingLeft = False
                        lastMoveSidewaysTime = time.time()
                    # rotating the piece (if there is room to rotate)
                    elif event.key == K_UP:
                        fallingPiece['rotation'] = (fallingPiece['rotation'] + 1) % len(PIECES[fallingPiece['shape']])
                        if not Lines.isValidPosition(board, fallingPiece):
                            fallingPiece['rotation'] = (fallingPiece['rotation'] - 1) % len(PIECES[fallingPiece['shape']])
                    # making the piece fall faster with the down key
                    elif event.key == K_DOWN:
                        movingDown = True
                        if Lines.isValidPosition(board, fallingPiece, adjY=1):
                            fallingPiece['y'] += 1
                        lastMoveDownTime = time.time()
                    # move the current piece all the way down
                    elif event.key == K_SPACE:
                        movingDown = False
                        movingLeft = False
                        movingRight = False
                        for i in range(1, BOARDHEIGHT):
                            if not Lines.isValidPosition(board, fallingPiece, adjY=i):
                                break
                        fallingPiece['y'] += i - 1

            # handle moving the piece because of user input
            if (movingLeft or movingRight) and time.time() - lastMoveSidewaysTime > MOVESIDEWAYSFREQ:
                if movingLeft and Lines.isValidPosition(board, fallingPiece, adjX=-1):
                    fallingPiece['x'] -= 1
                elif movingRight and Lines.isValidPosition(board, fallingPiece, adjX=1):
                    fallingPiece['x'] += 1
                lastMoveSidewaysTime = time.time()
            if movingDown and time.time() - lastMoveDownTime > MOVEDOWNFREQ and Lines.isValidPosition(board, fallingPiece, adjY=1):
                fallingPiece['y'] += 1
                lastMoveDownTime = time.time()

            # let the piece fall if it is time to fall
            if time.time() - lastFallTime > fallFreq:
                # see if the piece has landed
                if not Lines.isValidPosition(board, fallingPiece, adjY=1):
                    # falling piece has landed, set it on the board
                    Lines.addToBoard(board, fallingPiece)
                    score += Lines.removeCompleteLines(board)
                    level, fallFreq = calculateLevelAndFallFreq(score)
                    fallingPiece = None
                else:
                    # piece did not land, so move the piece down
                    fallingPiece['y'] += 1
                    lastFallTime = time.time()

        # drawing everything on the screen
            DISPLAYSURF.fill(BGCOLOR)
            aboutBoard_.drawBoard(board)
            aboutBoard_.drawStatus(score, level)
            aboutPieces.drawNextPiece(nextPiece)

            if fallingPiece is not None:
                aboutPieces.drawPiece(fallingPiece)
            pygame.display.update()
            FPSCLOCK.tick(FPS)

    def runGame2():
        # setup variables for the start of the game
        board = aboutBoard_.getBlankBoard()
        board2 = aboutBoard_.getBlankBoard()
        lastMoveDownTime = time.time()
        lastMoveSidewaysTime = time.time()
        lastFallTime = time.time()
        lastMoveDownTime2 = time.time()
        lastMoveSidewaysTime2 = time.time()
        lastFallTime2 = time.time()
        movingLeft = False
        movingRight = False
        movingDown = False
        movingLeft1 = False
        movingRight1 = False
        movingDown1 = False
        score = 0
        score2 = 0
        level, fallFreq = calculateLevelAndFallFreq(score)
        level2, fallFreq2 = calculateLevelAndFallFreq2(score2)
        fallingPiece = aboutPieces.getNewPiece()
        fallingPiece2 = aboutPieces2.getNewPiece2()
        nextPiece = aboutPieces.getNewPiece()
        nextPiece2 = aboutPieces2.getNewPiece2()

        while True:  # game loop
            if fallingPiece is None:
                # No falling piece in play, so start a new piece at the top
                fallingPiece = nextPiece
                nextPiece = aboutPieces.getNewPiece()
                lastFallTime = time.time()  # reset lastFallTime
                if not Lines.isValidPosition(board, fallingPiece):
                    return  # can't fit a new piece on the board, so game over

            if fallingPiece2 is None:
                # No falling piece in play, so start a new piece at the top
                fallingPiece2 = nextPiece2
                nextPiece2 = aboutPieces2.getNewPiece2()
                lastFallTime2 = time.time()  # reset lastFallTime2
                if not Lines.isValidPosition(board2, fallingPiece2):
                    return  # can't fit a new piece on the board, so game over
            checks.checkForQuit()

            for event in pygame.event.get():  # event handling loop
                if event.type == KEYUP:
                    if event.key == K_p:
                        # Pausing the game
                        DISPLAYSURF.fill(BGCOLOR)
                        Sound2.pause(object)
                        lastFallTime = time.time()
                        lastMoveDownTime = time.time()
                        lastMoveSidewaysTime = time.time()
                    elif event.key == K_LEFT:
                        movingLeft = False
                    elif event.key == K_RIGHT:
                        movingRight = False
                    elif event.key == K_DOWN:
                        movingDown = False
                    elif event.key == K_a:
                        movingLeft1 = False
                    elif event.key == K_d:
                        movingRight1 = False
                    elif event.key == K_s:
                        movingDown1 = False

                elif event.type == KEYDOWN:
                    # moving the piece sideways
                    if event.key == K_LEFT and Lines.isValidPosition(board, fallingPiece, adjX=-1):
                        fallingPiece['x'] -= 1
                        movingLeft = True
                        movingRight = False
                        lastMoveSidewaysTime = time.time()
                    if event.key == K_a:
                        fallingPiece2['x'] -= 1
                        movingLeft1 = True
                        movingRight1 = False
                        lastMoveSidewaysTime2 = time.time()
                    elif event.key == K_RIGHT and Lines.isValidPosition(board, fallingPiece, adjX=1):
                        fallingPiece['x'] += 1
                        movingRight = True
                        movingLeft = False
                        lastMoveSidewaysTime = time.time()
                    elif event.key == K_d:
                        fallingPiece2['x'] += 1
                        movingRight1 = True
                        movingLeft1 = False
                        lastMoveSidewaysTime2 = time.time()
                    elif event.key == K_UP:
                        fallingPiece['rotation'] = (fallingPiece['rotation'] + 1) % len(PIECES[fallingPiece['shape']])
                        if not Lines.isValidPosition(board, fallingPiece):
                            fallingPiece['rotation'] = (fallingPiece['rotation'] - 1) % len(PIECES[fallingPiece['shape']])
                    elif event.key == K_w:
                        fallingPiece2['rotation'] = (fallingPiece2['rotation'] + 1) % len(PIECES[fallingPiece2['shape']])
                    elif event.key == K_DOWN:
                        movingDown = True
                        if Lines.isValidPosition(board, fallingPiece, adjY=1):
                            fallingPiece['y'] += 1
                        lastMoveDownTime = time.time()
                    elif event.key == K_s:
                        movingDown1 = True
                        fallingPiece2['y'] += 1
                        lastMoveDownTime2 = time.time()

                # move the current piece all the way down
        # handle moving the piece because of user input
            if (movingLeft or movingRight) and time.time() - lastMoveSidewaysTime > MOVESIDEWAYSFREQ:
                if movingLeft and Lines.isValidPosition(board, fallingPiece, adjX=-1):
                    fallingPiece['x'] -= 1
                elif movingRight and Lines.isValidPosition(board, fallingPiece, adjX=1):
                    fallingPiece['x'] += 1
                lastMoveSidewaysTime = time.time()
            if movingDown and time.time() - lastMoveDownTime > MOVEDOWNFREQ and Lines.isValidPosition(board, fallingPiece, adjY=1):
                fallingPiece['y'] += 1
                lastMoveDownTime = time.time()

            if time.time() - lastFallTime > fallFreq or time.time() - lastFallTime2 > fallFreq2:
                # see if the piece has landed
                if not (Lines.isValidPosition(board, fallingPiece, adjY=1) or
                        Lines.isValidPosition(board2, fallingPiece2, adjY=1)):
                    #  falling piece has landed, set it on the board
                    Lines.addToBoard(board, fallingPiece)
                    score += Lines.removeCompleteLines(board)
                    level, fallFreq = calculateLevelAndFallFreq(score)
                    fallingPiece = None
                else:
                    # piece did not land, just move the piece down
                    fallingPiece['y'] += 1
                    lastFallTime = time.time()
                    fallingPiece2['y'] += 1
                    lastFallTime2 = time.time()

        # drawing everything on the screen
            DISPLAYSURF.fill(BGCOLOR)
            aboutBoard_.drawBoard(board)
            aboutBoard_.drawBoard2(board)

            aboutBoard_.drawStatus(score, level)
            aboutBoard_.drawStatus2(score2, level2)

            aboutPieces.drawNextPiece(nextPiece)
            aboutPieces2.drawNextPiece2(nextPiece2)

            if fallingPiece is not None:
                aboutPieces.drawPiece(fallingPiece)
            if fallingPiece2 is not None:
                aboutPieces.drawPiece(fallingPiece2)
            pygame.display.update()
            FPSCLOCK.tick(FPS)

    def terminate():
        pygame.quit()
        sys.exit()


class aboutPieces:

    def drawNextPiece(piece):
        # draw the "next" text
        nextSurf = BASICFONT.render('Next:', True, TEXTCOLOR)
        nextRect = nextSurf.get_rect()
        nextRect.topleft = (WINDOWWIDTH - 120, 80)
        DISPLAYSURF.blit(nextSurf, nextRect)

        # draw the "next" piece
        aboutPieces.drawPiece(piece, pixelx=WINDOWWIDTH-120, pixely=100)

    def drawPiece(piece, pixelx=None, pixely=None):
        shapeToDraw = PIECES[piece['shape']][piece['rotation']]
        if pixelx is None and pixely is None:
            pixelx, pixely = drawBox_.convertToPixelCoords(piece['x'],
                                                           piece['y'])
        # draw each of the boxes that make up the piece
        for x in range(TEMPLATEWIDTH):
            for y in range(TEMPLATEHEIGHT):
                if shapeToDraw[y][x] != BLANK:
                    drawBox_.drawBox(None, None, piece['color'], pixelx +
                                     (x * BOXSIZE), pixely + (y * BOXSIZE))

    def getNewPiece():
        # return a random new piece in a random rotation and color
        shape = random.choice(list(PIECES.keys()))
        newPiece = {'shape': shape,
                    'rotation': random.randint(0, len(PIECES[shape]) - 1),
                    'x': int(BOARDWIDTH / 2) - int(TEMPLATEWIDTH / 2),
                    'y': -2,  # start it above the board (less than 0)
                    'color': random.randint(0, len(COLORS)-1)}
        return newPiece


class aboutPieces2:
    def drawNextPiece2(piece):
        # draw the "next" text
        nextSurf = BASICFONT.render('Next:', True, TEXTCOLOR)
        nextRect = nextSurf.get_rect()
        nextRect.topleft = (WINDOWWIDTH - 240, 80)
        DISPLAYSURF.blit(nextSurf, nextRect)

        # draw the "next" piece
        aboutPieces.drawPiece(piece, pixelx=WINDOWWIDTH-250, pixely=100)

    def getNewPiece2():
        # return a random new piece in a random rotation and color
        shape = random.choice(list(PIECES.keys()))
        newPiece2 = {'shape': shape,
                     'rotation': random.randint(0, len(PIECES[shape]) - 1),
                     'x': int((BOARDWIDTH2 / 2) - 12) - int(TEMPLATEWIDTH / 2),
                     'y': -2,  # start it above the board (i.e. less than 0)
                     'color': random.randint(0, len(COLORS)-1)}
        return newPiece2


class aboutBoard_:
    def drawBoard(board):
        # draw the border around the board
        pygame.draw.rect(DISPLAYSURF, BORDERCOLOR,
                         (XMARGIN - 3, TOPMARGIN - 7, (BOARDWIDTH * BOXSIZE) + 8,
                          (BOARDHEIGHT * BOXSIZE) + 8), 5)
        # fill the background of the board
        pygame.draw.rect(DISPLAYSURF, BGCOLOR, (XMARGIN, TOPMARGIN, BOXSIZE * BOARDWIDTH, BOXSIZE * BOARDHEIGHT))
        # draw the individual boxes on the board
        for x in range(BOARDWIDTH):
            for y in range(BOARDHEIGHT):
                drawBox_.drawBox(x, y, board[x][y])

    def drawBoard2(board2):
        # draw the border around the board
        pygame.draw.rect(DISPLAYSURF, BORDERCOLOR,
                         (XMARGIN - 250, TOPMARGIN - 7,
                          (BOARDWIDTH2 * BOXSIZE) + 12, (BOARDHEIGHT2 * BOXSIZE) + 250), 5)
        # fill the background of the board
        pygame.draw.rect(DISPLAYSURF, BGCOLOR,
                         (XMARGIN, TOPMARGIN,
                          BOXSIZE * BOARDWIDTH2, BOXSIZE * BOARDHEIGHT2))
        # draw the individual boxes on the board
        for x in range(BOARDWIDTH2):
            for y in range(BOARDHEIGHT2):
                drawBox_.drawBox(x, y, board2[x][y])

    def getBlankBoard():
        # create and return a new blank board data structure
        board = []
        for i in range(BOARDWIDTH):
            board.append([BLANK] * BOARDHEIGHT)
        return board

    def showTextScreen(text):
        # This function displays large text in the
        # center of the screen until a key is pressed.
        titleSurf, titleRect = makeTextObjs(text, BIGFONT, TEXTSHADOWCOLOR)
        titleRect.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2))
        DISPLAYSURF.blit(titleSurf, titleRect)

        # Draw the text
        titleSurf, titleRect = makeTextObjs(text, BIGFONT, TEXTCOLOR)
        titleRect.center = (int(WINDOWWIDTH / 2) - 3,
                            int(WINDOWHEIGHT / 2) - 3)
        DISPLAYSURF.blit(titleSurf, titleRect)

        # Draw the additional "Press a key to play." text.
        pressKeySurf, pressKeyRect = makeTextObjs('Press a key to play.', BASICFONT, TEXTCOLOR)
        pressKeyRect.center = (int(WINDOWWIDTH / 2),
                               int(WINDOWHEIGHT / 2) + 100)
        DISPLAYSURF.blit(pressKeySurf, pressKeyRect)

        while checks.checkForKeyPress() is None:
            pygame.display.update()
            FPSCLOCK.tick()

    def drawStatus(score, level):
        # draw the score text

        scoreSurf = BASICFONT.render('Score: %s' % score, True, TEXTCOLOR)
        scoreRect = scoreSurf.get_rect()
        scoreRect.topleft = (WINDOWWIDTH - 150, 20)
        DISPLAYSURF.blit(scoreSurf, scoreRect)

        # draw the level text
        levelSurf = BASICFONT.render('Level: %s' % level, True, TEXTCOLOR)
        levelRect = levelSurf.get_rect()
        levelRect.topleft = (WINDOWWIDTH - 150, 50)
        DISPLAYSURF.blit(levelSurf, levelRect)

    def drawStatus2(score2, level2):
        # draw the score text

        scoreSurf = BASICFONT.render('Score: %s' % score2, True, TEXTCOLOR)
        scoreRect = scoreSurf.get_rect()
        scoreRect.topleft = (WINDOWWIDTH - 270, 20)
        DISPLAYSURF.blit(scoreSurf, scoreRect)

        # draw the level text
        levelSurf = BASICFONT.render('Level: %s' % level2, True, TEXTCOLOR)
        levelRect = levelSurf.get_rect()
        levelRect.topleft = (WINDOWWIDTH - 270, 50)
        DISPLAYSURF.blit(levelSurf, levelRect)


class Sound(object):
    # Creates a sound file, currently placeholder

    def __init__(self, sound_file):
        self.sound_file = sound_file

    def play(self):
        while True:  # game loop
            if random.randint(0, 1) == 0:
                pygame.mixer.music.load('tetrisb.mid')
            else:
                pygame.mixer.music.load('tetrisc.mid')
            pygame.mixer.music.play(-1, 0.0)
            Game.runGame()
            pygame.mixer.music.stop()
            aboutBoard_.showTextScreen('Game Over')
        pass

    def pause(self):
        pygame.mixer.music.stop()
        aboutBoard_.showTextScreen('Paused')
        # pause until a key press
        pygame.mixer.music.play(-1, 0.0)
        pass

    def stop(self):
        pygame.mixer.music.stop()
        pass

    def __repr__(self):
        return '%s(%r)' % (self.__class__, self.__dict__)


class Sound2(object):
    # Creates a sound file, currently placeholder

    def __init__(self, sound_file):
        self.sound_file = sound_file

    def play(self):
        while True:  # game loop
            if random.randint(0, 1) == 0:
                pygame.mixer.music.load('tetrisb.mid')
            else:
                pygame.mixer.music.load('tetrisc.mid')
            pygame.mixer.music.play(-1, 0.0)
            Game.runGame2()
            pygame.mixer.music.stop()
            aboutBoard_.showTextScreen('Game Over')
        pass

    def pause(self):
        pygame.mixer.music.stop()
        aboutBoard_.showTextScreen('Paused')
        # pause until a key press
        pygame.mixer.music.play(-1, 0.0)
        pass

    def stop(self):
        pygame.mixer.music.stop()
        pass

    def __repr__(self):
        return '%s(%r)' % (self.__class__, self.__dict__)


class checks:
    def checkForKeyPress():
        # Go through event queue looking for a KEYUP event.
        # Grab KEYDOWN events to remove them from the event queue.
        checks.checkForQuit()
        for event in pygame.event.get([KEYDOWN, KEYUP]):
            if event.type == KEYDOWN:
                continue
            return event.key
        return None

    def checkForQuit():
        for event in pygame.event.get(QUIT):  # get all the QUIT events
            Game.terminate()
        for event in pygame.event.get(KEYUP):  # get all the KEYUP events
            if event.key == K_ESCAPE:
                Game.terminate()
            pygame.event.post(event)  # put the other KEYUP event objects back


class Lines:
    def addToBoard(board, piece):
        # fill in the board based on piece's location, shape, and rotation
        for x in range(TEMPLATEWIDTH):
            for y in range(TEMPLATEHEIGHT):
                if PIECES[piece['shape']][piece['rotation']][y][x] != BLANK:
                    board[x + piece['x']][y + piece['y']] = piece['color']

    def addToBoard2(board, piece):
        # fill in the board based on piece's location, shape, and rotation

        for x in range(TEMPLATEWIDTH):
            for y in range(TEMPLATEHEIGHT):
                if PIECES[piece['shape']][piece['rotation']][y][x] != BLANK:
                    board[[x + piece['x']][y + piece['y']]].append(piece['color'])

    def isOnBoard(x, y):
        return x >= 0 and x < BOARDWIDTH and y < BOARDHEIGHT

    def isValidPosition(board, piece, adjX=0, adjY=0):
        # Return True if the piece is within the board and not colliding
        for x in range(TEMPLATEWIDTH):
            for y in range(TEMPLATEHEIGHT):
                isAboveBoard = y + piece['y'] + adjY < 0
                if isAboveBoard or PIECES[piece['shape']][piece['rotation']][y][x] == BLANK:
                    continue
                if not Lines.isOnBoard(x + piece['x'] + adjX, y + piece['y'] + adjY):
                    return False
                if board[x + piece['x'] + adjX][y + piece['y'] + adjY] != BLANK:
                    return False
        return True

    def isCompleteLine(board, y):
        # Return True if the line filled with boxes with no gaps.
        for x in range(BOARDWIDTH):
            if board[x][y] == BLANK:
                return False
        return True

    def isCompleteLine2(board, y):
        # Return True if the line filled with boxes with no gaps.
        for x in range(BOARDWIDTH2):
            if board[x][y] == BLANK:
                return False
        return True

    def removeCompleteLines(board):
        numLinesRemoved = 0
        y = BOARDHEIGHT - 1
        while y >= 0:
            if Lines.isCompleteLine(board, y):
                # Remove the line and pull boxes down by one line.
                for pullDownY in range(y, 0, -1):
                    for x in range(BOARDWIDTH):
                        board[x][pullDownY] = board[x][pullDownY-1]
                # Set very top line to blank.
                for x in range(BOARDWIDTH):
                    board[x][0] = BLANK
                numLinesRemoved += 1
            else:
                y -= 1  # move on to check next row up
        return numLinesRemoved

def makeTextObjs(text, font, color):
    surf = font.render(text, True, color)
    return surf, surf.get_rect()


def calculateLevelAndFallFreq(score):
    # Based on the score, return the level the player is on and
    # how many seconds pass until a falling piece falls one space.
    level = int(score / 10) + 1
    fallFreq = 0.27 - (level * 0.02)
    return level, fallFreq


def calculateLevelAndFallFreq2(score2):
    # Based on the score, return the level the player is on and
    # how many seconds pass until a falling piece falls one space.
    level2 = int(score2 / 10) + 1
    fallFreq2 = 0.27 - (level2 * 0.02)
    return level2, fallFreq2


pygame.init()
pygame.display.set_caption('Tetris')
pygame.mouse.set_visible(True)
screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont('monospace', 30)
game = Game()


def start_level(level):
    main_menu.is_active = False
    pygame.mouse.set_visible(False)


def start_main_menu():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, BIGFONT
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    BIGFONT = pygame.font.Font('freesansbold.ttf', 100)
    pygame.display.set_caption('Tetris')
    aboutBoard_.showTextScreen('Tetris')

    while main_menu.is_active:
        main_menu.draw()
        handle_menu_event(main_menu)
        pygame.display.update()
        clock.tick(FPS)


def start_single_player_level_menu():
    game.is_multiplayer = False
    Sound.play(object)


def start_multiplayer_level_menu():
    game.is_multiplayer = True
    Sound2.play(object)


main_menu = Menu(
    screen, OrderedDict(
        [
         ('Single Player',  start_single_player_level_menu),
         ('Two Players', start_multiplayer_level_menu),
         ('Quit Game', Game.terminate)]
    ))

levels_available = [(str(lvl), (start_level, lvl))
                    for lvl in range(1, 1)]
load_level_menu = Menu(screen, OrderedDict(levels_available))


def handle_menu_event(menu):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game.terminate()

        elif event.type == KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if menu == main_menu:
                    Game.terminate()
                else:
                    start_main_menu()

            if (event.key == pygame.K_UP or event.key == pygame.K_DOWN)\
                    and menu.current_option is None:
                menu.current_option = 0
                pygame.mouse.set_visible(False)
            elif event.key == pygame.K_UP and menu.current_option > 0:
                menu.current_option -= 1
            elif event.key == pygame.K_UP and menu.current_option == 0:
                menu.current_option = len(menu.options) - 1
            elif event.key == pygame.K_DOWN \
                    and menu.current_option < len(menu.options) - 1:
                menu.current_option += 1
            elif event.key == pygame.K_DOWN \
                    and menu.current_option == len(menu.options) - 1:
                menu.current_option = 0
            elif event.key == pygame.K_RETURN and \
                    menu.current_option is not None:
                option = menu.options[menu.current_option]
                if not isinstance(option.function, tuple):
                    option.function()
                else:
                    option.function[0](option.function[1])

        elif event.type == MOUSEBUTTONUP:
            for option in menu.options:
                if option.is_selected:
                    if not isinstance(option.function, tuple):
                        option.function()
                    else:
                        option.function[0](option.function[1])

        if pygame.mouse.get_rel() != (0, 0):
            pygame.mouse.set_visible(True)
            menu.current_option = None
