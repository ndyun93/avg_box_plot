import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#avoid pdf font type 3

sns.set(style="whitegrid")

plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42
# # include if using a Jupyter notebook
# %matplotlib inline
# #reference
# # https://ultrabem-branch3.com/statistics/basics/error_bar
# # https://bookdown.org/max/FES/detecting-interaction-effects.html
# #https://stackoverflow.com/questions/18498742/how-do-you-make-an-errorbar-plot-in-matplotlib-using-linestyle-none-in-rcparams
# # zoom out and in 
# # https://matplotlib.org/3.1.1/gallery/subplots_axes_and_figures/axes_margins.html




# mean average
hm_mean = 3.05
hs_mean = 3.57 #orange
rm_mean = 2.98
rs_mean = 2.51 #orange


#standard deviation
hm_std = 0.92
hs_std = 1.34
rm_std = 0.91
rs_std = 1.08

labels = ['Human motion', 'Human Static','Robot Motion', 'Robot Static' ]
# x_pos = np.arange(len(label))


hm = [hm_mean,hm_std]
hs = [hs_mean,hs_std]
rm = [rm_mean,rm_std]
rs = [rs_mean,rs_std]

alldata = [hm,hs,rm,rs]

fig, ax = plt.subplots()


ax.boxplot( alldata,
            vert=True,  # vertical box alignment
            patch_artist =True,  # fill with color
            labels=labels,
            showmeans=True,
            meanline=True
            )

# plt.grid()
plt.savefig("anthro_test1.pdf") 
plt.show()
 
