#!/bin/bash

./AmberMdPrep.sh -p ../../../top_files/ctv.prmtop -c ctv.rst7 --temp 300  --mask :120 --skipfinaleq
pmemd.cuda -O -i final.1.in -o final.1.out -p ../../../top_files/ctv.prmtop -c step9.rst7 -r ectv.rst7 -x ectv.nc

exit 0
