"""
## ImportModule ##
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class ImportModule(QWidget):
	def __init__(self):
		super().__init__()		# Llamada obligatoria al constructor del padre
		self.import_label = QLabel("Grupo")		# Proporciona una visualización de texto
		self.import_combo = QComboBox()			# Combo
		self.layout = QHBoxLayout()		# Layout horizontal
		# <prueba>
		self.import_combo.addItems(['Perú', 'Brasil', 'Bolivia'])	# Items del combo
		# </prueba>
		self.layout.addWidget(self.import_label)	# Adicion al layout 
		self.layout.addWidget(self.import_combo)	# Adicion al layout 

		self.setLayout(self.layout)
