import sys
from PyQt5 import QtGui , QtCore

class Window(QtGui.MainWindow):

	def __init__(self):
		super(Window , self).__init__()
		self.setGeometry(50 , 50 , 500 , 300)
		self.setWindowTitle('PyQt')
		self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))
		self.home()

	def home(self):
		btn = QtGui.QPushButton("Quit" , self)
		btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
		btn.resize(100 , 100)
		btn.move(100 , 100)
		self.show()

def run():
	app = QtGui.QCoreApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())

run()