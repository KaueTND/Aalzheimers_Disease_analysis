#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 14:20:32 2019

@author: kduarte
"""

#This is responsible for Giving the view of each ADNI file
import sys
from pprint import pprint
from PyQt5.QtWidgets import (QWidget, QGridLayout, QPushButton, QApplication, QSizePolicy)
from PyQt5.QtGui import QIcon, QPixmap
from functools import partial
from PyQt5.Qt import Qt
import os
from glob import glob
from os import listdir
from os.path import isfile, join
import pandas as pd
import math
import numpy as np
import pickle
from operator import methodcaller, itemgetter



#put

       
############### PART 1: Grid Generator
def splitFile(path,slice):
    myFiles = glob(path+"/*png")
    #myFiles = os.listdir(path)
    myFiles = map(methodcaller("split", "_"), myFiles)
    for filex in myFiles:
        if(len(filex) > 6):    
            filex[-3] = int(filex[-3])
    x = sorted(myFiles, key=itemgetter(-3))
    x[slice][-3] = str(x[slice][-3])
    return(x[slice])
    

#print(newDf.loc[2]['002_S_0559'])

class ADNIViewer(QWidget):
    def __init__(self):
        global globalContScroll
        super(QWidget,self).__init__()
        grid_layout = QGridLayout()
        self.setLayout(grid_layout)
        positions = [(i,j) for i in range(4) for j in range(6)]
        #position of arrays in tuple
        pprint("position="+str(positions))
        for position in positions:
            print("position="+str(position))
            #print("value="+str(value))
            #if value == '':
            #    continue
            newFormattedPosition = str(position).replace('(','').replace(')','').replace(' ','')
            vecID = newFormattedPosition.split(',')
            currentPatient = subset.loc[int(vecID[0])][vecPatients[6*globalContScroll+int(vecID[1])]]
            
            
            
            button = QPushButton()
            button.setObjectName(newFormattedPosition)
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            currentPatient = 'asd.png' if isinstance(currentPatient,float) else currentPatient
            button.setStyleSheet("background-image: url('"+ currentPatient +"'); border: none;")
            button.clicked.connect(self.buttonClicked)
            grid_layout.addWidget(button,*position)
    
    def buttonClicked(self):
        sending_button = self.sender()
        
        vecID = str(sending_button.objectName()).split(',')#line = vecID[0], column = vecID[1]        
        chosenList[globalContScroll*6+int(vecID[1])] = newDf.loc[int(vecID[0])][vecPatients[6*globalContScroll+int(vecID[1])]]
        print(chosenList)
        
        
    #keyboard show new screen
    def keyPressEvent(self, event):
        global globalContScroll
        global globalContScrollMAX
        global grid_layout
        #with open('chosenList', 'wb') as f:
        #    pickle.dump(chosenList, f)
        print('key')
        if event.key() == Qt.Key_Right:
            globalContScroll = globalContScroll + 1
            print('go further to '+str(globalContScroll))
            
            if(globalContScrollMAX < globalContScroll):
                globalContScrollMax = globalContScroll
                np.save('dataViewer/globalContScroll.npy',globalContScrollMax)
                with open('dataViewer/chosenList_'+str(globalContScrollMax-1), 'wb') as f:
                    pickle.dump(chosenList, f)                    
            
        if event.key() == Qt.Key_Left:
            if(globalContScroll > 0):
                print('go back to')
                globalContScroll = globalContScroll - 1
                print('go back to '+str(globalContScroll))

        if event.key() == Qt.Key_Down:
            for i in reversed(range(grid_layout.count())): 
                grid_layout.itemAt(i).widget().setParent(None)    

                
        
        
       
if __name__ == '__main__':
    firstTime = False
    
    
    
    if(firstTime):

        
        paths = [x[0] for x in os.walk('PNG_ADNI')]#('ADNI_3_N')]
        myPatients = list()
        myDir = list()
        myNumbered = list()
        patientName = 'null'
        counter = 0
        slice = 80
        #creating List of Patients
        for path in paths:
            if (path.count('/') == 4):#last folder of the program
                #print(path)
                #take the id of the patient
                currentPatient = path.split('/')[1]
                #append the id of the patient to a vector
                myPatients.append(currentPatient)    
                #split the file in the correct path according to a defined slice
                myFile = splitFile(path,slice)
                myDir.append('_'.join(myFile))
                if(patientName == currentPatient):
                    myNumbered.append(counter)
                    counter = counter + 1
                else:
                    patientName = currentPatient
                    myNumbered.append(0)
                    counter=1
        
        df = pd.DataFrame({
                            "patient" : myPatients,
                            "dir" : myDir,
                            "line": myNumbered
                          })
        
        newDf = df.pivot(index='line', columns='patient', values='dir')
        vecPatients = newDf.columns.tolist()
        
        globalContScroll = 0
        globalContScrollMAX = 0
        chosenList = [None] * len(vecPatients)        
        subset = newDf.iloc[:,globalContScrollMAX*6:globalContScrollMAX*6+6]
        
        #### SAVES
        newDf.to_csv('dataViewer/dataframeSubjects.csv')        
        np.save('dataViewer/globalContScroll.npy',globalContScroll)        
    else:
        #### LOADS
        globalContScrollMAX = np.load('dataViewer/globalContScroll.npy')
        globalContScroll = globalContScrollMAX
        with open('dataViewer/chosenList_'+str(globalContScrollMAX-1), 'rb') as f:
           chosenList = pickle.load(f)                   

        newDf = pd.read_csv('dataViewer/dataframeSubjects.csv',index_col=0)

        vecPatients = newDf.columns.tolist()
        subset = newDf.iloc[:,globalContScrollMAX*6:globalContScrollMAX*6+6]
   
#    #Interface
    app = QApplication(sys.argv)
    pprint("input parameters="+str(sys.argv))
    adniViewer = ADNIViewer()
    adniViewer.show()