"""
## UpoladAlnButton ##
install easygui
	sudo apt-get install python3-easygui
"""
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import easygui as eg
import shutil

class UploadAlnButton(QPushButton):
	def __init__(self, listing_module):
		super().__init__()			# Llamada obligatoria al constructor del padre
		self.listing_module = listing_module
		self.setMaximumSize(33, 27)		# Determina el tamaño maximo
		self.setIcon(QIcon("assets/upload_icon.png"))	# Establecer icono de borrar
		self.clicked.connect(self.uploadAln)

	def uploadAln(self):
		print("Subir archivos .aln")

		ext = ["*.aln"]
		file =eg.fileopenbox(msg="Cargar alineamiento",
								title="Buscador",
								default='',
								filetypes=ext)
		if file != None:
			shutil.move(file,"data/aligments/otros/")		# Se mueve el archivo a la carpeta aligments
		else:
			print("Archivo no seleccionado")