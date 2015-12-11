import unittest
from wizard import Wizard

class TestWizard(unittest.TestCase):
    def test_existance(self):
        wizard = Wizard('Merlin', 40, 10, 20)

    def test_inheritance(self):
        wizard = Wizard('Merlin', 40, 10, 20)
        self.assertEqual(wizard.hp, 40)

    def test_manna(self):
        wizard = Wizard('Merlin', 40, 10, 20)
        self.assertEqual(wizard.manna, 20)

    def test_strike(self):
        wizard = Wizard('Merlin', 40, 10, 20)
        opponent = Wizard('Hitler', 40, 20, 22)
        wizard.strike(opponent)
        self.assertEqual(wizard.hp, 43)
        self.assertEqual(opponent.hp, 30)

    def test_reduce_manna(self):
        wizard = Wizard('Merlin', 40, 10, 20)
        wizard.reduce_manna(self)
        self.assertEqual(wizard.manna, 15)
unittest.main()
