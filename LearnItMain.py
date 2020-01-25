
import sys
import os
#from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from PyQt5 import QtCore, QtGui
#from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Player import Player
from FileManager import Filemanager
import time 
from LearnIt import Ui_MainWindow
# NOTE: USE the next in CMD for compiling the form: pyuic5 -x qtdestest.ui -o pyform.py
import logging

#logging.basicConfig(level=logging.DEBUG)
#logging.debug('This will get logged')
# logging.basicConfig(filename='LearnItapp.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')
# logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
# logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logging.basicConfig(filename='LearnItApp.log', filemode='a', format='%(asctime)s-%(process)d-%(name)s-%(levelname)s- %(message)s', level=logging.INFO)
#try:
#   c = a / b
# except Exception as e:
#   logging.error("Exception occurred", exc_info=True)
#logging.info('This will get logged to a file')
#logging.warning('This will get logged to a file')

class MainWin(QMainWindow, Ui_MainWindow):

    def __init__(self):
        # multiple inheritance approach
        super(MainWin, self).__init__()
        self.pl=Player()
        self.fl=Filemanager()
        # Set up the user interface from Designer.
        self.setupUi(self)
        #self.prompt.setText('Open Lesson folder, please')
        self.tableView.setWindowIconText(self.fl.files[0])
        # Connect up the buttons.        
        self.recordbutton.setStyleSheet("background-color: red")        
        self.recordbutton.clicked.connect(self.record)        
        self.listenbutton.clicked.connect(self.listen)
        self.examplebutton.clicked.connect(self.example)        

        self.nextbutton.clicked.connect(self.next)
        self.prevbutton.clicked.connect(self.prev)
        self.updategui()

    def record(self):
        logging.info('The record is started')
        #self.recordbutton.setStyleSheet("background-color: red")                            
        self.pl.record(self.fl.recordfilepath)        
        #self.recordbutton.setStyleSheet("background-color: green")

    def updategui(self):
        self.recordbutton.setStyleSheet("background-color: red")
        self.showprompt()         

    def listen(self):        
        self.pl.play(self.fl.recordfilepath)

    def example(self):
        self.pl.play(self.fl.examplefilepath)    

    def showprompt(self):
        self.prompt.setText(self.fl.prompttext)

    def next(self):
        self.fl.nextfile()

    def prev(self):
        self.fl.prevfile()        



if __name__ == "__main__":
    logging.info('GUI main is started!')    
    app = QApplication(sys.argv)
    w = MainWin()
    w.show()    
    sys.exit(app.exec_())

    
