# This widget is a file selector dialog. It enables the user to navigate through the file system
# and select a file to open or save.
# The dialog is invoked either through static functions or by calling exec_() function on the dialog object.

# Static functions of QFileDialog class (getOpenFileName() and getSaveFileName()) c
# all the native file dialog of the current operating system.

# A file filter can also applied to display only files of the specified extensions.
# The starting directory and default file name can also be set.

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class CustomDialog(QFileDialog):

    def __init__(self, *args, **kwargs):
        super(CustomDialog, self).__init__(*args, **kwargs)

        self.setWindowTitle("HELLO!")

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


class filedialogdemo(QWidget):
    def __init__(self, parent=None):
        super(filedialogdemo, self).__init__(parent)

        layout = QVBoxLayout()

        self.btn1 = QPushButton("QFileDialog object")
        self.btn1.clicked.connect(self.getfiles)
        layout.addWidget(self.btn1)

        self.contents = QTextEdit()
        layout.addWidget(self.contents)
        self.setLayout(layout)
        self.setWindowTitle("File Dialog demo")

    def getfiles(self, s):
        print("click", s)
        dlg = CustomDialog(self)
        if dlg.exec_():
            filenames = dlg.selectedFiles()
        f = open(filenames[0], 'r')

        with f:
            data = f.read()
            self.contents.setText(data)


def main():
    app = QApplication(sys.argv)
    ex = filedialogdemo()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()