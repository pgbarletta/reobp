# -*- coding: utf-8 -*-
# `nb_templater` generated Python script
# Generated from .ipynb template: apo_rmsd.ipynb
# www.github.com/ismailuddin/jupyter-nb-templater/
# Generated on: 2020-10-12 20:00 

import nbformat as nbf 
import sys
nb = nbf.v4.new_notebook() 

cell_0=r"""
using DataFrames, FileIO, DelimitedFiles
using Plots, Optim, LsqFit
""".strip()

cell_1=r"""
# Get ready
home = "/home/pbarletta/labo/20/cph_obp/"
dir_apo_pdt = string(home, "run/apo/pdt/")
dir_apo_all_pdt = string(home, "run/apo/all_pdt/")

nstlim = 12000
phs = collect(2.0:.5:7.5)
idx = collect(1:12)

titrable_resis = [4, 5, 11, 13, 20, 24, 30, 33, 37, 39, 40,
    48, 58, 73, 77, 78, 87, 93, 94, 97, 117]
titrable_resnames = ["GL4", "GL4", "HIP", "GL4", "GL4", "AS4",
    "AS4", "GL4", "AS4", "GL4", "AS4", "GL4", "AS4", "GL4", "AS4",
    "GL4", "AS4", "GL4", "GL4", "HIP", "AS4"]
titrable_cnt = length(titrable_resis)
""".strip()

cell_2=r"""
for i in 1:length(idx)
    PH = convert(Int64, phs[i] * 10)
    global rmsd_apo_idx = readdlm(joinpath(dir_apo_pdt, string(phs[i]),
            string("rmsd_apo_", idx[i])))[2:end, 2]
    global rmsd_apo_ph = readdlm(joinpath(dir_apo_all_pdt, string(phs[i]),
            string("rmsd_apo_", phs[i])))[2:end, 2]

    sym_rmsd_apo_idx = Symbol("rmsd_apo_", idx[i])
    sym_rmsd_apo_ph = Symbol("rmsd_apo_", PH)
    eval(:($sym_rmsd_apo_idx = rmsd_apo_idx))
    eval(:($sym_rmsd_apo_ph = rmsd_apo_ph))
end
""".strip()

cell_3=r"""
## RMSD por pH
""".strip()

nb['cells'] = [
    nbf.v4.new_code_cell(cell_0),
    nbf.v4.new_code_cell(cell_1),
    nbf.v4.new_code_cell(cell_2),
    nbf.v4.new_markdown_cell(cell_3)
]

for PH in range(20, 80, 5):
    ph = PH / 10
    celda_ph = (r"""plot(collect(1:nstlim) ./ 100, """ + "rmsd_apo_" + str(PH) + r""", 
        title = string("RMSD - pH = ", """ + str(ph) + r"""), size = (750, 400),
        yaxis = "RMSD [A]", xaxis = "Time [ns]")
    """).strip()
    nb['cells'].append(nbf.v4.new_code_cell(celda_ph))

celda_titulo=r"""
## RMSD por idx
""".strip()

nb['cells'].append(nbf.v4.new_markdown_cell(celda_titulo))

for idx in range(1, 11):
    celda_idx = (r"""plot(collect(1:nstlim) ./ 100, """ + "rmsd_apo_" + str(idx) + r""", 
        title = string("RMSD - idx = ", """ + str(idx) + r"""), size = (750, 400),
        yaxis = "RMSD [A]", xaxis = "Time [ns]")
    """).strip()
    nb['cells'].append(nbf.v4.new_code_cell(celda_idx))



nb['metadata'] = {'kernelspec': {'display_name': 'Julia 1.5.0', 'language': 'julia', 'name': 'julia-1.5'}}


nbf.write(nb, r'/home/pbarletta/labo/20/cph_obp/src/informe_apo_rmsd.ipynb')
print(r"Jupyter notebook /home/pbarletta/labo/20/cph_obp/src/informe_apo_rmsd.ipynb successfully generated.")
