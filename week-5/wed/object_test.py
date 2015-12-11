import unittest
import object

class TestFunc(unittest.TestCase):

    def test_apply_function(self):
        array = [1, 2, 3]
        self.assertEqual(object.adder(array), [2, 3, 4])


unittest.main()
