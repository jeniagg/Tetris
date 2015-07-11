import unittest
from Tetris import *


class ANewBoard(unittest.TestCase):
    def setUp(self):
        board = []
        self.board = aboutBoard_.drawBoard()

    def isBlankBoard(self):
        expected_board = aboutBoard_.getBlankBoard()
        self.assertEqual(expected_board, self.board)

    def drawBoardTest(self):
        board = []
        self.assertEqual(aboutBoard_.drawBoard(), self.board)


if __name__ == '__main__':
    unittest.main()