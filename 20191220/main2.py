import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from keypress import Ui_MainWindow
from PyQt5.QtCore import QEvent, Qt


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close)
        self.setMouseTracking(True)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

    def mouseMoveEvent(self, event):
        print(111)

    def grabMouse(self, event):
        print(222)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec_())
