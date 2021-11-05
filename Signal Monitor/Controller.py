# -*- coding: utf-8 -*-
"""
Created on Mon Jan 9 15:09:13 2021

@author: Carlos Mateo Jurado Díaz
"""

from PyQt5 import QtWidgets, QtCore
import numpy as np
import serial
import sys

from View import MAINWINDOW
from Model import ACQUIRE_SIGNAL
        
app = QtWidgets.QApplication(sys.argv)
main = MAINWINDOW()
main.show()

def START():
    
    """
    Serial communication starts and a QTimer is created
    to read and graph the data every 300ms 
    """
    
    main.psoc = serial.Serial('COM3', 9600, timeout = 1)
    main.ECG = np.ndarray((0),dtype=np.int);
    main.timer = QtCore.QTimer()
    main.timer.timeout.connect(ADD_SIGNAL)
    main.timer.start(300)
    
def STOP():
    
    """
    Serial communication and timer is stopped
    """
    
    main.timer.stop()
    main.psoc.close()
    
def ADD_SIGNAL():
    
    """
    Function used by the QTimer in the START() function 
    """
    
    ACQUIRE_SIGNAL(main)
            
main.pushButton.clicked.connect(START)
main.pushButton_2.clicked.connect(STOP)

sys.exit(app.exec_())