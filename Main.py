import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from random import randint


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        global a, b
        MainWindow.setObjectName("MainWindow")
        a = randint(200, 800)
        b = randint(200, 600)
        MainWindow.resize(a, b)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 100, 75, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Окружность"))


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        global a, b, rr, gg, bb
        rr = 0
        gg = 0
        bb = 0
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        global a, b, r, g, bb
        self.pushButton.clicked.connect(self.start)
        self.x, self.y, self.r = 100, 100, 0

    def start(self):
        global a, b, rr, gg, bb
        rr, gg, bb = randint(0, 255), randint(0, 255), randint(0, 255)
        self.x, self.y, self.r = randint(0, a), randint(0, b), randint(0, abs(a + b) // 2)
        self.paintEvent(self.event)

    def paintEvent(self, event):
        global a, b, rr, gg, bb
        ris = QPainter()
        ris.begin(self)
        ris.setBrush(QColor(rr, gg, bb))
        ris.drawEllipse(self.x, self.y, self.r, self.r)
        self.update()
        ris.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())