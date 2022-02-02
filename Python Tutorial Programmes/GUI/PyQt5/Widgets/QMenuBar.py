# A horizontal QMenuBar just below the title bar of a QMainWindow object is reserved for displaying QMenu objects.

# QMenu class provides a widget which can be added to menu bar.
# It is also used to create context menu and popup menu.
# Each QMenu object may contain one or more QAction objects or cascaded QMenu objects.

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class menudemo(QMainWindow):
    def __init__(self, parent=None):
        super(menudemo, self).__init__(parent)

        layout = QHBoxLayout()
        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("New")

        save = QAction("Save", self)
        save.setShortcut("Ctrl+S")
        file.addAction(save)

        edit = file.addMenu("Edit")
        edit.addAction("copy")
        edit.addAction("paste")

        quit = QAction("Quit", self)
        file.addAction(quit)
        file.triggered[QAction].connect(self.processtrigger)
        self.setLayout(layout)
        self.setWindowTitle("menu demo")

    def processtrigger(self, q):
        print(q.text() + " is triggered")


def main():
    app = QApplication(sys.argv)
    ex = menudemo()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()