from board import Board
import unittest

class Test_board(unittest.TestCase):

	def setUp(self):
		self.game=Board()

	def tearDown(self):
		pass

	def test_get_board_1(self):
		self.assertEqual(type(self.game.get_board()), dict)

	def test_get_board_2(self):
		self.assertTrue(len(self.game.get_board())>0)

	def test_read_block_1(self):
		for i in range(25):
		    self.assertIn(self.game.read_block(i), ['normal', 'energy', 'poision', 'tools', 'snake'])


if __name__ == '__main__':
	unittest.main()