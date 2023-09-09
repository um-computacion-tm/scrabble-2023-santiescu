import unittest
from Game.cell import Cell 
from Game.models import Tile

class TestCell(unittest.TestCase):
    def test_init(self):
        cell= Cell(multiplier=2, multiplier_type='letter', letter=None)
        self.assertEqual(
            cell.multiplier,
            2,
        )
        self.assertEqual(
            cell.multiplier_type,
            'letter',
        )
        self.assertIsNone(cell.letter)

    def test_add_letter(self):
        cell = Cell(multiplier=1, multiplier_type='')
        letter= Tile(letter='p', value=3)
        cell.add_letter(letter=letter)
        self.assertEqual(cell.letter, letter)

    def test_cell_value(self):
        cell = Cell(multiplier=1, multiplier_type='letter')
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter=letter)
        self.assertEqual(
            cell.calculate_value(),
            3,
        )

    def test_cell_multiplier_word(self):
        cell = Cell(multiplier=1, multiplier_type='letter')
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter=letter)

if __name__ == '__main__':
    unittest.main()
