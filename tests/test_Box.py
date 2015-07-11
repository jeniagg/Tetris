import unittest
from class_drawBox import *


class PixelCoordTest(unittest.TestCase):
    def setUp(self):
        self.boxx = 320 + (boxx * 20)
        self.boxy = 75 + (boxy * 20)

    def converToPixelCoordsTest(self):
        self.pixel = (self.boxx,self.boxy)
        self.assertEqual(self.pixel(5,10),(420,275))
         

if __name__ == '__main__':
    unittest.main()