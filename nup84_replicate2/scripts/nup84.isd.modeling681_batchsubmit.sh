#!/bin/bash
#$ -S /bin/bash
#$ -l arch=linux-x64    # Specify architecture, required
#$ -l mem_free=6G       # Memory usage, required.  Note that this is per slot
#$ -l h_rt=48:0:0
#$ -pe ompi 6           # Specify parallel environment and number of slots, required
#$ -R yes               # SGE host reservation, highly recommended
#$ -V                   # Pass current environment to exec node, required
#$ -cwd                 # Current working directory
#$ -m bea
#$ -M seth.axen@ucsf.edu

qstat -j $JOB_ID

# Load OpenMPI-1.5 environment
module load openmpi-1.6-nodlopen
module load imp-fast-mpi

# Run application
mpirun -np $NSLOTS python nup84.isd.modeling681.py &> nup84.isd.modeling681.out
