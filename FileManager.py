import os

class Filemanager():
    def __init__(self):        
        self.currentfolder=os.path.dirname(__file__)
        self.listenfilepath = os.path.join(
            self.currentfolder,
            'resources',
            'example.wav')
        self.recordfilepath = os.path.join(
            self.currentfolder,
            'records',
            'currentrecord.wav')                        
        self.prompttext     =''
        #self.file_open()
        self.showfilestree()

    def showfilestree(self):
        self.files = os.listdir(self.currentfolder+'\\resources')
        print(self.files)
        self.readwavmetadata()

    def file_open(self):
        self.filename = QFileDialog.getOpenFileName(directory=self.currentfolder)
        print(self.filename)     

    def readwavmetadata(self):
        self.prompttext     ='Show text prompt!'        

    def nextfile(self):
        print('next')        

    def prevfile(self):
        print('prev')


