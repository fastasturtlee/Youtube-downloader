import os
import sys


import pytube

from PyQt5.QtWidgets import QFileDialog, QMainWindow, QLineEdit, QProgressBar, QPushButton, QMenuBar, QWidget, \
    QVBoxLayout, QApplication, QAction, QLabel, QDialog, QBoxLayout,qApp,QHBoxLayout
from PyQt5.QtGui import QIcon

class Function(QWidget):
    def __init__(self):
        super().__init__()
        self.lb = QLabel()
    def open_dialog(self):
        self.d1 = QDialog()
        self.lb.setText('Developed by fast_as_turtle')
        d_layout = QVBoxLayout()
        d_layout.addStretch()
        d_layout.addWidget(self.lb)
        d_layout.addStretch()
        self.d1.setLayout(d_layout)
        self.d1.setWindowTitle('message from developer')
        self.d1.show()
    def exit(self):
        qApp.quit()
    def save(self):
        path = QFileDialog.getSaveFileName(self,'Download location',os.getenv('Downloads'))
        global loc
        loc = path[0]











class Downloader(QWidget):
    def __init__(self):
        super().__init__()

        self.form_function = Function
        self.form_download_function = FileDownload
        self.init_ui()

    def init_ui(self):
        self.url = QLineEdit('Enter the url')
        self.dbar = QPushButton('Download')
        h_box = QHBoxLayout()
        v_box = QVBoxLayout()
        h_box.addWidget(self.url)
        h_box.addWidget(self.dbar)
        v_box.addLayout(h_box)
        self.setLayout(v_box)
        #getting the text from line edit
        #self.link = self.url.text()


        #clicking the download button
        self.dbar.clicked.connect(self.form_download_function.download_video)

        global link
        link = self.url
        self.show()







class FileDownload(pytube.YouTube):
    def __init__(self):
        super().__init__()

    def download_video(self):
        url = link.text()
        list = loc.split('/')
        name = list[-1]
        dir = str('/'.join(i for i in list if i not in name))+'/'
        try:
            yt = pytube.YouTube(url).streams

            yt.first().download(dir)
            print('task completed')
        except:
            print('connection error')









class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.form_widget = Downloader()
        self.setCentralWidget(self.form_widget)


        self.dp = QProgressBar()

        self.form_function = Function()


        self.init_ui()
    def init_ui(self):
        bar = QMenuBar()           #adding menu bar to the ui
        bar = self.menuBar()
        file = bar.addMenu('File')
        about = bar.addMenu('About')
        save = QAction('Save',self)
        exit = QAction('Exit',self)
        info = QAction('Info',self)
        file.addAction(save)
        file.addAction(exit)
        about.addAction(info)
        exit.triggered.connect(self.form_function.exit)
        info.triggered.connect(self.form_function.open_dialog)
        save.triggered.connect(self.form_function.save)


        #setting up windows
        self.setWindowTitle('Youtube Downloader')
        self.setWindowIcon(QIcon('download (2).jpg'))
        self.show()


app = QApplication(sys.argv)
soft = Window()
sys.exit(app.exec_())