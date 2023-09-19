

# This script cross correlates the ligo strain channel with various PEM channels
# A similar example is provided in the docs at https://gwpy.github.io/docs/stable/examples/timeseries/correlate/
# -----------------------------------



from gwpy.timeseries import TimeSeries
from gwpy.detector import ChannelList
import numpy as np 

from scipy import signal


# First select the channels we want to get data from
strain_channel = 'L1:GDS-CALIB_STRAIN'
pem_channel = "L1:PEM-CS_MAINSMON_EBAY_1_DQ"


#Timespan
t0 = 1172489751
t1 = 1172489815


#Get the data
h   = TimeSeries.get(strain_channel,t0, t1)
aux = TimeSeries.get(pem_channel,t0, t1)
aux = h
# PEM data usually at a lower rate  to strain data - downsample to one rate
h_downsampled = h.resample(aux.sample_rate)

#Set the units to be the same to allow for correlation
h_downsampled.override_unit(aux.unit) # using to() is preferred but '' (dimensionless) and 'NONE' are not convertible

#Get the correlation using the native correlate function e.g. https://gwpy.github.io/docs/latest/examples/timeseries/correlate/
correlation_GWpy = h_downsampled.correlate(aux)


#Correlate using scipy https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.correlate.html
h_np = np.array(h_downsampled)
aux_np = np.array(aux)

correlation_scipy = signal.correlate(h_np,aux_np,mode="same")




#Check the length of the two solutions is the same
assert len(correlation_scipy) == len(correlation_GWpy)


#plot it 
from matplotlib import pyplot as plt
import scienceplots
plt.style.use('science')
fig, (ax1,ax2) = plt.subplots(nrows=1, ncols=2, figsize=(20,12),sharex=False)

ax1.plot(correlation_GWpy)
ax2.plot(correlation_scipy)


ax1.set_title("GWpy solution")
ax2.set_title("scipy solution")

plt.savefig("../data/compare_correlation_methods.png")
plt.close()



