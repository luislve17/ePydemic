"""
## EditionModule ##
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class EditionModule(QWidget):
	def __init__(self, initial_text_list=['', '', '']):
		super().__init__()		# Llamada obligatoria al constructor del padre
		self.module_layout = QVBoxLayout()		# Layout vertical
		self.group_label = QLabel("Grupo")		# Proporciona una visualización de texto
		self.group_input = QLineEdit(initial_text_list[0])	# Campo de entrada
		self.name_label = QLabel("Nombre")		# Proporciona una visualización de texto
		self.name_input = QLineEdit(initial_text_list[1])	# Campo de entrada
		self.path_label = QLabel("Ruta")		# Proporciona una visualización de texto
		self.path_input = QLineEdit(initial_text_list[2])	# Campo de entrada

		self.group_layout = QHBoxLayout()		# Layout horizontal
		self.group_layout.addWidget(self.group_label)	# Adicion al layout 
		self.group_layout.addWidget(self.group_input)	# Adicion al layout 

		self.name_layout = QHBoxLayout()		# Layout horizontal
		self.name_layout.addWidget(self.name_label)		# Adicion al layout 
		self.name_layout.addWidget(self.name_input)		# Adicion al layout 

		self.path_layout = QHBoxLayout()		# Layout horizontal
		self.path_layout.addWidget(self.path_label)		# Adicion al layout 
		self.path_layout.addWidget(self.path_input)		# Adicion al layout 

		self.module_layout.addLayout(self.group_layout)	# Agregar un cuadro que contiene otro Layout
		self.module_layout.addLayout(self.name_layout)
		self.module_layout.addLayout(self.path_layout)

		self.setLayout(self.module_layout)

	def getValues(self):
		return ({
			"group":self.group_input.text(),
			"name": self.name_input.text(),
			"path": self.path_input.text()
		})
