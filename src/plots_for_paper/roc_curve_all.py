from scipy.io import loadmat
import numpy as np 


from matplotlib import pyplot as plt
import scienceplots
from mpl_toolkits.axes_grid1 import make_axes_locatable
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

import sys

plt.style.use('science')


path = "../../data/rocALL.mat"




def load_data(path):

    data = loadmat(path)

    return data['pd_PEM'].flatten(),data['pd_RLS'].flatten(),data['pd_no_PEM'].flatten(),data['pfa_PEM'].flatten(),data['pfa_RLS'].flatten(),data['pfa_no_PEM'].flatten()


def plot_roc(pd_PEM, pd_RLS, pd_no_PEM, pfa_PEM, pfa_RLS, pfa_no_PEM,fname=None):

    #Plot figure
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(12,12),sharex=False)



    ax.plot(pfa_PEM,pd_PEM,label = 'no filtering')
    ax.plot(pfa_no_PEM,pd_no_PEM,label = 'no interference')
    ax.plot(pfa_RLS,pd_RLS,label = 'RLS')


    # #Formattting
    fs = 20
    ax.set_xlabel(r'False postive rate',fontsize=fs)
    ax.set_ylabel(r'True positive rate',fontsize=fs)
    ax.axes.tick_params(axis="both", labelsize=fs-4)

    #plt.legend()

    if fname is not None:
        plt.savefig(f'../../data/images/{fname}',bbox_inches='tight',dpi=300)


    plt.show()

pd_PEM, pd_RLS, pd_no_PEM, pfa_PEM, pfa_RLS, pfa_no_PEM = load_data(path)

plot_roc(pd_PEM, pd_RLS, pd_no_PEM, pfa_PEM, pfa_RLS, pfa_no_PEM,fname="roc_new")





