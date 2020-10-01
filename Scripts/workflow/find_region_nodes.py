import nibabel as nib
import numpy as np
import scipy

f = open('../../whichFiles.txt','r')
all_subject_id = f.read()
all_subject_id = all_subject_id.split('\n')


regions = [0]

for subject_id in all_subject_id:
    print(subject_id)
    whereFileAre = '../../freesurfer/'+subject_id+'/mri/aparc.DKTatlas+aseg.mgz'
    n1_atlas = nib.load(whereFileAre) 
    n1_atlas = n1_atlas.get_data()
    regions_label = np.unique(n1_atlas.ravel())
    regions = np.append(regions,regions_label)
    #print(regions_label)  

scipy.io.savemat('../../all_regions_nodes.mat',dict(regions=np.unique(regions)[1:]))
