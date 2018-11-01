import numpy as np
import matplotlib.pyplot as plt

N = 9
ind = np.arange(N)  # the x locations for the groups
width = 0.15      # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)

LRU_vals = [372116476.0, 405730589.0, 746298547.0, 503073222.0, 526027270.0, 1673491846.0, 885902764.0, 392916661.0, 422518717.0]
rects1 = ax.bar(ind, LRU_vals, width, color='#cccccc')

LFU_vals = [372116908.0, 412711519.0, 727013364.0, 499345847.0, 525815952.0, 1678171657.0, 728875544.0, 392916650.0, 445819568.0]

rects2 = ax.bar(ind+width, LFU_vals, width, color='#969696')

SRRIP_vals = [372116872.0, 395811931.0, 727718913.0, 508576599.0, 526588511.0, 1670937383.0, 621808110.0, 392932382.0, 444796783.0]
rects3 = ax.bar(ind+width*2, SRRIP_vals, width, color='#525252')

ax.set_ylabel('Cycles', fontsize=20)
ax.set_xticks(ind+width)
ax.set_xticklabels( ('blackscholes', 'bodytrack', 'canneal', 'dedup', 'fluidanimate', 'freqmine', 'streamcluster', 'swaptions', 'x264'), rotation=90, fontsize=20)
ax.legend( (rects1[0], rects2[0], rects3[0]), ('LRU', 'LFU', 'SRRIP'),fontsize = 'x-large' )

def autolabel(rects):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%d'%int(h),
                ha='center', va='bottom')

#autolabel(rects1)
#autolabel(rects2)
#autolabel(rects3)
ax.tick_params(axis = 'y', which = 'major', labelsize = 15)
ax.tick_params(axis = 'y', which = 'minor', labelsize = 15)
plt.show()
