#!/bin/bash

pdb="eol"
k=0

for i in `cat lista`
do
    k=`expr $k + 1`
    ph=$(echo $i | cut -d ";" -f 1)
    phh=$(echo $i | cut -d ";" -f 2)
    
    # vol por idx
    cd ${k}
    tail +35 ../../pca/${k}/top_${pdb}_${k}.pdb | head -n-99 > cut_top_${pdb}_${k}.pdb
    echo "END" >> cut_top_${pdb}_${k}.pdb
    ANA2 cut_top_${pdb}_${k}.pdb -n fix_cut_top_${pdb}_${k}.pdb
    ANA2 fix_cut_top_${pdb}_${k}.pdb -c ../plantillas/obp_ndd_2.cfg -M ../../pca/${k}/modes_${pdb}_${k} -O vgv_${pdb}_${k} -Z 5 
    ANA2 fix_cut_top_${pdb}_${k}.pdb -c ../plantillas/obp_ndd_3.cfg -M ../../pca/${k}/modes_${pdb}_${k} -Z 5 > flx_${pdb}_${k}
    cd ..

    # vol por pH
    cd ${ph}ph
    tail +35 ../../pca/${ph}ph/top_${pdb}_${ph}.pdb | head -n-99 > cut_top_${pdb}_${ph}.pdb
    echo "END" >> cut_top_${pdb}_${ph}.pdb
    ANA2 cut_top_${pdb}_${ph}.pdb -n fix_cut_top_${pdb}_${ph}.pdb
    ANA2 fix_cut_top_${pdb}_${ph}.pdb -c ../plantillas/obp_ndd_2.cfg -M ../../pca/${ph}ph/modes_${pdb}_${ph} -O vgv_${pdb}_${ph} -Z 5
    ANA2 fix_cut_top_${pdb}_${ph}.pdb -c ../plantillas/obp_ndd_3.cfg -M ../../pca/${ph}ph/modes_${pdb}_${ph} -Z 5 > flx_${pdb}_${ph}
    cd ..
done

exit 0
