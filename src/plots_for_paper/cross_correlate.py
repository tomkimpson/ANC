
# This module defines a cross correlation function and a plotter
# It takes two time series and plots them along with their cross correlation
# The cross correlation is done using scipy. GWpy does have correlate function https://gwpy.github.io/docs/latest/examples/timeseries/correlate/
# but it is a bit of a black box and I am not confident exactly what is going on under the hood
# -----------------------------------

from gwpy.timeseries import TimeSeries
from gwpy.detector import ChannelList
import numpy as np 

from scipy import signal



#plot it 
from matplotlib import pyplot as plt
import scienceplots
plt.style.use('science')

from astropy import units as u


"""
Given two timeseries x1 and x2, downsample to the same, and return the cross correlation and the lag,along with the time series
"""

def cross_correlate(x1,x2):

    
    print("Original sampling rates for two channels (Hz): ",x1.sample_rate, x2.sample_rate)
    
    selected_sample_rate = 1024.0 * u.Hz 


    if x1.sample_rate != selected_sample_rate:
        print("resampling x1", x1.sample_rate, selected_sample_rate)
        x1 = x1.resample(selected_sample_rate)


    if x2.sample_rate != selected_sample_rate:
        print("resampling x2", x2.sample_rate, selected_sample_rate)
        x2 = x2.resample(selected_sample_rate)


    print("Resampled rates(Hz): ",x1.sample_rate, x2.sample_rate)



    #Make it a numpy array and save the sampling rate
    dt = x1.dt
    t = np.arange(len(x1)) * dt
    x1 = np.array(x1)
    x2 = np.array(x2)

    #Cross correlate using scipy


    correlation_mode = "full"
    cross_correlation= signal.correlate(x1,x2,mode=correlation_mode) # mode can be ``full`, `valid` or `same`. Looks like GWpy uses `same`
    lags = signal.correlation_lags(len(x1), len(x2),mode=correlation_mode) * dt #time sampling is constant


    return t,x1,x2,lags,cross_correlation




def check_plot(t0,t1,x1_string, x2_string,fname):


    #Fetch the data
    print("Cross correlating ", x1_string, " and", x2_string)
    h1   = TimeSeries.get(x1_string,start=t0, end=t1,host='losc-nds.ligo.org')
    h2   = TimeSeries.get(x2_string,start=t0, end=t1,host='losc-nds.ligo.org')


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
    fs = 20
    axd["C"].set_xlabel('t [s]')
    axd["B"].set_xlabel(r'$\tau$ [s]',fontsize = fs)
    axd["B"].set_ylabel(r'$(h \star$ PEM$) (\tau)$',fontsize = fs)
    axd["A"].set_ylabel(r'$h(t)$', fontsize = fs)
    axd["C"].set_ylabel(r'PEM$(t)$',fontsize = fs)




   
    axd["A"].axes.tick_params(axis="both", labelsize=fs-4)
    axd["B"].axes.tick_params(axis="both", labelsize=fs-4)
    axd["C"].axes.tick_params(axis="both", labelsize=fs-4)





    fig = plt.gcf()
    #fig.suptitle(f" Cross correlation of {x1_string} and {x2_string}",fontsize=20)
    #plt.savefig(f"../data/images/{fname}.png",bbox_inches='tight', dpi=300)
    savepath = f"../../data/images/{fname}.png"
    print("Saving image at:", savepath)
    #plt.show()
    plt.savefig(savepath,dpi=300)
    plt.close()

    print('------------------------------------------')
    return lags,cross_correlation 



