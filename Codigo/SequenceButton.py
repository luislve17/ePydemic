from PyQt4.QtCore import *
from PyQt4.QtGui import *

class SequenceButton(QPushButton):
	def __init__(self, listing_module, align_widget):
		super().__init__()
		self.listing_module = listing_module
		self.align_widget = align_widget
		self.setText("Ver secuencia")
		self.clicked.connect(self.showSequence)

	def showSequence(self):
		selected_species = self.listing_module.list_widget.list.selectedItems()[0]
		path = "data/content/" + selected_species.data(35).lower().replace(" ", "_") + "/seq.fasta"
		self.align_widget.seq_desc.setText(open(path).read())