
#https://gwpy.github.io/docs/stable/examples/spectrogram/coherence/#calculating-the-time-dependent-coherence-between-two-channels


from gwpy.timeseries import TimeSeriesDict, TimeSeries
import pandas as pd
import sys
import numpy as np

L1_string = 'L1:DCS-CALIB_STRAIN_C01_AR' #strain channel
pem = 'L1:PEM-CS_MAINSMON_EBAY_1_DQ'     # pem channel


#Selelct some times from the O3 segments
df = pd.read_csv('../../data/L1-O3a-segments.csv',header=None)
i = 0
t0 = df.iloc[i][0]
t1 = t0 + (10*60)#10 mins later

print("Duration of data segment:", t1-t0)

#Load the data, compute the coherence spectrogram
hoft   = TimeSeries.get(L1_string,start=t0, end=t1,host='losc-nds.ligo.org')
acc   = TimeSeries.get(pem,start=t0, end=t1,host='losc-nds.ligo.org')
coh = hoft.coherence_spectrogram(acc, 10, fftlength=.5, overlap=.25)



upper_f_limit = coh.yindex.max().value


import matplotlib.pyplot as plt 
import scienceplots
plt.style.use('science')

plot = coh.plot()
ax = plot.gca()
ax.set_ylabel('Frequency [Hz]')
ax.set_yscale('log')
ax.set_ylim(10, upper_f_limit)
#ax.set_title(
 #   f'Coherence between {L1_string} and {pem}',
#)
ax.grid(True, 'both', 'both')
ax.colorbar(label='Coherence', clim=[0, 1], cmap='plasma')


#plot.show()
savepath = '../../data/manuscript_images/coherence_spectrogram.png'
print("Saving figure at: ", savepath)
plot.savefig(savepath,bbox_inches='tight',dpi=300)

