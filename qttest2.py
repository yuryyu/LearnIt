
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QDialog

from pyform import Ui_Dialog
# NOTE: USE the next in CMD for compiling the form: pyuic5 -x qtdestest.ui -o pyform.py

class MainWin(QDialog, Ui_Dialog):

    def __init__(self):
        # multiple inheritance approach
        super(MainWin, self).__init__()

        # Set up the user interface from Designer.
        self.setupUi(self)

        # Make some local modifications - TBD
        #self.colorDepthCombo.addItem("2 colors (1 bit per pixel)")

        # Connect up the buttons.       
        self.SHOWButton.clicked.connect(self.showtext)
        


    def showtext(self):
        print('Show text enabled!')
        self.labelshow.setText('Show text enabled!')



if __name__ == "__main__":    
    app = QApplication(sys.argv)
    w = MainWin()
    w.show()    
    sys.exit(app.exec_())
