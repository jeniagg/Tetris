class colors:

    #         R    G    B
    WHITE = (255, 255, 255)
    GRAY = (185, 185, 185)
    BLACK = (0, 0, 0)
    RED = (155, 0, 0)
    LIGHTRED = (175, 20, 20)
    GREEN = (0, 155, 0)
    LIGHTGREEN = (20, 175, 20)
    BLUE = (0, 0, 155)
    LIGHTBLUE = (20, 20, 175)
    YELLOW = (155, 155, 0)
    LIGHTYELLOW = (175, 175, 20)

BORDERCOLOR = colors.BLUE
BGCOLOR = colors.BLACK
TEXTCOLOR = colors.WHITE
TEXTSHADOWCOLOR = colors.GRAY
COLORS = (colors.BLUE, colors.GREEN, colors.RED, colors.YELLOW)
LIGHTCOLORS = (colors.LIGHTBLUE, colors.LIGHTGREEN,
               colors.LIGHTRED, colors.LIGHTYELLOW)
assert len(COLORS) == len(LIGHTCOLORS)  # each color must have light color
