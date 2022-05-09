# -*- coding: utf-8 -*-
# `nb_templater` generated Python script
# Generated from .ipynb template: eol_watlig.ipynb
# www.github.com/ismailuddin/jupyter-nb-templater/
# Generated on: 2022-04-14 12:17 

import nbformat as nbf 
import sys
nb = nbf.v4.new_notebook() 

cell_0=r"""
using DataFrames, FileIO, DelimitedFiles
using Plots, Optim, LsqFit, JUMD
using Statistics, NamedArrays
""".strip()

cell_1=r"""
# Get ready
dir_eol_watlig = "/home/pbarletta/labo/20/reobp/run/eol/watlig"

aa = 119
nstlim = 12000
phs = collect(2.0:.5:7.5)
idx = collect(1:12)

titrable_resis = [4, 5, 11, 13, 20, 24, 30, 33, 37, 39, 40,
    48, 58, 73, 77, 78, 87, 93, 94, 97, 117]
titrable_resnames = ["GL4", "GL4", "HIP", "GL4", "GL4", "AS4",
    "AS4", "GL4", "AS4", "GL4", "AS4", "GL4", "AS4", "GL4", "AS4",
    "GL4", "AS4", "GL4", "GL4", "HIP", "AS4"]
titrable_cnt = length(titrable_resis)

idx_of_titrable = fill(0, aa)
[ idx_of_titrable[titrable_resis[i]] = i for i in 1:titrable_cnt ];

titrable_residues = [ string(titrable_resnames[i], "_", titrable_resis[i]) 
    for i in 1:titrable_cnt ];
""".strip()

cell_2=r"""
for i in 1:12
    PH = convert(Int64, phs[i] * 10)
    global watlig_phs = convert(Array{Float64, 1},
    readdlm(joinpath(dir_eol_watlig, string(phs[i]), "close_wat.dat"))[2:end, 3])

    sym_watlig_1_phs = Symbol("watlig_dist_1_", PH)
    sym_watlig_2_phs = Symbol("watlig_dist_2_", PH)
    eval(:($sym_watlig_1_phs = watlig_phs[1:2:end]))
    eval(:($sym_watlig_2_phs = watlig_phs[2:2:end]))
end
""".strip()

cell_3=r"""
## O1 distance to closest water
""".strip()

nb['cells'] = [
    nbf.v4.new_code_cell(cell_0),
    nbf.v4.new_code_cell(cell_1),
    nbf.v4.new_code_cell(cell_2),
    nbf.v4.new_markdown_cell(cell_3)
]

for ph in range(20, 80, 5):
    PH = ph / 10
    celda_ph = (r"""
min_dist = 0
max_dist = 10
plot(collect(1:nstlim) ./ 100, watlig_dist_1_""" + str(ph) + r""",
    title = string("O1 distance to closest water - pH = ", """ + str(PH) + r"""), size = (750, 400),
    ylims = (min_dist, max_dist), label = false,
    yticks = collect(2:1:8),
    linecolor = Colors.colorant"Brown",
    guidefont = font(18, "Arial"), tickfont = font(12, "Arial"),
    legendfont = font(12, "Arial"),
    yaxis = "Distance [A]", xaxis = "Time [ns]")
""").strip()

    celda_ph_his = (r"""
st = .2
bin_watlig = collect(min_dist:st:max_dist)
wgh_watlig = fill(1.0, length(watlig_dist_1_""" + str(ph) + r"""))

# Histograma ponderado
Wbins_watlig, Whis_watlig = JUMD.weightedHist(watlig_dist_1_""" + str(ph) + r""", bin_watlig, wgh_watlig, true, false);

bar(Wbins_watlig, Whis_watlig,
    xlims = (st*10, max_dist), ylims = (0, .2),
    xticks = st*10:st*5:max_dist+st,
    linecolor = false, fillcolor = Colors.colorant"Brown",
    grid = false, legend = false,
    guidefont = font(18, "Arial"), tickfont = font(12, "Arial"),
    legendfont = font(12, "Arial"),
    title = string("Histogram of N1 distance to closest water - pH = ", 20),
    yaxis = "Relative probability", xaxis = "Distance [A]")
""").strip()
    nb['cells'].append(nbf.v4.new_code_cell(celda_ph))
    nb['cells'].append(nbf.v4.new_code_cell(celda_ph_his))

cell_6=r"""
## O2 distance to closest water
""".strip()


for ph in range(20, 80, 5):
    PH = ph / 10
    celda_ph = (r"""
min_dist = 0
max_dist = 10
plot(collect(1:nstlim) ./ 100, watlig_dist_2_""" + str(ph) + r""",
    title = string("O2 distance to closest water - pH = ", """ + str(PH) + r"""), size = (750, 400),
    ylims = (min_dist, max_dist), label = false,
    yticks = collect(2:1:8),
    linecolor = Colors.colorant"Brown",
    guidefont = font(18, "Arial"), tickfont = font(12, "Arial"),
    legendfont = font(12, "Arial"),
    yaxis = "Distance [A]", xaxis = "Time [ns]")
""").strip()

    celda_ph_his = (r"""
st = .2
bin_watlig = collect(min_dist:st:max_dist)
wgh_watlig = fill(1.0, length(watlig_dist_2_20))

# Histograma ponderado
Wbins_watlig, Whis_watlig = JUMD.weightedHist(watlig_dist_2_20, bin_watlig, wgh_watlig, true, false);

bar(Wbins_watlig, Whis_watlig,
    xlims = (st*10, max_dist), ylims = (0, .2),
    xticks = st*10:st*5:max_dist+st,
    linecolor = false, fillcolor = Colors.colorant"Brown",
    grid = false, legend = false,
    guidefont = font(18, "Arial"), tickfont = font(12, "Arial"),
    legendfont = font(12, "Arial"),
    title = string("Histogram of N1 distance to closest water - pH = ", 20),
    yaxis = "Relative probability", xaxis = "Distance [A]")
""").strip()

    nb['cells'].append(nbf.v4.new_code_cell(celda_ph))
    nb['cells'].append(nbf.v4.new_code_cell(celda_ph_his))


celda_tabla_ph=r"""vals = vcat("""
for ph in range(20, 80, 5):
    if ph == 75:
        celda_tabla_ph = celda_tabla_ph + (r"""
        [ mean(watlig_dist_1_""" + str(ph) + r""") std(watlig_dist_1_""" + str(ph) + r""") std(watlig_dist_1_""" + str(ph) + r""") / mean(watlig_dist_1_""" + str(ph) + r""") ])""").strip() + "\n" + "\n"
        break
    
    celda_tabla_ph = celda_tabla_ph + (r"""
    [ mean(watlig_dist_1_""" + str(ph) + r""") std(watlig_dist_1_""" + str(ph) + r""") std(watlig_dist_1_""" + str(ph) + r""") / mean(watlig_dist_1_""" + str(ph) + r""") ],""").strip() + "\n"

celda_tabla_ph= celda_tabla_ph + r"""NamedArray(vals, (string.(phs), ["μ" ; "std" ; "μ/std"]))"""
nb['cells'].append(nbf.v4.new_code_cell(celda_tabla_ph))

celda_tabla_ph=r"""vals = vcat("""
for ph in range(20, 80, 5):
    if ph == 75:
        celda_tabla_ph = celda_tabla_ph + (r"""
        [ mean(watlig_dist_2_""" + str(ph) + r""") std(watlig_dist_2_""" + str(ph) + r""") std(watlig_dist_2_""" + str(ph) + r""") / mean(watlig_dist_2_""" + str(ph) + r""") ])""").strip() + "\n" + "\n"
        break
    
    celda_tabla_ph = celda_tabla_ph + (r"""
    [ mean(watlig_dist_2_""" + str(ph) + r""") std(watlig_dist_2_""" + str(ph) + r""") std(watlig_dist_2_""" + str(ph) + r""") / mean(watlig_dist_2_""" + str(ph) + r""") ],""").strip() + "\n"

celda_tabla_ph= celda_tabla_ph + r"""NamedArray(vals, (string.(phs), ["μ" ; "std" ; "μ/std"]))"""
nb['cells'].append(nbf.v4.new_code_cell(celda_tabla_ph))

nb['metadata'] = {'kernelspec': {'display_name': 'Julia 1.6.2', 'language': 'julia', 'name': 'julia-1.6'}}


nbf.write(nb, r'/home/pbarletta/labo/20/reobp/src/informe_eol_watlig.ipynb')
print(r"Jupyter notebook /home/pbarletta/labo/20/reobp/src/informe_eol_watlig.ipynb successfully generated.")
