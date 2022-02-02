# A GUI widget can be placed inside the container window by specifying its absolute coordinates measured in pixels.
# The coordinates are relative to the dimensions of the window defined by setGeometry() method.

# setGeometry() syntax

# QWidget.setGeometry(xpos, ypos, width, height)

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def window():
    app = QApplication(sys.argv)
    w = QWidget()

    b = QPushButton(w)
    b.setText("Hello World!")
    b.move(70, 20)

    w.setGeometry(100, 100, 200, 100)
    w.setWindowTitle("PyQt")
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()