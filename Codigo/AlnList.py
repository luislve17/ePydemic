"""
## AlnList ##
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *

# Se muestra el contenido de los archivos mostrados en el ListWidget
class AlnList(QListWidget):
	def __init__(self, aln_list):
		super().__init__()
		self.setSelectionMode(QAbstractItemView.ExtendedSelection)
		self.aln_list = aln_list
		self.itemDoubleClicked.connect(self.showAlnList)

	def showAlnList(self, item):
		path = item.data(35)
		self.aln_list.setText(open(path).read())