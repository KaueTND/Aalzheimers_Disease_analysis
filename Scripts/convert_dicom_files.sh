#! /bin/bash

for i in "${@}"; do
  find $i -name "*.dcm" -exec ./convert.sh {} ";"
done

