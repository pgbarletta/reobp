#!/bin/bash

pdb="eol"
k=0

for i in `cat lista`
do
    k=`expr $k + 1`
    ph=$(echo $i | cut -d ";" -f 1)
    phh=$(echo $i | cut -d ";" -f 2)
    
    # vol por pH
    mkdir ${phh}
    cd ${phh}
    echo ${phh}
    
    tail +35 ../../pca/${phh}/top_${pdb}_${phh}.pdb | head -n-99 > cut_top_${pdb}_${phh}.pdb 
    echo "END" >> cut_top_${pdb}_${phh}.pdb
    ANA2 cut_top_${pdb}_${phh}.pdb -n fix_cut_top_${pdb}_${phh}.pdb

    ANA2 fix_cut_top_${pdb}_${phh}.pdb -c ../plantillas/obp.cfg -M ../../pca/${phh}/modes_${pdb}_${phh} -Z 5 > flx_${pdb}_${phh}_5

    cd ..
done

exit 0
