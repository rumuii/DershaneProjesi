

## ==> SPLASH SCREEN
from Mavi_Dershanem.login_gecis.deneme2 import SplashScreen
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from Mavi_Dershanem.qrc_dosyası import d
import sqlite3
from Mavi_Dershanem.ogrenci.main_cek import ui_MainWindow

class Ui_Form1(object):

    def yukleme(self):
          self.ui = SplashScreen()
          self.ui.show()



    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(364, 517)
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
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(252, 128, 128, 0));")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/Hopstarter-Sleek-Xp-Basic-Close.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(25, 25))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.verticalLayout_6.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(252, 128, 128, 0));")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.mavi_dershanem = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mavi_dershanem.sizePolicy().hasHeightForWidth())
        self.mavi_dershanem.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.mavi_dershanem.setFont(font)
        self.mavi_dershanem.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mavi_dershanem.setStyleSheet("color:rgba(255,255,255,210);\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(252, 128, 128, 0));")
        self.mavi_dershanem.setAlignment(QtCore.Qt.AlignCenter)
        self.mavi_dershanem.setObjectName("mavi_dershanem")
        self.verticalLayout_4.addWidget(self.mavi_dershanem)
        self.hosgeldiniz = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.hosgeldiniz.setFont(font)
        self.hosgeldiniz.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.hosgeldiniz.setStyleSheet("color:rgba(255,255,255,210);")
        self.hosgeldiniz.setAlignment(QtCore.Qt.AlignCenter)
        self.hosgeldiniz.setObjectName("hosgeldiniz")
        self.verticalLayout_4.addWidget(self.hosgeldiniz)
        self.label = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("\n"
"color:rgba(255, 255, 255, 210);\n"
"\n"
"")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.email = QtWidgets.QLineEdit(self.frame_4)
        self.email.setStyleSheet("#email{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(196, 171, 232, 198), stop:1 rgba(255, 255, 255, 255));\n"
"   border-bottom:2px solid rgba(255,255,255,255);\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:10px;\n"
"  \n"
"}\n"
"#email:hover{    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(114, 90, 150, 221), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"#email:pressed{    \n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(105, 118, 132, 200);\n"
"}")
        self.email.setObjectName("email")
        self.verticalLayout_4.addWidget(self.email)
        self.parola = QtWidgets.QLineEdit(self.frame_4)
        self.parola.setStyleSheet("#parola{    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(196, 171, 232, 198), stop:1 rgba(255, 255, 255, 255));\n"
"   border-bottom:2px solid rgba(255,255,255,255);\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:10px;\n"
"  \n"
"}\n"
"#parola:hover{    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(114, 90, 150, 221), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"#parola:pressed{    \n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(105, 118, 132, 200);\n"
"}")
        self.parola.setText("")
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.parola.setObjectName("parola")
        self.verticalLayout_4.addWidget(self.parola)
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_4.addWidget(self.frame_6)

        self.giris_butonu = QtWidgets.QPushButton(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.giris_butonu.setFont(font)
        self.giris_butonu.setStyleSheet("#giris_butonu{    \n"
"   border-bottom:2px solid rgba(255,255,255,255);\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:1px;\n"
"  \n"
"}\n"
"\n"
"\n"
"#giris_butonu:pressed{    \n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(105, 118, 132, 200);\n"
"}")
        self.giris_butonu.setObjectName("giris_butonu")
        self.verticalLayout_4.addWidget(self.giris_butonu)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(252, 128, 128, 0));")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.i_icon = QtWidgets.QPushButton(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(20)
        self.i_icon.setFont(font)
        self.i_icon.setStyleSheet("color: rgb(181, 107, 223);\n"
"border-radius:12px;\n"
"")
        self.i_icon.setObjectName("i_icon")
        self.horizontalLayout_2.addWidget(self.i_icon)
        self.w_icon = QtWidgets.QPushButton(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(20)
        self.w_icon.setFont(font)
        self.w_icon.setStyleSheet("color: rgb(60, 255, 1);\n"
"border-radius:12px;")
        self.w_icon.setObjectName("w_icon")
        self.horizontalLayout_2.addWidget(self.w_icon)
        self.y_icon = QtWidgets.QPushButton(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(20)
        self.y_icon.setFont(font)
        self.y_icon.setStyleSheet("color: rgb(170, 35, 8);\n"
"border-radius:12px;")
        self.y_icon.setObjectName("y_icon")
        self.horizontalLayout_2.addWidget(self.y_icon)
        self.t_icon = QtWidgets.QPushButton(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(20)
        self.t_icon.setFont(font)
        self.t_icon.setStyleSheet("color: rgb(43, 255, 28);\n"
"border-radius: 12px;")
        self.t_icon.setObjectName("t_icon")
        self.horizontalLayout_2.addWidget(self.t_icon)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addWidget(self.frame_5)
        self.verticalLayout_6.addWidget(self.frame_4)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


        self.i_icon.clicked.connect(lambda: webbrowser.open('https://www.instagram.com/'))
        self.w_icon.clicked.connect(lambda: webbrowser.open('https://web.whatsapp.com/'))
        self.y_icon.clicked.connect(lambda: webbrowser.open('https://www.youtube.com/'))
        self.t_icon.clicked.connect(lambda: webbrowser.open('https://twitter.com/'))

        self.giris_butonu.clicked.connect(self.loginfunc)
        # tuşa basınca önce ki pencere kapatılır.
        self.giris_butonu.clicked.connect(Form.close)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.mavi_dershanem.setText(_translate("Form", "MAVİ DERSHANEM"))
        self.hosgeldiniz.setText(_translate("Form", "HOŞGELDİNİZ!"))
        self.label.setText(_translate("Form", "ÖĞRENCİ"))
        self.email.setPlaceholderText(_translate("Form", "E-mail :"))
        self.parola.setPlaceholderText(_translate("Form", "Parola :"))
        self.giris_butonu.setText(_translate("Form", "GİRİŞ"))
        self.i_icon.setText(_translate("Form", "Q"))
        self.w_icon.setText(_translate("Form", "L"))
        self.y_icon.setText(_translate("Form", "P"))
        self.t_icon.setText(_translate("Form", "m"))

    def loginfunc(self):
        user_name = self.email.text()
        password_ = self.parola.text()
        if len(user_name) == 0 or len(password_) == 0:
            print("Lütfen tüm alanları doldurun.")
        else:
            try:
                conn = sqlite3.connect("ProjeDershanem.db")
                cur = conn.cursor()
                cur.execute("SELECT parola FROM tbl_ogrenci WHERE email=?", [user_name])
                data = cur.fetchone()[0]
            except TypeError:
                print("Böyle bir kulanici bulunmuyor.")
            else:
                if data == password_:
                     self.yukleme()

                else:
                    print("Parola yanlış.")
            finally:
                conn.close()






if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        app.setStyle("fusion")
        Form = QtWidgets.QWidget()
        ui = Ui_Form1()
        ui.setupUi(Form)
        Form.show()
        sys.exit(app.exec_())
