#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 10:02:07 2020

@author: kduarte
"""
import sys
import numpy as np
import nibabel as nib
import scipy.io 
import vtk
from vtk.util import numpy_support
from scipy.io import loadmat
import os
import numpy

def vtkNumpyToImage(binaryVolume):
    vtk_image = vtk.vtkImageData()
    shape = binaryVolume.shape
    typeBinaryVolume = binaryVolume.dtype
    VTK_data = numpy_support.numpy_to_vtk(num_array=binaryVolume.ravel(), deep=True)    
    vtk_image.SetDimensions(shape[2],shape[1],shape[0])
    vtk_image.GetPointData().SetScalars(VTK_data)
    #print(vtk_image)
    return vtk_image

   
def refine_mesh(stlName):
    # The colors module defines various useful colors.

    # This creates a polygonal mesh from an STL
    stlReader = vtk.vtkSTLReader()
    stlReader.SetFileName('brain_region_mat/'+stlName+'_initial.stl')

    # remove holes from inside
    stlConnectivity = vtk.vtkConnectivityFilter()
    #stlConnectivity.SetInputConnection(stlReverse.GetOutputPort())
    stlConnectivity.SetInputConnection(stlReader.GetOutputPort())
    stlConnectivity.SetExtractionModeToLargestRegion()
    stlConnectivity.Update()
    
    smooth = vtk.vtkSmoothPolyDataFilter()
    smooth.SetInputConnection(stlConnectivity.GetOutputPort())
    smooth.SetRelaxationFactor(0.08)
    smooth.SetNumberOfIterations(40)
    smooth.Update()

    # write to a new STL file
    stlWriter = vtk.vtkSTLWriter()
    stlWriter.SetInputConnection(smooth.GetOutputPort())
    stlWriter.SetFileName('brain_region_mat/'+stlName+'.stl')
    stlWriter.Write()

def generate_mesh(stlName,binaryVolume):
    x = loadmat('brain_region_mat/'+stlName+'.mat')
    binaryVolume = x['n1_true']
    # one-liner to read a single variable
    vtk_image = vtkNumpyToImage(binaryVolume)
    dmc = vtk.vtkDiscreteMarchingCubes()
    #dmc.SetInputConnection(threshold.GetOutputPort())
    dmc.SetInputData(vtk_image)
    #print(threshold.GetOutputPort())
    dmc.GenerateValues(1, 1, 1)
    dmc.Update()
    writer = vtk.vtkSTLWriter()
    writer.SetInputConnection(dmc.GetOutputPort())
    writer.SetFileTypeToBinary()
    writer.SetFileName('brain_region_mat/'+stlName+"_initial.stl")
    writer.Write()




if __name__ == '__main__':
    #regions_label = np.load('list_of_labels.npy')
    #generate_adjacent_matrix(sys.argv[1],regions_label)
    subject_name = sys.argv[1]+'/'
    whereFileAre = 'freesurfer/'+subject_name+'mri/aparc.DKTatlas+aseg.mgz'
    n1_atlas = nib.load(whereFileAre) 
    n1_atlas = n1_atlas.get_data()
    regions_label = np.unique(n1_atlas.ravel())
    #print(regions_label.shape)    
    for i in regions_label:
        if(int(i) != 0):
            n1_true = n1_atlas == int(i)
    #        print(subject_name+sys.argv[1]+'x'+str(i))
            scipy.io.savemat('brain_region_mat/'+subject_name+sys.argv[1]+'x'+str(i)+'.mat',dict(n1_true=n1_true))        
            generate_mesh(subject_name+sys.argv[1]+'x'+str(i),n1_true)
            refine_mesh(subject_name+sys.argv[1]+'x'+str(i))
        
        
        
       # 

