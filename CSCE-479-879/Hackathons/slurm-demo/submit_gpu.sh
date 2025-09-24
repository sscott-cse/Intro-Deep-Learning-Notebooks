#!/bin/sh
#SBATCH --time=6:00:00                        # Maximum run time in hh:mm:ss
#SBATCH --mem=16000                           # Maximum memory required (in megabytes)
#SBATCH --job-name=default_479                # Job name (to track progress)   
#SBATCH --partition=csce_gpu,csce_gpu_preempt # Partition on which to run job 
#SBATCH --gres=gpu:1                          # Don't change this, it requests a GPU
#SBATCH --constraint=gpu_16gb                 # will request a GPU with 16GB of RAM, independent of the type of card

echo "CUDA_VISIBLE_DEVICES: $CUDA_VISIBLE_DEVICES"
nvidia-smi

module load mamba
conda activate /mnt/nrdstor/cse479/shared/envs
export LD_LIBRARY_PATH=/mnt/nrdstor/cse479/shared/envs/lib

$@