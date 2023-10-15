from PyQt5.QtWidgets import *
import sys

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
    def setupUi(self):
        self.setWindowTitle("Hello, world")
        self.resize(300, 200)
        self.lbl = QLabel('Hello, world!', self)
        self.lbl.move(120, 50)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())


    