from PyQt4.QtCore import *
from PyQt4.QtGui import *

from EditButton import *

class OperationsModule(QWidget):
	def __init__(self, listing_module):
		super().__init__()
		self.listing_module = listing_module
		self.layout = QHBoxLayout()
		self.edit_button = EditButton(self.listing_module)
		self.text_label = QLabel("TEST")
		self.layout.addWidget(self.edit_button)
		self.setLayout(self.layout)