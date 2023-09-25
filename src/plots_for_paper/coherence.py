
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
#t0 = df.iloc[i][0]
t0 = 1238166208

#t1 = t0 + (10*60)#10 mins later
t1 = t0 + (60*60)#1 hour later
#t1 = t0 + (60)#1 hour later


print("Duration of data segment:", t1-t0)

#Load the data, compute the coherence spectrogram
hoft   = TimeSeries.get(L1_string,start=t0, end=t1,host='losc-nds.ligo.org')
acc   = TimeSeries.get(pem,start=t0, end=t1,host='losc-nds.ligo.org')

fftlength = .5
overlap=.25


fftlength = 2
overlap=1
interval = 10*60


coh = hoft.coherence_spectrogram(acc, interval, fftlength=fftlength, overlap=overlap)
#coh = hoft.coherence_spectrogram(acc, 10, fftlength=2, overlap=1)

#coh = hoft.coherence_spectrogram(acc, 100, fftlength=.5, overlap=.25)


#Make it a np array for extracting values
coh_array = np.array(coh) #shape 60 x 257, i.e. time x freq

slice_indexes = [29,30,31]

for s in slice_indexes:

#assert coh.frequencies[30].value == 60.0 #check you are selecting the correct index
    frequency_slice = coh_array[:,s]
    print("Frequency: ", coh.frequencies[s].value)
    print("The average coherence over the total time period is:", np.mean(frequency_slice))
    print("The variance is:", np.var(frequency_slice))






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
cbar = ax.colorbar(clim=[0, 1], cmap='plasma')


cbar.set_label(label=r'$C_{xr}(f)$',rotation=0)




#plot.show()
savepath = '../../data/manuscript_images/coherence_spectrogram_long4.png'
print("Saving figure at: ", savepath)
plot.savefig(savepath,bbox_inches='tight',dpi=300)







#Also get the max coherence over the entire time period 
coh_net = hoft.coherence(acc, fftlength=fftlength, overlap=overlap)
coherence_frequencies = np.array(coh_net.frequencies)
coherence_values = np.array(coh_net)
  
  
selected_idx = np.where(coherence_frequencies <= 100)[0]
selected_f = coherence_frequencies[selected_idx]
selected_v = coherence_values[selected_idx]



print("Maximum coherence over the entire time period is", np.max(selected_v))