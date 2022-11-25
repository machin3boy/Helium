#!/bin/bash
#
#SBATCH --job-name=mesa_test_2
#
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --time=1:00:00
#SBATCH --mem=15G

export OMP_NUM_THREADS=8
python3 skeleton_script.py
