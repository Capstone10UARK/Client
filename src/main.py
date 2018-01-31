import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction
from PyQt5.QtGui import QIcon

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'VFI Analysis Application'
        self.left = 350
        self.top = 150
        self.width = 800
        self.height = 600
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        mainMenu = self.menuBar()
        mainMenu.setNativeMenuBar(False) #For MacOS
        fileMenu = mainMenu.addMenu('File')
        helpMenu = mainMenu.addMenu('Help')

        uploadVideoAction = QAction('Upload Video', self)
        uploadVideoAction.setStatusTip('Upload Video')

        uploadPhotoAction = QAction('Upload Photo', self)
        uploadPhotoAction.setStatusTip('Upload Photo')

        exitAction = QAction('Exit', self)
        exitAction.setStatusTip('Exit Program')
        exitAction.triggered.connect(self.close)

        fileMenu.addAction(uploadVideoAction)
        fileMenu.addAction(uploadPhotoAction)
        fileMenu.addSeparator()
        fileMenu.addAction(exitAction)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
