"""
## DisplayModule ##
-- Por implementar --
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from InfoWidget import *
from AlignWidget import *
from TreeWidget import *
from HelpModule import *

class DisplayModule(QWidget):
	def __init__(self, tools_module):
		super().__init__()		# Llamada obligatoria al constructor del padre
		self.layout = QVBoxLayout()			# Layout vertical
		
		self.tools_module = tools_module

		self.main_tab_widget = QTabWidget()		# Proporciona una pila de widgets con pestañas
		self.main_tab_widget.currentChanged.connect(self.loadOperations)
		self.layout.addWidget(self.main_tab_widget)		# Adicion al layout 
		self.group_box = QGroupBox("Display Module")	# Proporciona una marco de cuadro de grupo con titulo, Display Module
		self.group_box.setLayout(self.layout)			# Fijación del Layout

		self.info_tab = InfoWidget(self.tools_module.listing_module)	# Llamada a la clase InfoWidget
		self.align_tab = AlignWidget()				# Llamada a la clase AlignWidget
		self.tree_tab = TreeWidget()
		self.help_tab = HelpModule()

		self.main_tab_widget.addTab(self.info_tab, "Información")		# Añade pestaña "Info"
		self.main_tab_widget.addTab(self.align_tab, "Alineamiento")		# Añade pestaña "Alineamiento"
		self.main_tab_widget.addTab(self.tree_tab, "Arbol Filogenético")# Añade pestaña "Arbol FIlogenético"
		self.main_tab_widget.addTab(self.help_tab, "Ayuda(?)")			# Añade pestaña "Ayuda"

		self.main_layout = QVBoxLayout()		# Layout vertical
		self.main_layout.addWidget(self.group_box)		# Adicion al layout 
		self.setLayout(self.main_layout)		# Fijación del Layout

	def loadOperations(self):
		# Cleaning layouts
		if hasattr(self.tools_module, 'operations_module'): # Revisa si se inicializo el objeto correctamente
			operations_sublayout = self.tools_module.operations_module.sub_layout
			operations_layout = self.tools_module.operations_module.layout
			for i in reversed(range(operations_layout.count())): 
				if operations_layout.itemAt(i).widget() != None:
					operations_layout.itemAt(i).widget().setParent(None)

			for i in reversed(range(operations_sublayout.count())): 
				if operations_sublayout.itemAt(i).widget() != None:
					operations_sublayout.itemAt(i).widget().setParent(None)

			# Crear botones
			current_tab = self.main_tab_widget.currentIndex()
			if current_tab is 0:
				self.tools_module.operations_module.loadInfoOperations()

			elif current_tab is 1:
				self.tools_module.operations_module.loadAlignmentOperations()

			elif current_tab is 2:
				self.tools_module.operations_module.loadTreeOperations()