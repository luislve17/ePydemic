from PyQt4.QtCore import *
from PyQt4.QtGui import *

#from EditButton import *
from ImportButton import *
from AlignButton import *
from DeleteButton import *
from SequenceButton import *

class OperationsModule(QWidget):
	def __init__(self, listing_module, display_module):
		super().__init__()
		self.setMinimumHeight(150)
		self.listing_module = listing_module
		self.display_module = display_module
		self.layout = QVBoxLayout()
		self.sub_layout = QHBoxLayout()
		self.import_button = ImportButton(self.listing_module)
		self.delete_button = DeleteButton(self.listing_module)
		self.sub_layout.addWidget(self.import_button)
		self.sub_layout.addWidget(self.delete_button)
		self.layout.addLayout(self.sub_layout)
		self.setLayout(self.layout)

	def loadInfoOperations(self):
		self.import_button = ImportButton(self.listing_module)
		self.delete_button = DeleteButton(self.listing_module)
		self.sub_layout.addWidget(self.import_button)
		self.sub_layout.addWidget(self.delete_button)

	def loadAlignmentOperations(self):
		self.sequence_button = SequenceButton(self.listing_module, self.display_module.align_tab)
		self.align_button = AlignButton(self.listing_module)
		self.delete_button = DeleteButton(self.listing_module)

		self.layout.addWidget(self.sequence_button)
		self.sub_layout.addWidget(self.align_button)
		self.sub_layout.addWidget(self.delete_button)