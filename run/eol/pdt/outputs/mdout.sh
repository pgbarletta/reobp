#!/bin/bash

# Extract heat and equil mdout info

for PH in 2.0 2.5 3.0 3.5 4.0 4.5 5.0 5.5 6.0 6.5 7.0 7.5
do
    perl process_mdout.perl ${PH}pdt1.out
    
    mv summary.ETOT    ${PH}etot.dat
    mv summary.EPTOT   ${PH}eptot.dat
    mv summary.EKTOT   ${PH}ektot.dat
    mv summary.TEMP    ${PH}temp.dat
    mv summary.PRES    ${PH}pres.dat
    mv summary.VOLUME  ${PH}vol.dat
    mv summary.DENSITY ${PH}density.dat
    
    rm summary*
done

exit 0
