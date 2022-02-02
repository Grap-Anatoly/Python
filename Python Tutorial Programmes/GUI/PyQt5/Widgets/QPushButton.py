# In any GUI design, the command button is the most important and most often used control.
# uttons with Save, Open, OK, Yes, No and Cancel etc. as caption are familiar to any computer user.
# In PyQt API, the QPushButton class object presents a
# button which when clicked can be programmed to invoke a certain function.

# QPushButton class inherits its core functionality from QAbstractButton class.
# It is rectangular in shape and a text caption or icon can be displayed on its face.

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        layout = QVBoxLayout()
        self.b1 = QPushButton("Button1")
        self.b1.setCheckable(True)
        self.b1.toggle()
        self.b1.clicked.connect(lambda: self.whichbtn(self.b1))
        self.b1.clicked.connect(self.btnstate)
        layout.addWidget(self.b1)

        self.b2 = QPushButton()
        self.b2.setIcon(QIcon(QPixmap("python.gif")))
        self.b2.clicked.connect(lambda: self.whichbtn(self.b2))
        layout.addWidget(self.b2)
        self.setLayout(layout)
        self.b3 = QPushButton("Disabled")
        self.b3.setEnabled(False)
        layout.addWidget(self.b3)

        self.b4 = QPushButton("&Default")
        self.b4.setDefault(True)
        self.b4.clicked.connect(lambda: self.whichbtn(self.b4))
        layout.addWidget(self.b4)

        self.setWindowTitle("Button demo")

    def btnstate(self):
        if self.b1.isChecked():
            print("button pressed")
        else:
            print("button released")

    def whichbtn(self, b):
        print("clicked button is " + b.text())


def main():
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()