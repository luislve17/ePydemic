"""
## AlignWidget ##
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from SeqsList import *
from AlignModule import *

class AlignWidget(QWidget):
	def __init__(self):
		super().__init__()		# Llamada obligatoria al constructor del padre
		self.main_layout = QVBoxLayout()	# Layout vertical
		self.upper_layout = QHBoxLayout()	# Layout horizontal de lista-herramientas

		self.seq_desc = QTextEdit()			# Proporciona un widget que se utiliza para editar y mostrar texto sin formato
		self.seq_desc.setReadOnly(True)		# Solo lectura
		self.seq_list = SeqsList(self.seq_desc) # Lista de secuencias
		self.align_module = AlignModule(self.seq_list)	# Modulo de herramientas de alineamiento
		self.main_splitter = QSplitter(Qt.Vertical)

		self.upper_layout.addWidget(self.seq_list)
		self.upper_layout.addWidget(self.align_module)
		self.upper_widget = QWidget()
		self.upper_widget.setLayout(self.upper_layout)
		self.main_splitter.addWidget(self.upper_widget)	# Adicion de la lista
		self.main_splitter.addWidget(self.seq_desc)	# Adicion al layout 
		self.main_layout.addWidget(self.main_splitter)

		self.setLayout(self.main_layout)	# Fijación del Layout