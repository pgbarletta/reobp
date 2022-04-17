#!/bin/bash

pdb="ctv"
k=0
cpp_script="volmap_cpp"

for i in `cat lista`
do
    k=`expr $k + 1`
    ph=$(echo $i | cut -d ";" -f 1)
    phh=$(echo $i | cut -d ";" -f 2)
    
    mkdir ${phh}
    sed s/3.0/${phh}/g plantillas/${cpp_script} > ${phh}/${cpp_script}

    cd ${phh}
    cpptraj < ${cpp_script}
    cd ..
done

exit 0
