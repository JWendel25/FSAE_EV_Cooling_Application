import os
import sys
import shutil

# Import PyQt5 classes for GUI
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QDialog

# Import UI
from UI_Files.qt_Startup import Ui_Dialog

class startup_window(QtWidgets.QMainWindow, QDialog):
    def __init__(self):
        super(startup_window, self).__init__()
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)       # May not be needed when changed to app
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowStaysOnTopHint)      # May not be needed when changed to app
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        # Initialize other parameters
        self.ui.stackedWidget.setCurrentIndex(0)
        self.previousIndex = None
        
        self.assign_widgets()
        self.show()
    
    def fill(self):
        print("Not yet tied to a function")
        
    def nav_new(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def nav_copy(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def nav_edit(self):
        self.ui.stackedWidget.setCurrentIndex(3)
    
    def launch_new(self):
        newFileName = self.ui.textEdit_NewSim.toPlainText() + ".xlsm"
        newFilePath = os.path.join('Simulations', newFileName)
        shutil.copy(r'Simulations/Template.xlsm', newFilePath)
        print('Sucess') # Need to add error handle if no text is entered
        # Add opening next stage of app
    
    def select_file_copy(self):
        pass
    
    def launch_copy(self):
        pass
    
    def select_file_edit(self):
        pass
    
    def launch_edit(self):
        pass
    
    def back(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    
    def error_return(self):
        self.ui.stackedWidget.setCurrentIndex(self.previousIndex)

    def assign_widgets(self):
        # Landing Page Buttons
        self.ui.NavNew.clicked.connect(self.nav_new)
        self.ui.NavCopy.clicked.connect(self.nav_copy)
        self.ui.NavEdit.clicked.connect(self.nav_edit)
        
        # New Simulation Buttons
        self.ui.LaunchNew.clicked.connect(self.launch_new)
        self.ui.BackNew.clicked.connect(self.back)
        
        # New from Copy Buttons
        self.ui.SelectFileCopy.clicked.connect(self.fill)
        self.ui.LaunchCopy.clicked.connect(self.fill)
        self.ui.BackCopy.clicked.connect(self.back)
        
        # Edit Previous Buttons
        self.ui.SelectFileEdit.clicked.connect(self.fill)
        self.ui.LaunchEdit.clicked.connect(self.fill)
        self.ui.BackEdit.clicked.connect(self.back)
        
        # Error Buttons
        self.ui.ErrorReturn.clicked.connect(self.error_return)

if __name__ == '__main__':
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
        #app.setStyle('Windows')
        #app.setStyleSheet("QWidget { background-color: #d4d0c8; }")
    app.aboutToQuit.connect(app.deleteLater)
    main_win = startup_window()
    sys.exit(app.exec_())