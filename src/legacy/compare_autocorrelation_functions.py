

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


#Get the correlation using the native correlate function e.g. https://gwpy.github.io/docs/latest/examples/timeseries/correlate/
correlation_GWpy = h.correlate(h)


#Correlate using scipy https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.correlate.html
h_np = np.array(h)

correlation_scipy = signal.correlate(h_np,h_np,mode="full") # mode can be ``full`, `valid` or `same`. Looks like GWpy uses `same`
lags = signal.correlation_lags(len(h_np), len(h_np),mode="full") * h.dt #time sampling is constant

#Check the length of the two solutions is the same
#assert len(correlation_scipy) == len(correlation_GWpy)

#plot it 
from matplotlib import pyplot as plt
import scienceplots
plt.style.use('science')
fig, (ax1,ax2) = plt.subplots(nrows=1, ncols=2, figsize=(20,12),sharex=False)

ax1.plot(correlation_GWpy)
ax2.plot(lags,correlation_scipy)


ax1.set_title("GWpy solution")
ax2.set_title("scipy solution")

plt.savefig("../data/compare_autocorrelation_methods.png")
plt.close()



