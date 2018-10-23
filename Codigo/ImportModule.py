from PyQt4.QtCore import *
from PyQt4.QtGui import *

class ImportModule(QWidget):
	def __init__(self):
		super().__init__()
		self.import_label = QLabel("Grupo")
		self.import_combo = QComboBox()
		self.layout = QHBoxLayout()
		# <prueba>
		self.import_combo.addItems(['Perú', 'Brasil', 'Bolivia'])
		# </prueba>
		self.layout.addWidget(self.import_label)
		self.layout.addWidget(self.import_combo)

		self.setLayout(self.layout)
