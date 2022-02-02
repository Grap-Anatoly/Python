# A QSpinBox object presents the user with a textbox which displays an integer with up/down button on its right.
# The value in the textbox increases/decreases if the up/down button is pressed.

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class spindemo(QWidget):
    def __init__(self, parent=None):
        super(spindemo, self).__init__(parent)

        layout = QVBoxLayout()
        self.l1 = QLabel("current value:")
        self.l1.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.l1)
        self.sp = QSpinBox()

        layout.addWidget(self.sp)
        self.sp.valueChanged.connect(self.valuechange)
        self.setLayout(layout)
        self.setWindowTitle("SpinBox demo")

    def valuechange(self):
        self.l1.setText("current value:" + str(self.sp.value()))


def main():
    app = QApplication(sys.argv)
    ex = spindemo()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()