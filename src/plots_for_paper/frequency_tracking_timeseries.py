from scipy.io import loadmat
import numpy as np 


from matplotlib import pyplot as plt
import scienceplots
from mpl_toolkits.axes_grid1 import make_axes_locatable
from mpl_toolkits.axes_grid1.inset_locator import inset_axes


plt.style.use('science')


path1 = "../../data/fig_plot_8_and_9_viterbi_path_ANC_example_1.mat"
path2 = "../../data/fig_plot_8_and_9_viterbi_path_ANC_example_2.mat"



def load_data(path):

    data = loadmat(path)


    viterbi_with_pem = data['Y'] #Viterbi input matrix with PEM and GW. (131, 50)
    viterbi_without_pem = data['y'] # Viterbi input matrix with PEM cancelled #(131, 50)
    f = data['w0'].flatten()
    t = data['time'].flatten()

    GW_freq_true  = data['fq'].flatten()
    GW_freq_estim  = data['fhat_RLS'].flatten() #estimated GW frequency (with Viterbi) after the ANC

    return viterbi_with_pem,viterbi_without_pem,f,t,GW_freq_true,GW_freq_estim



def plot_timeseries(t,GW_f_true,GW_f_estim,fname=None):

    #Plot figure
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(12,12),sharex=False)


    ax.plot(t,GW_f_true)
    ax.scatter(t,GW_f_true)

    ax.plot(t,GW_f_estim)
    ax.scatter(t,GW_f_estim)


    fs = 20
    ax.set_xlabel(r'Time [units?]',fontsize=fs)
    ax.set_ylabel(r'$f$ [Hz]',fontsize=fs)
    ax.axes.tick_params(axis="both", labelsize=fs-4)

    if fname is not None:
       plt.savefig(f'../../data//images/{fname}',bbox_inches='tight',dpi=300)

    plt.show()



#Path 1
viterbi_with_pem,viterbi_without_pem,f,t,GW_freq_true,GW_freq_estim = load_data(path1)
plot_timeseries(t,GW_freq_true,GW_freq_estim,fname='timeseries_f_tracking_example_1')

#Path 2
viterbi_with_pem,viterbi_without_pem,f,t,GW_freq_true,GW_freq_estim = load_data(path2)
plot_timeseries(t,GW_freq_true,GW_freq_estim,fname='timeseries_f_tracking_example_2')
