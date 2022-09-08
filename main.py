
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from Mavi_Dershanem.login.yeni_giris import Ui_Form #Giris sayfasına yönlendiriyor.


if __name__ == "__main__":
        app = QApplication(sys.argv)
        app.setStyle("fusion")
        form = QWidget()
        pencere = Ui_Form()  #giris sayfasını acıyoruz.
        pencere.setupUi(form)
        form.show()
        sys.exit(app.exec_())

