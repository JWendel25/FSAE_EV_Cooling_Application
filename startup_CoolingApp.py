import os
import sys
import shutil
import pathlib

# Import PyQt5 classes for GUI
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog

# Import UI
from UI_Files.qt_Startup import Ui_Dialog

class startup_window(QtWidgets.QMainWindow, QDialog):
    def __init__(self):
        super(startup_window, self).__init__()
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)       # May not be needed when changed to app
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowStaysOnTopHint)      # May not be needed when changed to app
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        # Initialize Parameters
        self.ui.stackedWidget.setCurrentIndex(0)
        self.simFilePath = None
        self.copyFileName = None
        self.editFileName = None
        self.previousIndex = None
        self.errorMessage = None
        
        # Start UI
        self.assign_widgets()
        self.show()
    
    
    def fill(self):
        print('Not yet tied to a function')
        
    
    # NAVIGATION DEFINITIONS
    
    def nav_new(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def nav_copy(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def nav_edit(self):
        self.ui.stackedWidget.setCurrentIndex(3)
    
    def back(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.copyFileName = None
        self.editFileName = None
    
    
    # NEW SIMULATION DEFINITIONS
    
    def launch_new(self):
        newNameEntered = self.ui.textEdit_New.toPlainText()
        if newNameEntered != '' :
            newFileName = newNameEntered + '.xlsm'
            newFilePath = os.path.join('Simulations', newFileName)
            shutil.copy(r'Simulations/Template.xlsm', newFilePath)
            print('Sucess')
            self.simFilePath = newFilePath
            # Add opening next stage of app
        else:
            self.errorMessage = 'Error: Failed to enter file name. Please hit the \"OK\" button and enter a name into the given text box before launching the simulation.'
            self.error_send()
    
    
    # NEW SIMULATION FROM COPY DEFINITIONS
    
    def select_file_copy(self):
        copyFilePath = QFileDialog.getOpenFileName(None, 'Select File', os.path.join(pathlib.Path().resolve(), 'Simulations'))[0]                        # Stores the opened file name as a self variable
        QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))                      # Dispalys a loading cursor
        app.processEvents()                                                         # Ensures the app will remain responsive after opening the file
        QApplication.restoreOverrideCursor()                                        # Turns of the loading cursor once the app has finished processing
        self.copyFileName = os.path.basename(copyFilePath[:-5])
        self.ui.textEdit_Copy.setText(self.copyFileName)                          # Displays the file name in the dedicated text bar
    
    def launch_copy(self):
        newNameEntered = self.ui.textEdit_Copy.toPlainText()
        if self.copyFileName == None :
            self.errorMessage = 'Error: No file was selected. Please hit the \"OK\" button and select a file before launching the simulation.'
            self.error_send()
        elif newNameEntered != '' and newNameEntered != self.copyFileName :
            newFileName = newNameEntered + '.xlsm'
            newFilePath = os.path.join('Simulations', newFileName)
            copyFilePath = os.path.join('Simulations', self.copyFileName + '.xlsm')
            shutil.copy(copyFilePath, newFilePath)
            print('Sucess')
            self.simFilePath = newFilePath
            # Add opening next stage of app
        else:
            if newNameEntered == self.copyFileName :
                self.errorMessage = 'Error: Failed to change file name. Please hit the \"OK\" button and enter a name into the given text box before launching the simulation.'
            else:
                self.errorMessage = 'Error: Failed to enter file name. Please hit the \"OK\" button and enter a name into the given text box before launching the simulation.'
            self.error_send()
            
            
    # EDIT SIMULATION DEFINITIONS
    
    def select_file_edit(self):
        editFilePath = QFileDialog.getOpenFileName(None, 'Select File', os.path.join(pathlib.Path().resolve(), 'Simulations'))[0]                        # Stores the opened file name as a self variable
        QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))                      # Dispalys a loading cursor
        app.processEvents()                                                         # Ensures the app will remain responsive after opening the file
        QApplication.restoreOverrideCursor()                                        # Turns of the loading cursor once the app has finished processing
        self.editFileName = os.path.basename(editFilePath[:-5])
        self.ui.textEdit_Edit.setText(self.editFileName)                          # Displays the file name in the dedicated text bar
    
    def launch_edit(self):
        if self.editFileName == None :
            self.errorMessage = 'Error: No file was selected. Please hit the \"OK\" button and select a file before launching the simulation.'
            self.error_send()
        else:
            print('Sucess')
            self.simFilePath = self.editFileName
            # Add opening next stage of app
        
        
    # ERROR HANDLING DEFINITIONS
    
    def error_send(self):
        self.previousIndex = self.ui.stackedWidget.currentIndex()
        self.ui.textDisplayError.setText(self.errorMessage)
        self.ui.stackedWidget.setCurrentIndex(4)
    
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
        self.ui.SelectFileCopy.clicked.connect(self.select_file_copy)
        self.ui.LaunchCopy.clicked.connect(self.launch_copy)
        self.ui.BackCopy.clicked.connect(self.back)
        
        # Edit Previous Buttons
        self.ui.SelectFileEdit.clicked.connect(self.select_file_edit)
        self.ui.LaunchEdit.clicked.connect(self.launch_edit)
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