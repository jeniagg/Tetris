import unittest
from Tetris import *


class APieceRotationTest(unittest.TestCase):
    def setUp(self):
        self.piece_L = ['.....',
                     '...O.',
                     '.OOO.',
                     '.....',
                     '.....']
        self.piece = random.randint(0, len(L_SHAPE_TEMPLATE) - 1),

    def test_rotation(self):
        self.assertEqual(self.piece_L, str(self.piece))


    def test_rotation_right(self):
        expected_piece = ['.....',
                          '..OO.',
                          '..O..',
                          '..O..',
                          '.....'],
        self.assertEqual(expected_piece, str(self.piece))


    def test_rotation_left(self):
        expected_piece = ['.O...',
                          '.OOO.',
                          '.....',
                          '.....'],
        self.assertEqual(expected_piece, str(self.piece))

if __name__ == '__main__':
    unittest.main()

