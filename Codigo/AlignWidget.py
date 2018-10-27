from PyQt4.QtCore import *
from PyQt4.QtGui import *

class AlignWidget(QWidget):
	def __init__(self):
		super().__init__()
		self.main_layout = QVBoxLayout()

		self.seq_desc = QTextEdit()
		self.seq_desc.setReadOnly(True)

		self.main_layout.addWidget(self.seq_desc)

		self.setLayout(self.main_layout)