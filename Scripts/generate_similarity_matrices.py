#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 10:26:20 2020

@author: kduarte
"""

import matplotlib.pyplot as plt
import os
from scipy.io import loadmat, savemat
from matplotlib import cm
import numpy as np
import random
import glob
from sklearn.cluster import KMeans




allregions = loadmat('../all_regions_nodes.mat')['regions']
allregionssimilarity = []
fileID = open('../procedure_mat.txt','r');
dirinfo = fileID.read().split('\n')
path = os.getcwd()
path = path.split('/')[0:-1]
path = '/'.join(path)

for region in allregions.ravel():



    try:
    #    if region == 4:
            
        print(region)
        
        regionFileExtensionMAT = '*x'+str(region)+'.mat'
        regionFileExtensionSTL = '*x'+str(region)+'.stl'
           
        dirDescriptor = '../descriptor/'
        dirBrain = '../brain_region_mat/'
    
    
        subdirinfo = []#cell(length(dirinfo),1);% remove . and .. dirs
        pathToStructure = []#cell(length(dirinfo),1);
    #
        for K,thisdir in enumerate(dirinfo):
            #thisdir = dirinfo{K};
            searchDir = dirDescriptor+thisdir+'/'+regionFileExtensionMAT 
            subdirinfo.append(glob.glob(searchDir))
            op = subdirinfo[K]
            if len(op) >0:
                op = path+op[0][2:]
                pathToStructure.append(op)
            else:
                pathToStructure.append('/')
    
        workIDs = []
        followID = 1
        for K in range(len(pathToStructure)):
            if pathToStructure[K] != '/':
                workIDs.append(K)
                followID = followID+1
    
        sizeSihks = np.zeros(len(pathToStructure));
    
        final_stack_region = []
        for value in workIDs:
    
            #print(pathToStructure[value])
            descriptor = loadmat(pathToStructure[value])['descriptor']
            descriptor = descriptor[0,0]
            #print(descriptor['sihks'].shape)
            zscoredsihks = (descriptor['sihks']);
            
            if len(final_stack_region) != 0:
                final_stack_region = np.concatenate((final_stack_region,zscoredsihks))
            else:
                final_stack_region = zscoredsihks
            sizeSihks[value] = len(zscoredsihks);
    
        k=30
        kmeans = KMeans(n_clusters=k).fit(final_stack_region)
        idx = kmeans.predict(final_stack_region)
           
    
        accumulator=0
    #
        sihksResults = []
        histograms = []
    #    disp('Splitting vectors after kMeans');
    #% 
        for value in workIDs:
            #print(accumulator)
            resultx = idx[accumulator:int(sizeSihks[value])+accumulator]
            sihksResults.append(resultx)
            accumulator = int(accumulator + sizeSihks[value]);
    
        for i in range(len(workIDs)):
    
            H, bin_edges = np.histogram(sihksResults[i],k)
            histograms.append(H)
    
    # 
    # 
    # 
        similaritymatrix = np.zeros((len(dirinfo),len(dirinfo)))
    # 
        for i,wKi in enumerate(workIDs):
            for j,wKj in enumerate(workIDs):
                coef = np.corrcoef(histograms[wKi],histograms[wKj])
                similaritymatrix[wKi,wKj] = abs(coef[0,1])
    
        fileX = '../preliminary_results/simi_'+str(region)+'.mat';
        savemat(fileX,{'simi':similaritymatrix})
            
    except:
        print(str(region)+': something happened')