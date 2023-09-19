
# This script takes two time series and plots them along with their cross correlation
# -----------------------------------



from gwpy.timeseries import TimeSeries
from gwpy.detector import ChannelList
import numpy as np 

from scipy import signal



#plot it 
from matplotlib import pyplot as plt
import scienceplots
plt.style.use('science')








"""
Given two timeseries x1 and x2, downsample to the same, and return the cross correlation and the lag,along with the time series
"""

def cross_correlate(x1,x2):


    #Downsample to one rate
    if x1.sample_rate > x2.sample_rate:
        #downsample x1
        x1 = x1.resample(x2.sample_rate)
    elif x1.sample_rate < x2.sample_rate:
        #downsample x2
        x2 = x2.resample(x1.sample_rate)

   
    #Make it a numpy array and save the sampling rate
    dt = x1.dt
    t = np.arange(len(x1)) * dt
    x1 = np.array(x1)
    x2 = np.array(x2)

    #Cross correlate using scipy
    #GWpy does have correlate function https://gwpy.github.io/docs/latest/examples/timeseries/correlate/
    #but it is a bit of a black box and I am not confident exactly waht is going on under the hood

    correlation_mode = "full"
    cross_correlation= signal.correlate(x1,x2,mode=correlation_mode) # mode can be ``full`, `valid` or `same`. Looks like GWpy uses `same`
    lags = signal.correlation_lags(len(x1), len(x2),mode=correlation_mode) * dt #time sampling is constant


    return t,x1,x2,lags,cross_correlation




def check_plot(t0,t1,x1_string, x2_string,fname):


    #Fetch the data
    h1   = TimeSeries.get(x1_string,t0, t1)
    h2   = TimeSeries.get(x1_string,t0, t1)

    #Cross correlate
    t,x1,x2,lags,cross_correlation = cross_correlate(h1,h2)



    #setup the plots figure
    axd = plt.figure(figsize=(20,12),layout="constrained").subplot_mosaic(
        """
        AB
        CB
        """,
        gridspec_kw = {'wspace':0, 'hspace':0}
)

    axd["A"].plot(t,x1)
    axd["C"].plot(t,x2)
    axd["B"].plot(lags,cross_correlation)


    ### Plot formatting
    axd["C"].set_xlabel('t [s]')
    axd["B"].set_xlabel(r'$\tau$ [s]')
    axd["B"].set_ylabel(r'$f \star g (\tau)$')
    axd["A"].set_ylabel(r'$f(t)$')
    axd["C"].set_ylabel(r'$g(t)$')


    fig = plt.gcf()
    fig.suptitle(f" Cross correlation of {x1_string} and {x2_string}",fontsize=20)
    plt.savefig(f"../data/{fname}.png",bbox_inches='tight', dpi=300)
    plt.close()







strain_channel = 'L1:GDS-CALIB_STRAIN'

#Timespan
t0 = 1172489751
t1 = 1172489815


check_plot(t0,t1,strain_channel,strain_channel,'newtest')

