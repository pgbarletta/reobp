#!/bin/bash
#SBATCH --job-name=pato_eol
#SBATCH --output=eol.out 
#SBATCH --error=eol.err 
#SBATCH --account=cwr109
#SBATCH --time=12:00:00
#SBATCH --nodes=3
#SBATCH --ntasks=12
#SBATCH --cpus-per-task=1
#SBATCH --gpus=12
#SBATCH --partition=gpu
#SBATCH --qos=gpu-unlim

module purge

module load gpu/0.15.4  openmpi/4.0.4 amber/20
module load slurm


export EXE=pmemd.cuda_SPFP.MPI

export OMPI_MCA_btl_openib_allow_ib=1


srun -n 12 $EXE -ng 12 -groupfile groupfile  -rem 4 -remlog rem.log

