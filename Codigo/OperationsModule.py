from PyQt4.QtCore import *
from PyQt4.QtGui import *

from EditButton import *
from ImportButton import *

class OperationsModule(QWidget):
	def __init__(self, listing_module):
		super().__init__()
		self.listing_module = listing_module
		self.layout = QVBoxLayout()
		self.import_button = ImportButton(self.listing_module)
		self.edit_button = EditButton(self.listing_module)
		self.text_label = QLabel("TEST")
		self.layout.addWidget(self.import_button)
		#self.layout.addWidget(self.edit_button)
		self.setLayout(self.layout)