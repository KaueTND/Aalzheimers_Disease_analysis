#! /bin/bash

for i in "${@}"; do
  find $i -name "*.dcm" -exec dcmodify -nb -imt -g -e 5200,9230 -ep {} ";"
done

