"""
## ListWidget ##

Widget de listado y acceso a los archivos/data genetica provista en files. Cada item presenta los
siguientes campos al ser creados, modificados o leidos.

# 33: Grupo perteneciente
# 34: Valor del item
# 35: Path al archivo genetico
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class ListWidget(QWidget):
	def __init__(self):
		super().__init__()	# Llamada rutinaria al constructor del padre
		self.list = QListWidget()	# Lista
		self.list.setSelectionMode(QAbstractItemView.ExtendedSelection)
		self.items_list = []	# Lista de items (posible utilidad posterior)

		# Coneccion de accion->click de items al metodo 'self.itemSelected'
		self.list.itemClicked.connect(self.itemSelected)

		# Definicion del layout y adicion de la lista
		self.layout = QHBoxLayout()
		self.layout.addWidget(self.list)
		self.setLayout(self.layout)

		### <Pruebas>
		for j in ["Tapaculo 1", "Tapaculo 2", "Tapaculo 3"]:
			self.addItem(j, "Perú", "posible_path.jpeg")
		### </Pruebas>

	def addItem(self, value, grp_name="Otros", path=None):
		new_item = QListWidgetItem(grp_name + "::" + value)	# Label del item en la lista
		new_item.setData(33, grp_name)	# new_item[33] = nombre de grupo/pais de procedencia de la especie
		new_item.setData(34, value)	# new_item[34] = valor/nombre del especimen
		new_item.setData(35, path)	# new_item[35] = path al archivo de secuencia
		self.list.addItem(new_item)	# Adicion del item
		self.items_list.append(new_item)	# Consideracion de la lista (posible utilidad futura)

	# Funcion de manejo de seleccion de item
	def itemSelected(self, item):
		print("Clicked->{}:{}:{}".format(item.data(33), item.data(34), item.data(35)))