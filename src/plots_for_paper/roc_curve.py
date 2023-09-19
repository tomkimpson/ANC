from scipy.io import loadmat
import numpy as np 


from matplotlib import pyplot as plt
import scienceplots
from mpl_toolkits.axes_grid1 import make_axes_locatable
from mpl_toolkits.axes_grid1.inset_locator import inset_axes


plt.style.use('science')


path = "../../data/roc.mat"




def load_data(path):

    data = loadmat(path)
    roc_after_ANC = data['roc']
    roc_before_ANC = data['roc0']

    return roc_after_ANC,roc_before_ANC


def plot_roc(roc_after_ANC,roc_before_ANC,fname=None):

    #Plot figure
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(12,12),sharex=False)

    pfa_after = roc_after_ANC[:,0]
    pd_after = roc_after_ANC[:,1]

    pfa_before = roc_before_ANC[:,0]
    pd_before = roc_before_ANC[:,1]

    ax.plot(pfa_after,pd_after)
    ax.plot(pfa_before,pd_before)


    

    #Formattting
    fs = 20
    ax.set_xlabel(r'False postive rate',fontsize=fs)
    ax.set_ylabel(r'True positive rate',fontsize=fs)
    ax.axes.tick_params(axis="both", labelsize=fs-4)



    if fname is not None:
       plt.savefig(f'../../data//images/{fname}',bbox_inches='tight',dpi=300)


    plt.show()


roc_after_ANC,roc_before_ANC = load_data(path)
plot_roc(roc_after_ANC,roc_before_ANC,fname="roc")





