"""
## Clase MainWindow ##
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
from ToolsModule import *
from DisplayModule import *

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()	# Llamada obligatoria al constructor del padre
		self.setWindowTitle("ePydemic")	# Titulo del programa
		self.setMinimumSize(900, 500)	# Dimensiones minimas
		self.create_gui()				# Metodo local de construccion

	def create_gui(self):
		self.main_layout = QHBoxLayout()	# Layout horizontal principal
		self.main_splitter = QSplitter(Qt.Horizontal)	# Widget de division dinamica
		self.main_widget = QWidget()	# Widget principal

		self.tools_module = ToolsModule()	# Modulo de herramientas

		self.display_module = DisplayModule() # Modulo de dibujo/muestra

		# Adicion de ambos modulos al splitter dinamico
		self.main_splitter.addWidget(self.tools_module)
		self.main_splitter.addWidget(self.display_module)
		# Proporcion inicial de espacios de distribucion
		self.main_splitter.setSizes([250,480])

		# Adicion del splitter al layout horizontal principal
		self.main_layout.addWidget(self.main_splitter)
		# Fijacion del layout como principal
		self.main_widget.setLayout(self.main_layout)
		# Fijacion del widget principal
		self.setCentralWidget(self.main_widget)

def main():
	QApplication.setStyle("cleanlooks")
	App = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	App.exec_()

if __name__ == "__main__":
	main()