from scipy.io import loadmat
import numpy as np 


from matplotlib import pyplot as plt
import scienceplots
from mpl_toolkits.axes_grid1 import make_axes_locatable
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

import sys

plt.style.use('science')


path = "../../data/roc_curves_final.mat"

import glob 





def load_and_plot(x1_str,y1_str,x2_str,y2_str,x3_str,y3_str,ax,ls):

    data = loadmat(path)
    for k in data.keys():
        print(k)

    x1 = data[x1_str].flatten()
    y1 = data[y1_str].flatten()

    x2 = data[y2_str].flatten()
    y2 = data[y2_str].flatten()

    x3 = data[x3_str].flatten()
    y3 = data[y3_str].flatten()


    ax.plot(x1,y1,linestyle=ls,c='C0')
    ax.plot(x2,y2,linestyle=ls,c='C1')
    ax.plot(x3,y3,linestyle=ls,c='C2')


 

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(12,12),sharex=False)








load_and_plot('pfa_h_002_gammah_0001_df_0_NO_PEM',
              'pd_h_002_gammah_0001_df_0_NO_PEM',
              'pfa_h_002_gammah_0001_df_0_ref_1',
              'pd_h_002_gammah_0001_df_0_ref_1',
              'pfa_h_002_gammah_0001_df_0_ref_2',
              'pd_h_002_gammah_0001_df_0_ref_2',
              ax,ls="dotted",
             )





# # Settings 2
load_and_plot('pfa_h_002_gammah_001_df_05_NO_PEM',
              'pd_h_002_gammah_001_df_05_NO_PEM',
              'pfa_h_002_gammah_001_df_05_ref_1',
              'pd_h_002_gammah_001_df_05_ref_1',
              'pfa_h_002_gammah_001_df_05_ref_2',
              'pd_h_002_gammah_001_df_05_ref_2',
              ax,ls="solid")



load_and_plot('pfa_h_002_gammah_001_df_0_NO_PEM',
              'pd_h_002_gammah_001_df_0_NO_PEM',
              'pfa_h_002_gammah_001_df_0_ref_1',
              'pd_h_002_gammah_001_df_0_ref_1',
              'pfa_h_002_gammah_001_df_0_ref_2',
              'pd_h_002_gammah_001_df_0_ref_2',
              ax,ls='dashed')



fs = 20
ax.set_xlabel(r'False postive rate',fontsize=fs)
ax.set_ylabel(r'True positive rate',fontsize=fs)
ax.axes.tick_params(axis="both", labelsize=fs-4)




#     #plt.legend()

# if fname is not None:
fname='roc_final_stacked'
plt.savefig(f'../../data/images/{fname}',bbox_inches='tight',dpi=300)


# plt.show()



plt.show()