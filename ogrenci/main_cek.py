from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineSettings, QWebEngineView
from PySide2 import *
import smtplib
from Mavi_Dershanem.ogrenci.dokuman_file.dokuman import Ui_Form1
import webbrowser
from Mavi_Dershanem.ogrenci.ogrenci_email_file.ui_email import Ui_widget

from Mavi_Dershanem.ogrenci.program_setup_file.program_setup import Ui_Form3
from Mavi_Dershanem.ogrenci.ders_programi_file.deneme import WindowsApplication
import qdarkstyle  #Otamatik dark Designer Görünümü Kazandıran FrameWork


import sys

popups = []


class Widget(QWidget): # YOUTUBe Açıldıktan sonra youtube duşuna basınca yeni youtube sayfasının  içine giriyor.
    def __init__(self, parent=None):
        super().__init__(parent)
        self.view = QWebEngineView()
        lay = QVBoxLayout(self)
        lay.addWidget(self.view)
        self.resize(640, 480)


class WebEnginePage(QWebEnginePage):
    def createWindow(self, _type):
        w = Widget()
        w.show()
        popups.append(w)
        return w.view.page()


class ui_MainWindow(QMainWindow):

    def ders_programac(self): #ders programını açmak için bağlandık.
        self.ui = WindowsApplication()
        self.ui.show()

    def email_ac(self): #email göndermek için penceremizi bağladık.
        self.window = QWidget()
        self.ui = Ui_widget()
        self.ui.setupUi(self.window)
        self.window.show()

    def dokuman(self): #dökuman için penceremizi  bağladık.
        self.window = QWidget()
        self.ui = Ui_Form1()
        self.ui.setupUi(self.window)
        self.window.show()

    def setup_indir(self): #indirilecek setup programlar için penceremizi bağladık.
        self.window = QWidget()
        self.ui = Ui_Form3()
        self.ui.setupUi(self.window)
        self.window.show()

    def __init__(self,parent=None):
        QMainWindow.__init__(self,parent=None)
        uic.loadUi("video_panel.ui",self)

        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())  #otamatik import ettiğimiz qdarkstyle efektini kullandık.
        # or in new API
        self.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))

        self.setWindowFlags(Qt.FramelessWindowHint)


        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0,192,157,550))

        def moveWindow(e):  #tut çek sürükle ile üst frame bağladık.
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
        # Add click event/Mouse move event/drag event to the top header to move the window
        #######################################################################
        self.frame_9.mouseMoveEvent = moveWindow




        self.menu_kp.clicked.connect(lambda: self.slideLeftMenu()) #slidermenu fonksiyonuna bağlandı

        #Discorda gidis Butonu
        self.pushButton_2.clicked.connect(lambda: webbrowser.open('https://discord.com/channels/936526645999828993/936531614102605844'))

        #emaile soru gonderme

        self.pushButton.clicked.connect(self.ders_programac)
        self.soru_sor.clicked.connect(self.email_ac)
        self.dkm_ara.clicked.connect(self.dokuman)
        self.setup_indir1.clicked.connect(self.setup_indir)

        # menu acma kapama

        # Sağ köşe button işlemleri
        self.tam_ekran.clicked.connect(self.fullekran)
        self.kapat.clicked.connect(self.kapama)
        self.kaybet.clicked.connect(self.minimize_tusu)

        # ders videolarına gidis butonları
        self.ders1.clicked.connect(self.video_gosterme1)

        self.ders2.clicked.connect(self.video_gosterme2)

        self.ders3.clicked.connect(self.video_gosterme3)
        self.ders4.clicked.connect(self.video_gosterme4)
        self.ders5.clicked.connect(self.video_gosterme5)
        self.ders6.clicked.connect(self.video_gosterme6)
        self.ders7.clicked.connect(self.video_gosterme7)

    def mousePressEvent(self, event):
        # ###############################################
        # Get the current position of the mouse
        self.clickPosition = event.globalPos()
        # We will use this value to move the window
    #######################################################################
    #######################################################################

    #slider menü açılmasını kapanmasını sağladık.
    def slideLeftMenu(self):
        # Get current left menu width
        width = self.menu.width()

        # If minimized
        if width == 0:
            # Expand menu
            newWidth = 200
            self.menu_kp.setText("Menü Kapat")
        # self.menu_kp(QtGui.QIcon(u":/icons/icons/align-left.svg")) icon eklemek istersek.
        # If maximized
        else:
            # Restore menu
            newWidth = 0
            self.menu_kp.setText("Menü Aç")
            #self.menu_kp(QtGui.QIcon(u":/icons/icons/align-left.svg")) icon eklemek istersek.


        # Animate the transition
        self.animation = QPropertyAnimation(self.menu, b"maximumWidth")  # Animate minimumWidht
        self.animation.setDuration(250)
        self.animation.setStartValue(width)  # Start value is the current menu width
        self.animation.setEndValue(newWidth)  # end value is the new menu width
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

     #youtube videolarını gösterdik.
    def video_gosterme1(self):
        self.webview = QWebEngineView()
        self.page = WebEnginePage()
        self.webview.setPage(self.page)
        self.webview.settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)

        self.webview.load(QUrl("https://www.youtube.com/embed/yiIT8416Dlg?list=PLDjUp0pPODIBAOV9AqRiCgSK0y1_mZZsx"))
        v_box = QVBoxLayout()
        v_box.addWidget(self.webview)
        self.widget.setLayout(v_box)


    def video_gosterme2(self):

        self.webview = QWebEngineView()
        self.page = WebEnginePage()
        self.webview.setPage(self.page)
        self.webview.settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)

        self.webview.load(QUrl("https://www.youtube.com/embed/lbolOHwgT6I?list=PLDjUp0pPODIBAOV9AqRiCgSK0y1_mZZsx"))

        v_box = QVBoxLayout()
        v_box.addWidget(self.webview)
        self.widget.setLayout(v_box)

    def video_gosterme3(self):


        self.webview = QWebEngineView()
        self.page = WebEnginePage()
        self.webview.setPage(self.page)
        self.webview.settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)

        self.webview.load(QUrl("https://www.youtube.com/embed/cmT04IGw_FM?list=PLDjUp0pPODIBAOV9AqRiCgSK0y1_mZZsx"))

        v_box = QVBoxLayout()
        v_box.addWidget(self.webview)
        self.widget.setLayout(v_box)
    def video_gosterme4(self):


        self.webview = QWebEngineView()
        self.page = WebEnginePage()
        self.webview.setPage(self.page)
        self.webview.settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)

        self.webview.load(QUrl("https://www.youtube.com/embed/G2B_A6wcWbs?list=PLDjUp0pPODIBAOV9AqRiCgSK0y1_mZZsx"))

        v_box = QVBoxLayout()
        v_box.addWidget(self.webview)
        self.widget.setLayout(v_box)
    def video_gosterme5(self):
        self.webview = QWebEngineView()
        self.page = WebEnginePage()
        self.webview.setPage(self.page)
        self.webview.settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)

        self.webview.load(QUrl("https://www.youtube.com/embed/YqWKcTyeLmY?list=PLDjUp0pPODIBAOV9AqRiCgSK0y1_mZZsx"))

        v_box = QVBoxLayout()
        v_box.addWidget(self.webview)
        self.widget.setLayout(v_box)
    def video_gosterme6(self):
        self.webview = QWebEngineView()
        self.page = WebEnginePage()
        self.webview.setPage(self.page)
        self.webview.settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)

        self.webview.load(QUrl("https://www.youtube.com/embed/MumreQedfkk?list=PLDjUp0pPODIBAOV9AqRiCgSK0y1_mZZsx"))

        v_box = QVBoxLayout()
        v_box.addWidget(self.webview)
        self.widget.setLayout(v_box)
    def video_gosterme7(self):
        self.webview = QWebEngineView()
        self.page = WebEnginePage()
        self.webview.setPage(self.page)
        self.webview.settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)

        self.webview.load(QUrl("https://www.youtube.com/embed/cMQkbkEWK6U?list=PLDjUp0pPODIBAOV9AqRiCgSK0y1_mZZsx"))

        v_box = QVBoxLayout()
        v_box.addWidget(self.webview)
        self.widget.setLayout(v_box)


    #Minimize Tuşlarının yönetim fonksiyonları
    def kapama(self):
        self.close()
    def minimize_tusu(self):
        self.showMinimized()
    def fullekran(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    #Mesaj Box Kod bu bir kalıbdır. Çıkış yaptığımızda gösterdiği uyarı.

    def showMessageBox(self, title, content):
        msgBox = QMessageBox()
        msgBox.setWindowTitle(title)
        msgBox.setText(content)
        msgBox.exec_()

    def closeEvent(self, event):

        msg = "Ders Platformunu Kapmak Mı İstiyorsunuz ?"
        reply = QMessageBox.question(self, 'UYARI !',
                                     msg, QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()