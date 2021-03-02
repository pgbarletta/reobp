apo:
----
    pdb4amber -i 3S0A.pdb -o apo.pdb // *pdb4amber* conserva los CONECT de los
puentes disulfuro y a la vez le pone *CYX* a esas cysteínas, así q todo bien.

    Luego le hago lo siguiente a *apo.pdb*:
        borro las 1eras líneas de SMTRY
        %s/ASP/AS4/g
        %s/GLU/GL4/g
        %s/HIS/HIP/g
ctv:
----
    pdb4amber -i 3S0D.pdb -o ctv.pdb // *pdb4amber* conserva los CONECT de los
puentes disulfuro y a la vez le pone *CYX* a esas cysteínas, así q todo bien.

    Luego le hago lo siguiente a *ctv.pdb*:
        borro las 1eras líneas de SMTRY
        %s/ASP/AS4/g
        %s/GLU/GL4/g
        %s/HIS/HIP/g
          
eol:
----
    pdb4amber -i 3S0E.pdb -o eol.pdb // *pdb4amber* conserva los CONECT de los
puentes disulfuro y a la vez le pone *CYX* a esas cysteínas, así q todo bien.

    Luego le hago lo siguiente a *eol.pdb*:
        borro las 1eras líneas de SMTRY
        %s/ASP/AS4/g
        %s/GLU/GL4/g
        %s/HIS/HIP/g
          
