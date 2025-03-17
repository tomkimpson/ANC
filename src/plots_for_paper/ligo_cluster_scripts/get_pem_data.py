
from gwpy.timeseries import TimeSeries
import numpy as np 


import matplotlib.pyplot as plt 
import scienceplots
plt.style.use('science')

#Manually copied from
#https://git.ligo.org/detchar/ligo-channel-lists/-/blob/master/O3/L1-O3-pem.ini
list_of_pem_channels = ['L1:PEM-CS_MAINSMON_EBAY_1_DQ',
                        'L1:PEM-CS_MAINSMON_EBAY_2_DQ',
                        'L1:PEM-CS_MAINSMON_EBAY_3_DQ',
                        'L1:PEM-EX_MAINSMON_EBAY_1_DQ',
                        'L1:PEM-EX_MAINSMON_EBAY_2_DQ',
                        'L1:PEM-EX_MAINSMON_EBAY_3_DQ',
                        'L1:PEM-EY_MAINSMON_EBAY_1_DQ',
                        'L1:PEM-EY_MAINSMON_EBAY_2_DQ',
                        'L1:PEM-EY_MAINSMON_EBAY_3_DQ',
                        ] 



strain_channel = 'L1:DCS-CALIB_STRAIN_C01_AR' #strain channel

#Setup the figure
num_pem_channels = len(list_of_pem_channels)
fig, axes = plt.subplots(nrows=num_pem_channels, ncols=1, figsize=(10,18),sharex=True)



#Time interval
start_time = 1238166208
num_intervals = 10
end_time = start_time + 64*num_intervals
times = np.arange(start_time, end_time, 64)




#Path to L1, O3 data files
root = '/archive/frames/O3/raw/L1/L-L1_R-12381/'
list_of_files = [root + f'L-L1_R-{t}-64.gwf' for t in times]


#Load the strain data
#hoft = TimeSeries.read(list_of_files,strain_channel)
hoft   = TimeSeries.get(strain_channel,start=start_time, end=end_time,host='losc-nds.ligo.org')
print("Sampling rate of the strain channel is ", hoft.sample_rate)




fs = 20
running_average = 0
for i in range(num_pem_channels):


    pem = list_of_pem_channels[i]

    #Load the pem channel from disk
    acc = TimeSeries.read(list_of_files,list_of_pem_channels[i])
    print(i, pem,acc.sample_rate)
    
    #Coherence
 #   coh = hoft.coherence(acc, fftlength=2, overlap=1)
    coh = hoft.coherence(acc,fftlength=8)


    coherence_frequencies = np.array(coh.frequencies)
    coherence_values = np.array(coh)
    

    print("Frequency resolution of coherence = ", coh.df)


    selected_idx = np.where(coherence_frequencies <= 100)[0]
    selected_f = coherence_frequencies[selected_idx]
    selected_v = coherence_values[selected_idx]


    print("Maximum coherence is", np.max(selected_v))
    running_average += np.max(selected_v)

    ax = axes[i]

    ax.plot(coherence_frequencies,coherence_values)

    idx = np.argmax(selected_v)
#    ax.scatter(selected_f[idx],selected_v[idx],c='r')
    print(selected_f[idx],selected_v[idx])

    ax.set_xlim(1, 100)
    ax.set_ylim(0, 1)

    ax.set_ylabel(r'$C_{xy}$',fontsize=fs)
    ax.axes.tick_params(axis="both", labelsize=fs-4)
    ax.set_title(pem)


    #ax.set_yscale('log')


axes[-1].set_xlabel(r'Frequency [Hz]',fontsize=fs)
fname='stacked_coherence_plot'
plt.savefig(f'{fname}',bbox_inches='tight',dpi=300)

print("The average max coherence value was = ", running_average/num_pem_channels)

