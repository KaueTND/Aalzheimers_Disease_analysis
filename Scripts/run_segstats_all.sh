#! /bin/bash

for subject_id in $(cat subjects_for_stats.txt); do
	qsub -N "S$subject_id" -S /bin/bash -cwd -j y Scripts/run_segstats_one_subject.sh $subject_id
done
