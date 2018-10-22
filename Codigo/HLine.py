"""

creditos:
* https://stackoverflow.com/questions/5671354/how-to-programmatically-make-a-horizontal-line-in-qt
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class HLine(QFrame):
    def __init__(self):
        super().__init__()
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Sunken)