import os
# first install the next:
# pip install tinytag
from tinytag import TinyTag



class Filemanager():
    def __init__(self):        
        self.currentfolder=os.path.dirname(__file__)
        self.examplefilepath = os.path.join(
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
        tags = TinyTag.get(self.examplefilepath)
        self.prompttext = tags.comment       

    def nextfile(self):
        print('next')        

    def prevfile(self):
        print('prev')


