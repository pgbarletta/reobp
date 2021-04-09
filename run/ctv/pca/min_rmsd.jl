# Script p/ encontrar y escribir el PDB "top", es decir, el frame más parecido
# al average de la corrida.
# Leo el archivo de rmsd entre el PDB average y la corrida (fiteada a ese
# mismo average) y encuentro el frame correspondiente. Uso ese nro de frame p/
# modificar el archivo plantilla "get_top_cpp" y lo corro con cpptraj p/ obtener el PDB.

using DelimitedFiles

pdb = "ctv"
casa = joinpath("/home/pbarletta/labo/20/reobp/run", pdb, "pca")
cd(casa)
cpp_plantilla = readlines(joinpath("plantillas", "get_top_cpp"))

#for idx = 1:12
#    cpp = copy(cpp_plantilla)
#    rmsd_fn = joinpath(string(idx), string("rmsd_avg_", pdb, "_", idx))
#
#    rms = convert(Array{Float64,1}, readdlm(rmsd_fn)[2:end, 2])
#    frm = findmin(rms)[2]
#
#    cpp[1] = replace(cpp[1], "apo" => pdb)
#    cpp[3] = replace(cpp[3], "X" => string(frm))
#    cpp[3] = replace(cpp[3], "apo_1" => string(pdb, "_", idx))
#    cpp[4] = replace(cpp[4], "apo_1" => string(pdb, "_", idx))
#    
#
#    writedlm(joinpath(string(idx), "get_top_cpp"), cpp)
#
#    cd(string(idx))
#    run(`cpptraj -i get_top_cpp`)
#    cd("..")
#end

for ph in collect(2.0:.5:7.5)
    cpp = copy(cpp_plantilla)
    rmsd_fn = joinpath(string(ph), string("rmsd_avg_", pdb, "_", ph))

    rms = convert(Array{Float64,1}, readdlm(rmsd_fn)[2:end, 2])
    frm = findmin(rms)[2]

    cpp[1] = replace(cpp[1], "apo" => pdb)
    cpp[3] = replace(cpp[3], "X" => string(frm))
    cpp[3] = replace(cpp[3], "apo_1" => string(pdb, "_", ph))
    cpp[4] = replace(cpp[4], "apo_1" => string(pdb, "_", ph))
    

    writedlm(joinpath(string(ph), "get_top_cpp"), cpp)

    cd(string(ph))
    run(`cpptraj -i get_top_cpp`)
    cd("..")
end
