from PyQt4.QtCore import *
from PyQt4.QtGui import *

import os

class InfoWidget(QWidget):
	def __init__(self, listing_module):
		super().__init__()
		self.main_layout = QVBoxLayout()

		self.img_and_name_layout = QHBoxLayout()

		self.name_layout = QVBoxLayout()

		self.desc_layout = QHBoxLayout()

		self.listing_module = listing_module
		self.listing_module.list_widget.list.itemDoubleClicked.connect(self.showInfo)

		self.img_frame = QLabel()
		self.img_frame.resize(100, 100); # TODO

		self.name = QLabel()
		self.name.setFont(QFont("Arial", 20, QFont.Bold))
		self.sci_name = QLabel()
		self.sci_name.setFont(QFont("Arial", 12, italic=True))
		self.desc = QTextEdit()
		self.desc.setReadOnly(True)

		self.name_layout.addWidget(self.name)
		self.name_layout.addWidget(self.sci_name)

		self.desc_layout.addWidget(self.desc)

		self.img_and_name_layout.addWidget(self.img_frame)
		self.img_and_name_layout.addLayout(self.name_layout)
		self.main_layout.addLayout(self.img_and_name_layout)
		self.main_layout.addLayout(self.desc_layout)
		self.setLayout(self.main_layout)

	def showInfo(self, item):
		root_path = "data/content/"+item.data(35).lower().replace(" ", "_")+"/"

		img_path = root_path + item.data(38)
		self.img_frame.setPixmap(QPixmap(img_path).scaled(256, 256, Qt.KeepAspectRatio, Qt.FastTransformation))

		name = item.data(36)
		self.name.setText(name)

		sci_name = item.data(35)
		self.sci_name.setText('('+sci_name+')')

		desc_path = root_path + item.data(39)
		self.desc.setText(open(desc_path).read())
		
