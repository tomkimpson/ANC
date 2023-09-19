#!/opt/local/bin/python

import numpy
import gwpy
from gwpy.plot import Plot
from gwpy import frequencyseries
import matplotlib as mpl
mpl.use('agg')
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)

majorFormatter = FormatStrFormatter('%d')

mpl.rc('axes', labelsize=20, edgecolor='k')
mpl.rc('xtick', labelsize=20)
mpl.rc('ytick', labelsize=20)
mpl.rc('font', family='Times New Roman')


red  = '#D55E00'  #213, 94, 0
blue = '#56B4E9'  #86, 180, 233


H1data = frequencyseries.FrequencySeries.read('2017-06-10_DCH_C02_H1_O2_Sensitivity_strain_asd.txt')
L1data = frequencyseries.FrequencySeries.read('2017-08-06_DCH_C02_L1_O2_Sensitivity_strain_asd.txt')
#V1data = frequencyseries.FrequencySeries.read('Hrec_hoft_V1O2Repro2A_16384Hz.txt')

plot = Plot(figsize=(10, 6.18))
ax = plot.gca(xscale='log', xlim=(10, 5000), xlabel='Frequency (Hz)',
              yscale='log', ylim=(3e-24, 5e-20),
              ylabel=r'Strain noise (\sqrt{ Hz})')

ax.xaxis.set_major_formatter(majorFormatter)

#kw = {'marker': '.', 'markersize': 1, 'linestyle': ''}

for i, (data, label, col) in enumerate([
        (H1data, 'LIGO-Hanford', red),
        (L1data, 'LIGO-Livingston', blue),
#        (V1data, 'Virgo'),
]):
    color = 'gwpy:{}'.format(label.lower())
    ax.plot([0], label=label, color=col)  # dummy for labelling
    ax.plot(data.frequencies, data.value,
            color=col)

#plot.show()
#ax.grid(color='darkgrey', linewidth=1, linestyle='--')



# the inset
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid.inset_locator import (inset_axes, InsetPosition,
                                                  mark_inset)
ax2 = plt.axes([0,0,1,1])
# Manually set the position and relative size of the inset axes within ax1
ip = InsetPosition(ax, [0.2,0.45,0.4,0.5])
ax2.set_axes_locator(ip)
# Mark the region corresponding to the inset axes on ax1 and draw lines
# in grey linking the two axes.
mark_inset(ax, ax2, loc1=2, loc2=4, fc="none", ec='0.5')

import numpy as np
for (data,color) in ([(H1data, red), (L1data, blue)]):

    fstep = data.df.value
    fmin = min(data.frequencies.value)
    indexLow  = int( (50.-fmin) / fstep ) + 1
    indexHigh = int( (70.-fmin) / fstep ) 
    fs = data.frequencies[indexLow:indexHigh]
    vs = data.value[indexLow:indexHigh]
    ax2.plot(data.frequencies[indexLow:indexHigh],data.value[indexLow:indexHigh], color=color)


ax2.set_yscale('log')
ax2.set_ylim(7e-24,3e-23)
ax2.set_xlim(57,63)

ax.legend()

#plot.save('/home/hannah.middleton//public_html/o2catalog-asd.pdf')
#plot.save('~/hannah.middleton/public_html/o2catalog-asd.png')

