from PyQt4.QtCore import *
from PyQt4.QtGui import *


from AlignHandler import *

class AlignModule(QWidget):
	def __init__(self, seqs_list):
		super().__init__()
		self.seqs_list = seqs_list
		# Boton
		self.align_button = QPushButton("Alinear secuencias")
		# Boton borrar
		self.delete_button = QPushButton()
		self.delete_button.setMaximumSize(33, 27)		# Determina el tamaño maximo
		self.delete_button.setIcon(QIcon("assets/trash_icon.png"))	# Establecer icono de borrar

		self.align_name = QLineEdit()
		self.align_name.setPlaceholderText("Nombre del archivo resultante")
		# Label
		self.notif_label = QTextEdit()
		self.notif_label.setMaximumHeight(50)
		self.notif_label.setReadOnly(True)		# Solo lectura


		self.align_button.clicked.connect(self.align)
		self.delete_button.clicked.connect(self.deleteItem)

		self.module_layout = QVBoxLayout()
		self.buttons_layout = QHBoxLayout()
		self.buttons_layout.addWidget(self.align_button)
		self.buttons_layout.addWidget(self.delete_button)
		self.module_layout.addWidget(self.align_name)
		self.module_layout.addLayout(self.buttons_layout)
		self.module_layout.addWidget(self.notif_label)
		self.setLayout(self.module_layout)

	def align(self):
		fastas_list = self.seqs_list.selectedItems()
		if len(fastas_list) == 0:	# Si no se selecciona un archivo, se muestra mensaje
			self.notif_label.setStyleSheet("color: #c67e61;")
			self.notif_label.setText("Error:Seleccione al menos un .fasta para alinear")
		else:
			if len(fastas_list) == 1: # Si solo se selecciona una secuencia 
				fastas_list = [fastas_list[0], fastas_list[0]] # La copiamos para alinearla sobre si misma
			# Si no, se procede con normalidad
			result_path, result_name = AlignHandler.mergeFastas(fastas_list, self.align_name.text())
			clustalw_out_path = AlignHandler.alignSeqs(result_path, result_name)

			clustal_output = open(clustalw_out_path).read()
			aln_file_content = open(result_path+result_name+".aln").read()
			dnd_file_content = open(result_path+result_name+".dnd").read()

			# Cargando el contenido de los files luego de usar clustalw
			output = "######## CLUSTAL OUTPUT ########\n" 
			output += clustal_output
			output += "######## ALN FILE ########\n" 
			output += aln_file_content
			output += "######## DND FILE ########\n" 
			output += dnd_file_content
			
			self.seqs_list.seq_desc.setText(output)

			self.notif_label.setStyleSheet("color:#42663a;")
			self.notif_label.setText("Feed:Alineacion exitosa ("+ result_path +")")

	def deleteItem(self):
		items = self.seqs_list.selectedItems()
		for i in items:
			self.seqs_list.takeItem(self.seqs_list.row(i))