from PyQt4.QtCore import *
from PyQt4.QtGui import * 

class HelpModule(QScrollArea):
	def __init__(self):
		super().__init__()
		self.help_label = QLabel()
		self.help_label.setPixmap(QPixmap("assets/help.jpeg"))
		self.setWidget(self.help_label);