from PyQt4.QtCore import *
from PyQt4.QtGui import *

from ListWidget import *

class ListingModule(QWidget):
	def __init__(self):
		super().__init__()
		self.layout = QHBoxLayout()
		self.list_widget = ListWidget()
		self.layout.addWidget(self.list_widget)
		self.setLayout(self.layout)