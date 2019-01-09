import unittest
from dice import Dice


class TestDice(unittest.TestCase):

	def setUp(self):
		print("Setting up test...")
		self.dice1=Dice("Bob")
		#self.dice2=Dice("Rob")
		#self.dice3=Dice(23)

	def tearDown(self):
		pass

	def test_name_dice_for_casea(self):
		self.assertEqual(self.dice1.get_name, "Bob")

	"""
	def test_name_dice1b(self):
		self.assertNotEqual(self.dice1.get_name, "Rob")

	def test_name_dice1c(self):
		self.assertIsNotNone(self.dice1.get_name)

	def test_name_dice1d(self):
		self.assertIsNotEqual(self.dice1.get_name(), "Bob")

	def test_name_dice3a(self):
		self.assertEqual(self.dice3.get_name, 23)

	def test_name_dice3b(self):
		self.assertNotEqual(self.dice3.get_name, 98)

	def test_name_dice3c(self):
		self.assertIsNotNone(self.dice3.get_name)

	def test_name_dice3d(self):
		self.assertIsNotEqual(self.dice3.get_name(), 23)
     """


	if __name__ == '__main__':
		unittest.main()



