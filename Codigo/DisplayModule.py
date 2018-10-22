"""
## DisplayModule ##
-- Por implementar --
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class DisplayModule(QWidget):
	def __init__(self):
		super().__init__()
		self.layout = QVBoxLayout()
		self.layout.addWidget(QLabel("TEST"))
		self.group_box = QGroupBox("Display Module")
		self.group_box.setLayout(self.layout)
		self.main_layout = QVBoxLayout()
		self.main_layout.addWidget(self.group_box)
		self.setLayout(self.main_layout)
