
from matplotlib import pyplot as plt
import scienceplots
import glob
import numpy as np
plt.style.use('science')
rows = 9
cols = 1

fig, axes_object = plt.subplots(nrows=rows, ncols=cols, figsize=(12,40),sharex=True)
axes = fig.get_axes()


data_files = sorted(glob.glob("../data/*.npy"))




"""
Parse the fname ot get the PEM channel then load and plot the data
"""
def parse_load_plot(f,ax):


    pem = f.split('PEM_')[-1].split('.')[0]


    data=np.load(f)
    lag = data[0,:]
    cc  = data[1,:]
    
    exponent = np.abs(np.floor(np.log10(np.max(cc))))
    ax.plot(lag,cc*10**exponent)

    print(pem,exponent)
    exponent_int = int(exponent)
    fs=16

    ax.xaxis.set_tick_params(labelsize=fs-4)
    ax.yaxis.set_tick_params(labelsize=fs-4)
    ylabel = rf'$\rho$ ({pem}) $\times 10^{{{exponent_int}}}$'  
    ax.set_ylabel(ylabel ,fontsize=8)

    del data,lag,cc #explitly remove from memory



for i in range(len(data_files)):
    parse_load_plot(data_files[i],axes[i])
        

#Only label edge subplots
fs = 16
axes[-1].set_xlabel(r'$\tau [s]$',fontsize=fs)

plt.subplots_adjust(hspace=0.0)
plt.savefig('../data/vertical_stacked_pem_plot.png',bbox_inches='tight',dpi=300)


