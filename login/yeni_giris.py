
from PyQt5 import QtCore, QtGui, QtWidgets

from Mavi_Dershanem.ogrenci.yeni_ogrenci_giris import Ui_Form1
from Mavi_Dershanem.ogretmen.ogretmen_giris2 import Ui_Form4
from Mavi_Dershanem.yonetici.yonetici_giris import Ui_Form5
import webbrowser
import sys


class Ui_Form(object):

    def ogrenci_login(self):
            self.window = QtWidgets.QWidget()
            self.ui = Ui_Form1()
            self.ui.setupUi(self.window)
            self.window.show()

    def ogretmen_login(self):
            self.window = QtWidgets.QWidget()
            self.ui = Ui_Form4()
            self.ui.setupUi(self.window)
            self.window.show()
    def yonetici_login(self):
            self.window = QtWidgets.QWidget()
            self.ui = Ui_Form5()
            self.ui.setupUi(self.window)
            self.window.show()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(331, 442)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setStyleSheet("\n"
"border-radius:35px;\n"
"background-color: qconicalgradient(cx:0.483051, cy:0.489, angle:0, stop:0 rgba(114, 90, 150, 221));\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setStyleSheet("background-color:rgba(0,0,0,190);\n"
"border-radius:50px;\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 0));")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.pushButton = QtWidgets.QPushButton(self.frame_4)
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/Hopstarter-Sleek-Xp-Basic-Close.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(25, 25))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_7.addWidget(self.pushButton, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.verticalLayout_6.addWidget(self.frame_4)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 0));")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.mavi_dershanem = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.mavi_dershanem.setFont(font)
        self.mavi_dershanem.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mavi_dershanem.setStyleSheet("color:rgba(255,255,255,210);\n"
"\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 0));")
        self.mavi_dershanem.setAlignment(QtCore.Qt.AlignCenter)
        self.mavi_dershanem.setObjectName("mavi_dershanem")
        self.verticalLayout_5.addWidget(self.mavi_dershanem)
        self.hosgeldiniz = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.hosgeldiniz.setFont(font)
        self.hosgeldiniz.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.hosgeldiniz.setStyleSheet("color:rgba(255,255,255,210);\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 0));")
        self.hosgeldiniz.setAlignment(QtCore.Qt.AlignCenter)
        self.hosgeldiniz.setObjectName("hosgeldiniz")
        self.verticalLayout_5.addWidget(self.hosgeldiniz)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.verticalLayout_8.addLayout(self.verticalLayout_5)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.yonetici_girisi = QtWidgets.QPushButton(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.yonetici_girisi.setFont(font)
        self.yonetici_girisi.setStyleSheet("#yonetici_girisi{    \n"
"   border-bottom:2px solid rgba(255,255,255,255);\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:1px;\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 0));\n"
"}\n"
"#yonetici_girisi:hover{    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(114, 90, 150, 221), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"#yonetici_girisi:pressed{    \n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(105, 118, 132, 200);\n"
"}\n"
"")
        self.yonetici_girisi.setObjectName("yonetici_girisi")
        self.verticalLayout_3.addWidget(self.yonetici_girisi)
        self.ogretmen_girisi = QtWidgets.QPushButton(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.ogretmen_girisi.setFont(font)
        self.ogretmen_girisi.setStyleSheet("#ogretmen_girisi{    \n"
"   border-bottom:2px solid rgba(255,255,255,255);\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:1px;\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 0));\n"
"}\n"
"#ogretmen_girisi:hover{    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(114, 90, 150, 221), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"#ogretmen_girisi:pressed{    \n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(105, 118, 132, 200);\n"
"}")
        self.ogretmen_girisi.setObjectName("ogretmen_girisi")
        self.verticalLayout_3.addWidget(self.ogretmen_girisi)
        self.ogrenci_girisi = QtWidgets.QPushButton(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.ogrenci_girisi.setFont(font)
        self.ogrenci_girisi.setStyleSheet("#ogrenci_girisi{    \n"
"   border-bottom:2px solid rgba(255,255,255,255);\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:1px;\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 0));\n"
"}\n"
"#ogrenci_girisi:hover{    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(114, 90, 150, 221), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"#ogrenci_girisi:pressed{    \n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(105, 118, 132, 200);\n"
"}")
        self.ogrenci_girisi.setObjectName("ogrenci_girisi")
        self.verticalLayout_3.addWidget(self.ogrenci_girisi)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.verticalLayout_8.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.i_icon = QtWidgets.QPushButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(20)
        self.i_icon.setFont(font)
        self.i_icon.setStyleSheet("color: rgb(181, 107, 223);\n"
"border-radius:12px;\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 0));")
        self.i_icon.setObjectName("i_icon")
        self.horizontalLayout_2.addWidget(self.i_icon)
        self.w_icon = QtWidgets.QPushButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(20)
        self.w_icon.setFont(font)
        self.w_icon.setStyleSheet("color: rgb(60, 255, 1);\n"
"border-radius:12px;\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 0));")
        self.w_icon.setObjectName("w_icon")
        self.horizontalLayout_2.addWidget(self.w_icon)
        self.y_icon = QtWidgets.QPushButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(20)
        self.y_icon.setFont(font)
        self.y_icon.setStyleSheet("color: rgb(170, 35, 8);\n"
"border-radius:12px;\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 0));")
        self.y_icon.setObjectName("y_icon")
        self.horizontalLayout_2.addWidget(self.y_icon)
        self.t_icon = QtWidgets.QPushButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(20)
        self.t_icon.setFont(font)
        self.t_icon.setStyleSheet("color: rgb(43, 255, 28);\n"
"border-radius: 12px;\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 0));")
        self.t_icon.setObjectName("t_icon")
        self.horizontalLayout_2.addWidget(self.t_icon)
        self.verticalLayout_8.addLayout(self.horizontalLayout_2)
        self.verticalLayout_6.addWidget(self.frame_3)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.i_icon.clicked.connect(lambda: webbrowser.open('https://www.instagram.com/'))
        self.w_icon.clicked.connect(lambda: webbrowser.open('https://web.whatsapp.com/'))
        self.y_icon.clicked.connect(lambda: webbrowser.open('https://www.youtube.com/'))
        self.t_icon.clicked.connect(lambda: webbrowser.open('https://twitter.com/'))

        self.ogrenci_girisi.clicked.connect(self.ogrenci_login)
        # tuşa basınca önce ki pencere kapatılır.
        self.ogrenci_girisi.clicked.connect(Form.close)
        self.ogretmen_girisi.clicked.connect(self.ogretmen_login)
        # tuşa basınca önce ki pencere kapatılır.
        self.ogretmen_girisi.clicked.connect(Form.close)
        self.yonetici_girisi.clicked.connect(self.yonetici_login)
        # tuşa basınca önce ki pencere kapatılır.
        self.yonetici_girisi.clicked.connect(Form.close)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.mavi_dershanem.setText(_translate("Form", "MAVİ DERSHANEM"))
        self.hosgeldiniz.setText(_translate("Form", "HOŞGELDİNİZ!"))
        self.yonetici_girisi.setText(_translate("Form", "YÖNETİCİ GİRİŞİ"))
        self.ogretmen_girisi.setText(_translate("Form", "ÖĞRETMEN GİRİŞİ"))
        self.ogrenci_girisi.setText(_translate("Form", "ÖĞRENCİ GİRİŞİ"))
        self.i_icon.setText(_translate("Form", "Q"))
        self.w_icon.setText(_translate("Form", "L"))
        self.y_icon.setText(_translate("Form", "P"))
        self.t_icon.setText(_translate("Form", "m"))







