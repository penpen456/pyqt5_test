import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from first import Ui_MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main)
    main.show()
    sys.exit(app.exec_())
