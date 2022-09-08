
from PyQt5 import QtCore, QtGui, QtWidgets

import qdarkstyle
import sys
from PyQt5 import uic
import webbrowser
from Mavi_Dershanem.yonetici.ui_email_yonetici import Ui_widget

class ui_MainWindow3(QtWidgets.QWidget):
    def email_ac(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_widget()
        self.ui.setupUi(self.window)
        self.window.show()

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent=None)
        uic.loadUi("yonetici_email.ui", self)


        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        # or in new API
        self.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.pushButton_2.clicked.connect(lambda: webbrowser.open('https://www.google.com/intl/tr/gmail/about/'))
        self.pushButton.clicked.connect(self.email_ac)



if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        app.setStyle("fusion")
        pencere = ui_MainWindow3()
        pencere.show()
        sys.exit(app.exec_())

