# Chimera command script showing Nup84 densities
#
#open *.mrc
#2.5 x Volume ; complex 2.5 x volume
#3-xray
#Nup120
volume #0 style surface level 0.00963 color forestgreen step 2
#Nup133
volume #1 style surface level 0.00959 color khaki step 2
#Nup145c
volume #2 style surface level 0.01 color gray step 2
#Nup84
volume #3 style surface level 0.00849 color lightblue step 2 
#Nup85 
volume #4 style surface level 0.00818 color gold step 2 
#Sec13 
volume #5 style surface level 0.0112 color brown step 2 
#Seh1 
volume #6 style surface level 0.0106 color dodgerblue step 2 
#all
volume #7 style surface transparency 0.9 level 0.00961 color white step 2 
volume all show
background solid white
set bgTransparency
echo script finished
