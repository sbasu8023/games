import unittest
from dice import Dice


class TestDice(unittest.TestCase):

	def setUp(self):
		print("Setting up test...")
		self.dice1=Dice("Bob", 6)
		self.dice2=Dice("Rob", 6)
		self.dice3=Dice(23)

	def tearDown(self):
		print("Tearing down test....")
		pass

	def test_name_dice1a(self):
		self.assertEqual(self.dice1.get_name, "Bob")

	
	def test_name_dice1b(self):
		self.assertNotEqual(self.dice1.get_name, "Rob")

	def test_name_dice1c(self):
		self.assertIsNotNone(self.dice1.get_name)
	
	def test_name_dice2a(self):
		self.assertEqual(self.dice2.get_name, "Rob")

	
	def test_name_dice2b(self):
		self.assertNotEqual(self.dice2.get_name, "Bob")

	def test_name_dice2c(self):
		self.assertIsNotNone(self.dice2.get_name)


	"""
	def test_name_dice1d(self):
		self.assertIsNotEqual(self.dice1.get_name(), "Bob")
	"""

	def test_name_dice3a(self):
		self.assertEqual(self.dice3.get_name, 23)

	def test_name_dice3b(self):
		self.assertNotEqual(self.dice3.get_name, 98)

	def test_name_dice3c(self):
		self.assertIsNotNone(self.dice3.get_name)

	def test_roll_dice1a(self):
		for _ in range(100):
		    self.assertIn(self.dice1.roll(), [1, 2, 3, 4, 5, 6])
		    self.assertNotIn(self.dice1.roll(), [0, 7])
	
	def test_roll_dice2a(self):
		for _ in range(100):
		    self.assertIn(self.dice2.roll(), [1, 2, 3, 4, 5, 6])
		    self.assertNotIn(self.dice2.roll(), [0, 7])




if __name__ == '__main__':
	unittest.main()



