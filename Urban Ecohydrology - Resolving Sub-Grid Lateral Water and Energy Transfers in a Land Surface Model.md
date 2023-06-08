
Materials supporting submitted manuscript about integrating lateral surface water transfers changes water and energy fluxes within a land surface model (noah-mp for heterogneous urban environments (HUE))

## Initilization
Each sub directory within this directoyr contains the noah-mp initilization file and a single namelist file that contains all of the model choices to run this model. Because 271 different simluations were run for this  study, one would take the namelist file and add perturb the *FAREA_INPUT* variable to recreate the suite of simulations. 

In addition, NLDAS-2 data (Milwaukee_NLDAS2_HRLDAS_input_hrly.dat) is provied. This data needs to be fed into the HRLDAS setup .ncl files to createa a single file per hour for forcing. NLDAS-2 data is ordered as: 
 + Year (YYYY)
 + Month (MM)
 + Day (DD)
 + Hour (HH)
 + Wind Speed ($m \enspace s^{-1}$)
 + AIr Temperature ($K$)
 + Specific Humidity ( $kg \enspace kg ^{-1}$ )
 + Air Pressure ($Pa$)
 + Longwave Radiation ($W \enspace m^{-2}$)
 + Shortwave Radiation ($W \enspace m^{-2}$)
 + Precipitation ($mm \enspace s^{-1}$)

## Noahmp-HUE
This is the noah-mp code that was modified for this study. New changes are found in the phys/module_sf_noahmplsm.F, phys/module_sf_noahmpdrv.F, IO_code/module_NoahMP_hrldas_driver.F.

To compile and run, please see (https://github.com/NCAR/hrldas-release/tree/master), which is the specific version of Noah-MP used in this study.

## Scripts-Extract 
All scripts, seperated by figure, represent the specific python scripts used to extract data from RAW hrldas output. These data respresent the data that were used to create the figures withing this study.

### Figure 2
For Figure 2, one would need to extract the rainfall bool (is it raining vs. not raining) first. First, run *figure_2_rainfall_bool_creation.py*, and then run all others. 

### Figure 3
Extraction of seasonal water fluxes was done on a growing season basis. One needs to modify both scripts in this repository to extract years 2018, 2019, 2020. Effectively, one would just need to change the time-stamps throughtout the scripts. 

### Figure 4
Extraction of seasonal water fluxes was done on a growing season basis. One needs to modify both scripts in this repository to extract years 2018, 2019, 2020. Effectively, one would just need to change the time-stamps throughtout the scripts. 

### Figure 7
To understand how peak diurnal heat fluxes changed, this script loops over each simulation, colapses each day into a single dirunal time series of sensible heat and latent heat, and then extracts the median and IQR to be saved for later use. The collapsing of the data is a bit computationally expsneive due to the use of pandas to resampling. 

### Figure 8 
For each day in the growing season, this script extracts sensible heat flux, and then integrates it to an energy (converting from watts to joules), and then summing over the entire day. 

This gives the amount of energy per day, which we then extracted for every model simluation for a growing season. One would need to re-run this to extract 2018, 2019, and 2020 by changing around datetime strings within the script. 

### Figure 9
This is exactly the same to Figure 8 in terms of workflow, but for latent heat flux instead of sensible heat flux. 

## Intermediate-data
Intermediate data is organized by figure, and represents the summary data that was used to gnerate figures throughought this study. Descriptions provided explain the CSV files organization. 

### Figure 2
+ *Rain_bool_12_hour_window.csv*: A boolean of True or False depending on if it is raining. Note that this uses the definition of a storm has at least 12 hours of time between rainfall events. 
+ *RAINFALL_12hour_EVENT_WINDOW.csv* : Rainfall totals for all 125 storms that occured during the three growing seasons in this study
+ *three_season_tree_sharetree_siltloam_12hourwindow.csv*: Runoff totals for each storm from the entire model domain. Columns are different rainfall events. Row 0 is typical model representation. Row 1 through 71 represent different model amounts of extra tree canopy from new LSM. 
+  *three_season_tree_shifttree_siltloam_12hourwindow.csv*: Runoff totals for each storm from the entire model domain. Columns are different rainfall events. Row 0 is typical model representation. Row 1 through 71 represent different model amounts of extra tree canopy from new LSM. 
+  *three_season_turfgrass_12hourwindow.csv*: Runoff totals for each storm from the entire model domain. Columns are different rainfall events. Row 0 is typical model representation. Row 1 through 61 represent different model amounts of downspout disconnection
+  *three_season_permeable_pavement_12hourwindow.csv*: Runoff totals for each storm from the entire model domain. Columns are different rainfall events. Row 0 is typical model representation. Row 1 through 51 represent different model amounts of permeable pavement. 

### Figure 3
Extracted data from each growing season for urban shift tree and urban tree expansion. 

Each CSV file is organized such that the columns represent different model representations with the first column showing the typical LSM representaiton. 

Rows are [all in mm]: 
+ rainfall
+ runoff from pavement (uncovered)
+ runoff from pavement with tree over 
+ runoff from vegetated surface
+ evapotranspiration from vegetated surface
+ evapotranspiration ffrom tree over pavement
+ soil moisture storage
+ deep drainiage 

### Figure 4
This is set up the exact same of Figure 3. Rows are the different model representatiions with the first colum showing the typical LSM. 

Rows are [all in mm]: 
+ rainfall
+ runoff from pavement (uncovered)
+ runoff from vegetated surface/ permeable surface 
+ ET from pavement 
+ ET from permeable surface
+ soil moisture storage
+ deep drainiage 

### Figure 6 
For soil mositure time-series plots, each intermediate data file is organized to give the **COLUMN TOTAL SOIL MOISTURE** through time for select simulations. Each time series is organized with timesteps as the first column, and volumetric soil moisture in $m^3 \enspace m^3$ for the second column. 

### Figure 7
Dirunal patterns of fluxes are saved as CSV files, and are identical to those showin in Figure 7. Each CSV file is either the HFX or LH, and is the median, 25% or 75% quantiles for the typical LSM or the most extreme. 

Files that are of the form *XXX_extracted_max_min* are the extracted maximum, minimum, and IQR around these values in for all idfferent simulations. Each column represents a different model. The order is:
+ Median of the daily max
+ 25%  of the daily max
+ 75% of the daily max
+ Median of the daily min
+ 25% of the daily min
+ 75% of the daily min

### Figure 8
Daily intereagread heat fluxes for latent heat fluxes. The columsn represent different model simulations, with the first column representing a typical LSM for each sub directory. The rows represent the different days through the growing season, starting on the 1 May and ending on 31 Oct for 2018, 2019 or 2020 depending on the CSV. 

### Figure 9 

Daily intereagread heat fluxes for latent heat fluxes. The columsn represent different model simulations, with the first column representing a typical LSM for each sub directory. The rows represent the different days through the growing season, starting on the 1 May and ending on 31 Oct for 2018, 2019 or 2020 depending on the CSV. 


## Scripts-Plot

For each figure in the study, we provide the scirpts used to generate each plot. Note that you will need to modify the paths to include either the correct raw data file (from noah-mp HRLDAS) or the correct intermeidate data file to recreate the figures. 

Within each scripts plot, there maybe print statements that are used to generate the specific statistical amounts that were presented throughout the text. 


# Questions/Issues?
Please contact gaalexander3@wisc.edu for questions or discussion 
