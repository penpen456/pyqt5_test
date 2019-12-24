import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from UI import Ui_MainWindow


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.openimg)
        self.pushButton_2.clicked.connect(self.opnefile)

    def openimg(self):
        dia = QFileDialog()
        img = dia.getOpenFileName(self, 'open img', 'C:\\', "Image files (*.jpg *.gif *.png *.jpeg)")
        print(img)

    def opnefile(self):
        allfile = QFileDialog.getOpenFileName(self, 'open file', 'D:\\', 'All Files (*)')
        print(allfile)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MyWindow()
    main.show()
    sys.exit(app.exec_())
