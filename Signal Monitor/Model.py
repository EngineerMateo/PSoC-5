# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 15:31:56 2021

@author: Carlos Mateo Jurado Díaz
"""

import numpy as np

from View import GRAPH
            
def ACQUIRE_SIGNAL(main):
    
        """
        Reading protocol, the values read from the UART
        are saved in main.ECG and the last 250 values are
        plotted in main.graph
        """
        
        main.data = main.psoc.read(main.psoc.inWaiting())
        main.data=str(main.data,"ascii")      
        readings=0
        values=np.zeros(1)
        a=0
        b=0
        c=0
        d=0
        cases=0
        x=0
        
        for datum in main.data:
            if datum == 'b':
                x = 1
            if cases == 1:
                a = float(datum)
            if cases == 2:
                b = float(datum)
            if cases == 3:
                c = float(datum)
            if cases == 4:
                d = float(datum)
            if x == 1:
                if datum == 'c':
                    readings+=1
                    values=np.append(values, 0)
                    value = a+0.1*b+0.01*c+0.001*d
                    values[readings]=value
                    a=0
                    b=0
                    c=0
                    d=0
                    cases=0
                    x=0
                if x == 1:
                    cases+=1
    
        values = values[1:readings]
        main.ECG = np.append(main.ECG, values) 
        t = np.linspace(0, 0.0118*len(main.ECG), len(main.ECG)) 
        GRAPH(t[-250:-1],main.ECG[-250:-1],main.graph)