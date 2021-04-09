#!/bin/bash

pdb="ctv"
k=0
cpp_pca="pca_cpp"
cpp_fit="fit_avg_cpp"
cpp_rms="rms_cpp"

for i in `cat lista`
do
    k=`expr $k + 1`
    ph=$(echo $i | cut -d ";" -f 1)
    phh=$(echo $i | cut -d ";" -f 2)
    
    # PCA por idx
#    mkdir ${k}
#    sed s/3.0/${phh}/g plantillas/${cpp_pca} > ${k}/${cpp_pca}
#    sed -i s/apo_1/${pdb}_${k}/g ${k}/${cpp_pca}
#    sed -i s/apo/${pdb}/g ${k}/${cpp_pca}
#
#    sed s/3.0/${phh}/g plantillas/${cpp_fit} > ${k}/${cpp_fit}
#    sed -i s/apo_1/${pdb}_${k}/g ${k}/${cpp_fit}
#    sed -i s/apo/${pdb}/g ${k}/${cpp_fit}
#
#    sed s/3.0/${phh}/g plantillas/${cpp_rms} > ${k}/${cpp_rms}
#    sed -i s/apo_1/${pdb}_${k}/g ${k}/${cpp_rms}
#    sed -i s/apo/${pdb}/g ${k}/${cpp_rms}
#
#    cd ${k}
#    cpptraj < ${cpp_pca}
#    cpptraj < ${cpp_fit}
#    cpptraj < ${cpp_rms}
#    cd ..

    # PCA por pH
    mkdir ${phh}
    sed s/3.0/${phh}/g plantillas/${cpp_pca} > ${phh}/${cpp_pca}
    sed -i s/apo_1/${pdb}_${phh}/g ${phh}/${cpp_pca}
    sed -i s/apo/${pdb}/g ${phh}/${cpp_pca}
    sed -i s/pdt/all_pdt/g ${phh}/${cpp_pca}

    sed s/3.0/${phh}/g plantillas/${cpp_fit} > ${phh}/${cpp_fit}
    sed -i s/apo_1/${pdb}_${phh}/g ${phh}/${cpp_fit}
    sed -i s/apo/${pdb}/g ${phh}/${cpp_fit}
    sed -i s/pdt/all_pdt/g ${phh}/${cpp_fit}

    sed s/3.0/${phh}/g plantillas/${cpp_rms} > ${phh}/${cpp_rms}
    sed -i s/apo_1/${pdb}_${phh}/g ${phh}/${cpp_rms}
    sed -i s/apo/${pdb}/g ${phh}/${cpp_rms}
    sed -i s/pdt/all_pdt/g ${phh}/${cpp_rms}

    cd ${phh}
    cpptraj < ${cpp_pca}
    cpptraj < ${cpp_fit}
    cpptraj < ${cpp_rms}
    cd ..
done

exit 0
