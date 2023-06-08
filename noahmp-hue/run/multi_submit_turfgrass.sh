#!/bin/bash
#
#
scratch_directory='/glade/scratch/galexand/three_season_long_simulations_turf_grass_with_some_disconnect/'


#For loop to increment over the vegetation amounts
for i in $(seq -w 01 01 60) 
do 
#constant amount of turf grass and urban amount (70% 30%). Increment 
# the 30% to be more and more connected to the turf grass
echo $i
j=1
k=$((((10#$i)*10000+70)/10#$j))
foo=$(printf "%04d" $k)
echo "$foo"


#create name of directory
name_directory="turfgrass_with_some_disconnect_$i"
namelist_name="namelist.turfgrass_with_some_disconnect_$i"

#create mkdir
mkdir "$scratch_directory/$name_directory"

directory="$scratch_directory/$name_directory"
echo $directory

#modify the namelist
sed "s#OUTDIR = #OUTDIR = \"$directory\"#g" namelist.draft >> $namelist_name
sed -i "s/FAREA_INPUT = 1.0,1.0,1.0/FAREA_INPUT = 1.0,0.$foo,1.0/g" $namelist_name

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


