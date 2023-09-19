
from matplotlib import pyplot as plt
import scienceplots
import glob
import numpy as np
plt.style.use('science')
rows = 3
cols = 3

fig, axes_object = plt.subplots(nrows=rows, ncols=cols, figsize=(20,12),sharex=False)
axes = fig.get_axes()


data_files = sorted(glob.glob("../data/*.npy"))








"""
Parse the fname ot get the PEM channel then load and plot the data
"""
def parse_load_plot(f,ax):


    pem = f.split('PEM_')[-1].split('.')[0]
    print(pem)


    data=np.load(f)
    lag = data[0,:]
    cc  = data[1,:]
    ax.plot(lag,cc)

    ax.title.set_text(pem)

    fs=16

    ax.xaxis.set_tick_params(labelsize=fs-4)
    ax.yaxis.set_tick_params(labelsize=fs-4)


    del data,lag,cc #explitly remove from memory



for i in range(len(data_files)):
    parse_load_plot(data_files[i],axes[i])
        

#Only label edge subplots
fs = 16

axes[0].set_ylabel(r'$\rho$',fontsize=fs)
axes[3].set_ylabel(r'$\rho$',fontsize=fs)
axes[6].set_ylabel(r'$\rho$',fontsize=fs)


axes[6].set_xlabel(r'$\tau [s]$',fontsize=fs)
axes[7].set_xlabel(r'$\tau [s]$',fontsize=fs)
axes[8].set_xlabel(r'$\tau [s]$',fontsize=fs)

plt.subplots_adjust(wspace=0.1,hspace=0.1)
plt.savefig('../data/stacked_pem_plot.png',bbox_inches='tight',dpi=300)


