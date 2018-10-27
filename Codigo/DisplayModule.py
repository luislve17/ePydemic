"""
## DisplayModule ##
-- Por implementar --
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from InfoWidget import *
from AlignWidget import *

class DisplayModule(QWidget):
	def __init__(self, tools_module):
		super().__init__()
		self.layout = QVBoxLayout()
		
		self.tools_module = tools_module

		self.main_tab_widget = QTabWidget()
		self.main_tab_widget.currentChanged.connect(self.loadOperations)
		self.layout.addWidget(self.main_tab_widget)
		self.group_box = QGroupBox("Display Module")
		self.group_box.setLayout(self.layout)

		self.info_tab = InfoWidget(self.tools_module.listing_module)
		self.align_tab = AlignWidget()
		self.main_tab_widget.addTab(self.info_tab, "Info")		
		self.main_tab_widget.addTab(self.align_tab, "Alineamiento")		

		self.main_layout = QVBoxLayout()
		self.main_layout.addWidget(self.group_box)
		self.setLayout(self.main_layout)

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

			current_tab = self.main_tab_widget.currentIndex()
			if current_tab is 0:
				self.tools_module.operations_module.loadInfoOperations()

			elif current_tab is 1:
				self.tools_module.operations_module.loadAlignmentOperations()
						