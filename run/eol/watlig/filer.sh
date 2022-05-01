#!/bin/bash

pdb="eol"
k=0
wat_pca="wat_cpp"

for i in `cat lista`
do
    k=`expr $k + 1`
    ph=$(echo $i | cut -d ";" -f 1)
    phh=$(echo $i | cut -d ";" -f 2)
    
    mkdir ${phh}
    sed s/3.0/${phh}/g plantillas/${wat_pca} > ${phh}/${wat_pca}

    cd ${phh}
    cpptraj < ${wat_pca}
    cd ..
done

exit 0
