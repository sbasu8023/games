import csv
import re
import sys

class Board (object):

	def __init__ (self): 
		self._block=None

 
		self._load_file='games.csv'
		try:
		    with open(self._load_file, 'r') as csv_file:
			    csv_content=csv.reader(csv_file)
			    self._board={line[0]:re.findall(r'[a-z]+', line[1])[0] for line in csv_content}
		except:
			self._board={}
			print("ERROR: File Not Found or invalid file")
			sys.exit (1)

	def get_board(self):
		return self._board

	def read_block(self, block_number):
		if self._board:
			self._block=str(block_number)
			return self._board[self._block]

	def set_board(self, game_file):
		self._load_file=game_file
		with open(self._load_file, 'r') as csv_file:
			csv_content=csv.reader(csv_file)
			self._board={line[0]:re.findall(r'[a-z]+', line[1])[0] for line in csv_content}


