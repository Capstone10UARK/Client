from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.phonon import Phonon
from my_ui import Ui_MainWindow

class MyMainUi(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyMainUi, self).__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication([])
    my_ui = MyMainUi()
    my_ui.show()
    app.exit(app.exec_())