from scipy.io import loadmat
import numpy as np 


from matplotlib import pyplot as plt
import scienceplots
from mpl_toolkits.axes_grid1 import make_axes_locatable
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

import sys

plt.style.use('science')


path = "../../data/filter_order_experiments.mat"

data = loadmat(path)



print(data)



L_1ref = data['L_1ref'].flatten()
L_2ref = data['L_2ref'].flatten()

m1 = data['m1'].flatten()
m2 = data['m2'].flatten()

m1=np.arange(len(L_1ref))
m2=np.arange(len(L_2ref))



 #Plot figure
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(12,12),sharex=False)

ax.plot(m1,L_1ref,label = 'ref 1')
ax.plot(m2,L_2ref,label = 'ref 2')


# #Formattting
fs = 20
ax.set_xlabel(r'M',fontsize=fs)
ax.set_ylabel(r'$\hat{h}$',fontsize=fs)
ax.axes.tick_params(axis="both", labelsize=fs-4)

#plt.legend()

# if fname is not None:

fname = "filter_order"
plt.savefig(f'../../data/images/{fname}',bbox_inches='tight',dpi=300)
plt.show()
