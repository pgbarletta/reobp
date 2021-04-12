#!/bin/bash

for i in 1 3 4 5
do
    getEtot.sh step${i}.out > Etot_min_${i}
done

for i in 2 6 7 8 9
do
    perl process_mdout.perl step${i}.out
    
    mv summary.ETOT     ${i}_etot.dat
    mv summary.EPTOT    ${i}_eptot.dat
    mv summary.EKTOT    ${i}_ektot.dat
    mv summary.TEMP     ${i}_temp.dat
    mv summary.PRES     ${i}_pres.dat
    mv summary.VOLUME   ${i}_vol.dat
    mv summary.DENSITY  ${i}_density.dat
    
    rm summary*
done

perl process_mdout.perl final.1.out

mv summary.ETOT     equ_etot.dat
mv summary.EPTOT    equ_eptot.dat
mv summary.EKTOT    equ_ektot.dat
mv summary.TEMP     equ_temp.dat
mv summary.PRES     equ_pres.dat
mv summary.VOLUME   equ_vol.dat
mv summary.DENSITY  equ_density.dat

rm summary*

exit 0
