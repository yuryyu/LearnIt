import matplotlib.pyplot as plt
import numpy as np 
import sys
#from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QGridLayout, QDesktopWidget

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class PrettyWidget(QMainWindow):


    def __init__(self):
        #super(PrettyWidget, self).__init__()
        #self.initUI()
        super().__init__()
        title = "Matplotlib Embeding In PyQt5"
        top = 400
        left = 400
        width = 900
        height = 500
 
        self.setWindowTitle(title)
        self.setGeometry(top, left, width, height)
 
        self.initUI()
 


    def initUI(self):

        self.setGeometry(100,100,800,600)
        self.center()
        self.setWindowTitle('S Plot')

        grid = QGridLayout()
        self.setLayout(grid)

        btn1 = QPushButton('Plot 1 ',self)
        btn1.resize(btn1.sizeHint())
        btn1.clicked.connect(self.plot1)
        grid.addWidget(btn1,5,0)

        btn2 = QPushButton('Plot 2 ',self)
        btn2.resize(btn2.sizeHint())
        btn2.clicked.connect(self.plot2)
        grid.addWidget(btn2,5,1)

        self.figure = plt.figure(figsize = (150,50))
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        grid.addWidget(self.canvas, 3,0,1,2)
        

        self.show()

    def plot1(self):
        plt.cla()
        ax1 = self.figure.add_subplot(211)
        x1 = [i for i in range(100)]
        y1 = [i**0.5 for i in x1]
        ax1.plot(x1,y1,'b.-')

        ax2 = self.figure.add_subplot(212)
        x2 = [i for i in range(100)]
        y2 = [i for i in x2]
        ax2.plot(x2,y2,'b.-')
        self.canvas.draw()

    def plot2(self):
        plt.cla()
        ax3 = self.figure.add_subplot(111)
        x = [i for i in range(100)]
        y = [i**0.5 for i in x]
        ax3.plot(x,y,'r.-')
        ax3.set_title('Square Root Plot')
        self.canvas.draw()    

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == "__main__":    
    app = QApplication(sys.argv)
    w = PrettyWidget()
    w.show()    
    sys.exit(app.exec_())


# #app = QtGui.QApplication(sys.argv)
# app = QApplication(sys.argv)
# app.aboutToQuit.connect(app.deleteLater)
# GUI = PrettyWidget()
# sys.exit(app.exec_())