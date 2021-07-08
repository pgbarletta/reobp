#!/bin/bash

pdb1="apo"
pdb2="ctv"
k=0
cpp_1="cluster_idx_cpp"
cpp_2="cluster_ph_cpp"

for i in `cat lista`
do
    k=`expr $k + 1`
    ph=$(echo $i | cut -d ";" -f 1)
    phh=$(echo $i | cut -d ";" -f 2)
    
#    # Cluster por idx
#    mkdir ${k}
#    sed s/30/${ph}/g plantillas/${cpp_1} > ${k}/${cpp_1}
#    sed -i s/apo_1/${pdb}_${k}/g ${k}/${cpp_1}
#
#    cd ${k}
#    sed -i s/top_cluster/top_cluster_${k}/g ${cpp_1}
#    sed -i s/avg_cluster/avg_cluster_${k}/g ${cpp_1}
#    cpptraj < ${cpp_1}
#    cd ..

    # Cluster por pH
    mkdir ${phh}
    sed s/3\.0/${phh}/g plantillas/${cpp_2} > ${phh}/${cpp_2}
    sed -i s/${pdb1}/${pdb2}/g ${phh}/${cpp_2}
    sed -i s/top_cluster/top_cluster_${phh}/g ${phh}/${cpp_2}
    sed -i s/avg_cluster/avg_cluster_${phh}/g ${phh}/${cpp_2}

    cd ${phh}
    cpptraj < ${cpp_2}
    cd ..
done

exit 0
