#! /bin/bash

for source_dcm in $(cat run_failed1.txt); do
	subject_id=${source_dcm:5:10}
	qsub -N "S$subject_id" -S /bin/bash -cwd -j y Scripts/run_freesurfer_one_subject.sh "$source_dcm"
done;
