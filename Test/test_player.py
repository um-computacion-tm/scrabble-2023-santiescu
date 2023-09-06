import unittest
from Game.player import Player 

class TestPlayer(unittest.TestCase)
    def test_init(self):
        board = board()
        self.assertEqual(
            len(board.grid),
            15,
        )
        self.assertEqual(
            len(board.grid [0]),
            15,
        )

if __name__ == '__main__':
    unittest.main()