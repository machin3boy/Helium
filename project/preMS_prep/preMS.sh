#!/bin/bash
#
#SBATCH --job-name=mesa_test
#
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --time=100:00:00
#SBATCH --mem=15G
module load python/3.8.5
export OMP_NUM_THREADS=4
python3 preMS.py
