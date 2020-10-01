#! /bin/bash
#setting up the labels of the process
#$(python Scripts/workflow/find_region_nodes.py)

#processing the entire workflow
for subject_id in $(cat final_test_100_patients_per_class.txt); do
	qsub -N "S$subject_id" -S /bin/bash -cwd -j y Scripts/matrix_generation_one_subject.sh "$subject_id"
	#Scripts/matrix_generation_one_subject.sh "$subject_id" > "S$subject_id".txt
done;
