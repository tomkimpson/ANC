from scipy.io import loadmat
import numpy as np 


from matplotlib import pyplot as plt
import scienceplots
from mpl_toolkits.axes_grid1 import make_axes_locatable
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

import sys

plt.style.use('science')







path1 = "../../data/roc_sec4_1.mat"
path2 = "../../data/roc_sec4_2.mat"

import glob 





def load_and_plot(path,fname=None):


    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(12,12),sharex=False)

    data = loadmat(path)


    pd = data["pd"] #shape (3,1001)
    pfa = data["pfa"].flatten() #shape (1,1001)



    labels = [r'$\gamma = 0.001$', r'$\gamma = 0.01$',r'$\gamma = 0.1$']
    for i in range(len(pd)):
        ax.plot(pfa, pd[i,:], label = labels[i])




    fs = 20
    ax.set_xlabel("False positive rate",fontsize=fs)
    ax.set_ylabel("True positive rate",fontsize=fs)
    ax.axes.tick_params(axis="both", labelsize=fs-4)

    #plt.legend(title=None)
    #ax.set_title(r'$\Delta f = 0.0, \gamma = \{ 0.001, 0.01, 0.1 \} $, dataset = roc_sec4_1.mat ')

   
    if fname is not None:
        plt.savefig(f'../../data/images/{fname}',bbox_inches='tight',dpi=300)
        



    



load_and_plot(path1,fname='example_powerline_roc_curve_1')
load_and_plot(path2,fname='example_powerline_roc_curve_2')





#load_and_plot(path2)






# load_and_plot('pfa_h_002_gammah_0001_df_0_NO_PEM',
#               'pd_h_002_gammah_0001_df_0_NO_PEM',
#               'pfa_h_002_gammah_0001_df_0_ref_1',
#               'pd_h_002_gammah_0001_df_0_ref_1',
#               'pfa_h_002_gammah_0001_df_0_ref_2',
#               'pd_h_002_gammah_0001_df_0_ref_2',
#               ax,ls="dotted",
#              )





# # # Settings 2
# load_and_plot('pfa_h_002_gammah_001_df_05_NO_PEM',
#               'pd_h_002_gammah_001_df_05_NO_PEM',
#               'pfa_h_002_gammah_001_df_05_ref_1',
#               'pd_h_002_gammah_001_df_05_ref_1',
#               'pfa_h_002_gammah_001_df_05_ref_2',
#               'pd_h_002_gammah_001_df_05_ref_2',
#               ax,ls="solid")



# load_and_plot('pfa_h_002_gammah_001_df_0_NO_PEM',
#               'pd_h_002_gammah_001_df_0_NO_PEM',
#               'pfa_h_002_gammah_001_df_0_ref_1',
#               'pd_h_002_gammah_001_df_0_ref_1',
#               'pfa_h_002_gammah_001_df_0_ref_2',
#               'pd_h_002_gammah_001_df_0_ref_2',
#               ax,ls='dashed')



# fs = 20
# ax.set_xlabel(r'False postive rate',fontsize=fs)
# ax.set_ylabel(r'True positive rate',fontsize=fs)
# ax.axes.tick_params(axis="both", labelsize=fs-4)




# #     #plt.legend()

# # if fname is not None:
# fname='roc_final_stacked'
# plt.savefig(f'../../data/images/{fname}',bbox_inches='tight',dpi=300)


# # plt.show()



# plt.show()