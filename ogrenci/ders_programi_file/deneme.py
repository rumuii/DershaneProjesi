import os
import sys
from io import BytesIO
from  PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtWidgets import QLabel, QPushButton, QMessageBox
from PyQt5.QtGui import QPixmap, QImage
import requests

url = """https://i.ibb.co/2Zg3q7Q/ders-program.png
"""


# Отловить ошибки в слотах PyQt5
def hata_gorme(ex_cls, ex, tb):
    text = '{}: {}:\n'.format(ex_cls.__name__, ex)
    import traceback
    text += ''.join(traceback.format_tb(tb))

    print(text)
    QMessageBox.critical(None, 'Bir hata var !', text)
    quit()
sys.excepthook = hata_gorme


class WindowsApplication(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('Ekran görüntüsü')
		self.setGeometry(300, 200, 800, 600)
		vbox = QVBoxLayout(self)

		label = QLabel()
		button = QPushButton(text='Ekran görüntüsü için tıklayın')
		button.clicked.connect(self.buttonHandler)

		vbox.addWidget(label)
		vbox.addWidget(button)

		content = requests.get(url).content

		pixmap = QPixmap()
		pixmap.loadFromData(content)

		label.setPixmap(pixmap)
	def buttonHandler(self):
		grab = self.grab()
		grab.save('dersprograminiz.png', 'png')
		os.startfile('dersprograminiz.png')
		print('END')



if __name__ == '__main__':
	app = QApplication(sys.argv)
	main_window = WindowsApplication()
	main_window.show()
	sys.exit(app.exec_())