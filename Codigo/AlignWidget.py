"""
## AlignWidget ##
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class AlignWidget(QWidget):
	def __init__(self):
		super().__init__()		# Llamada obligatoria al constructor del padre
		self.main_layout = QVBoxLayout()	# Layout vertical

		self.seq_desc = QTextEdit()			# Proporciona un widget que se utiliza para editar y mostrar texto sin formato
		self.seq_desc.setReadOnly(True)		# Solo lectura

		self.main_layout.addWidget(self.seq_desc)	# Adicion al layout 

		self.setLayout(self.main_layout)	# Fijación del Layout