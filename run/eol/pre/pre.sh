#!/bin/bash

./AmberMdPrep.sh -p ../../../top_files/eol.prmtop -c eol.rst7 --temp 300  --mask :120 --skipfinaleq
pmemd.cuda -O -i final.1.in -o final.1.out -p ../../../top_files/eol.prmtop -c step9.rst7 -r eeol.rst7 -x eeol.nc

exit 0
