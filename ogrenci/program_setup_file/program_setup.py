from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import webbrowser

class Ui_Form3(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(591, 336)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 1, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 0, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 1, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 2, 0, 1, 1)

        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(
            lambda: webbrowser.open('https://code.visualstudio.com/docs/?dv=win64'))
        self.pushButton_2.clicked.connect(
            lambda: webbrowser.open('https://www.python.org/downloads/'))
        self.pushButton_3.clicked.connect(lambda: webbrowser.open(
            'https://drive.google.com/file/d/1yQ_CXmzsfnPn9KsVtuZv5qxiUdLWhAUS/view'))

        self.pushButton_4.clicked.connect(lambda: webbrowser.open(
            'https://www.jetbrains.com/pycharm/'))

        self.pushButton_5.clicked.connect(lambda: webbrowser.open(
            'https://www.apachefriends.org/xampp-files/8.1.1/xampp-windows-x64-8.1.1-2-VS16-installer.exe'))

        self.pushButton_6.clicked.connect(
            lambda: webbrowser.open('https://repo.anaconda.com/archive/Anaconda3-2021.11-Windows-x86_64.exe'))

        self.pushButton_7.clicked.connect(
            lambda: webbrowser.open('http://officecdn.microsoft.com/pr/492350f6-3a01-4f97-b9c0-c7c6ddf67d60/media/tr-tr/Professional2019Retail.img'))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Program Setupları"))
        self.pushButton.setText(_translate("Form", "VİSUAL STUDİO CODE İNDİR"))
        self.pushButton_2.setText(_translate("Form", "PYTHON  3.10.02 İNDİR"))
        self.pushButton_3.setText(_translate("Form", "SQL2012 İNDİR"))
        self.pushButton_4.setText(_translate("Form", "PYCHARM İNDİR"))
        self.pushButton_5.setText(_translate("Form", "XAMP İNDİR"))
        self.pushButton_6.setText(_translate("Form", "WİN10 64X ANACONDA İNDİR"))
        self.pushButton_7.setText(_translate("Form", "MİCROSOFT OFFİCE LİNK"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("fusion")
    Form = QtWidgets.QWidget()
    ui = Ui_Form3()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
