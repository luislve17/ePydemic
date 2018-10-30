"""
## EditButton ##
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from EditionPopup import *

class EditButton(QPushButton):
	def __init__(self, listing_module):
		super().__init__()		# Llamada obligatoria al constructor del padre
		self.setText("Editar")		# Reemplaza el texto 
		self.edit_popup = EditionPopup()
		self.clicked.connect(self.edit_selection)	# Conectar el botón a la función
		self.listing_module = listing_module	

	def edit_selection(self):
		selected_items = self.listing_module.list_widget.list.selectedItems()
		#message = ""
		#for i in selected_items:
		#	message += i.data(33) + "|" + i.data(34) + "|" + i.data(35)
		self.edit_popup.loadParameters(selected_items)
		self.edit_popup.show()