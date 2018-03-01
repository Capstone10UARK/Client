from PyQt4.QtGui import *
from PyQt4.QtCore import QPoint, QRect, QSize, Qt
from PyQt4.phonon import Phonon
from my_ui import Ui_MainWindow

class MyMainUi(QMainWindow, Ui_MainWindow, QLabel):

    def __init__(self, parent=None):
        super(MyMainUi, self).__init__(parent)
        QLabel.__init__(self, parent)
        self.rubberBand = QRubberBand(QRubberBand.Rectangle, self)
        self.origin = QPoint()

        # Setup UI.
        self.setupUi(self)
        self.play_pauseButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.stopButton.setIcon(self.style().standardIcon(QStyle.SP_MediaStop))

        # Setup video widget.
        self.mediaObject = Phonon.MediaObject()
        self.videoWidget = self.videoPlayer.videoWidget()
        Phonon.createPath(self.mediaObject, self.videoWidget)
        self.mediaObject.stateChanged.connect(self.stateChanged)

        # Connect seek slider.
        self.seekSlider.setMediaObject(self.mediaObject)

        # Connect menu options (load, analyze, and exit).
        self.actionLoad.triggered.connect(self.loadVideo)
        self.actionAnalyze_Area.triggered.connect(self.analyzeArea)
        self.actionExit.triggered.connect(self.exit)

        # Connect video buttons.
        self.play_pauseButton.clicked.connect(self.playPause)
        self.stopButton.clicked.connect(self.stop)
		
		# Selection rubber band
		
    def stateChanged(self, newstate, oldstate):
        if self.mediaObject.state() == Phonon.ErrorState:
            self.play_pauseButton.setEnabled(False)
            self.stopButton.setEnabled(False)
            messageBox = QMessageBox()
            messageBox.critical(None, 'ERROR', self.mediaObject.errorString() + '.')
        elif self.mediaObject.state() == Phonon.PlayingState:
            self.play_pauseButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
            self.play_pauseButton.setToolTip('Pause')
        else:
            self.play_pauseButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
            self.play_pauseButton.setToolTip('Play')

    def loadVideo(self):
        file = QFileDialog.getOpenFileName(self, None, '')

        if file != '':
            self.mediaObject.setCurrentSource(Phonon.MediaSource(file))
            self.play_pauseButton.setEnabled(True)
            self.stopButton.setEnabled(True)
            self.mediaObject.play()
            self.mediaObject.pause()

    def analyzeArea(self):
        # TODO.
		
        print('')
    def mousePressEvent(self, event):
    
        if event.button() == Qt.LeftButton:
        
            self.origin = QPoint(event.pos())
            self.rubberBand.setGeometry(QRect(self.origin, QSize()))
            self.rubberBand.show()
    
    def mouseMoveEvent(self, event):
    
        if not self.origin.isNull():
            self.rubberBand.setGeometry(QRect(self.origin, event.pos()).normalized())
    
    def mouseReleaseEvent(self, event):
    
        if event.button() == Qt.LeftButton:
            self.rubberBand.hide()
        
    def exit(self):
        app.exit()

    def playPause(self):
        if self.mediaObject.state() == Phonon.PlayingState:
            self.mediaObject.pause()
        # Restart if at end of video.
        elif self.mediaObject.remainingTime() == 0:
            self.mediaObject.seek(0)
            self.mediaObject.play()
        else:
            self.mediaObject.play()

    def stop(self):
        self.mediaObject.stop()

if __name__ == "__main__":
    app = QApplication([])
    my_ui = MyMainUi()
    my_ui.show()
    app.exit(app.exec_())