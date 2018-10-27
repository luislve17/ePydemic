"""
## ToolsModule ##
* Widgets incluidos:
	* ListingModule: Lista de elementos geneticos cargados
	* OperactionsModule: Modulo de acciones a aplicar a los items en ListingModule

* Ubicacion absoluta: Izquierda
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from ListingModule import *
from OperationsModule import *
from HLine import *

class ToolsModule(QWidget):
	def __init__(self):
		super().__init__()	# Llamada al constructor del padre
		self.layout = QVBoxLayout()	# Layout vertical
		self.layout_splitter = QSplitter(Qt.Vertical)
		self.listing_module = ListingModule()	# Modulo de lista de items/secuencias geneticas
		#self.display_module = display_module
		#self.operations_module = OperationsModule(self.listing_module, self.display_module)	# Modulo de acciones
		
		# Adicion de los widgets al layout splitter
		self.layout_splitter.addWidget(self.listing_module)
		#self.layout_splitter.addWidget(self.operations_module)	

		self.layout.addWidget(self.layout_splitter)

		self.group_box = QGroupBox("Tools Module") # Marco del modulo
		self.group_box.setLayout(self.layout)	# Asignacion del layout vertical al marco
		self.main_layout = QVBoxLayout()	# Fijacion del layout principal
		self.main_layout.addWidget(self.group_box) # Adicion del marco al layout principal

		self.setLayout(self.main_layout) # Setteo del layout principal

	def setOperationsModule(self, display_module):
		self.display_module = display_module
		self.operations_module = OperationsModule(self.listing_module, self.display_module)	# Modulo de acciones
		self.layout_splitter.addWidget(self.operations_module)	

