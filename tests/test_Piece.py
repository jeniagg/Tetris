import unittest 
from designe import *
from Tetris import *


class TestPiece(unittest.TestCase):
  
    def setUp(self):
        piece = 'T'
        piece1 = 'S'
        piece2 = 'Z'
        piece3 = 'I'
        piece4 = 'O'
        piece5 = 'J'
        piece6 = 'L'
        
        self.piece6 = aboutPieces.drawPiece(piece6)
        self.piece5 = aboutPieces.drawPiece(piece5)
        self.piece4 = aboutPieces.drawPiece(piece4)
        self.piece3 = aboutPieces.drawPiece(piece3)
        self.piece2 = aboutPieces.drawPiece(piece2)
        self.piece1 = aboutPieces.drawPiece(piece1)
        self.piece = aboutPieces.drawPiece(piece)

    def test_t_shape(self):
        self.assertEqual([['.....',
                     '.O...',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..OO.',
                     '..O..',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '...O.',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..O..',
                     '.OO..',
                     '.....']], str(self.piece))

    def test_s_shape(self):
        self.assertEqual([['.....',
                     '.....',
                     '..OO.',
                     '.OO..',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..OO.',
                     '...O.',
                     '.....']], list(self.piece1))
    
    def test_z_shape(self):
        self.assertEqual([['.....',
                     '.....',
                     '.OO..',
                     '..OO.',
                     '.....'],
                    ['.....',
                     '..O..',
                     '.OO..',
                     '.O...',
                     '.....']], str(self.piece2))

    def test_I_shape(self):
        self.assertEqual([['..O..',
                     '..O..',
                     '..O..',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     'OOOO.',
                     '.....',
                     '.....']], str(self.piece3))

    def test_o_shape(self):
        self.assertEqual([['.....',
                     '.....',
                     '.OO..',
                     '.OO..',
                     '.....']], str(self.piece4))


    def test_J_shape(self):
        self.assertEqual([['.....',
                     '.O...',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..OO.',
                     '..O..',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '...O.',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..O..',
                     '.OO..',
                     '.....']], str(self.piece5))

    def test_L_shape(self):
        self.assertEqual([['.....',
                     '...O.',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..O..',
                     '..OO.',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '.O...',
                     '.....'],
                    ['.....',
                     '.OO..',
                     '..O..',
                     '..O..',
                     '.....']], str(self.piece6))

if __name__ == '__main__':
    unittest.main()