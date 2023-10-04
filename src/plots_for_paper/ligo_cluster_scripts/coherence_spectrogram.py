
#https://gwpy.github.io/docs/stable/examples/spectrogram/coherence/#calculating-the-time-dependent-coherence-between-two-channels


from gwpy.timeseries import TimeSeriesDict, TimeSeries
import pandas as pd
import sys
import numpy as np

L1_string = 'L1:DCS-CALIB_STRAIN_C01_AR' #strain channel
pem = 'L1:PEM-CS_MAINSMON_EBAY_1_DQ'     # pem channel


t0 = 1238166208
#t0 = 1238163456 #the actual time O3a starts
#t0 = 1238163520
num_intervals = 57
#num_intervals = 10
t1 = t0 + 64*num_intervals 
times = np.arange(t0, t1, 64)
print("Duration of data segment:", t1-t0)

#Load the data, compute the coherence spectrogram
hoft   = TimeSeries.get(L1_string,start=t0, end=t1,host='losc-nds.ligo.org')

#Path to L1, O3 data files
root = '/archive/frames/O3/raw/L1/L-L1_R-12381/'
list_of_files = [root + f'L-L1_R-{t}-64.gwf' for t in times]





#hoft = TimeSeries.read(list_of_files,L1_string)

#Get the pem data
acc   = TimeSeries.read(list_of_files,pem)


#Canonical settings for spectrogram
pixel_width = 10
fftlength = .5
overlap = .25



#Settings for the coherence spectrogram
#delta f = 1/fft length
#fftlength = 60
#overlap=None

#fftlength=2
#overlap=1
#pixel_width = 640


#Get the coherence(f,t)
coh = hoft.coherence_spectrogram(acc, pixel_width, fftlength=fftlength, overlap=overlap)


#Make it a np array for extracting values
#...and surface some numbers
coh_array = np.array(coh) #shape 60 x 257, i.e. time x freq
slice_indexes = [29,30,31]
for s in slice_indexes:
    frequency_slice = coh_array[:,s]
    print("Frequency: ", coh.frequencies[s].value)
    print("The average coherence over the total time period is:", np.mean(frequency_slice))
    print("The variance is:", np.var(frequency_slice))





#Now plot it 


import matplotlib.pyplot as plt 
import scienceplots
plt.style.use('science')

plot = coh.plot()
ax = plot.gca()
ax.set_ylabel('Frequency [Hz]')
ax.set_yscale('log')
upper_f_limit = coh.yindex.max().value
ax.set_ylim(10, upper_f_limit)
ax.grid(True, 'both', 'both')
cbar = ax.colorbar(clim=[0, 1], cmap='plasma')
cbar.set_label(label=r'$C_{xr}(f)$',rotation=0)




savepath = 'coherence_spectrogram_canonical_new.png'
print("Saving figure at: ", savepath)
plot.savefig(savepath,bbox_inches='tight',dpi=300)







#Also get the max coherence over the entire time period 
#i.e. do what we did in get_pem_data.py
coh_net = hoft.coherence(acc, fftlength=fftlength, overlap=overlap)
coherence_frequencies = np.array(coh_net.frequencies)
coherence_values = np.array(coh_net)
  
  
selected_idx = np.where(coherence_frequencies <= 100)[0]
selected_f = coherence_frequencies[selected_idx]
selected_v = coherence_values[selected_idx]


#for i in range(len(selected_f)):
 #   print(selected_f[i], selected_v[i])

print("Maximum coherence over the entire time period is", np.max(selected_v))
