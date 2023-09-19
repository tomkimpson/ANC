
#https://gwpy.github.io/docs/latest/examples/timeseries/correlate/

from gwpy.timeseries import TimeSeriesDict, TimeSeries
import pandas as pd
import sys
import numpy as np

L1_string = 'L1:DCS-CALIB_STRAIN_C01_AR'
pem = 'L1:PEM-CS_MAINSMON_EBAY_1_DQ'


#Select some times from the O3 segments
df = pd.read_csv('../../data/L1-O3a-segments.csv',header=None)
i = 0
t0 = df.iloc[i][0]
t1 = t0 + (10*60)#10 mins later
print("duration", t1-t0)



hoft   = TimeSeries.get(L1_string,start=t0, end=t1,host='losc-nds.ligo.org')
aux   = TimeSeries.get(pem,start=t0, end=t1,host='losc-nds.ligo.org')



print(hoft)
print(aux)
print("-------------------")

hoft = hoft.resample(aux.sample_rate) #downsample hoft
hoft.override_unit(aux.unit) 


print(hoft)
print(aux)



#whiten. Why?
#whoft = hoft.whiten(8, 4)
#waux = aux.whiten(8, 4)

snr = hoft.correlate(aux).abs()

plot = snr.plot()
plot.axes[0].set_ylabel('Signal-to-noise ratio', fontsize=16)
plot.show()

plot.savefig('/home/tom.kimpson/LIGO_ANC/data/coherence_time.png',bbox_inches='tight',dpi=300)





qhoft = hoft.q_transform(
    whiten=False,  # already white
    qrange=(4, 150),  # wider Q-transform range
   # outseg=(1172489782.57, 1172489783.57),  # region of interest
)
plot = qhoft.imshow(figsize=[8, 4])
ax = plot.gca()
ax.set_xscale('seconds')
ax.set_yscale('log')
#ax.set_epoch(1172489783.07)
#ax.set_ylim(20, 5000)
ax.set_ylabel('Frequency [Hz]')
ax.grid(True, axis='y', which='both')
ax.colorbar(cmap='viridis', label='Normalized energy', clim=[0, 25])
plot.show()

plot.savefig('/home/tom.kimpson/LIGO_ANC/data/coherence_time2D.png',bbox_inches='tight',dpi=300)
