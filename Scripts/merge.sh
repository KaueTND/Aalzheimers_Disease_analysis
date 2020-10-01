# merge downloads for ADNI data

# add subscripts to series folders according to which ADNI dir it is in
for j in 2 3 4 5 6 7 8 9 10; do for i in ADNI\ ${j}/*/*; do mv "${i}" "${i}_${j}"; done; done
# make all subject directories in the base ADNI folder
for j in 2 3 4 5 6 7 8 9 10; do for i in ADNI\ ${j}/*; do mkdir -p ADNI/$(basename "${i}"); done; done
# move all the data (now renamed) into the ADNI folder
for j in 2 3 4 5 6 7 8 9 10; do for i in ADNI\ ${j}/*; do mv "${i}"/* ADNI/$(basename "${i}"); done; done
