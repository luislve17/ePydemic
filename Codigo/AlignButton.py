"""
## AlignButton ##
"""
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class AlignButton(QPushButton):
	def __init__(self, listing_module):
		super().__init__()			# Llamada obligatoria al constructor del padre
		self.listing_module = listing_module
		self.setText("Alinear")		# Nombre del botón
		self.clicked.connect(self.alignSequences)	# Conectar el botón a la función

	def alignSequences(self):
		print("TODO: Alineamiento") #TODO