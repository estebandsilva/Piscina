####REQUIREMENTS
#pip install PySide2
#pip install PySide6
#pip install Pycairo
#pip install pipwin
#pipwin install cairocffi
#pip install pyqt5

##Generamos el python con PySide2
    #pyuic5 -x interface.ui -o ui_interface.py
#lo mismo con resources
#pyrcc5 resources.qrc -o resources_rc.py

#otros
# pip install QT-PyQt-PySide-Custom-Widgets

#EN RASPBERRYPI
#$ sudo apt-get install --upgrade python3-pyside2.qt3dcore python3-pyside2.qt3dinput python3-pyside2.qt3dlogic python3-pyside2.qt3drender python3-pyside2.qtcharts python3-pyside2.qtconcurrent python3-pyside2.qtcore python3-pyside2.qtgui python3-pyside2.qthelp python3-pyside2.qtlocation python3-pyside2.qtmultimedia python3-pyside2.qtmultimediawidgets python3-pyside2.qtnetwork python3-pyside2.qtopengl python3-pyside2.qtpositioning python3-pyside2.qtprintsupport python3-pyside2.qtqml python3-pyside2.qtquick python3-pyside2.qtquickwidgets python3-pyside2.qtscript python3-pyside2.qtscripttools python3-pyside2.qtsensors python3-pyside2.qtsql python3-pyside2.qtsvg python3-pyside2.qttest python3-pyside2.qttexttospeech python3-pyside2.qtuitools python3-pyside2.qtwebchannel python3-pyside2.qtwebsockets python3-pyside2.qtwidgets python3-pyside2.qtx11extras python3-pyside2.qtxml python3-pyside2.qtxmlpatterns
# export QT_QPA_PLATFORM_PLUGIN_PATH=/usr/lib/python3.9/site-packages/PySide2/plugins/platforms
#sudo pip install QT-PyQt-PySide-Custom-Widgets
# Execute as super user
# sudo ./pruebaqt.sh

# cairocffi @ file:///C:/Users/esteb/pipwin/cairocffi-1.3.0-cp310-cp310-win_amd64.whl#sha256=44ab832c1aa061ff740bb5ea981c6d1a01bffa71d4068d51aeb65907e29970ca


### MANUAL INSTALATION ON PC
#pipwin install cairocffi


###IMPORTS
import os
import sys

from ui_interface_test import *
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel
# IMPORTED ON ui_interface

from Custom_Widgets.Widgets import *

#GRAPHICS Version 1.0
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


########################################################################
##   MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)




         # APPLY JSON STYLESHEET
        ########################################################################
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        loadJsonStyle(self, self.ui)
################
        # SHOW WINDOW
        #######################################################################
        #########################################################
        self.show()

        # EXPAND CENTER MENU WIDGET SIZE
        #self.ui.settingsBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        #self.ui.infoBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        #self.ui.helpBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())

        # CLOSE CENTER MENU WIDGET SIZE
        self.ui.closeCenterMenuBtn.clicked.connect(lambda: self.ui.centerMenuContainer.collapseMenu())

        # CLOSE RIGHT MENU WIDGET SIZE
        self.ui.closeRightMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.collapseMenu())
        self.ui.closeRightMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.collapseMenu())

################Prueba Button

#######################

        ### BOTONES DEL PANEL
        self.ui.panel_1c.clicked.connect(lambda:self.ui.label_4.raise_())
        self.ui.panel_1o.clicked.connect(lambda:self.ui.label_4.lower())

        self.ui.panel_2c.clicked.connect(lambda: self.ui.close_2.raise_())
        self.ui.panel_2o.clicked.connect(lambda: self.ui.close_2.lower())

        self.ui.panel_3c.clicked.connect(lambda: self.ui.close_3.raise_())
        self.ui.panel_3o.clicked.connect(lambda: self.ui.close_3.lower())

        self.ui.panel_4c.clicked.connect(lambda: self.ui.close_4.raise_())
        self.ui.panel_4o.clicked.connect(lambda: self.ui.close_4.lower())

        self.ui.panel_5c.clicked.connect(lambda: self.ui.close_5.raise_())
        self.ui.panel_5o.clicked.connect(lambda: self.ui.close_5.lower())

        self.ui.panel_6c.clicked.connect(lambda: self.ui.close_6.raise_())
        self.ui.panel_6o.clicked.connect(lambda: self.ui.close_6.lower())

        self.ui.panel_7c.clicked.connect(lambda: self.ui.close_7.raise_())
        self.ui.panel_7o.clicked.connect(lambda: self.ui.close_7.lower())

        self.ui.panel_8c.clicked.connect(lambda: self.ui.close_8.raise_())
        self.ui.panel_8o.clicked.connect(lambda: self.ui.close_8.lower())

        self.ui.panel_9c.clicked.connect(lambda: self.ui.close_9.raise_())
        self.ui.panel_9o.clicked.connect(lambda: self.ui.close_9.lower())

        self.ui.panel_10c.clicked.connect(lambda: self.ui.close_10.raise_())
        self.ui.panel_10o.clicked.connect(lambda: self.ui.close_10.lower())




    def printprueba(sef):
       print("prueba")


########################################################################
## EXECUTE  APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ########################################################################
    ##
    ########################################################################
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

########################################################################
## END
###########