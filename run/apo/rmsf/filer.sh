#!/bin/bash

pdb="apo"
k=0
cpp_rmsf="rmsf_cpp"

for i in `cat lista`
do
    k=`expr $k + 1`
    ph=$(echo $i | cut -d ";" -f 1)
    phh=$(echo $i | cut -d ";" -f 2)
    
    # PCA por idx
#    mkdir ${k}
#    
#    sed s/30/${ph}/g plantillas/${cpp_rmsf} > ${k}/${cpp_rmsf}
#    sed -i s/apo_1/${pdb}_${k}/g ${k}/${cpp_rmsf}
#    sed -i s/apo/${pdb}/g ${k}/${cpp_rmsf}
#    sed -i "s/\/1\//\/${k}\//g" ${k}/${cpp_rmsf}
#
#    cd ${k}
#    cpptraj < ${cpp_pca}
#    cpptraj < ${cpp_fit}
#    cpptraj < ${cpp_rmsf}
#    cd ..

    # RMSF por pH
    mkdir ${phh}

    sed s/30/${phh}/g plantillas/${cpp_rmsf} > ${phh}/${cpp_rmsf}
    sed -i s/apo_1/${pdb}_${phh}/g ${phh}/${cpp_rmsf}
    sed -i s/apo/${pdb}/g ${phh}/${cpp_rmsf}
    sed -i "s/\/1\//\/${phh}\//g" ${phh}/${cpp_rmsf}
    
    cd ${phh}
    cpptraj < ${cpp_rmsf}
    cd ..
done

exit 0
