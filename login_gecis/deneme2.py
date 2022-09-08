import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import sys


## ==> SPLASH SCREEN
from Mavi_Dershanem.login_gecis.ui_splash_screen import Ui_SplashScreen
from Mavi_Dershanem.ogrenci.main_cek import ui_MainWindow


## ==> GLOBALS
counter = 0


# YOUR APPLICATION
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui3 = ui_MainWindow()

    def log_uncaught_exceptions(ex_cls, ex, tb):
        text = '{}: {}:\n'.format(ex_cls.__name__, ex)
        import traceback
        text += ''.join(traceback.format_tb(tb))

        print(text)
        QMessageBox.critical(None, 'Bir Hata var', text)
        quit()

        sys.excepthook = log_uncaught_exceptions





# SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(15)

        # CHANGE DESCRIPTION

        # Initial Text
        self.ui.label_description.setText("<strong>HOŞGELDİN</strong> Geleceğin Yazılımcısı")

        # Change Texts
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>CODE DÜNYASI </strong> Seni bekliyor."))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>İyi Çalışmalar. </strong>DEKSTOP & APP"))


        ## SHOW ==> MAİN WİİNDOWU GÖRÜNTÜLEME
        ########################################################################
        self.show()
        ## ==> SON #

    ## ==> FONKSİYON EKLEME
    ########################################################################

    def progress(self):

        global counter

        # SET VALUE GETİRME PROGRESS BAR'A
        self.ui.progressBar.setValue(counter)

        # Cubuk 100 olunca kapansın öğrenci sayfasına gitsin.
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW main_cekin içerisinde ki  ui_maini çektik.
            self.main = ui_MainWindow()
            self.main.show()

            # doldurma işlemi bitti kapat.
            self.close()

        # INCREASE COUNTER
        counter += 1



if __name__ == "__main__":
        app = QApplication(sys.argv)
        app.setStyle("fusion")
        pencere = SplashScreen()
        pencere.show()
        sys.exit(app.exec_())

