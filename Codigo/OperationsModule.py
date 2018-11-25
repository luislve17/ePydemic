"""
## OperationsModule ##
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from ImportButton import *
from AlignButton import *
from DeleteButton import *
from SequenceButton import *
from LoadButton import *
from UploadAlnButton import *
from LoadAlnButton import *

class OperationsModule(QWidget):
	def __init__(self, listing_module, display_module):
		super().__init__()		# Llamada rutinaria al constructor del padre
		self.setMinimumHeight(150)
		self.listing_module = listing_module
		self.display_module = display_module
		self.layout = QVBoxLayout()		# Layout vertical
		self.sub_layout = QHBoxLayout()		# Layout horizontal
		self.import_button = ImportButton(self.listing_module)	# Boton importar
		self.delete_button = DeleteButton(self.listing_module)	# boton delete
		self.sub_layout.addWidget(self.import_button)	# Adicion al layout
		self.sub_layout.addWidget(self.delete_button)	# Adicion al layout
		self.layout.addLayout(self.sub_layout)		# Agregar un cuadro que contiene otro Layout
		self.setLayout(self.layout)		# Fijacion del Layout

	def loadInfoOperations(self):
		self.import_button = ImportButton(self.listing_module)
		self.delete_button = DeleteButton(self.listing_module)

		self.sub_layout.addWidget(self.import_button)
		self.sub_layout.addWidget(self.delete_button)

	def loadAlignmentOperations(self):
		#self.sequence_button = SequenceButton(self.listing_module, self.display_module.align_tab)
		#self.align_button = AlignButton(self.listing_module)
		self.load_button = LoadButton(self.listing_module, self.display_module.align_tab.seq_list)
		self.delete_button = DeleteButton(self.listing_module)

		#self.layout.addWidget(self.sequence_button)
		self.sub_layout.addWidget(self.load_button)
		self.sub_layout.addWidget(self.delete_button)

	def loadTreeOperations(self):
		self.load_aln_button = LoadAlnButton(self.display_module.tree_tab.aln_list)
		self.upload_aln_button = UploadAlnButton(self.listing_module)
		self.delete_button = DeleteButton(self.listing_module)

		self.sub_layout.addWidget(self.load_aln_button)
		self.sub_layout.addWidget(self.upload_aln_button)
		self.sub_layout.addWidget(self.delete_button)