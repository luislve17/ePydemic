"""
## AlnModule ##
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import * 

from PhylogeneticTree import *
import re

class AlnModule(QWidget):
	def __init__(self, aln_list):
		super().__init__()
		self.aln_list = aln_list
		# Boton
		self.tree_button = QPushButton("Mostrar Arbol")	#

		# Boton Borrar
		self.delete_button = QPushButton()	
		self.delete_button.setMaximumSize(33, 27)	
		self.delete_button.setIcon(QIcon("assets/trash_icon.png"))

		# Label
		self.notif_label = QTextEdit()
		self.notif_label.setMaximumHeight(50)
		self.notif_label.setReadOnly(True)

		self.tree_button.clicked.connect(self.tree)
		self.delete_button.clicked.connect(self.deleteItem)

		self.module_layout = QVBoxLayout()
		self.buttons_layout = QHBoxLayout()
		self.buttons_layout.addWidget(self.tree_button)
		self.buttons_layout.addWidget(self.delete_button)

		self.module_layout.addLayout(self.buttons_layout)
		self.module_layout.addWidget(self.notif_label)
		self.setLayout(self.module_layout)

	def tree(self):
		aln_item = self.aln_list.selectedItems()
		
		"""
		Se verifica que el alineamiento sea de mas de 2 secuencias
		"""
		aln_path = aln_item[0].data(35).split("/")[-1].split(".")[0]+".aln"
		#dnd_path = aln_item[0].data(35).split("/")[-1].split(".")[0]+".aln"
		aln_path = '/'.join(aln_item[0].data(35).split("/")[:-1]) + "/" + aln_path
		tree_safe_boolean = self.getSafetyInfo(aln_path) # Ver si es segura la generacion del arbol
		print("safe_bool:", tree_safe_boolean)
		if len(aln_item) == 0:			# Si no se ha seleccionado ningun archivo, se muestra mensaje
			self.notif_label.setStyleSheet("color: #c67e61;")
			self.notif_label.setText("Error: No ha seleccionado ningun archivo .aln")
		elif not tree_safe_boolean:		# Si el alineamientos es de 2 secuencias se muestra mensaje de error
			self.notif_label.setStyleSheet("color: #c67e61;")
			self.notif_label.setText("Error: Seleccione un alineamiento de mas de 2 secuencias")
		else:			# Para alineamientos de mas de 2 secuencias
			aln = [item.data(35) for item in aln_item]
			cant_cod = 0
			for path in aln:
				handle = open(path)
			#self.notif_label.setStyleSheet("color:#42663a;")
			#self.notif_label.setText("Feed: Operacion exitosa")
			PhylogeneticTree.tree(aln_item)		#  Se muestra arbol filogenetico
			
	def deleteItem(self):
		items = self.aln_list.selectedItems()
		for i in items:
			self.aln_list.takeItem(self.aln_list.row(i))

	def getSafetyInfo(self, path):
		cont = 0
		with open(path) as file:
			for line, i in zip(file, range(1000)):
				for char in line:
					if i == 5 and char == " ":
						return False
		return True