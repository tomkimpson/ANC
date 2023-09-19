from scipy.io import loadmat
import numpy as np 


from matplotlib import pyplot as plt
import scienceplots
from mpl_toolkits.axes_grid1 import make_axes_locatable
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

import sys

plt.style.use('science')


path = "../../data/rocNref.mat"




def load_data(path):

    data = loadmat(path)


    return data['pd_1ref'].flatten(),data['pd_2ref'].flatten(),data['pfa_1ref'].flatten(),data['pfa_2ref'].flatten()
    
    
    
    
    
 


def plot_roc(pd_1ref, pd_2ref, pfa_1ref, pfa_2ref,fname=None):

    #Plot figure
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(12,12),sharex=False)

    ax.plot(pfa_1ref,pd_1ref,label = 'ref 1')
    ax.plot(pfa_2ref,pd_2ref,label = 'ref 2')
 
    # #Formattting
    fs = 20
    ax.set_xlabel(r'False postive rate',fontsize=fs)
    ax.set_ylabel(r'True positive rate',fontsize=fs)
    ax.axes.tick_params(axis="both", labelsize=fs-4)

    plt.legend()

    if fname is not None:
        plt.savefig(f'../../data/images/{fname}',bbox_inches='tight',dpi=300)


    plt.show()

pd_1ref, pd_2ref, pfa_1ref, pfa_2ref = load_data(path)
plot_roc(pd_1ref, pd_2ref, pfa_1ref, pfa_2ref,fname="roc_new_n_pem")





