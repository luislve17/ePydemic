"""
## ImportModule ##
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import os

class ImportModule(QWidget):
	def __init__(self):
		super().__init__()		# Llamada obligatoria al constructor del padre
		self.import_label = QLabel("Grupo")		# Proporciona una visualización de texto
		self.import_combo = QComboBox()			# Combo
		self.layout = QHBoxLayout()		# Layout horizontal
		self.loadGroups()				# Cargar grupos al combo del popup
		self.layout.addWidget(self.import_label)	# Adicion al layout 
		self.layout.addWidget(self.import_combo)	# Adicion al layout 

		self.setLayout(self.layout)

	def loadGroups(self):
		root_path = "data/group"
		for root, dirs, files in os.walk(root_path): # Para todos los archivos de secuencia
			if len(dirs) != 0: # Si son directorios utilies de grupos
				self.import_combo.addItems(dirs) # Anadirlos