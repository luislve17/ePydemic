"""
## ListModule ##
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from ListWidget import *

class ListingModule(QWidget):
	def __init__(self):		
		super().__init__()		# Llamada obligatoria al constructor del padre
		self.layout = QHBoxLayout()		# Layout horizontal
		self.list_widget = ListWidget()
		self.layout.addWidget(self.list_widget)	# Adicion al layout
		self.setLayout(self.layout)		# Fijacion del Layout