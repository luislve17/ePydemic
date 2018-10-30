"""

creditos:
* https://stackoverflow.com/questions/5671354/how-to-programmatically-make-a-horizontal-line-in-qt
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class HLine(QFrame):
    def __init__(self):
        super().__init__()	# Llamada obligatoria al constructor del padre
        # Mantiene el valor de forma de marco del estilo de marco
        self.setFrameShape(QFrame.HLine)	
        # Mantiene el valor de la sombra del marco desde el estilo del marco
        self.setFrameShadow(QFrame.Sunken)