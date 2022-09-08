
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_Dokuman(object):
    def setupUi(self, Dokuman):
        Dokuman.setObjectName("Dokuman")
        Dokuman.resize(412, 284)
        Dokuman.setMinimumSize(QtCore.QSize(412, 284))
        Dokuman.setMaximumSize(QtCore.QSize(412, 284))
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 1, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 0, 1, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 2, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 2, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 2, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 0, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 1, 0, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 2, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.frame)
        Dokuman.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.tab_2)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_13 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_2.addWidget(self.pushButton_13, 2, 2, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_2.addWidget(self.pushButton_12, 1, 2, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout_2.addWidget(self.pushButton_15, 2, 1, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_2.addWidget(self.pushButton_10, 0, 2, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_2.addWidget(self.pushButton_11, 0, 1, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout_2.addWidget(self.pushButton_14, 1, 1, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout_2.addWidget(self.pushButton_16, 1, 0, 1, 1)
        self.pushButton_17 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout_2.addWidget(self.pushButton_17, 0, 0, 1, 1)
        self.pushButton_18 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridLayout_2.addWidget(self.pushButton_18, 2, 0, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_2)
        self.verticalLayout_3.addWidget(self.frame_2)
        Dokuman.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_3 = QtWidgets.QFrame(self.tab_3)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_22 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_22.setObjectName("pushButton_22")
        self.gridLayout_3.addWidget(self.pushButton_22, 1, 1, 1, 1)
        self.pushButton_20 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_20.setObjectName("pushButton_20")
        self.gridLayout_3.addWidget(self.pushButton_20, 2, 2, 1, 1)
        self.pushButton_24 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_24.setObjectName("pushButton_24")
        self.gridLayout_3.addWidget(self.pushButton_24, 2, 1, 1, 1)
        self.pushButton_21 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_21.setObjectName("pushButton_21")
        self.gridLayout_3.addWidget(self.pushButton_21, 1, 2, 1, 1)
        self.pushButton_23 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_23.setObjectName("pushButton_23")
        self.gridLayout_3.addWidget(self.pushButton_23, 0, 1, 1, 1)
        self.pushButton_19 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_19.setObjectName("pushButton_19")
        self.gridLayout_3.addWidget(self.pushButton_19, 0, 2, 1, 1)
        self.pushButton_25 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_25.setObjectName("pushButton_25")
        self.gridLayout_3.addWidget(self.pushButton_25, 0, 0, 1, 1)
        self.pushButton_26 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_26.setObjectName("pushButton_26")
        self.gridLayout_3.addWidget(self.pushButton_26, 1, 0, 1, 1)
        self.pushButton_27 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_27.setObjectName("pushButton_27")
        self.gridLayout_3.addWidget(self.pushButton_27, 2, 0, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_3)
        self.verticalLayout_5.addWidget(self.frame_3)
        Dokuman.addTab(self.tab_3, "")

        self.retranslateUi(Dokuman)
        Dokuman.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Dokuman)

    def retranslateUi(self, Dokuman):
        _translate = QtCore.QCoreApplication.translate
        Dokuman.setWindowTitle(_translate("Dokuman", "Dokuman-pdf"))
        self.pushButton_5.setText(_translate("Dokuman", "PYTHON-5"))
        self.pushButton_4.setText(_translate("Dokuman", "PYTHON-4"))
        self.pushButton_6.setText(_translate("Dokuman", "PYTHON-6"))
        self.pushButton.setText(_translate("Dokuman", "PYTHON-7"))
        self.pushButton_2.setText(_translate("Dokuman", "PYTHON-8"))
        self.pushButton_3.setText(_translate("Dokuman", "PYTHON-7"))
        self.pushButton_7.setText(_translate("Dokuman", "PYTHON-1"))
        self.pushButton_8.setText(_translate("Dokuman", "PYTHON-2"))
        self.pushButton_9.setText(_translate("Dokuman", "PYTHON-3"))
        Dokuman.setTabText(Dokuman.indexOf(self.tab), _translate("Dokuman", "PYTHON"))
        self.pushButton_13.setText(_translate("Dokuman", "HTML-9"))
        self.pushButton_12.setText(_translate("Dokuman", "HTML-8"))
        self.pushButton_15.setText(_translate("Dokuman", "HTML-6"))
        self.pushButton_10.setText(_translate("Dokuman", "HTML-7"))
        self.pushButton_11.setText(_translate("Dokuman", "HTML-4"))
        self.pushButton_14.setText(_translate("Dokuman", "HTML-5"))
        self.pushButton_16.setText(_translate("Dokuman", "HTML-2"))
        self.pushButton_17.setText(_translate("Dokuman", "HTML-1"))
        self.pushButton_18.setText(_translate("Dokuman", "HTML-3"))
        Dokuman.setTabText(Dokuman.indexOf(self.tab_2), _translate("Dokuman", "HTML"))
        self.pushButton_22.setText(_translate("Dokuman", "VERİTABANİ-5"))
        self.pushButton_20.setText(_translate("Dokuman", "VERİTABANİ-9"))
        self.pushButton_24.setText(_translate("Dokuman", "VERİTABANİ-6"))
        self.pushButton_21.setText(_translate("Dokuman", "VERİTABANİ-8"))
        self.pushButton_23.setText(_translate("Dokuman", "VERİTABANİ-4"))
        self.pushButton_19.setText(_translate("Dokuman", "VERİTABANİ-7"))
        self.pushButton_25.setText(_translate("Dokuman", "VERİTABANİ-1"))
        self.pushButton_26.setText(_translate("Dokuman", "VERİTABANİ-2"))
        self.pushButton_27.setText(_translate("Dokuman", "VERİTABANİ-3"))
        Dokuman.setTabText(Dokuman.indexOf(self.tab_3), _translate("Dokuman", "VERİTABANİ"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("fusion")
    Form = QtWidgets.QWidget()
    ui = Ui_Dokuman()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

