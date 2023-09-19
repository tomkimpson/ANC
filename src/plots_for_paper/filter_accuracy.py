from scipy.io import loadmat
import numpy as np 

import matplotlib.pyplot as plt 

path = "../../data/filter_accuraacy.mat"

data = loadmat(path)
LL = data["LL"]
dw = data["dw"]
gamma = data["gamma"]
gamma_a = data["gamma_a"]
h = data["h"]







#Plot figure
fig, ax1 = plt.subplots(nrows=1, ncols=1, figsize=(12,12))


for i in range(4):
    y = LL[i,:]
    x = np.arange(len(y))

    ax1.plot(x,y)
    ax1.scatter(x,y)




fs = 20
ax1.set_ylabel(r'MSE',fontsize=fs)
ax1.set_xlabel(r'Number of taps',fontsize=fs)
ax1.axes.tick_params(axis="both", labelsize=fs-4)
  
fname = "taps_vs_error"
plt.savefig(f'../../data/images/{fname}',bbox_inches='tight',dpi=300)

plt.show()
