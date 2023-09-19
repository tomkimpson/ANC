
# This script cross correlates the ligo strain channel with various PEM channels
# -----------------------------------



from gwpy.timeseries import TimeSeries
from gwpy.detector import ChannelList
import numpy as np


# First select the channels we want to get data from

## Strain channels
#strain_channels = ['L1:GDS-CALIB_STRAIN',  'H1:GDS-CALIB_STRAIN'] #low latency, O1
#strain_channels = ['L1:DCS-CALIB_STRAIN_CO2',  'H1:DCS-CALIB_STRAIN_CO2'] #high latency
strain_channels = ['L1:DCS-CALIB_STRAIN_C01_AR',  'H1:DCS-CALIB_STRAIN_C01_AR'] 


## PEM channels
## Two options here. Can get ALL PEM channels or just those listed in the open data release

### Option 1: all PEM channels. Following example of https://git.ligo.org/gwosc/tutorials/gwosc-aux-tutorials/-/blob/main/Tutorials/data_access.ipynb
chanlist = ChannelList.query_nds2('*', host='losc-nds.ligo.org' )
pem_channel_H1 = [chan for chan in chanlist if 'H1:PEM' in chan.name]
pem_channel_L1 = [chan for chan in chanlist if 'L1:PEM' in chan.name]


### Option 2: open pem channels
import pandas as pd
url = "https://git.ligo.org/gwosc/tutorials/gwosc-aux-tutorials/-/raw/main/Channels/O3_bulk_aux_channel_list.csv"
df=pd.read_csv(url,on_bad_lines='skip')

df_PEM_H1 = df[df['Channel'].str.contains("H1:PEM")]
df_PEM_L1 = df[df['Channel'].str.contains("L1:PEM")]

print (f"We have {len(pem_channel_H1)} H1 channels and {len(pem_channel_L1)} L1 channels in the full dataset")
print (f"We have {len(df_PEM_H1)} H1 channels and {len(df_PEM_L1)} L1 channels in the open dataset")






#Worked exmple: Cross correlate the Livingston strain data with the 9 open PEM L1 channels 
#Timespan
h = strain_channels[0]
#Load O3 segments
df = pd.read_csv('../data/L1-O3a-segments.csv',header=None)
#Load a segment of data
i = 0
t0 = df.iloc[i][0]
t1 = df.iloc[i][1]
print("Duration of segment is: ", t1-t0)
print("--------------------------------------------------")
print("--------------------------------------------------")
print("--------------------------------------------------")




from cross_correlate import check_plot
for i in range(len(df_PEM_L1)):
    aux = df_PEM_L1['Channel'].iloc[i]
    lag,cc = check_plot(t0,t1,h,aux,f'correlation_{h}_{aux}')

    #save the data for manipulation later
    IO_array = np.array([lag,cc])
    np.save(f'../data/correlation_h_{h}_PEM_{aux}.npy',IO_array)



