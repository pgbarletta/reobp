# -*- coding: utf-8 -*-
# `nb_templater` generated Python script
# Generated from .ipynb template: ctv_cluster.ipynb
# www.github.com/ismailuddin/jupyter-nb-templater/
# Generated on: 2020-10-13 18:43 

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
dir_ctv_clu = "/home/pbarletta/labo/20/cph_obp/run/ctv/cluster"

nstlim = 19500
phs = collect(30:5:75)
idx = collect(1:10)
pdt_steps = collect(0:1:7)
titrable_cnt = 36
titrable_resis = [4, 5, 7, 11, 13, 18, 20, 24, 27, 30, 33, 37, 39,
    40, 41, 42, 48, 52, 58, 59, 64, 69, 73, 77, 78, 82, 87, 93, 94,
    97, 99, 102, 109, 111, 114, 117];
titrable_resnames = ["GL4", "GL4", "LYS", "HIP", "GL4", "LYS", "GL4", "AS4", "LYS",
    "AS4", "GL4", "AS4", "GL4", "AS4", "LYS", "LYS", "GL4", "LYS",
    "AS4", "LYS", "LYS", "LYS", "GL4", "AS4", "GL4", "LYS", "AS4",
    "GL4", "GL4", "HIP", "LYS", "LYS", "LYS", "LYS", "LYS", "AS4"];
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
for ph in range(30, 80, 5):
    i += 1
    celda_titulo=(r"""#### ph = """ + str(ph)).strip()
    celda_ph_1=(r"""viewstruc(read(joinpath(dir_ctv_clu,  string(phs[""" + str(i) + r"""], "ph"), "top_cluster.c0.pdb"), PDB))""").strip()
    celda_ph_2=(r"""viewstruc(read(joinpath(dir_ctv_clu,  string(phs[""" + str(i) + r"""], "ph"), "top_cluster.c1.pdb"), PDB))""").strip()
    celda_ph_3=(r"""viewstruc(read(joinpath(dir_ctv_clu,  string(phs[""" + str(i) + r"""], "ph"), "top_cluster.c2.pdb"), PDB))""").strip()
    nb['cells'].append(nbf.v4.new_markdown_cell(celda_titulo))
    nb['cells'].append(nbf.v4.new_code_cell(celda_ph_1))
    nb['cells'].append(nbf.v4.new_code_cell(celda_ph_2))
    nb['cells'].append(nbf.v4.new_code_cell(celda_ph_3))


nb['metadata'] = {'kernelspec': {'display_name': 'Julia 1.5.0', 'language': 'julia', 'name': 'julia-1.5'}}


nbf.write(nb, r'/home/pbarletta/labo/20/cph_obp/src/informe_ctv_cluster_phs.ipynb')
print(r"Jupyter notebook /home/pbarletta/labo/20/cph_obp/src/informe_ctv_cluster_phs.ipynb successfully generated.")
