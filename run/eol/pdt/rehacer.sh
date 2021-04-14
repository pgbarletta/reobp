#!/bin/bash

# convierto los nombres de los archivos de Roitberg a mis nombres.
pdb1=apo
pdb2=eol
k=0

for PH in 2.0 2.5 3.0 3.5 4.0 4.5 5.0 5.5 6.0 6.5 7.0 7.5
do
    k=`expr $k + 1`

    sed s/3.0/${PH}/g plantillas/strip_cpp > ${PH}/strip_cpp
    sed -i s/${pdb1}_1/${pdb2}_${k}/g ${PH}/strip_cpp
    sed -i s/${pdb1}/${pdb2}/g ${PH}/strip_cpp

    cd ${PH}
    
    mv pdt.in.${PH} ${PH}pdt.in
    mv cpout.${PH} ${PH}cpout_p1_${pdb1}
    mv cprestrt.${PH} ${PH}cprst_p1_${pdb1}.rst7
    mv mdcrd.${PH}.nc ${PH}p1_${pdb1}.nc
    mv mdout.${PH} ${PH}pdt1.out
    mv rst.rst7 ${PH}p1_${pdb1}.rst7
    cpptraj < strip_cpp
    cd ..
done

