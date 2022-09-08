import qdarkstyle
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
from PySide2 import *
from PyQt5 import  QtSql
import smtplib
import sys
import webbrowser
from Mavi_Dershanem.ogretmen.ogretmen_email_giris import ui_MainWindow3




class ui_MainWindow2(QMainWindow):
    def email_opsiyon(self):
        form = QWidget
        self.ui = ui_MainWindow3()
        self.ui.show()

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent=None)
        uic.loadUi("ogretmen_yeni.ui", self)

        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('ProjeDershanem.db')

        if not db.open():
            QMessageBox.critical(self, 'HATA', 'hata', QMessageBox.Cancel)

        self.model = QtSql.QSqlTableModel()
        self.model.setTable('tbl_ogrenci')
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.model.select()
        self.model.setHeaderData(0, Qt.Horizontal, 'AD')
        self.model.setHeaderData(1, Qt.Horizontal, 'Soyad')
        self.model.setHeaderData(2, Qt.Horizontal, 'Numara')
        self.model.setHeaderData(3, Qt.Horizontal, 'email')
        self.model.setHeaderData(4, Qt.Horizontal, 'parola')

        self.tableView.setModel(self.model)
        self.tableView.clicked.connect(self.satirAl)

        self.delrow = -1



        self.gncl.clicked.connect(self.satirekle)
        self.sil.clicked.connect(lambda: self.model.removeRow(view.currentIndex().row()))

        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        # or in new API
        self.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))

        self.setWindowFlags(Qt.FramelessWindowHint)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 192, 157, 550))

        self.slider.clicked.connect(lambda: self.slideLeftMenu())  # slidermenu fonksiyonuna bağlandı

        self.dicort.clicked.connect(lambda: webbrowser.open('https://discord.com/channels/936526645999828993/936531614102605844'))
        self.pushButton_7.clicked.connect(lambda: webbrowser.open('https://drive.google.com/drive/folders/1PaaUgnxHuCZtHe_Sse8kljNXXTt6l3Yu'))


        #email secim penceresini acıyor.

        self.email.clicked.connect(self.email_opsiyon)

        # Sağ köşe button işlemleri
        self.full.clicked.connect(self.fullekran)
        self.kapat.clicked.connect(self.kapama)
        self.alt.clicked.connect(self.minimize_tusu)

        #liste ile stackedwidget geçiş
        self.grevler.currentRowChanged.connect(self.gecis1)

        def moveWindow(e):
            # Detect if the window is  normal size
            # ###############################################
            if self.isMaximized() == False: #Not maximized
                # Move window only when window is normal size
                # ###############################################
                #if left mouse button is clicked (Only accept left mouse button clicks)
                if e.buttons() == Qt.LeftButton:
                    #Move window
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
        #######################################################################

        #######################################################################
        # hangi frame tıklıyorsa ekranı sürüklemeye yarar.
        #######################################################################
        self.frame_6.mouseMoveEvent = moveWindow
        self.frame_16.mouseMoveEvent = moveWindow
        self.frame_9.mouseMoveEvent = moveWindow
        self.frame_3.mouseMoveEvent = moveWindow



    def satirekle(self):
        self.model.insertRows(self.model.rowCount(),1)

    def satirAl(self,i):
        self.delrow = i.row()

    def gecis1(self,q):
        self.stackedWidget.setCurrentIndex(q)


    def mousePressEvent(self, event):
        # ###############################################
        # Get the current position of the mouse
        self.clickPosition = event.globalPos()
        # We will use this value to move the window

        #######################################################################
        #######################################################################

    def slideLeftMenu(self):
         # Get current left menu width
        width = self.frame_2.width()

            # If minimized
        if width == 0:
                # Expand menu
            newWidth = 200
            self.slider.setText("Menü Kapat")
        # self.menu_kp(QtGui.QIcon(u":/icons/icons/align-left.svg")) icon eklemek istersek.
        # If maximized
        else:
            # Restore menu
            newWidth = 0
            self.slider.setText("Menü Aç")
                # self.menu_kp(QtGui.QIcon(u":/icons/icons/align-left.svg")) icon eklemek istersek.

            # Animate the transition
        self.animation = QPropertyAnimation(self.frame_2, b"maximumWidth")  # Animate minimumWidht
        self.animation.setDuration(250)
        self.animation.setStartValue(width)  # Start value is the current menu width
        self.animation.setEndValue(newWidth)  # end value is the new menu width
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()


    def kapama(self):
        self.close()
    def minimize_tusu(self):
        self.showMinimized()
    def fullekran(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()
#Mesaj Box Kod bu bir kalıbdır.

    def showMessageBox(self, title, content):
        msgBox = QMessageBox()
        msgBox.setWindowTitle(title)
        msgBox.setText(content)
        msgBox.exec_()

    def closeEvent(self, event):

        msg = "Öğretmen Ders Platformunu Kapmak Mı İstiyorsunuz ?"
        reply = QMessageBox.question(self, 'UYARI !',
                                     msg, QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
        app = QApplication(sys.argv)
        app.setStyle("fusion")
        pencere = ui_MainWindow2()
        pencere.show()
        sys.exit(app.exec_())

