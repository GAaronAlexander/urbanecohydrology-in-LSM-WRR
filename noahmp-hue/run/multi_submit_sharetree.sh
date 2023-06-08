#!/bin/bash
#
#
scratch_directory='/glade/u/home/galexand/scratch/three_season_long_simulations/tree_overhang_expansion_clayloam/'


#For loop to increment over the vegetation amounts
for i in $(seq -w 01 01 70) 
do 
#create the vegetation amount of tree overhang pavement and 
# the urban tree
echo $i
j=$((100-10#$i))
k=$((8*10#$i))
foo=$(printf "%03d" $k)
echo "$foo"


#create name of directory
name_directory="tree_overhang_expansion_clayloam_$i"
namelist_name="namelist.tree_overhang_expansion_clayloam_$i"

#create mkdir
mkdir "$scratch_directory/$name_directory"

directory="$scratch_directory/$name_directory"
echo $directory

#modify the namelist
sed "s#OUTDIR = #OUTDIR = \"$directory\"#g" namelist.draft >> $namelist_name
sed -i "s/FAREA_INPUT = 1.0,1.0,1.0/FAREA_INPUT = 1.0,0.$i,1.0/g" $namelist_name

#create directory to submit things from 
mkdir $name_directory

#copy data needed to be able to submit the hrldas
cp -r $namelist_name *.TBL *.exe runHRLDAS.sh $name_directory

#get present working directory
present_working_dir=$(pwd)

#create symbolic link to get namelist.hrldas
ln -s $present_working_dir/$name_directory/$namelist_name $present_working_dir/$name_directory/namelist.hrldas

# submit the hrldasshell script
cd $present_working_dir/$name_directory
qsub runHRLDAS.sh

cd $present_working_dir
done


