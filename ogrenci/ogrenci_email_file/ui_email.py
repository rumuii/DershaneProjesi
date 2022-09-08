
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PyQt5 import QtWidgets
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import qdarkstyle  #Otamatik dark Designer Görünümü Kazandıran FrameWork


class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(378, 412)
        widget.setMaximumSize(QtCore.QSize(378, 412))

        self.verticalLayout = QtWidgets.QVBoxLayout(widget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        #Alici emaili LABEL
        self.alici = QtWidgets.QLabel(widget)
        self.alici.setObjectName("alici")
        self.horizontalLayout.addWidget(self.alici)

        self.frame = QtWidgets.QFrame(widget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout.addWidget(self.frame)


        #alici yazısı
        self.alici_yazisi = QtWidgets.QLineEdit(widget)
        self.alici_yazisi.setStyleSheet(" \n"
"color: rgb(0, 0, 0);")
        self.alici_yazisi.setInputMask("")
        self.alici_yazisi.setText("")
        self.alici_yazisi.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.alici_yazisi.setCursorPosition(0)
        self.alici_yazisi.setReadOnly(True)
        self.alici_yazisi.setObjectName("alici_yazisi")
        self.horizontalLayout.addWidget(self.alici_yazisi)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.mail_konusu_yazisi = QtWidgets.QLabel(widget)
        self.mail_konusu_yazisi.setObjectName("mail_konusu_yazisi")
        self.horizontalLayout_2.addWidget(self.mail_konusu_yazisi)
        self.frame_2 = QtWidgets.QFrame(widget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(widget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.mail_konusu = QtWidgets.QLineEdit(widget)
        self.mail_konusu.setObjectName("mail_konusu")
        self.horizontalLayout_2.addWidget(self.mail_konusu)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.mail_icerigi_yazisi = QtWidgets.QLabel(widget)
        self.mail_icerigi_yazisi.setObjectName("mail_icerigi_yazisi")
        self.verticalLayout_3.addWidget(self.mail_icerigi_yazisi)
        self.mail_icerigi = QtWidgets.QTextEdit(widget)
        self.mail_icerigi.setObjectName("mail_icerigi")
        self.verticalLayout_3.addWidget(self.mail_icerigi)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.mail_adresiniz_yazisi = QtWidgets.QLabel(widget)
        self.mail_adresiniz_yazisi.setObjectName("mail_adresiniz_yazisi")
        self.horizontalLayout_5.addWidget(self.mail_adresiniz_yazisi)
        self.mail_adresiniz = QtWidgets.QLineEdit(widget)
        self.mail_adresiniz.setObjectName("mail_adresiniz")
        self.horizontalLayout_5.addWidget(self.mail_adresiniz)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.frame_7 = QtWidgets.QFrame(widget)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_5.addWidget(self.frame_7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.sifreniz_yazisi = QtWidgets.QLabel(widget)
        self.sifreniz_yazisi.setObjectName("sifreniz_yazisi")
        self.horizontalLayout_4.addWidget(self.sifreniz_yazisi)

        self.lineEdit_4 = QtWidgets.QLineEdit(widget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.horizontalLayout_4.addWidget(self.lineEdit_4)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.button = QtWidgets.QPushButton(widget)
        self.button.setObjectName("button")
        self.horizontalLayout_4.addWidget(self.button)
        self.button1 = QtWidgets.QPushButton(widget)
        self.button1.setObjectName("button1")
        self.horizontalLayout_4.addWidget(self.button1)
        self.frame_4 = QtWidgets.QFrame(widget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(widget)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_4.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(widget)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_4.addWidget(self.frame_6)
        self.g_yazi = QtWidgets.QLabel(widget)
        self.g_yazi.setText("")
        self.g_yazi.setObjectName("g_yazi")
        self.horizontalLayout_4.addWidget(self.g_yazi)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

        self.button.clicked.connect(self.mail)
        self.button1.clicked.connect(widget.close)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "Soru gönder"))
        self.alici.setText(_translate("widget", "Alıcı Email Adresi:"))
        self.alici_yazisi.setPlaceholderText(_translate("widget", "turanyazilim01@gmail.com"))
        self.mail_konusu_yazisi.setText(_translate("widget", "Mail konusu:"))
        self.mail_icerigi_yazisi.setText(_translate("widget", "Mail içeriği:"))
        self.mail_adresiniz_yazisi.setText(_translate("widget", "Email:"))
        self.sifreniz_yazisi.setText(_translate("widget", "Şifre:"))
        self.button.setText(_translate("widget", "Gönder"))
        self.button1.setText(_translate("widget", "Cıkış"))



    def mail(self):
        mesaj = MIMEMultipart()

        mesaj["Subject"] = self.mail_konusu.text()

        yazi = self.mail_icerigi.toPlainText()

        mesaj_govdesi = MIMEText(yazi, 'plain')

        mesaj.attach(mesaj_govdesi)

        try:
            mail = smtplib.SMTP('smtp.gmail.com', 587)

            mail.ehlo()
            mail.starttls()
            mail.login(self.mail_adresiniz.text(), self.lineEdit_4.text())

            mail.sendmail(self.mail_adresiniz.text(), self.alici_yazisi.placeholderText(), mesaj.as_string())
            self.g_yazi.setText('Mail gönderildi.')
            mail.close()
        except:
            self.g_yazi.setText('Bir hata oluştu.')



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("fusion")
    Form = QtWidgets.QWidget()
    ui = Ui_widget()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
