"""
## DisplayModule ##
-- Por implementar --
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from InfoWidget import *

class DisplayModule(QWidget):
	def __init__(self, tools_module):
		super().__init__()
		self.layout = QVBoxLayout()
		
		self.tools_module = tools_module

		self.main_tab_widget = QTabWidget() 
		self.layout.addWidget(self.main_tab_widget)
		self.group_box = QGroupBox("Display Module")
		self.group_box.setLayout(self.layout)

		self.info_tab = InfoWidget(self.tools_module.listing_module)
		self.main_tab_widget.addTab(self.info_tab, "Info")		

		self.main_layout = QVBoxLayout()
		self.main_layout.addWidget(self.group_box)
		self.setLayout(self.main_layout)
