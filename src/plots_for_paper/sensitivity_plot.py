from gwpy.timeseries import TimeSeries
from matplotlib import pyplot as plt
import scienceplots
import pandas as pd 
import numpy as np 

plt.style.use('science')



#Example from https://gwpy.github.io/docs/latest/spectrum/
#gwdata = TimeSeries.get('H1:LDAS-STRAIN', 'September 16 2010 06:40','September 16 2010 06:50')

print("hello")
#Channels that we will plot the ASD of
L1_string = 'L1:DCS-CALIB_STRAIN_C01_AR'
H1_string = 'H1:DCS-CALIB_STRAIN_C01_AR'


#Setelct some times from the O3 segments
df = pd.read_csv('../../data/L1-O3a-segments.csv',header=None)
i = 0
t0 = df.iloc[i][0]
t1 = t0 + (10*60)#10 mins later


#Get the data
print("get the data")
gwdata_L1   = TimeSeries.get(L1_string,start=t0, end=t1,host='losc-nds.ligo.org')
spectrum_L1 = gwdata_L1.asd(8, 4) #Welch method. Also used in GWPy example

print("get data 2")
gwdata_H1   = TimeSeries.get(H1_string,start=t0, end=t1,host='losc-nds.ligo.org')
spectrum_H1 = gwdata_H1.asd(8, 4) #Welch method. Also used in GWPy example



freqs_L1 = np.arange(len(spectrum_L1))*spectrum_L1.df
asd_L1 = np.array(spectrum_L1)


freqs_H1 = np.arange(len(spectrum_H1))*spectrum_H1.df
asd_H1 = np.array(spectrum_H1)



print("plot ti ")
from matplotlib import pyplot as plt
import scienceplots
import glob
import numpy as np
plt.style.use('science')

#fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(12,8),sharex=False)

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(12,12),sharex=False)

ax.plot(freqs_L1,asd_L1,c="C0")
ax.plot(freqs_H1,asd_H1,c="C2")



ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlim(10, 5000)
ax.set_ylim(3e-24, 5e-20)


fs = 20
ax.set_ylabel(r'GW strain ASD [strain$/\sqrt{\mathrm{Hz}}$]',fontsize=fs)
ax.set_xlabel(r'f [Hz]',fontsize=fs)


ax.axes.tick_params(axis="both", labelsize=fs-4)



#Add an inset plot as https://git.ligo.org/hannah.middleton/anc/-/blob/master/code/plottingScripts/asdInset/plotASDInsetFromGWOSC.py

#import matplotlib.pyplot as plt
#from mpl_toolkits.axes_grid1.inset_locator import (inset_axes, InsetPosition,
 #                                                 mark_inset)
#ax2 = plt.axes([0,0,1,1])
# Manually set the position and relative size of the inset axes within ax1
#ip = InsetPosition(ax, [0.3,0.45,0.4,0.5])
#ax2.set_axes_locator(ip)



#ax2.plot(freqs_L1,asd_L1,c="C0")
#ax2.plot(freqs_H1,asd_H1,c="C2")

# Mark the region corresponding to the inset axes on ax1 and draw lines
# in grey linking the two axes.
#mark_inset(ax, ax2, loc1=2, loc2=4, fc="none", ec='0.5')
#ax2.set_yscale('log')
#ax2.set_ylim(1e-23,1e-21)
#ax2.set_xlim(57,63)

















#plt.savefig('../../data/manuscript_images/sensitivity.png',bbox_inches='tight',dpi=300)
plt.savefig('../../data/manuscript_images/sensitivity_sq.png',bbox_inches='tight',dpi=300)

