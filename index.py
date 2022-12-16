from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import pafy

from PyQt5.uic import loadUiType
import urllib.request                                  #to download Files from Internet
#import pafy
#import humanize

import os
from os import path


ui,_ = loadUiType(path.join(path.dirname(__file__),'main.ui')) #to code live with ui file 

class MainApp(QMainWindow , ui):
    def __init__(self , parent=None):
        super(MainApp , self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_ui()
        self.Handel_buttons()
        
        
        
        
    def func(self,a):
        b=str(a)
        c=b[2:].split(',')
        d=c[0]
        e=d[0:-1]
        return e
    
    def Handel_ui(self):
        self.setWindowTitle('Python Download Manager')
        self.setFixedSize(1500,1500)
        

    def Handel_buttons(self):
        
        "to connect the Button with a function" 'pushButton is the name of the button'  'Handel_download is the function'
        self.pushButton_2.clicked.connect(self.Handel_download)   
        self.pushButton.clicked.connect(self.Handel_browse)
        self.pushButton_4.clicked.connect(self.Handel_youtube_download)

    def Handel_browse(self):
        save_place=QFileDialog.getSaveFileName(self, caption='SAVE AS', directory='.', filter=('All Files *.*')) #to show the 'save as' window
        name=self.func(save_place)
        print(name)
        browse=self.lineEdit_2.setText(name)

    def Handel_progressbar(self, blocknum, blocksize, totalsize):
        read=blocknum*blocksize
        if totalsize>0:
            percent= read * 100 / totalsize
            self.progressBar.setValue(percent)
            QApplication.processEvents()  #to solve NOT RESPONDING Problem

    def Handel_download(self):
        url=self.lineEdit.text()       #from where to download 
        save=self.lineEdit_2.text()    #where to save the file
        
        try: #to try just the download command
            urllib.request.urlretrieve(url,save,self.Handel_progressbar) #command to download
        except Exception:
            QMessageBox.warning(self,'Download ERROR','Download not finished')
        QMessageBox.information(self,'Download Completed','Download finished')  #when the Download completed show a message
        self.progressBar.setValue(0) #Reset the Value of the Progressbar after download
        self.lineEdit.setText('') #Reset the value of the URL 
        self.lineEdit_2.setText('') #Reset the value of the save link

    def Handel_youtube_download(self):
        youtube_url=self.lineEdit_3.text()
        youtube_save= self.lineEdit_4.text()
        #try:
        v=pafy.new(youtube_url)
        #except Exception:
            #QMessageBox.warning(self,'Download from Youtube ERROR','Download not finished')
        #print(v.title)
        # print(v.duration)
        # print(v.rating)
        # print(v.author)
        # print(v.length)
        # print(v.keywords)
        # #print(v.thumb)
        # print(v.videoid)
        # print(v.viewcount)
        pass
def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()