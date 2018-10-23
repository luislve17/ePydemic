from PyQt4.QtCore import *
from PyQt4.QtGui import *

from ImportModule import *
from FileHandler import *
from os import walk

class ImportPopup(QMainWindow):
	def __init__(self, listing_module):
		super().__init__()
		self.main_widget = QWidget()
		self.main_widget.setMinimumWidth(400)

		self.listing_module = listing_module
		
		self.popup_layout = QVBoxLayout()
		
		self.main_widget.setLayout(self.popup_layout)
		self.setCentralWidget(self.main_widget)
		self.loadPopup()

	def loadPopup(self):
		# Limpiando el popup antes de cargar algo
		for i in reversed(range(self.popup_layout.count())): 
			if self.popup_layout.itemAt(i).widget() != None:
				self.popup_layout.itemAt(i).widget().setParent(None)

		self.import_module = ImportModule()
		self.popup_layout.addWidget(self.import_module)
		self.save_btn = QPushButton("OK")
		self.save_btn.clicked.connect(self.loadGroup)
		self.cancel_btn = QPushButton("Cancelar")
		self.cancel_btn.clicked.connect(self.close)
		self.buttons_layout = QHBoxLayout()
		self.buttons_layout.addWidget(self.save_btn)
		self.buttons_layout.addWidget(self.cancel_btn)
		self.buttons_widget = QWidget()
		self.buttons_widget.setLayout(self.buttons_layout)
		self.popup_layout.addWidget(self.buttons_widget)

	def loadGroup(self):
		selected_group = self.import_module.import_combo.currentText()
		f = []
		group_path = 'data/group/'+selected_group+'/'
		for (dirpath, dirnames, filenames) in walk(group_path):
			file_paths = filenames
		for path in file_paths:
			self.listing_module.list_widget.addItem(FileHandler.loadEpyFile(group_path+path))
		self.close()