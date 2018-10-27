from PyQt4.QtCore import *
from PyQt4.QtGui import *

class AlignButton(QPushButton):
	def __init__(self, listing_module):
		super().__init__()
		self.listing_module = listing_module
		self.setText("Alinear")
		self.clicked.connect(self.alignSequences)

	def alignSequences(self):
		print("TODO: Alineamiento") #TODO