#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 11:33:42 2020

@author: kduarte
"""

import matplotlib.pyplot as plt
import os
from scipy.io import loadmat
from matplotlib import cm
import numpy as np
import random
namesDict = {
'2':  ' Left-Cerebral-White-Matter            ', 
'3':  ' Left-Cerebral-Cortex                  ', 
'4':  ' Left-Lateral-Ventricle                ', 
'5':  ' Left-Inf-Lat-Vent                     ', 
'6':  ' Left-Cerebellum-Exterior              ', 
'7':  ' Left-Cerebellum-White-Matter          ', 
'8':  ' Left-Cerebellum-Cortex                ', 
'9':  ' Left-Thalamus                         ', 
'10': ' Left-Thalamus-Proper                  ', 
'11': ' Left-Caudate                          ', 
'12': ' Left-Putamen                          ', 
'13': ' Left-Pallidum                         ', 
'14': ' 3rd-Ventricle                         ', 
'15': ' 4th-Ventricle                         ', 
'16': ' Brain-Stem                            ', 
'17': ' Left-Hippocampus                      ', 
'18': ' Left-Amygdala                         ', 
'19': ' Left-Insula                           ', 
'20': ' Left-Operculum                        ', 
'21': ' Line-1                                ', 
'22': ' Line-2                                ', 
'23': ' Line-3                                ', 
'24': ' CSF                                   ', 
'25': ' Left-Lesion                           ', 
'26': ' Left-Accumbens-area                   ', 
'27': ' Left-Substancia-Nigra                 ', 
'28': ' Left-VentralDC                        ', 
'29': ' Left-undetermined                     ', 
'30': ' Left-vessel                           ', 
'31': ' Left-choroid-plexus                   ', 
'32': ' Left-F3orb                            ', 
'33': ' Left-lOg                              ', 
'34': ' Left-aOg                              ', 
'35': ' Left-mOg                              ', 
'36': ' Left-pOg                              ', 
'37': ' Left-Stellate                         ', 
'38': ' Left-Porg                             ', 
'39': ' Left-Aorg                             ', 
'40': ' Right-Cerebral-Exterior               ', 
'41': ' Right-Cerebral-White-Matter           ', 
'42': ' Right-Cerebral-Cortex                 ', 
'43': ' Right-Lateral-Ventricle               ', 
'44': ' Right-Inf-Lat-Vent                    ', 
'45': ' Right-Cerebellum-Exterior             ', 
'46': ' Right-Cerebellum-White-Matter         ', 
'47': ' Right-Cerebellum-Cortex               ', 
'48': ' Right-Thalamus                        ', 
'49': ' Right-Thalamus-Proper                 ', 
'50': ' Right-Caudate                         ', 
'51': ' Right-Putamen                         ', 
'52': ' Right-Pallidum                        ', 
'53': ' Right-Hippocampus                     ', 
'54': ' Right-Amygdala                        ', 
'55': ' Right-Insula                          ', 
'56': ' Right-Operculum                       ', 
'57': ' Right-Lesion                          ', 
'58': ' Right-Accumbens-area                  ', 
'59': ' Right-Substancia-Nigra                ', 
'60': ' Right-VentralDC                       ', 
'61': ' Right-undetermined                    ', 
'62': ' Right-vessel                          ', 
'63': ' Right-choroid-plexus                  ', 
'64': ' Right-F3orb                           ', 
'65': ' Right-lOg                             ', 
'66': ' Right-aOg                             ', 
'67': ' Right-mOg                             ', 
'68': ' Right-pOg                             ', 
'69': ' Right-Stellate                        ', 
'70': ' Right-Porg                            ', 
'71': ' Right-Aorg                            ', 
'72': ' 5th-Ventricle                         ', 
'73': ' Left-Interior                         ', 
'74': ' Right-Interior                        ', 
'77': ' WM-hypointensities                    ', 
'78': ' Left-WM-hypointensities               ', 
'79': ' Right-WM-hypointensities              ', 
'80': ' non-WM-hypointensities                ', 
'81': ' Left-non-WM-hypointensities           ', 
'82': ' Right-non-WM-hypointensities          ', 
'83': ' Left-F1                               ', 
'84': ' Right-F1                              ', 
'85': ' Optic-Chiasm                          ', 
'192':' Corpus_Callosum                       ', 
'86': ' Left_future_WMSA                      ', 
'87': ' Right_future_WMSA                     ', 
'88': ' future_WMSA                           ', 
'96': ' Left-Amygdala-Anterior                ', 
'97': ' Right-Amygdala-Anterior               ', 
'98': ' Dura                                  ', 
'100':' Left-wm-intensity-abnormality         ', 
'101':' Left-caudate-intensity-abnormality    ', 
'102':' Left-putamen-intensity-abnormality    ', 
'103':' Left-accumbens-intensity-abnormality  ', 
'104':' Left-pallidum-intensity-abnormality   ', 
'105':' Left-amygdala-intensity-abnormality   ', 
'106':' Left-hippocampus-intensity-abnormalit ', 
'107':' Left-thalamus-intensity-abnormality   ', 
'108':' Left-VDC-intensity-abnormality        ', 
'109':' Right-wm-intensity-abnormality        ', 
'110':' Right-caudate-intensity-abnormality   ', 
'111':' Right-putamen-intensity-abnormality   ', 
'112':' Right-accumbens-intensity-abnormality ', 
'113':' Right-pallidum-intensity-abnormality  ', 
'114':' Right-amygdala-intensity-abnormality  ', 
'115':' Right-hippocampus-intensity-abnormali ',
'116':' Right-thalamus-intensity-abnormality  ', 
'117':' Right-VDC-intensity-abnormality       ', 
'118':' Epidermis                             ', 
'119':' Conn-Tissue                           ', 
'120':' SC-Fat-Muscle                         ', 
'121':' Cranium                               ', 
'122':' CSF-SA                                ', 
'123':' Muscle                                ', 
'124':' Ear                                   ', 
'125':' Adipose                               ', 
'126':' Spinal-Cord                           ', 
'127':' Soft-Tissue                           ', 
'128':' Nerve                                 ', 
'129':' Bone                                  ', 
'130':' Air                                   ', 
'131':' Orbital-Fat                           ', 
'132':' Tongue                                ', 
'133':' Nasal-Structures                      ', 
'134':' Globe                                 ', 
'135':' Teeth                                 ', 
'136':' Left-Caudate-Putamen                  ', 
'137':' Right-Caudate-Putamen                 ', 
'138':' Left-Claustrum                        ', 
'139':' Right-Claustrum                       ', 
'140':' Cornea                                ', 
'142':' Diploe                                ', 
'143':' Vitreous-Humor                        ', 
'144':' Lens                                  ', 
'145':' Aqueous-Humor                         ', 
'146':' Outer-Table                           ', 
'147':' Inner-Table                           ', 
'148':' Periosteum                            ', 
'149':' Endosteum                             ', 
'150':' R-C-S                                 ', 
'151':' Iris                                  ', 
'152':' SC-Adipose-Muscle                     ', 
'153':' SC-Tissue                             ', 
'154':' Orbital-Adipose                       ', 
'155':' Left-IntCapsule-Ant                   ', 
'156':' Right-IntCapsule-Ant                  ', 
'157':' Left-IntCapsule-Pos                   ', 
'158':' Right-IntCapsule-Pos                  ', 
'159':' Left-Cerebral-WM-unmyelinated         ', 
'160':' Right-Cerebral-WM-unmyelinated        ', 
'161':' Left-Cerebral-WM-myelinated           ', 
'162':' Right-Cerebral-WM-myelinated          ', 
'163':' Left-Subcortical-Gray-Matter          ', 
'164':' Right-Subcortical-Gray-Matter         ', 
'165':' Skull                                 ', 
'166':' Posterior-fossa                       ', 
'167':' Scalp                                 ', 
'168':' Hematoma                              ', 
'169':' Left-Basal-Ganglia                    ', 
'176':' Right-Basal-Ganglia                   ', 
'170':' brainstem                             ', 
'171':' DCG                                   ', 
'172':' Vermis                                ', 
'173':' Midbrain                              ', 
'174':' Pons                                  ', 
'175':' Medulla                               ', 
'180':' Left-Cortical-Dysplasia               ', 
'181':' Right-Cortical-Dysplasia              ', 
'193':' Left-hippocampal_fissure              ', 
'194':' Left-CADG-head                        ', 
'195':' Left-subiculum                        ', 
'196':' Left-fimbria                          ', 
'197':' Right-hippocampal_fissure             ', 
'198':' Right-CADG-head                       ', 
'199':' Right-subiculum                       ', 
'200':' Right-fimbria                         ', 
'201':' alveus                                ', 
'202':' perforant_pathway                     ', 
'203':' parasubiculum                         ', 
'204':' presubiculum                          ', 
'205':' subiculum                             ', 
'206':' CA1                                   ', 
'207':' CA2                                   ', 
'208':' CA3                                   ', 
'209':' CA4                                   ', 
'210':' GC-ML-DG                              ', 
'211':' HATA                                  ', 
'212':' fimbria                               ', 
'213':' lateral_ventricle                     ', 
'214':' molecular_layer_HP                    ', 
'215':' hippocampal_fissure                   ', 
'216':' entorhinal_cortex                     ', 
'217':' molecular_layer_subiculum             ', 
'218':' Amygdala                              ', 
'219':' Cerebral_White_Matter                 ', 
'220':' Cerebral_Cortex                       ', 
'221':' Inf_Lat_Vent                          ', 
'222':' Perirhinal                            ', 
'223':' Cerebral_White_Matter_Edge            ', 
'224':' Background                            ', 
'225':' Ectorhinal                            ', 
'226':' HP_tail                               ', 
'250':' Fornix                                ', 
'251':' CC_Posterior                          ', 
'252':' CC_Mid_Posterior                      ', 
'253':' CC_Central                            ', 
'254':' CC_Mid_Anterior                       ', 
'255':' CC_Anterior                           ', 
'256':' Voxel-Unchanged                       ',
'1000':    'ctx-lh-unknown                    ', 
'1001':    'ctx-lh-bankssts                   ', 
'1002':    'ctx-lh-caudalanteriorcingulate    ', 
'1003':    'ctx-lh-caudalmiddlefrontal        ', 
'1004':    'ctx-lh-corpuscallosum             ', 
'1005':    'ctx-lh-cuneus                     ', 
'1006':    'ctx-lh-entorhinal                 ', 
'1007':    'ctx-lh-fusiform                   ', 
'1008':    'ctx-lh-inferiorparietal           ', 
'1009':    'ctx-lh-inferiortemporal           ', 
'1010':    'ctx-lh-isthmuscingulate           ', 
'1011':    'ctx-lh-lateraloccipital           ', 
'1012':    'ctx-lh-lateralorbitofrontal       ', 
'1013':    'ctx-lh-lingual                    ', 
'1014':    'ctx-lh-medialorbitofrontal        ', 
'1015':    'ctx-lh-middletemporal             ', 
'1016':    'ctx-lh-parahippocampal            ', 
'1017':    'ctx-lh-paracentral                ', 
'1018':    'ctx-lh-parsopercularis            ', 
'1019':    'ctx-lh-parsorbitalis              ', 
'1020':    'ctx-lh-parstriangularis           ', 
'1021':    'ctx-lh-pericalcarine              ', 
'1022':    'ctx-lh-postcentral                ', 
'1023':    'ctx-lh-posteriorcingulate         ', 
'1024':    'ctx-lh-precentral                 ', 
'1025':    'ctx-lh-precuneus                  ', 
'1026':    'ctx-lh-rostralanteriorcingulate   ', 
'1027':    'ctx-lh-rostralmiddlefrontal       ', 
'1028':    'ctx-lh-superiorfrontal            ', 
'1029':    'ctx-lh-superiorparietal           ', 
'1030':    'ctx-lh-superiortemporal           ', 
'1031':    'ctx-lh-supramarginal              ', 
'1032':    'ctx-lh-frontalpole                ', 
'1033':    'ctx-lh-temporalpole               ', 
'1034':    'ctx-lh-transversetemporal         ', 
'1035':    'ctx-lh-insula                     ', 
'2000':    'ctx-rh-unknown                    ', 
'2001':    'ctx-rh-bankssts                   ', 
'2002':    'ctx-rh-caudalanteriorcingulate    ', 
'2003':    'ctx-rh-caudalmiddlefrontal        ', 
'2004':    'ctx-rh-corpuscallosum             ', 
'2005':    'ctx-rh-cuneus                     ', 
'2006':    'ctx-rh-entorhinal                 ', 
'2007':    'ctx-rh-fusiform                   ', 
'2008':    'ctx-rh-inferiorparietal           ', 
'2009':    'ctx-rh-inferiortemporal           ', 
'2010':    'ctx-rh-isthmuscingulate           ', 
'2011':    'ctx-rh-lateraloccipital           ', 
'2012':    'ctx-rh-lateralorbitofrontal       ', 
'2013':    'ctx-rh-lingual                    ', 
'2014':    'ctx-rh-medialorbitofrontal        ', 
'2015':    'ctx-rh-middletemporal             ', 
'2016':    'ctx-rh-parahippocampal            ', 
'2017':    'ctx-rh-paracentral                ', 
'2018':    'ctx-rh-parsopercularis            ', 
'2019':    'ctx-rh-parsorbitalis              ', 
'2020':    'ctx-rh-parstriangularis           ', 
'2021':    'ctx-rh-pericalcarine              ', 
'2022':    'ctx-rh-postcentral                ', 
'2023':    'ctx-rh-posteriorcingulate         ', 
'2024':    'ctx-rh-precentral                 ', 
'2025':    'ctx-rh-precuneus                  ', 
'2026':    'ctx-rh-rostralanteriorcingulate   ', 
'2027':    'ctx-rh-rostralmiddlefrontal       ', 
'2028':    'ctx-rh-superiorfrontal            ', 
'2029':    'ctx-rh-superiorparietal           ', 
'2030':    'ctx-rh-superiortemporal           ', 
'2031':    'ctx-rh-supramarginal              ', 
'2032':    'ctx-rh-frontalpole                ', 
'2033':    'ctx-rh-temporalpole               ', 
'2034':    'ctx-rh-transversetemporal         ', 
'2035':    'ctx-rh-insula                     ', 
}

def covar(x,y):
    newX = x-np.mean(x)
    newY = y-np.mean(y)
    newXnewY = newX*newY
    return np.sum(newXnewY)/(len(newX)-1)


def check_fill_zeros_vector(vector,size=30):
    if len(vector) == 0:
        return np.zeros(size,dtype=int)
    else:
        return vector

def main(choiceResults):
    
    if choiceResults in [1,2,3]:
        
        path = [x[0] for x in os.walk('preliminary_results/')]
        
        fileNames = x[2]
        
        matSimilarity = []
        regionId = []
        randomList = []
        matAverage = np.zeros([25,25])
        
        for i in fileNames:
            regionId.append(i.split('_')[1].split('.')[0])
            matSimilarity.append(loadmat(x[0]+i)['simi'])
        
        
        cmap = cm.get_cmap('coolwarm')
        
        #what kind of flow you want (1) - region per region, (2) - average of all regions, (3) - sample of the lists
        choiceResults = 1
        
        for i in range(0,108):
            randomList.append(random.sample(regionId,20))
            
        
        for i in range(len(matSimilarity)):
            np.fill_diagonal(matSimilarity[i],0)
            #print(matSimilarity[i])
            for j in range(5):
                for k in range(5):
                    if j == k:
                        lo = np.sum(matSimilarity[i][j*5:j*5+5,k*5:k*5+5])
                        matSimilarity[i][j*5:j*5+5,k*5:k*5+5] = np.ones((5,5))*lo/20
                    else:
                        matSimilarity[i][j*5:j*5+5,k*5:k*5+5] = np.ones((5,5))*np.mean(matSimilarity[i][j*5:j*5+5,k*5:k*5+5])
        
        
        
        
        
        
        if choiceResults == 1:
            fig, axs = plt.subplots(6, 18)
            for i in range(len(matSimilarity)):        
                axs[i//18,i%18 ].imshow(matSimilarity[i],cmap=cmap,vmin=0,vmax=1)
                axs[i//18,i%18 ].set_title(namesDict[str(regionId[i])][0:11])
                #axs[i//18,i%18 ].set_title(str(regionId[i]))
                axs[i//18,i%18 ].axis('off')
            
            axs[5,17 ].axis('off')
            axs[5,16 ].axis('off')
        elif choiceResults == 2:
            for mat in matSimilarity:
                matAverage = matAverage + mat
            matAverage = matAverage /len(matSimilarity)
            plt.figure(1)
            plt.imshow(matAverage,cmap=cmap)
            plt.axis('off')
        elif choiceResults == 3:
            fig, axs = plt.subplots(6, 18)
            for i in range(108):
                newMat = np.zeros([25,25])
                for calculaI in randomList[i]:
                    index = regionId.index(calculaI)
                    newMat = newMat + matSimilarity[index]
                    #xxxxx = randomList[0]
                    #print(regionId.index(xxxxx[0]))            
                newMat = newMat/20    
                    
                axs[i//18,i%18 ].imshow(newMat,cmap=cmap)
                axs[i//18,i%18 ].set_title('Set '+str(i))
                axs[i//18,i%18 ].axis('off')
        
    elif choiceResults == 4:
        print(covar([2,3,4,5,7],[1,3,4,8,9]))
        
    elif choiceResults == 5:
        print('oi')
#main(5)

path = [x[0] for x in os.walk('histogram/')]        
fileNames = x[2]

histogram = []
regionId = []
randomList = []
matSimilarity = []
matAverage = np.zeros([500,500])
cmap = cm.get_cmap('coolwarm')

for i in fileNames:
    regionId.append(i.split('_')[1].split('.')[0])
    histogram.append(loadmat(x[0]+i)['histograms'])
            #print(histogram)
            
            
for i in range(len(histogram)):
    perregion = histogram[i]
    print(i)
    matAux = np.zeros([500,500])
    for pat1Ix in range(len(perregion)):
        for pat2Ix in range(pat1Ix,len(perregion)):
            pat1 = check_fill_zeros_vector(perregion[pat1Ix,0].ravel())
            pat2 = check_fill_zeros_vector(perregion[pat2Ix,0].ravel())
            matAux[pat1Ix,pat2Ix] = matAux[pat2Ix,pat1Ix] = abs(covar(pat1,pat2)) 
    matSimilarity.append(matAux)
    #break;        

#for i in range(len(matSimilarity)):
#    np.fill_diagonal(matSimilarity[i],0)
#    for j in range(5):
#        for k in range(5):
#            if j == k:1454788-
#                lo = np.sum(matSimilarity[i][j*100:j*100+100,k*100:k*100+100])
#                matSimilarity[i][j*100:j*100+100,k*100:k*100+100] = np.ones((100,100))*lo/9900
#            else:
#                matSimilarity[i][j*100:j*100+100,k*100:k*100+100] = np.ones((100,100))*np.mean(matSimilarity[i][j*100:j*100+100,k*100:k*100+100])    

fig, axs = plt.subplots(6, 18)
for i in range(len(matSimilarity)):        
    axs[i//18,i%18 ].imshow(matSimilarity[i],cmap=cmap)
    axs[i//18,i%18 ].set_title(namesDict[str(regionId[i])][0:11])
    #axs[i//18,i%18 ].set_title(str(regionId[i]))
    axs[i//18,i%18 ].axis('off')

