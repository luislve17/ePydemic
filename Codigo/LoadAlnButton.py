"""
## LoadAlnButton ##
"""
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import os 
import fnmatch

class LoadAlnButton(QPushButton):
	def __init__(self, aln_list):
		super().__init__()
		self.setText("Mostrar alineamientos")
		self.aln_list = aln_list
		self.clicked.connect(self.loadAln)

	def loadAln(self):
		rootDir = "data/aligments"
		for dirName, subdirList, fileList in os.walk(rootDir):
			#print("Directorio encontrado %s" % dirName)
			#for fname in fileList:
			#	print("\t%s" % fname)
			for fname in fileList:
				if fnmatch.fnmatch(fname, '*.aln'):
					new_aln = QListWidgetItem()
					new_aln.setText(fname)
					new_aln.setData(35, dirName+"/"+fname )
					self.aln_list.addItem(new_aln)