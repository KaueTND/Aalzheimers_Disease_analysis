#! /bin/bash

mkdir -p brain_region_mat/"${1}"
source Python/bin/activate
python Scripts/workflow/generate_brain_region_mat.py ${1}	
rm brain_region_mat/"${1}"/*.mat
rm brain_region_mat/"${1}"/*_initial.stl
mkdir -p eigs/"${1}"
mkdir -p descriptor/"${1}"
mkdir -p histogram/"${1}"
mkdir -p geometric_word/"${1}"
