

#This script demonstrates how to load and query different slices of LIGO data


from gwpy.detector import ChannelList, Channel
from gwpy.detector import Channel
import sys


from gwosc.datasets import run_segment


import pandas as pd
import sys

print ("Welcome to a demo script for LIGO data loading")

#The start/end times of an observing run can be read as e.g.
O1_segment = run_segment('O1')
print("O1 timestamps:", O1_segment)
#...however this doesn't yet work for O3. 
# We have downloaded the O3a segments from https://gwosc.org/O3/o3a_multi/ 
df = pd.read_csv('../data/L1-O3a-segments.csv',header=None)


num_segments = len(df)
very_first_time = df.iloc[0][0]
very_last_time = df.iloc[-1][1]

duration = very_last_time - very_first_time

print("Duration of O3a in days: ", duration/(60*60*24))
print("Number of O3a segments: ", num_segments)



#Load a segment of data
i = 0
t0 = df.iloc[i][0]
t1 = df.iloc[i][1]

print("Duration of segment is: ", t1-t0)




from gwpy.timeseries import TimeSeries
test_channels = ["L1:PEM-EY_ACC_BEAMTUBE_MAN_Y_DQ","L1:DCS-CALIB_STRAIN_C01_AR", "L1:DCS-CALIB_STRAIN_CLEAN-SUB60HZ_C01"]
test_channels = ["L1:DCS-CALIB_STRAIN_CLEAN-SUB60HZ_C01"]



chan = "L1:DCS-CALIB_STRAIN_CLEAN_SUB60HZ_C01_AR"
data = TimeSeries.fetch(chan, start=1240559616, end=1240559626, host='losc-nds.ligo.org')

#for chan in test_channels:
 #   print(chan)
  #  data = TimeSeries.fetch(chan, start=t0, end=t1)# a, host='losc-nds.ligo.org')

print("completed")


