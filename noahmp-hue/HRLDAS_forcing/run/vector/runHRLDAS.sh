#!/bin/bash
#
# LSF batch script to run the test MPI code
#
#PBS -N HRLDAS-create-inputs                           
#PBS -A UWIS0037                                     
#PBS -l walltime=04:00:00                            
#PBS -q regular                                      
#PBS -j oe                                             
#PBS -l select=1:ncpus=36:mpiprocs=1
#PBS -m abe                                            
#PBS -M gaalexander3@wisc.edu			
#
cd /glade/u/home/galexand/work/GreenInfrastructure-NOAH-MP-test_sharing_water_street_trees/HRLDAS/HRLDAS_forcing/run/examples/vector
module load ncl 
ncl create_ldasin_files.ncl


