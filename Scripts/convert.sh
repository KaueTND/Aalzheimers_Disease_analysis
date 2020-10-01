#! /bin/bash

#convert -normalize -contrast-stretch 0 "${1}" "PNG_${1%%.dcm}.png"
convert -define dcm:display-range=reset "${1}" -normalize "PNG_${1%%.dcm}.png"
