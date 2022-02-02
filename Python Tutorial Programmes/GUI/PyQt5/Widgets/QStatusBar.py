# QMainWindow object reserves a horizontal bar at the bottom as the status bar.
# It is used to display either permanent or contextual status information.

# There are three types of status indicators −
# Temporary − Briefly occupies most of the status bar.
# For example, used to explain tool tip texts or menu entries.

# Normal − Occupies part of the status bar and may be hidden by temporary messages.
# For example, used to display the page and line number in a word processor.

# Permanent − It is never hidden. Used for important mode indications.
# For example, some applications put a Caps Lock indicator in the status bar.

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class statusdemo(QMainWindow):
    def __init__(self, parent=None):
        super(statusdemo, self).__init__(parent)

        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("show")
        file.addAction("add")
        file.addAction("remove")
        file.triggered[QAction].connect(self.processtrigger)
        self.setCentralWidget(QTextEdit())

        self.statusBar = QStatusBar()
        self.b = QPushButton("click here")
        self.setWindowTitle("QStatusBar Example")
        self.setStatusBar(self.statusBar)

    def processtrigger(self, q):

        if (q.text() == "show"):
            self.statusBar.showMessage(q.text() + " is clicked", 2000)

        if q.text() == "add":
            self.statusBar.addWidget(self.b)

        if q.text() == "remove":
            self.statusBar.removeWidget(self.b)
            self.statusBar.show()


def main():
    app = QApplication(sys.argv)
    ex = statusdemo()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()