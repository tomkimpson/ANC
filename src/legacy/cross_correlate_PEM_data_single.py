
# This script cross correlates different ligo strain channels  with a single PEM channel, L1:PEM-CS_MAINSMON_EBAY_1_DQ
# It is a variation of `cross_correlate_PEM_data.py` but for a single PEM channel`
# -----------------------------------



from gwpy.timeseries import TimeSeries
import pandas as pd


# First select the channels we want to get data from

## Strain channels. Some different options here
strain_channels = ["L1:DCS-CALIB_STRAIN_CLEAN_SUB60HZ_C01_AR", # Reccomended channel, noise removed (linear + non linear)
                   "L1:DCS-CALIB_STRAIN_CLEAN_C01_AR",         # linear noise subtraction
                   "L1:DCS-CALIB_STRAIN_C01_AR"]               # no noise removed
                   # https://gwosc.org/O3/o3a_multi/  



## PEM channel
aux = "L1:PEM-CS_MAINSMON_EBAY_1_DQ"
#aux = "L1:PEM-EY_ACC_BEAMTUBE_MAN_Y_DQ"


# Get the timestamps over which O3 ran
# We have downloaded the O3a segments from https://gwosc.org/O3/o3a_multi/ 
df = pd.read_csv('../data/L1-O3a-segments.csv',header=None)

#Load a single segment of data. This is usually around 4000 seconds
i = 0
t0 = df.iloc[i][0]
t1 = df.iloc[i][1]
t1 = t0 + (60*10) #10 mins
print("Duration of segment is: ", t1-t0)


#Now cross correlate each strain channel with the PEM channel over this time period
from cross_correlate import check_plot
for h in strain_channels:
    lag,cc = check_plot(t0,t1,h,aux,f'10min_correlation_{h}_{aux}')



