#!/bin/bash

pdb1=apo
pdb2=ctv

for PH in 2.0 2.5 3.0 3.5 4.0 4.5 5.0 5.5 6.0 6.5 7.0 7.5
do
    mkdir ${PH}

    sed "s/remdtrajvalues 3.0/remdtrajvalues ${PH}/g" plantillas/get_ph_cpp > ${PH}/get_ph_cpp
    sed -i "s/${pdb1}_3.0/${pdb2}_${PH}/g" ${PH}/get_ph_cpp
    sed -i "s/${pdb1}/${pdb2}/g" ${PH}/get_ph_cpp

    cd ${PH}
    cpptraj < get_ph_cpp
    cd ..

done
exit 0
