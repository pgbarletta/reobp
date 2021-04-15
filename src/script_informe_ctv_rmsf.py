# -*- coding: utf-8 -*-
# `nb_templater` generated Python script
# Generated from .ipynb template: ctv_rmsf.ipynb
# www.github.com/ismailuddin/jupyter-nb-templater/
# Generated on: 2020-11-10 20:43 

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
dir_ctv_rmsf = string(home, "run/ctv/rmsf/")

aa = 113
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
for i in 1:length(phs)
    PH = convert(Int64, phs[i] * 10)
#     global rmsf_ctv_idx = readdlm(joinpath(dir_ctv_rmsf, string(i),
#             string("rmsf_ctv_", idx[i])))[2:end, 2]
    global rmsf_ctv_ph = readdlm(joinpath(dir_ctv_rmsf, string(phs[i]),
            string("rmsf_ctv_", phs[i])))[2:end, 2]

#     sym_rmsf_ctv_idx = Symbol("rmsf_ctv_", idx[i])
    sym_rmsf_ctv_ph = Symbol("rmsf_ctv_", PH)
#     eval(:($sym_rmsf_ctv_idx = rmsf_ctv_idx))
    eval(:($sym_rmsf_ctv_ph = rmsf_ctv_ph))
end
""".strip()

cell_3=r"""
## RMSF por pH
""".strip()

nb['cells'] = [
    nbf.v4.new_code_cell(cell_0),
    nbf.v4.new_code_cell(cell_1),
    nbf.v4.new_code_cell(cell_2),
    nbf.v4.new_markdown_cell(cell_3),
]

for ph in range(20, 80, 5):
    PH = ph / 10
    celda_ph = r"""plot(collect(1:aa), rmsf_ctv_""" + str(ph) + r""",
        title = string("RMSF - pH = ", """ + str(PH) + r"""), size = (750, 400), label = false,
        ylims = (0, +Inf), xticks = collect(5:10:aa), yaxis = "RMSF [A]", xaxis = "Residue #")
    """.strip()
    nb['cells'].append(nbf.v4.new_code_cell(celda_ph))


celda_titulo=r"""## RMSF por idx""".strip()
nb['cells'].append(nbf.v4.new_markdown_cell(celda_titulo))

for idx in range(1, 13):
    celda_idx=r"""plot(collect(1:aa), rmsf_ctv_""" + str(idx) + r""", 
        title = string("RMSF - idx = ", """ + str(idx) + r"""), size = (750, 400), label = false,
        ylims = (0, +Inf), xticks = collect(5:10:aa), yaxis = "RMSF [A]", xaxis = "Residue #")
    """.strip()
    nb['cells'].append(nbf.v4.new_markdown_cell(celda_idx))


nb['metadata'] = {'kernelspec': {'display_name': 'Julia 1.5.0', 'language': 'julia', 'name': 'julia-1.5'}}


nbf.write(nb, r'/home/pbarletta/labo/20/cph_obp/src/informe_ctv_rmsf.ipynb')
print(r"Jupyter notebook /home/pbarletta/labo/20/cph_obp/src/informe_ctv_rmsf.ipynb successfully generated.")
