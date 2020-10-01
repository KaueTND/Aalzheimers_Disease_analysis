#! /bin/bash

for i in *.o*; do echo -n $i ": " ; tail -1 $i; done > file_tail.txt
