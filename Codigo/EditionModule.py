from PyQt4.QtCore import *
from PyQt4.QtGui import *

class EditionModule(QWidget):
	def __init__(self, initial_text_list=['', '', '']):
		super().__init__()
		self.module_layout = QVBoxLayout()
		self.group_label = QLabel("Grupo")
		self.group_input = QLineEdit(initial_text_list[0])
		self.name_label = QLabel("Nombre")
		self.name_input = QLineEdit(initial_text_list[1])
		self.path_label = QLabel("Ruta")
		self.path_input = QLineEdit(initial_text_list[2])

		self.group_layout = QHBoxLayout()
		self.group_layout.addWidget(self.group_label)
		self.group_layout.addWidget(self.group_input)

		self.name_layout = QHBoxLayout()
		self.name_layout.addWidget(self.name_label)
		self.name_layout.addWidget(self.name_input)

		self.path_layout = QHBoxLayout()
		self.path_layout.addWidget(self.path_label)
		self.path_layout.addWidget(self.path_input)

		self.module_layout.addLayout(self.group_layout)
		self.module_layout.addLayout(self.name_layout)
		self.module_layout.addLayout(self.path_layout)

		self.setLayout(self.module_layout)

	def getValues(self):
		return ({
			"group":self.group_input.text(),
			"name": self.name_input.text(),
			"path": self.path_input.text()
		})
