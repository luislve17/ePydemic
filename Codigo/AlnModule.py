from PyQt4.QtCore import *
from PyQt4.QtGui import * 

from PhylogeneticTree import *
import re

class AlnModule(QWidget):
	def __init__(self, aln_list):
		super().__init__()
		self.aln_list = aln_list
		self.tree_button = QPushButton("Mostrar Árbol")

		self.delete_button = QPushButton()
		self.delete_button.setMaximumSize(33, 27)	
		self.delete_button.setIcon(QIcon("assets/trash_icon.png"))

		#self.tree_name = QLineEdit()
		#self.tree_name.setPlaceholderText("Nombre del archivo .png")

		self.notif_label = QTextEdit()
		self.notif_label.setMaximumHeight(50)
		self.notif_label.setReadOnly(True)

		self.tree_button.clicked.connect(self.tree)
		self.delete_button.clicked.connect(self.deleteItem)

		self.module_layout = QVBoxLayout()
		self.buttons_layout = QHBoxLayout()
		self.buttons_layout.addWidget(self.tree_button)
		self.buttons_layout.addWidget(self.delete_button)
		#self.module_layout.addWidget(self.tree_name)

		self.module_layout.addLayout(self.buttons_layout)
		self.module_layout.addWidget(self.notif_label)
		self.setLayout(self.module_layout)

	def tree(self):
		aln_item = self.aln_list.selectedItems()
		
		dnd_path = aln_item[0].data(35).split("/")[-1].split(".")[0]+".dnd"
		dnd_path = '/'.join(aln_item[0].data(35).split("/")[:-1]) + "/" + dnd_path

		tree_safe_boolean = self.getSafetyInfo(dnd_path) # Ver si es segura la generacion del arbol

		if len(aln_item) == 0:
			self.notif_label.setStyleSheet("color: #c67e61;")
			self.notif_label.setText("Error: No ha seleccionado ningun archivo .aln")
		elif not tree_safe_boolean:
			self.notif_label.setStyleSheet("color: #c67e61;")
			self.notif_label.setText("Error: Seleccione un alineamiento de más de 2 secuencias")
		else:
			aln = [item.data(35) for item in aln_item]
			cant_cod = 0
			for path in aln:
				handle = open(path)

			PhylogeneticTree.tree(aln_item)
			self.notif_label.setStyleSheet("color:#42663a;")
			self.notif_label.setText("Feed:Generacion de arbol exitosa")
			
	def deleteItem(self):
		items = self.aln_list.selectedItems()
		for i in items:
			self.aln_list.takeItem(self.aln_list.row(i))

	def getSafetyInfo(self, path):
		cont = 0
		with open(path) as file:
			for line in file:
				for char in line:
					if char == ",":
						cont += 1
					if cont > 1:
						return True
		return False