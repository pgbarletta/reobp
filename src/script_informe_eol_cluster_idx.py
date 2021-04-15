# -*- coding: utf-8 -*-
# `nb_templater` generated Python script
# Generated from .ipynb template: eol_cluster.ipynb
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
dir_eol_clu = "/home/pbarletta/labo/20/cph_obp/run/eol/cluster"

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

nb['cells'] = [
    nbf.v4.new_code_cell(cell_0),
    nbf.v4.new_code_cell(cell_1),
    nbf.v4.new_markdown_cell(cell_2),
    nbf.v4.new_markdown_cell(cell_3),
]

celda_titulo=r"""## cluster por idx""".strip()
nb['cells'].append(nbf.v4.new_markdown_cell(celda_titulo))

for idx in range(1, 11):
    celda_titulo=(r"""#### idx = """ + str(idx)).strip()
    celda_idx_1 = (r"""viewstruc(read(joinpath(dir_eol_clu, string(idx[""" + str(idx) + r"""]), "top_cluster.c0.pdb"), PDB))""").strip()
    celda_idx_2 = (r"""viewstruc(read(joinpath(dir_eol_clu, string(idx[""" + str(idx) + r"""]), "top_cluster.c1.pdb"), PDB))""").strip()
    celda_idx_3 = (r"""viewstruc(read(joinpath(dir_eol_clu, string(idx[""" + str(idx) + r"""]), "top_cluster.c2.pdb"), PDB))""").strip()
    nb['cells'].append(nbf.v4.new_markdown_cell(celda_titulo))
    nb['cells'].append(nbf.v4.new_code_cell(celda_idx_1))
    nb['cells'].append(nbf.v4.new_code_cell(celda_idx_2))
    nb['cells'].append(nbf.v4.new_code_cell(celda_idx_3))


nb['metadata'] = {'kernelspec': {'display_name': 'Julia 1.5.0', 'language': 'julia', 'name': 'julia-1.5'}}


nbf.write(nb, r'/home/pbarletta/labo/20/cph_obp/src/informe_eol_cluster_idx.ipynb')
print(r"Jupyter notebook /home/pbarletta/labo/20/cph_obp/src/informe_eol_cluster_idx.ipynb successfully generated.")
