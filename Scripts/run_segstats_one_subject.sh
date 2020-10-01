#! /bin/bash

export FREESURFER_HOME=/global/software/freesurfer/
source $FREESURFER_HOME/SetUpFreeSurfer.sh

subjects_dir=/Volumes/CipacProcessing/Projects/RF_KaueAlzheimers/freesurfer
subject_id=${1}
lut=${FREESURFER_HOME}/SurfaceLUT.txt

mri_segstats --seg ${subjects_dir}/${subject_id}/mri/aparc.DKTatlas+aseg.mgz --i ${subjects_dir}/${subject_id}/mri/orig.mgz --mask ${subjects_dir}/${subject_id}/mri/brainmask.mgz --sum ${subjects_dir}/${subject_id}/stats/DKTAtlas.stats --ctab ${lut}
