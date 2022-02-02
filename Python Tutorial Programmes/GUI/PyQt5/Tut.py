# Creating a simple GUI application using PyQt involves the following steps −

# Import QtCore, QtGui and QtWidgets modules from PyQt5 package.
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def window():

   app = QApplication(sys.argv) # Create an application object of QApplication class.
   w = QWidget()# A QWidget object creates top level window.
   b = QLabel(w)# Add QLabel object in it.
   b.setText("Hello World!")# Set the caption of label as "hello world".
   w.setGeometry(100,100,200,50)# Define the size and position of window by setGeometry() method.
   b.move(70,20)# Position of the text on panel
   w.setWindowTitle("PyQt5")# Title of the window
   w.show()# Visibility of the window
   sys.exit(app.exec_())# Enter the mainloop of application by app.exec_() method.

if __name__ == '__main__':
   window()