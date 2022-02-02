# A rectangular box before the text label appears when a QCheckBox object is added to the parent window.
# Just as QRadioButton, it is also a selectable button.
# Its common use is in a scenario when the user is asked to choose one or more of the available options.

# Unlike Radio buttons, check boxes are not mutually exclusive by default.
# In order to restrict the choice to one of the available items, the check boxes must be added to QButtonGroup.

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class checkdemo(QWidget):
    def __init__(self, parent=None):
        super(checkdemo, self).__init__(parent)

        layout = QHBoxLayout()
        self.b1 = QCheckBox("Button1")
        self.b1.setChecked(True)
        self.b1.stateChanged.connect(lambda: self.btnstate(self.b1))
        layout.addWidget(self.b1)

        self.b2 = QCheckBox("Button2")
        self.b2.toggled.connect(lambda: self.btnstate(self.b2))

        layout.addWidget(self.b2)
        self.setLayout(layout)
        self.setWindowTitle("checkbox demo")

    def btnstate(self, b):
        if b.text() == "Button1":
            if b.isChecked() == True:
                print(b.text() + " is selected")

            else:
                print(b.text() + " is deselected")


        if b.text() == "Button2":
            if b.isChecked() == True:
                print(b.text() + " is selected")

            else:
                print(b.text() + " is deselected")



def main():
    app = QApplication(sys.argv)
    ex = checkdemo()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
