#!/bin/bash

# ./AmberMdPrep.sh -p ../../../top_files/apo.prmtop -c apo.rst7 --temp 300  --mask :120 --skipfinaleq
pmemd.cuda -O -i final.1.in -o final.1.out -p ../../../top_files/apo.prmtop -c step9.rst7 -r eapo.rst7 -x eapo.nc

exit 0
