# -*- coding: utf-8 -*-
# `nb_templater` generated Python script
# Generated from .ipynb template: eol_cluster.ipynb
# www.github.com/ismailuddin/jupyter-nb-templater/
# Generated on: 2020-11-10 14:22 

import nbformat as nbf 
import sys
nb = nbf.v4.new_notebook() 

cell_0=r"""
using DataFrames, FileIO, DelimitedFiles
using Plots, Optim, LsqFit, JUMD
using Statistics, NamedArrays
using Bio3DView, BioStructures
""".strip()

cell_1=r"""
# Get ready
dir_eol_clu = "/home/pbarletta/labo/20/cph_obp/run/eol/cluster"

nstlim = 12000
phs = collect(2.0:.5:7.5)
idx = collect(1:12)
titrable_cnt = 36
titrable_resis = [4, 5, 11, 13, 20, 24, 30, 33, 37, 39, 40,
    48, 58, 73, 77, 78, 87, 93, 94, 97, 117]
titrable_resnames = ["GL4", "GL4", "HIP", "GL4", "GL4", "AS4",
    "AS4", "GL4", "AS4", "GL4", "AS4", "GL4", "AS4", "GL4", "AS4",
    "GL4", "AS4", "GL4", "GL4", "HIP", "AS4"]
titrable_cnt = length(titrable_resis)
""".strip()

cell_2=r"""
### Orientar a las moléculas como está acá:
""".strip()

cell_3=r"""
![OBP](obp.png)
""".strip()

cell_4=r"""
## cluster por pH
""".strip()

nb['cells'] = [
    nbf.v4.new_code_cell(cell_0),
    nbf.v4.new_code_cell(cell_1),
    nbf.v4.new_markdown_cell(cell_2),
    nbf.v4.new_markdown_cell(cell_3),
    nbf.v4.new_markdown_cell(cell_4),
]

i = 0
for ph in range(20, 50, 5):
    PH = ph / 10
    i += 1
    celda_titulo=(r"""#### ph = """ + str(PH)).strip()
    celda_ph_1=(r"""viewstruc(read(joinpath(dir_eol_clu,  string(phs[""" + str(i) + r"""]), "top_cluster_""" + str(PH) + r""".c0.pdb"), PDB))""").strip()
    celda_ph_2=(r"""viewstruc(read(joinpath(dir_eol_clu,  string(phs[""" + str(i) + r"""]), "top_cluster_""" + str(PH) + r""".c1.pdb"), PDB))""").strip()
    celda_ph_3=(r"""viewstruc(read(joinpath(dir_eol_clu,  string(phs[""" + str(i) + r"""]), "top_cluster_""" + str(PH) + r""".c2.pdb"), PDB))""").strip()
    nb['cells'].append(nbf.v4.new_markdown_cell(celda_titulo))
    nb['cells'].append(nbf.v4.new_code_cell(celda_ph_1))
    nb['cells'].append(nbf.v4.new_code_cell(celda_ph_2))
    nb['cells'].append(nbf.v4.new_code_cell(celda_ph_3))


nb['metadata'] = {'kernelspec': {'display_name': 'Julia 1.5.0', 'language': 'julia', 'name': 'julia-1.5'}}


nbf.write(nb, r'/home/pbarletta/labo/20/cph_obp/src/informe_eol_cluster_phs_2a5.ipynb')
print(r"Jupyter notebook /home/pbarletta/labo/20/cph_obp/src/informe_eol_cluster_phs_2a5.ipynb successfully generated.")
