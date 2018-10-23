from PyQt4.QtCore import *
from PyQt4.QtGui import *

from ImportPopup import *

class ImportButton(QPushButton):
	def __init__(self, listing_module):
		super().__init__()
		self.setText("Importar")
		self.import_popup = ImportPopup(listing_module)
		self.clicked.connect(self.import_selection)

	def import_selection(self):
		self.import_popup.show()