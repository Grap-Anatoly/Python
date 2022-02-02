import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        hbox = QVBoxLayout()
        self.edit1 = QTextEdit()
        hbox.addWidget(self.edit1)
        self.btn1 = QPushButton("Copy")
        hbox.addWidget(self.btn1)
        self.edit2 = QTextEdit()
        self.btn2 = QPushButton("Paste")
        hbox.addWidget(self.edit2)
        hbox.addWidget(self.btn2)
        self.btn1.clicked.connect(self.copytext)
        self.btn2.clicked.connect(self.pastetext)
        self.setLayout(hbox)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Clipboard')
        self.show()

    def copytext(self):
        # clipboard.setText(self.edit1.copy())
        self.edit1.copy()
        print(clipboard.text())

        msg = QMessageBox()
        msg.setText(clipboard.text() + " copied on clipboard")
        msg.exec_()

    def pastetext(self):
        self.edit2.setText(clipboard.text())


app = QApplication(sys.argv)
clipboard = app.clipboard()
ex = Example()
ex.setWindowTitle("clipboard Example")
sys.exit(app.exec_())