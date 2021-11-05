# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 15:09:13 2021

@author: Carlos Mateo Jurado Díaz
"""

from PyQt5 import QtWidgets, uic
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.qt_compat import QtWidgets as pltQtWidgets

class MAINWINDOW(QtWidgets.QMainWindow):
    
    """
    The .ui file is imported and the necessary variables
    to read and graph the data are created
    """
    
    def __init__(self):
        super(MAINWINDOW, self).__init__()
        uic.loadUi('View.ui', self)
        self.psoc=0
        self.ECG=0
        self.timer=0
        self.data=0
        self.graph = pltQtWidgets.QVBoxLayout(self.graphicsView)
        
def GRAPH(x,y,layout):
    
    """
    The data is plotted in the layout
    
    input variables :
        x : time vector 
        y : data read 
        layout : QVBoxLayout where the data is plotted 
    """
    
    CLEARLAYOUT(layout)
    canvas = FigureCanvas(Figure())
    layout.addWidget(canvas)
    axes = canvas.figure.subplots()        
    axes.plot(x,y)
    axes.set_xlabel("Time (s)")
    axes.set_ylabel("Amplitude")
    axes.set_title("Amplitude Vs Time")  
    
def CLEARLAYOUT(layout):
    
    """
    The layout is cleaned 
    
    input variables :
        layout : QVBoxLayout where the data is plotted 
    """
    
    for i in reversed(range(layout.count())):
        layoutItem = layout.itemAt(i)
        if layoutItem.widget() is not None:
            widgetToRemove = layoutItem.widget()
            widgetToRemove.setParent(None)
            layout.removeWidget(widgetToRemove)
        else:
            layoutToRemove = layout.itemAt(i)
            CLEARLAYOUT(layoutToRemove)