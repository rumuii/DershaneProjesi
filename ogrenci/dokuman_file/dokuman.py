#

from PyQt5 import QtCore, QtGui, QtWidgets
import webbrowser
import sys

class Ui_Form1(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(431, 138)
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
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 0, 2, 2, 1)

        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton_3.clicked.connect(lambda: webbrowser.open('https://mavidershanem.com/wp-content/uploads/2022/01/htmlgiris-.pdf'))
        self.pushButton_2.clicked.connect(lambda: webbrowser.open('https://drive.google.com/drive/folders/1PaaUgnxHuCZtHe_Sse8kljNXXTt6l3Yu'))
        self.pushButton.clicked.connect(lambda: webbrowser.open('https://yunus.hacettepe.edu.tr/~selcen10/veri%20tabani/VTYS-SQL_YAPISAL_SORGULAMA_DiLi.pdf'))
        self.pushButton_4.clicked.connect(lambda: webbrowser.open('https://mega.nz/file/ghtU3bZS#imRhJIxPpl_bvMSbdKOIeG65LWBtse7dpoXz4zk4w0E'))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "PDF"))
        self.pushButton.setText(_translate("Form", "Veritabanı PDF"))
        self.pushButton_2.setText(_translate("Form", "Python PDF"))
        self.pushButton_3.setText(_translate("Form", "HTML  PDF"))
        self.pushButton_4.setText(_translate("Form", "BOSTRAP  PDF"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("fusion")
    Form = QtWidgets.QWidget()
    ui = Ui_Form1()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
