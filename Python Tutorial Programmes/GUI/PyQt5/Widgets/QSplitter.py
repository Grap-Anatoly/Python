# This is another advanced layout manager which allows the size of child widgets to be changed dynamically by
# dragging the boundaries between them.
# The Splitter control provides a handle that can be dragged to resize the controls.

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()


def initUI(self):
    hbox = QHBoxLayout(self)

    topleft = QFrame()
    topleft.setFrameShape(QFrame.StyledPanel)
    bottom = QFrame()
    bottom.setFrameShape(QFrame.StyledPanel)

    splitter1 = QSplitter(Qt.Horizontal)
    textedit = QTextEdit()
    splitter1.addWidget(topleft)
    splitter1.addWidget(textedit)
    splitter1.setSizes([100, 200])

    splitter2 = QSplitter(Qt.Vertical)
    splitter2.addWidget(splitter1)
    splitter2.addWidget(bottom)

    hbox.addWidget(splitter2)

    self.setLayout(hbox)
    QApplication.setStyle(QStyleFactory.create('Cleanlooks'))

    self.setGeometry(300, 300, 300, 200)
    self.setWindowTitle('QSplitter demo')
    self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()