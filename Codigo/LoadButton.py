"""
## LoadButton ##
"""
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import os

class LoadButton(QPushButton):
	def __init__(self, species_list, seq_list):
		super().__init__()
		self.setText("Cargar secuencias")
		self.species_list = species_list
		self.seq_list = seq_list
		self.clicked.connect(self.loadList)

	def loadList(self):
		species_list = self.species_list.list_widget.list.selectedItems() # Especia de la que cargar las secuencias
		for species in species_list:
			specie_folder = species.data(35).replace(" ", "_").lower() # Nombre de la especie en su directorio
			seqs_path = "data/content/"+specie_folder+"/seqs/" # Folder de secuencias de la especie selecc.
			for root, dirs, files in os.walk(seqs_path): # Para todos los archivos de secuencia
				for f in files:
					new_seq = QListWidgetItem() # Se prepara un nuevo item
					new_seq.setText(species.data(35).replace(" ", "_")+"::"+f)
					new_seq.setData(35, seqs_path+f) # data(35) = path to seq
					self.seq_list.addItem(new_seq) # Se carga cada referencia de todas las secuencias encontradas