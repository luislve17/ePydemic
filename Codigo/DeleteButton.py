"""
## DeleteButton ##
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *


class DeleteButton(QPushButton):
	def __init__(self, listing_module):
		super().__init__()			# Llamada obligatoria al constructor del padre
		self.listing_module = listing_module
		self.setMaximumSize(33, 27)		# Determina el tamaño maximo
		self.setIcon(QIcon("assets/trash_icon.png"))	# Establecer icono de borrar
		self.clicked.connect(self.deleteItem)	# Conectar el botón a la función

	def deleteItem(self):
		items = self.listing_module.list_widget.list.selectedItems()
		for i in items:
			self.listing_module.list_widget.list.takeItem(self.listing_module.list_widget.list.row(i))