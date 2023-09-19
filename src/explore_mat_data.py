from scipy.io import loadmat
import numpy as np 


from matplotlib import pyplot as plt
import scienceplots
plt.style.use('science')









data = loadmat("../data/fig_spectrum.mat")
C = data['C'].flatten()
Q = data['Q'].flatten()
S = data['S'].flatten()
w = data['w'].flatten()



fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(12,8),sharex=False)


ax.plot(w,C,label="Cancelled signal")
ax.plot(w,Q,label="GW signal")
ax.plot(w,S,label="Primary signal")






# ax.plot(freqs_H1,asd_H1,c="C2")





# ax.set_xlim(10, 5000)
# ax.set_ylim(3e-24, 5e-20)


fs = 20
ax.set_ylabel(r'Amplitude',fontsize=fs)
ax.set_xlabel(r'$f$ [Hz]',fontsize=fs)



ax.set_yscale('log')
ax.axes.tick_params(axis="both", labelsize=fs-4)


plt.legend(title=None)
plt.savefig('../data/images/example_figure_check',bbox_inches='tight',dpi=300)

plt.show()












print(np.max(w))
print(np.min(w))


# con_list = [[element for element in upperElement] for upperElement in data['obj_contour']]



# print(con_list)

# import pandas as pd
# newData = list(zip(con_list[0], con_list[1]))
# columns = ['obj_contour_x', 'obj_contour_y']
# df = pd.DataFrame(newData, columns=columns)