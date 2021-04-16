using FileIO, DelimitedFiles
using Chemfiles
using Plots

casa = "/home/pbarletta/labo/20/cph_obp/run/eol"
nframes = 144000
nframes_per_trj = 144000 ÷ 12
phs = [ 2.0 ; 2.5 ; 3.0 ; 3.5 ; 4.0 ; 4.5 ; 5.0 ; 5.5 ; 6.0 ; 6.5 ; 7.0 ; 7.5 ]

texto = readdlm(joinpath(casa, "todo_cluster", "n_cluster_kmean.dat"), header=true)[1][:, 2]

masca = convert(Array{Bool,1}, texto)
frames_c1 = findall(masca)
n = length(frames_c1)
t = 21 # tritable residues: 21


trj_idx_c1 = Array{Int64,1}(undef, n)
trj_add_c1 = Array{Int64,1}(undef, n)
for i in 1:n
    # sumo 1 pq después voy a usar trj_idx_c1 p/ indexar los phs
    # y Julia tiene 1-index
    trj_idx_c1[i] = frames_c1[i] ÷ nframes_per_trj + 1
    # resto 1 pq después voy a usar trj_add_c1 p/ leer frames
    # con Chemfiles q es C== y tiene 0-index
    trj_add_c1[i] = frames_c1[i] % nframes_per_trj - 1
    
    if trj_add_c1[i] == - 1
        # frames_c1[i] is multiple of nframes_per_trj. The frame
        # we're after is the last frame of a trajectory. 
        trj_add_c1[i] += 1
        trj_idx_c1[i] -= 1
    end
end


i = 1
cpout = readdlm(joinpath(casa, "pdt", "cph_outputs",
string("reordered_cpouts.pH_", phs[trj_idx_c1[i]], "0")))

estados = Array{Int64,2}(undef, t, nframes_per_trj)
let linea = 1, i = 1
    # Hay más de nframes_per_trj frames y por lo tanto más records
    # de protonaciones, pero ya corté las trayectorias p/ esa longitud.
    while i <= nframes_per_trj
        if cpout[linea, 1] == "Time:"
            global estados[:, i] = cpout[linea + 1:linea + t, 4]
            linea += t
            i += 1
        else
            linea += 1
        end
    end
end


estados





