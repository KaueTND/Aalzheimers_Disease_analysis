#! /bin/bash

export FREESURFER_HOME=/global/software/freesurfer/
source $FREESURFER_HOME/SetUpFreeSurfer.sh

source_dcm="${1}"
freesurfer_command="recon-all.v6.hires -conf2hires"
subjects_dir=/Volumes/CipacProcessing/Projects/RF_KaueAlzheimers/freesurfer
subject_id=${source_dcm:5:10}

${freesurfer_command} -sd "${subjects_dir}" -s "${subject_id}" -i "$source_dcm" -all
