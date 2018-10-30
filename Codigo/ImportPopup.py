"""
## ImportPopup ##
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from ImportModule import *
from FileHandler import *
from os import walk

class ImportPopup(QMainWindow):
	def __init__(self, listing_module):
		super().__init__()		# Llamada obligatoria al constructor del padre
		self.main_widget = QWidget()		# Widget principal
		self.main_widget.setMinimumWidth(400)	# Dimensiones minimas

		self.listing_module = listing_module
		
		self.popup_layout = QVBoxLayout()	# Layout vertical
		
		self.main_widget.setLayout(self.popup_layout)	# Fijación del Layout
		self.setCentralWidget(self.main_widget)		# Fijacion del widget principal
		self.loadPopup()	# Funcion loadPopup

	def loadPopup(self):
		# Limpiando el popup antes de cargar algo
		for i in reversed(range(self.popup_layout.count())): 
			if self.popup_layout.itemAt(i).widget() != None:
				self.popup_layout.itemAt(i).widget().setParent(None)

		self.import_module = ImportModule()
		self.popup_layout.addWidget(self.import_module)	# Adicion al layout
		self.save_btn = QPushButton("OK")		# Boton OK
		self.save_btn.clicked.connect(self.loadGroup)	# Conectar el botón a la función
		self.cancel_btn = QPushButton("Cancelar")		# Boton Cancelar
		self.cancel_btn.clicked.connect(self.close)		# Conectar el botón a la función
		self.buttons_layout = QHBoxLayout()		# Layout Horizontal
		self.buttons_layout.addWidget(self.save_btn)	# Adicion al layout
		self.buttons_layout.addWidget(self.cancel_btn)	# Adicion al layout
		self.buttons_widget = QWidget()			# Widget
		self.buttons_widget.setLayout(self.buttons_layout)	# Fijación del Layout
		self.popup_layout.addWidget(self.buttons_widget)	# Adicion al layout

	def loadGroup(self):
		selected_group = self.import_module.import_combo.currentText()
		f = []
		group_path = 'data/group/'+selected_group+'/'
		for (dirpath, dirnames, filenames) in walk(group_path):
			file_paths = filenames
		for path in file_paths:
			self.listing_module.list_widget.addItem(FileHandler.loadEpyFile(group_path+path))
		self.close()