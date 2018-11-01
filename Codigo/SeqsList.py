from PyQt4.QtCore import *
from PyQt4.QtGui import *

class SeqsList(QListWidget):
	def __init__(self, seq_desc):
		super().__init__()
		self.setSelectionMode(QAbstractItemView.ExtendedSelection)
		self.seq_desc = seq_desc # Cuadro de muestra de la secuencia seleccionada
		self.itemDoubleClicked.connect(self.showSequence)

	def showSequence(self, item):
		path = item.data(35) # Ruta al archivo .fasta respectivo
		self.seq_desc.setText(open(path).read())	# Muestra la secuencia

