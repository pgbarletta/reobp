# -*- coding: utf-8 -*-
# `nb_templater` generated Python script
# Generated from .ipynb template: eol_titration.ipynb
# www.github.com/ismailuddin/jupyter-nb-templater/
# Generated on: 2020-10-12 15:05 

import nbformat as nbf 
import sys
nb = nbf.v4.new_notebook() 

cell_0=r"""
using DataFrames, FileIO, DelimitedFiles
using Plots, Optim, LsqFit
""".strip()

cell_1=r"""
function read_pop_file(filename, resnames)
    deprotonated_fraction =  Array{Float64, 1}(undef, length(resnames))
    pop_file = readdlm(filename, header = true)[1][2:end, 2:end]

    k = 0
    for resname in resnames
        k+=1
        if resname == "GL4"
            deprotonated_fraction[k] = pop_file[k, 3:end][1]
        elseif resname == "AS4"
            deprotonated_fraction[k] = pop_file[k, 3:end][1]
        elseif resname == "HIP"
            deprotonated_fraction[k] = 1 - pop_file[k, 3:end][1]
        elseif resname == "LYS"
            deprotonated_fraction[k] = 1 - pop_file[k, 3:end][1]
        elseif resname == "CYX"
            deprotonated_fraction[k] = 1 - pop_file[k, 3:end][1]
        elseif resname == "TYR"
            deprotonated_fraction[k] = 1 - pop_file[k, 3:end][1]
        end
    end
    
    return deprotonated_fraction
end
""".strip()

cell_2=r"""
# Get ready
home = "/home/pbarletta/labo/20/cph_obp/"
eol_cph_out = string(home, "run/eol/pdt/cph_outputs/")
eol_cph_pre_out = string(home, "run/eol/pre_pdt/cph_outputs/")

phs = collect(30:5:75)
pdt_steps = collect(0:1:7)
suffix_pka_file = "_pka"
suffix_pop_file = "_pop"
titrable_cnt = 36
titrable_resis = [4, 5, 7, 11, 13, 18, 20, 24, 27, 30, 33, 37, 39,
    40, 41, 42, 48, 52, 58, 59, 64, 69, 73, 77, 78, 82, 87, 93, 94,
    97, 99, 102, 109, 111, 114, 117];
titrable_resnames = ["GL4", "GL4", "LYS", "HIP", "GL4", "LYS", "GL4", "AS4", "LYS",
    "AS4", "GL4", "AS4", "GL4", "AS4", "LYS", "LYS", "GL4", "LYS",
    "AS4", "LYS", "LYS", "LYS", "GL4", "AS4", "GL4", "LYS", "AS4",
    "GL4", "GL4", "HIP", "LYS", "LYS", "LYS", "LYS", "LYS", "AS4"]
global const def_pka_as4 = 3.71
global const def_pka_gl4 = 4.15
global const def_pka_lys = 10.67
global const def_pka_hip = 6.04;
# global const def_pka_cyx = 8.14;
# global const def_pka_tyr = 10.1;
""".strip()

cell_3=r"""
def_res_pka = Array{Float64, 1}(undef, titrable_cnt)

for i in 1:titrable_cnt
    if titrable_resnames[i] == "AS4"
        def_res_pka[i] = def_pka_as4
    elseif titrable_resnames[i] == "GL4"
        def_res_pka[i] = def_pka_gl4
    elseif titrable_resnames[i] == "LYS"
        def_res_pka[i] = def_pka_lys
    elseif titrable_resnames[i] == "HIP"
        def_res_pka[i] = def_pka_hip
    end
end
""".strip()

cell_4=r"""
## Leo los \_pop files de todas las corridas
""".strip()

cell_5=r"""
# Obtengo las poblaciones deprotonadas de c/ residuo a c/ valor de pH
# Leo el State 0 de c/ residuo. P/ lods residuos ácidos (GL4, AS4)
# el state 0 es deprotonado, p/ los básicos es protonado.
# Usaré estas poblaciones p/ ajustar la curva de Hill y obtener el valor de pKa.
deprotonated_fraction =  Array{Float64, 2}(undef, titrable_cnt, length(phs))
for i in 1:length(phs)
    pop_filename = joinpath(eol_cph_out, "p", string(phs[i], suffix_pop_file))
    deprotonated_fraction[:, i] = read_pop_file(pop_filename, titrable_resnames)
end
""".strip()

cell_6=r"""
## Leo los \_pka files, sólo de pre_pdt
""".strip()

cell_7=r"""
# P/ ajustar bien la curva de Hill y obtener los parámetros n y pKa conviene
# empezar con unos buenos parámetros iniciales. P/ n eso es 1.0 y p/ pKa será
# el valor de pKa predicho durante la corrida con menor Offset. Por eso leo
# estos archivos de _pka, p/ obtener los pka predichos y sólo usar el q venga
# con de la corrida con menor offset. Cualquier cosa: ver papers de Swails.

res_offset_all = Array{Float64, 2}(undef, titrable_cnt, length(phs))
res_pka_pred_all = Array{Float64, 2}(undef, titrable_cnt, length(phs))
res_pka_pred =  Array{Float64, 1}(undef, titrable_cnt)

for i = 1:length(phs)
    pka_filename = joinpath(eol_cph_out, "p", string(phs[i], suffix_pka_file))
    pka_file = readdlm(pka_filename, header = true)[1][1:end-1, 1:end-1]    
    res_offset_all[:, i] = pka_file[:, 5]
    res_pka_pred_all[:, i] = pka_file[:, 7]
end

for i = 1:titrable_cnt
    min_offset_idx = findmin(abs.(res_offset_all[i, :]))[2]
    res_pka_pred[i] = res_pka_pred_all[i, min_offset_idx]
end
""".strip()

cell_8=r"""
## Determino Hill coefficients and pKas
""".strip()

cell_9=r"""
# Hill coefficient and pKa for each residue 
res_pka =  Array{Float64, 1}(undef, titrable_cnt)
res_hil =  Array{Float64, 1}(undef, titrable_cnt)

# Hill function
@. f(x, hill_coef) = 1 / (1 + 10 ^(hill_coef[1]*(hill_coef[2] - x)) )
xdata = phs ./ 10

# Fit the curves
for i = 1:titrable_cnt
    hill_coef = [1. ; res_pka_pred[i]]
    fit = curve_fit(f, xdata, deprotonated_fraction[i, :], hill_coef)    
    res_hil[i] = fit.param[1]
    res_pka[i] = fit.param[2]
end

# Guardo los pkas obtenidos
writedlm(joinpath(home, "rtdos_log", "pka_eol"), [titrable_resnames titrable_resis res_pka res_hil])
""".strip()

cell_10=r"""
## Diferencias entre pka calculado y default
""".strip()

cell_11=r"""
not_lys = titrable_resnames .!= "LYS"
etiquetas = string.(titrable_resnames[not_lys], " ", titrable_resis[not_lys])
dif_res_pka = map(-, res_pka, def_res_pka);
""".strip()

cell_12=r"""
bar(etiquetas[1:10], dif_res_pka[not_lys][1:10], label = :none,
    ylabel = "ΔpKa")
""".strip()

cell_13=r"""
bar(etiquetas[11:end], dif_res_pka[not_lys][11:end], label = :none,
    ylabel = "ΔpKa")
""".strip()

cell_14=r"""
### Plotteo
""".strip()

cell_15=r"""
function titration_curve(n, pKa, x)
    return (1 / (1 + 10 ^(n*(pKa - x))))
end
x = collect(1:.1:14);
""".strip()

nb['cells'] = [
    nbf.v4.new_code_cell(cell_0),
    nbf.v4.new_code_cell(cell_1),
    nbf.v4.new_code_cell(cell_2),
    nbf.v4.new_code_cell(cell_3),
    nbf.v4.new_markdown_cell(cell_4),
    nbf.v4.new_code_cell(cell_5),
    nbf.v4.new_markdown_cell(cell_6),
    nbf.v4.new_code_cell(cell_7),
    nbf.v4.new_markdown_cell(cell_8),
    nbf.v4.new_code_cell(cell_9),
    nbf.v4.new_markdown_cell(cell_10),
    nbf.v4.new_code_cell(cell_11),
    nbf.v4.new_code_cell(cell_12),
    nbf.v4.new_code_cell(cell_13),
    nbf.v4.new_markdown_cell(cell_14),
    nbf.v4.new_code_cell(cell_15)
]

for i in range(1, 37):
    celda=(r"""i = """ + str(i) + r"""
    plot(x, titration_curve.(res_hil[i], res_pka[i], x),
        label = "LSQ Fit",
        title = string(titrable_resnames[i], " ", titrable_resis[i]))
    
    scatter!(xdata, deprotonated_fraction[i, :],
        label = "A-")
    
    annotate!((res_pka[i] + 1.5), .5, 
        Plots.text(string("pKa = ", round(res_pka[i], digits = 2))))
    annotate!((res_pka[i] + 1.2), .4, 
        Plots.text(string("n = ", round(res_hil[i], digits = 2))))
    """).strip()

    nb['cells'].append(nbf.v4.new_code_cell(celda))


nb['metadata'] = {'kernelspec': {'display_name': 'Julia 1.5.0', 'language': 'julia', 'name': 'julia-1.5'}}


nbf.write(nb, r'/home/pbarletta/labo/20/cph_obp/src/informe_eol_titration.ipynb')
print(r"Jupyter notebook /home/pbarletta/labo/20/cph_obp/src/informe_eol_titration.ipynb successfully generated.")
