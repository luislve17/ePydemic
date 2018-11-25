"""
## TreeWidget ##
"""
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from AlnList import *
from AlnModule import *

class TreeWidget(QWidget):
	def __init__(self):
		super().__init__()
		self.main_layout = QVBoxLayout()	#Layout Vertical
		self.upper_layout = QHBoxLayout()		

		self.aln_desc = QTextEdit()
		self.aln_desc.setReadOnly(True)
		self.aln_list = AlnList(self.aln_desc)
		self.aln_module = AlnModule(self.aln_list)
		self.main_splitter = QSplitter(Qt.Vertical)

		self.upper_layout.addWidget(self.aln_list)
		self.upper_layout.addWidget(self.aln_module)
		self.upper_widget = QWidget()
		self.upper_widget.setLayout(self.upper_layout)
		self.main_splitter.addWidget(self.upper_widget)
		self.main_splitter.addWidget(self.aln_desc)
		self.main_layout.addWidget(self.main_splitter)

		self.setLayout(self.main_layout)	# Fijación del Layout   