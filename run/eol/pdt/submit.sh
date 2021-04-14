#!/bin/bash
#SBATCH --job-name=pato_eol
#SBATCH --output=eol.out 
#SBATCH --error=eol.err 
#SBATCH --account=cwr109
#SBATCH --time=12:00:00
#SBATCH --nodes=2
#SBATCH --ntasks=8
#SBATCH --cpus-per-task=1
#SBATCH --gpus=8
#SBATCH --partition=gpu
#SBATCH --qos=gpu-unlim

module purge

module load gpu/0.15.4  openmpi/4.0.4 amber/20
module load slurm


export EXE=pmemd.cuda_SPFP.MPI

export OMPI_MCA_btl_openib_allow_ib=1


srun -n 8 $EXE -ng 8 -groupfile groupfile -rem 4 -remlog rem.log

