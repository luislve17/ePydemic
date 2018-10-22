from PyQt4.QtCore import *
from PyQt4.QtGui import *

from EditionModule import *
from HLine import *

class EditionPopup(QMainWindow):
	def __init__(self):
		super().__init__()
		self.main_widget = QWidget()
		self.main_widget.setMinimumWidth(400)

		self.popup_layout = QVBoxLayout()
		
		self.main_widget.setLayout(self.popup_layout)
		self.setCentralWidget(self.main_widget)

	def loadParameters(self, items_list):
		# Limpiando el popup antes de cargar algo
		for i in reversed(range(self.popup_layout.count())): 
			if self.popup_layout.itemAt(i).widget() != None:
				self.popup_layout.itemAt(i).widget().setParent(None)

		if len(items_list) == 0:
			self.popup_layout.addWidget(QLabel("Seleccione algun item primero"))
			self.ok_btn = QPushButton("OK")
			self.ok_btn.clicked.connect(self.close)
			self.popup_layout.addWidget(self.ok_btn)

		else:
			for item in items_list:
				self.popup_layout.addWidget(EditionModule([item.data(33), item.data(34), item.data(35)]))
				self.popup_layout.addWidget(HLine())

			self.save_btn = QPushButton("Guardar")
			self.cancel_btn = QPushButton("Cancelar")
			self.cancel_btn.clicked.connect(self.close)
			self.buttons_layout = QHBoxLayout()
			self.buttons_layout.addWidget(self.save_btn)
			self.buttons_layout.addWidget(self.cancel_btn)
			self.buttons_widget = QWidget()
			self.buttons_widget.setLayout(self.buttons_layout)
			self.popup_layout.addWidget(self.buttons_widget)