from scipy.io import loadmat
import numpy as np 


from matplotlib import pyplot as plt
import scienceplots
from mpl_toolkits.axes_grid1 import make_axes_locatable
from mpl_toolkits.axes_grid1.inset_locator import inset_axes


plt.style.use('science')









data = loadmat("../data/fig_plot_8_and_9_viterbi_path_ANC_example_1.mat")

print(data.keys())

viterbi_with_pem = data['Y'] #Viterbi input matrix with PEM and GW. (131, 50)
viterbi_without_pem = data['y'] # Viterbi input matrix with PEM cancelled #(131, 50)
f = data['w0'].flatten()
t = data['time'].flatten()

GW_freq_true  = data['fq'].flatten()
GW_freq_estim  = data['fhat_RLS'].flatten() #estimated GW frequency (with Viterbi) after the ANC



def plot_2d(x,f,t,GW_f_true,GW_f_estim=None,fname=None):

    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(15,9),sharex=False)
    pos = ax.imshow(x, cmap='viridis', interpolation='nearest',vmin=np.min(x),vmax=np.max(x),extent=[f[0],f[-1],t[0],t[-1]],aspect=1/200)


    lw = 2.0
    ls = '--'
    ax.plot(GW_f_true,t,c='C2',linewidth=lw,linestyle=ls)

    if GW_f_estim is not None:
        print("plottign estimated")
        ax.plot(GW_f_estim,t,c='y',linewidth=lw,linestyle=ls)


    fs = 20
    ax.set_ylabel(r'Time',fontsize=fs)
    ax.set_xlabel(r'$f$ [Hz]',fontsize=fs)
    ax.axes.tick_params(axis="both", labelsize=fs-4)



    axins = inset_axes(ax, width = "5%", height = "100%", loc = 'lower left',
                       bbox_to_anchor = (1.02, 0., 1, 1), bbox_transform = ax.transAxes,
                       borderpad = 0)
    fig.colorbar(pos, cax = axins)

    axins.axes.tick_params(axis="both", labelsize=fs-4)
    axins.axes.tick_params(axis="both", labelsize=fs-4)
    #axins.set_label('# of contacts', labelsize=fs)
    #axins.axes.set_title('V',fontsize=fs)
    #axins.axes.set_xlabel('dfdfdfdf')
    axins.axes.set_ylabel('X',rotation=0,fontsize=fs)


    if fname is not None:
       plt.savefig(f'../data/images/{fname}',bbox_inches='tight',dpi=300)




    plt.show()




plot_2d(viterbi_with_pem.T,f,t,GW_freq_true,fname="BeforeANC")

plot_2d(viterbi_without_pem.T,f,t,GW_freq_true,GW_freq_estim,"AfterANC")