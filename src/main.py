import sys
import os.path
import vlc
from PyQt5.QtCore import Qt, QTimer, QDir
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import (QMainWindow, QWidget, QFrame, QSlider, QHBoxLayout,
    QPushButton, QVBoxLayout, QAction, QFileDialog, QApplication, QStyle,
    QSizePolicy, QLabel)

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'VFI Analysis'
        self.left = 350
        self.top = 150
        self.width = 800
        self.height = 600
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
'''
        self.instance = vlc.Instance()
        self.mediaPlayer = self.instance.media_player_new()

        if sys.platform == "darwin": # for MacOS
            from PyQt5.QtWidgets import QMacCocoaViewContainer
            self.videoFrame = QMacCocoaViewContainer(0)
        else:
            self.videoFrame = QFrame()

        self.palette = self.videoFrame.palette()
        self.palette.setColor (QPalette.Window,
                               QColor(0,0,0))
        self.videoFrame.setPalette(self.palette)
        self.videoFrame.setAutoFillBackground(True)

        self.playButton = QPushButton()
        self.playButton .setEnabled(False)
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.play)

        self.positionSlider = QSlider(Qt.Horizontal)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.setPosition)

        self.errorLabel = QLabel()
        self.errorLabel.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)

        mainMenu = self.menuBar()
        mainMenu.setNativeMenuBar(False) #For MacOS
        fileMenu = mainMenu.addMenu('File')
        helpMenu = mainMenu.addMenu('Help')

        uploadVideoAction = QAction('Load Video', self)
        uploadVideoAction.setStatusTip('Upload Video')
        uploadVideoAction.triggered.connect(self.openVideoFile)

        analyzeAreaAction = QAction('Analyze Area', self)
        analyzeAreaAction.setStatusTip('Analyze Area')

        exitAction = QAction('Exit', self)
        exitAction.setStatusTip('Exit Program')
        exitAction.triggered.connect(self.close)

        fileMenu.addAction(uploadVideoAction)
        fileMenu.addSeparator()
        fileMenu.addAction(analyzeAreaAction)
        fileMenu.addSeparator()
        fileMenu.addAction(exitAction)

        widget = QWidget(self)
        self.setCentralWidget(widget)

        controlLayout = QHBoxLayout()
        controlLayout.setContentsMargins(0, 0, 0, 0)
        controlLayout.addWidget(self.playButton)
        controlLayout.addWidget(self.positionSlider)

        layout = QVBoxLayout()
        layout.addWidget(self.videoFrame)
        layout.addLayout(controlLayout)
        layout.addWidget(self.errorLabel)

        widget.setLayout(layout)

    def play(self):
        if self.mediaPlayer.is_playing():
            self.mediaPlayer.pause()
            self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        else:
            self.mediaPlayer.play()
            self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))

    def openVideoFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Video", QDir.homePath())

        if fileName != '':
            self.mediaPlayer.set_media(self.instance.media_new(fileName))
            self.playButton.setEnabled(True)
            self.errorLabel.setText('')

            if sys.platform.startswith('linux'): # for Linux using the X Server
                self.mediaPlayer.set_xwindow(self.videoFrame.winId())
            elif sys.platform == "win32": # for Windows
                self.mediaPlayer.set_hwnd(self.videoFrame.winId())
            elif sys.platform == "darwin": # for MacOS
                self.mediaPlayer.set_nsobject(int(self.videoFrame.winId()))

    def setPosition(self, position):
        self.mediaPlayer.set_position(position / 1000.0)
'''
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

'''
import sys
import vlc
from PyQt5.QtWidgets import (QMainWindow, QPushButton, QWidget, QAction,
    QApplication, QFileDialog, QHBoxLayout, QLabel, QSizePolicy, QSlider,
    QStyle, QVBoxLayout)
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import QDir, Qt, QUrl
from PyQt5.QtGui import QIcon

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'VFI Analysis'
        self.left = 350
        self.top = 150
        self.width = 800
        self.height = 600
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        videoWidget = QVideoWidget()

        self.playButton = QPushButton()
        self.playButton .setEnabled(False)
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.play)

        self.positionSlider = QSlider(Qt.Horizontal)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.setPosition)

        self.errorLabel = QLabel()
        self.errorLabel.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)

        mainMenu = self.menuBar()
        mainMenu.setNativeMenuBar(False) #For MacOS
        fileMenu = mainMenu.addMenu('File')
        helpMenu = mainMenu.addMenu('Help')

        uploadVideoAction = QAction('Load Video', self)
        uploadVideoAction.setStatusTip('Upload Video')
        uploadVideoAction.triggered.connect(self.openVideoFile)

        analyzeAreaAction = QAction('Analyze Area', self)
        analyzeAreaAction.setStatusTip('Analyze Area')

        exitAction = QAction('Exit', self)
        exitAction.setStatusTip('Exit Program')
        exitAction.triggered.connect(self.close)

        fileMenu.addAction(uploadVideoAction)
        fileMenu.addSeparator()
        fileMenu.addAction(analyzeAreaAction)
        fileMenu.addSeparator()
        fileMenu.addAction(exitAction)

        widget = QWidget(self)
        self.setCentralWidget(widget)

        controlLayout = QHBoxLayout()
        controlLayout.setContentsMargins(0, 0, 0, 0)
        controlLayout.addWidget(self.playButton)
        controlLayout.addWidget(self.positionSlider)

        layout = QVBoxLayout()
        layout.addWidget(videoWidget)
        layout.addLayout(controlLayout)
        layout.addWidget(self.errorLabel)

        widget.setLayout(layout)

        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.stateChanged.connect(self.stateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)
        self.mediaPlayer.error.connect(self.handleError)

        self.show()

    def openVideoFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Video", QDir.homePath())

        if fileName != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))
            self.playButton.setEnabled(True)
            self.errorLabel.setText('')

    def play(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def stateChanged(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

    def positionChanged(self, position):
        self.positionSlider.setValue(position)

    def durationChanged(self, duration):
        self.positionSlider.setRange(0, duration)

    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)

    def handleError(self):
        self.playButton.setEnabled(False)
        self.errorLabel.setText('ERROR: ' + self.mediaPlayer.errorString() + '.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
'''
