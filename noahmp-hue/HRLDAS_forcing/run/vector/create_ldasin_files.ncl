;;;
;;;  This script created by Barlage to provide some guidance on how to create
;;;   HRLDAS forcing files for point-based simulations
;;;


load "$NCARG_ROOT/lib/ncarg/nclex/gsun/gsn_code.ncl"
load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/contributed.ncl"
load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/gsn_csm.ncl"  

begin

yyyy_start = 2018     ; time you want to start creating forcing
  mm_start = 4
  dd_start = 01
  hh_start = 00
  min_start = 0

min_spacing = 0
hh_spacing = 1      ; number of hours between forcing files

total_timesteps = 22704   ; set manually
number_stations = 2

nums = (/"00","01","02","03","04","05","06","07","08","09", \
         "10","11","12","13","14","15","16","17","18","19", \
	 "20","21","22","23","24","25","26","27","28","29", \
	 "30","31","32","33","34","35","36","37","38","39", \
	 "40","41","42","43","44","45","46","47","48","49", \
	 "50","51","52","53","54","55","56","57","58","59"/)
ddinmm = (/31,28,31,30,31,30,31,31,30,31,30,31/)

precip_input = new((/total_timesteps,number_stations/),float)
swdown_input = new((/total_timesteps,number_stations/),float)
lwdown_input = new((/total_timesteps,number_stations/),float)
sfctmp_input = new((/total_timesteps,number_stations/),float)
spechu_input = new((/total_timesteps,number_stations/),float)
u_wind_input = new((/total_timesteps,number_stations/),float)
v_wind_input = new((/total_timesteps,number_stations/),float)
sfcprs_input = new((/total_timesteps,number_stations/),float)

;;;;;;;;;;;;
; READ YOUR FORCING DATA INTO DATA STRUCTURES
;
; YOU WILL NEED THE FOLLOWING:
;    PRECIPITATION RATE [mm/s]
;    DOWNWARD SOLAR [W/m^2]
;    DOWNWARD LONGWAVE [W/m^2]
;    TEMPERATURE [K]
;    SPECIFIC HUMIDITY [kg/kg]
;    U/V WIND COMPONENTS [m/s] (the model doesn't care about direction)
;    PRESSURE [Pa]
;    
;    ***********Note: you may need to adjust units*************
;;;;;;;;;;;;

station1 = readAsciiTable("Milwaukee_NLDAS2_HRLDAS_input_hrly.dat" , 12, "float", 0)
station2 = readAsciiTable("Milwaukee_NLDAS2_HRLDAS_input_hrly.dat" , 12, "float", 0)
;station3 = readAsciiTable("Fond_Du_Lac_HRLDAS_input_5min_fixed_radiation.dat" , 12, "float", 0)
;station4 = readAsciiTable("Fond_Du_Lac_HRLDAS_input_5min_fixed_radiation.dat" , 12, "float", 0)
;station5 = readAsciiTable("Fond_Du_Lac_HRLDAS_input_5min_fixed_radiation.dat" , 12, "float", 0)
;station6 = readAsciiTable("Fond_Du_Lac_HRLDAS_input_5min_fixed_radiation.dat" , 12, "float", 0)
;station7 = readAsciiTable("Fond_Du_Lac_HRLDAS_input_5min_fixed_radiation.dat" , 12, "float", 0)
;station8 = readAsciiTable("Fond_Du_Lac_HRLDAS_input_5min_fixed_radiation.dat" , 12, "float", 0)
;;station3 = readAsciiTable("location3.dat" , 13, "float", 0)

precip_input(:,0) = station1(:,11)  ; precip in column 13 in example
precip_input(:,1) = station2(:,11)
;precip_input(:,2) = station3(:,11)
;precip_input(:,3) = station4(:,11)
;precip_input(:,4) = station5(:,11)
;precip_input(:,5) = station6(:,11)
;precip_input(:,6) = station7(:,11)
;precip_input(:,7) = station8(:,11)

swdown_input(:,0) = station1(:,10)  ; shortwave down in column 11 in example
swdown_input(:,1) = station2(:,10)
;swdown_input(:,2) = station3(:,9)
;swdown_input(:,3) = station4(:,9)
;swdown_input(:,4) = station5(:,9)
;swdown_input(:,5) = station6(:,9)
;swdown_input(:,6) = station7(:,9)
;swdown_input(:,7) = station8(:,9)

;swdown_input(:,2) = station3(:,10)

lwdown_input(:,0) = station1(:,9)  ; longwave down in column 12 in example
lwdown_input(:,1) = station2(:,9)
;lwdown_input(:,2) = station3(:,10)
;lwdown_input(:,3) = station4(:,10)
;lwdown_input(:,4) = station5(:,10)
;lwdown_input(:,5) = station6(:,10)
;lwdown_input(:,6) = station7(:,10)
;lwdown_input(:,7) = station8(:,10)
;lwdown_input(:,2) = station3(:,11)

sfctmp_input(:,0) = station1(:,6)   ; temperature in column 8 in example
sfctmp_input(:,1) = station2(:,6)
;sfctmp_input(:,2) = station3(:,6)
;sfctmp_input(:,3) = station4(:,6)
;sfctmp_input(:,4) = station5(:,6)
;sfctmp_input(:,5) = station6(:,6)
;sfctmp_input(:,6) = station7(:,6)
;sfctmp_input(:,7) = station8(:,6)
;sfctmp_input(:,2) = station3(:,7)

u_wind_input(:,0) = station1(:,5)   ; wind speed in column 6 in example
u_wind_input(:,1) = station2(:,5)
;u_wind_input(:,2) = station3(:,5)
;u_wind_input(:,3) = station4(:,5)
;u_wind_input(:,4) = station5(:,5)
;u_wind_input(:,5) = station6(:,5)
;u_wind_input(:,6) = station7(:,5)
;u_wind_input(:,7) = station8(:,5)
;u_wind_input(:,2) = station3(:,5)

v_wind_input(:,0) = 0.0             ; direction doesn't matter so set v=0
v_wind_input(:,1) = 0.0
;v_wind_input(:,2) = 0.0
;v_wind_input(:,3) = 0.0
;v_wind_input(:,4) = 0.0
;v_wind_input(:,5) = 0.0
;v_wind_input(:,6) = 0.0
;v_wind_input(:,7) = 0.0
;v_wind_input(:,2) = 0.0

sfcprs_input(:,0) = station1(:,8)     ; pressure in column 10 in example
sfcprs_input(:,1) = station2(:,8)     ; convert from hPa to Pa
;sfcprs_input(:,2) = station3(:,8)*100.0  
;sfcprs_input(:,3) = station4(:,8)*100.0  
;sfcprs_input(:,4) = station5(:,8)*100.0  
;sfcprs_input(:,5) = station6(:,8)*100.0  
;sfcprs_input(:,6) = station7(:,8)*100.0  
;sfcprs_input(:,7) = station8(:,8)*100.0  
;sfcprs_input(:,2) = station3(:,9) * 100.0

; RELATIVE humidity in column 9; convert to SPECIFIC humidity
;   1. calculate saturation vapor pressure from temperature
;   2. calculate vapor pressure from RH and 1.
;   3. calcuate spec hum using pressure and 2.

spechu_input(:,0) = station1(:,7)   ; this is actually RH in example
spechu_input(:,1) = station2(:,7)
;spechu_input(:,2) = station3(:,7)
;spechu_input(:,3) = station4(:,7)
;spechu_input(:,4) = station5(:,7)  
;spechu_input(:,5) = station6(:,7)  
;spechu_input(:,6) = station7(:,7)  
;spechu_input(:,7) = station8(:,7)  

;spechu_input(:,2) = station3(:,8)

;svp = 611.2*exp(17.67*(sfctmp_input-273.15)/(sfctmp_input-29.65)) ; [Pa]
;e   = spechu_input/100.0 * svp                                    ; [Pa]
;spechu_input = (0.622*e)/(sfcprs_input-(1.0-0.622)*e) ; now it is specific humidity

; DONE FILLING INPUT DATA STRUCTURE, NOW MOVE TO FORCING FILES
;
; Shouldn't need to modify anything below

do istep = 0, total_timesteps - 1
;nums(min_start)
 filename = yyyy_start+nums(mm_start)+nums(dd_start)+nums(hh_start)+".LDASIN_DOMAIN1"
 print( "Starting creation of: "+ filename )
 
 outfile = addfile(filename+".nc","c")
 filedimdef(outfile,(/"Time","south_north","west_east"/),(/1,1,number_stations/),(/True,False,False/))
 
 vartmp = new((/1,1,number_stations/),"float")
 vartmp!0 = "Time"
 vartmp!1 = "south_north"
 vartmp!2 = "west_east"
 
 vartmp(0,0,:) = (/ sfctmp_input(istep,:) /)  ; fill temporary structure with forcing
 vartmp@units = "K"
 outfile->T2D = vartmp
 
 vartmp(0,0,:) = (/ spechu_input(istep,:) /)  ; fill temporary structure with forcing
 vartmp@units = "kg/kg"
 outfile->Q2D = vartmp
 
 vartmp(0,0,:) = (/ u_wind_input(istep,:) /)  ; fill temporary structure with forcing
 vartmp@units = "m/s"
 outfile->U2D = vartmp

 vartmp(0,0,:) = (/ v_wind_input(istep,:) /)  ; fill temporary structure with forcing
 vartmp@units = "m/s"
 outfile->V2D = vartmp

 vartmp(0,0,:) = (/ sfcprs_input(istep,:) /)  ; fill temporary structure with forcing
 vartmp@units = "Pa"
 outfile->PSFC = vartmp

 vartmp(0,0,:) = (/ precip_input(istep,:) /)  ; fill temporary structure with forcing
 vartmp@units = "mm/s"
 outfile->RAINRATE = vartmp
 
 vartmp(0,0,:) = (/ swdown_input(istep,:) /)  ; fill temporary structure with forcing
 vartmp@units = "W/m^2"
 outfile->SWDOWN = vartmp
 
 vartmp(0,0,:) = (/ lwdown_input(istep,:) /)  ; fill temporary structure with forcing
 vartmp@units = "W/m^2"
 outfile->LWDOWN = vartmp
 
 delete(vartmp)
 
 system("mv "+filename+".nc "+filename)  ; get rid of the .nc
 
 ; now increment the time
 
 if(mod(yyyy_start,4).eq.0) then  ; take care of leap years, add more if necessary
   ddinmm(1) = 29
 end if
 
 ;min_start = min_start + min_spacing
 ;if(min_start .gt. 59) then
 ;	hh_start = hh_start + 1
 ;	min_start = min_start - 60
 ;end if
 
 hh_start = hh_start + hh_spacing
 if(hh_start .gt. 23) then
   dd_start = dd_start + 1
   hh_start = hh_start - 24
 end if
 
 if(dd_start .gt. ddinmm(mm_start-1)) then
   mm_start = mm_start + 1
   dd_start = 1
 end if
 
 if(mm_start .gt. 12) then
   yyyy_start = yyyy_start + 1
   mm_start = 1
 end if
 
end do

end

 
