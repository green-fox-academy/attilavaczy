import unittest
from encoder import duplicate_encode

class DuplicateEncode(unittest.TestCase):
    def test_char(self):
        self.assertEqual(duplicate_encode("din"),"(((")
        self.assertEqual(duplicate_encode("recede"),"()()()")
        self.assertEqual(duplicate_encode("Success"),")())())","should ignore case")
        self.assertEqual(duplicate_encode("(( @"),"))((")

unittest.main()
