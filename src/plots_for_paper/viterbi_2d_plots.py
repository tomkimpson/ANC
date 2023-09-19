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



def plot_2d(x,f,t,GW_f_true,vmin,vmax,GW_f_estim=None,fname=None,reverse_ordering=False):

    #Plot figure
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(15,9),sharex=False)
    pos = ax.imshow(x, cmap='viridis', interpolation='nearest',vmin=vmin,vmax=vmax,extent=[f[0],f[-1],t[0],t[-1]],aspect=1/200)
    lw = 2.0
    ls = '--'

    # manually reverse the ordering since it should go the other way around according to Sofia
    if reverse_ordering:
        GW_f_true = GW_f_true[::-1] 
    
    ax.plot(GW_f_true,t,c='C2',linewidth=lw,linestyle=ls)




    if GW_f_estim is not None:
        if reverse_ordering:
            GW_f_estim = GW_f_estim[::-1] 

        ax.plot(GW_f_estim,t,c='y',linewidth=lw,linestyle=ls)





    fs = 20
    ax.set_ylabel(r'Time [units?]',fontsize=fs)
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
    axins.axes.set_ylabel(r'$ \left |\mathcal{F} \left[ h(t)\right] \right|^2$',rotation=0,fontsize=fs,labelpad=25)


    ax.set_xlim(f[0],f[-1])
    ax.set_ylim(t[0],t[-1])


    if fname is not None:
       plt.savefig(f'../../data//images/{fname}',bbox_inches='tight',dpi=300)




    plt.show()








#Path 1
viterbi_with_pem,viterbi_without_pem,f,t,GW_freq_true,GW_freq_estim = load_data(path1)



##Low contrast
cbar_lower_limit = np.min(viterbi_with_pem)
cbar_upper_limit = np.max(viterbi_with_pem)
plot_2d(viterbi_with_pem.T,f,t,GW_freq_true,cbar_lower_limit,cbar_upper_limit,fname="BeforeANC_example_1_low_contrast",reverse_ordering=True)
plot_2d(viterbi_without_pem.T,f,t,GW_freq_true,cbar_lower_limit,cbar_upper_limit,GW_freq_estim,fname="AfterANC_example_1_low_contrast",reverse_ordering=True)


##High contrast
cbar_lower_limit = np.min(viterbi_without_pem)
cbar_upper_limit = np.max(viterbi_without_pem)
plot_2d(viterbi_with_pem.T,f,t,GW_freq_true,cbar_lower_limit,cbar_upper_limit,fname="BeforeANC_example_1_high_contrast",reverse_ordering=True)
plot_2d(viterbi_without_pem.T,f,t,GW_freq_true,cbar_lower_limit,cbar_upper_limit,GW_freq_estim,fname="AfterANC_example_1_high_contrast",reverse_ordering=True)





#Path 2 
viterbi_with_pem,viterbi_without_pem,f,t,GW_freq_true,GW_freq_estim = load_data(path2)


## Low contrast
cbar_lower_limit = np.min(viterbi_with_pem)
cbar_upper_limit = np.max(viterbi_with_pem)
plot_2d(viterbi_with_pem.T,f,t,GW_freq_true,cbar_lower_limit,cbar_upper_limit,fname="BeforeANC_example_2_low_contrast",reverse_ordering=True)
plot_2d(viterbi_without_pem.T,f,t,GW_freq_true,cbar_lower_limit,cbar_upper_limit,GW_freq_estim,fname="BeforeANC_example_2_low_contrast",reverse_ordering=True)

## High contrast
cbar_lower_limit = np.min(viterbi_without_pem)
cbar_upper_limit = np.max(viterbi_without_pem)
plot_2d(viterbi_with_pem.T,f,t,GW_freq_true,cbar_lower_limit,cbar_upper_limit,fname="BeforeANC_example_2_high_contrast",reverse_ordering=True)
plot_2d(viterbi_without_pem.T,f,t,GW_freq_true,cbar_lower_limit,cbar_upper_limit,GW_freq_estim,fname="AfterANC_example_2_high_contrast",reverse_ordering=True)

