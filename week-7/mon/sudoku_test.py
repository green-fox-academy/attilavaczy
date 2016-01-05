import unittest
from sudoku import *

class TestSudoku(unittest.TestCase):
   def test_validate_row(self):
       self.assertEqual(validate_row([]), False)

   def test_size2(self):
       self.assertEqual(validate_row([1, 2]), True)

unittest.main()
