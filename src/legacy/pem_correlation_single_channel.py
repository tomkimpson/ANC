

# This script cross correlates the ligo strain channel with various PEM channels
# A similar example is provided in the docs at https://gwpy.github.io/docs/stable/examples/timeseries/correlate/
# -----------------------------------



from gwpy.timeseries import TimeSeries
from gwpy.detector import ChannelList
import numpy as np 



# First select the channels we want to get data from

## Strain channels
strain_channels = ['L1:GDS-CALIB_STRAIN',  'H1:GDS-CALIB_STRAIN']
#strain_channels = ['L1:DCS-CALIB_STRAIN_CO2',  'H1:DCS-CALIB_STRAIN_CO2'] alternatively we can use these strain channels. Which is preferred?


## PEM channels
## Two options here. Can get ALL PEM channels or just those listed in the open data release



# Option 1: all PEM channels. Following example of https://git.ligo.org/gwosc/tutorials/gwosc-aux-tutorials/-/blob/main/Tutorials/data_access.ipynb
chanlist = ChannelList.query_nds2('*', host='losc-nds.ligo.org' )
pem_channel_H1 = [chan for chan in chanlist if 'H1:PEM' in chan.name]
pem_channel_L1 = [chan for chan in chanlist if 'L1:PEM' in chan.name]


# Option 2: open pem channels
import pandas as pd
url = "https://git.ligo.org/gwosc/tutorials/gwosc-aux-tutorials/-/raw/main/Channels/O3_bulk_aux_channel_list.csv"
df=pd.read_csv(url,on_bad_lines='skip')

df_PEM_H1 = df[df['Channel'].str.contains("H1:PEM")]
df_PEM_L1 = df[df['Channel'].str.contains("L1:PEM")]




print (f"We have {len(pem_channel_H1)} H1 channels and {len(pem_channel_L1)} L1 channels in the full dataset")
print (f"We have {len(df_PEM_H1)} H1 channels and {len(df_PEM_L1)} L1 channels in the open dataset")



from scipy import signal

def correlate_data(strain_channel,pem_channel,t0,t1):


    print(f"Correlating data from {strain_channel} and {pem_channel} for the time period {t0} + {t1-t0} seconds")

    #Get the data
    h   = TimeSeries.get(strain_channel,t0, t1)
    aux = TimeSeries.get(pem_channel,t0, t1)

    # PEM data usually at a lower rate  to strain data - downsample to one rate
    h_downsampled = h.resample(aux.sample_rate)

    #Set the units to be the same to allow for correlation
    h_downsampled.override_unit(aux.unit) # using to() is preferred but '' (dimensionless) and 'NONE' are not convertible


    h_np = np.array(h_downsampled)
    aux_np = np.array(aux)


#    return h_downsampled.correlate(aux)
 #   return np.correlate(h_np,aux_np) 
    return signal.correlate(h_np,aux_np)


#Timespan
t0 = 1172489751
t1 = 1172489815
h = strain_channels[0]
aux = df_PEM_L1['Channel'].iloc[0]
d = correlate_data(h,aux,t0,t1)

print(d)
import matplotlib.pyplot as plt 

plt.plot(d)
plt.savefig("example-np.png")
plt.close()



