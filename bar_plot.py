import numpy as np
import matplotlib.pyplot as plt

N = 7
ind = np.arange(N)  # the x locations for the groups
width = 0.20      # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)

yvals = [4,9,2,1,4,5,9,5,6]
rects1 = ax.bar(ind, yvals, width, color='r')
zvals = [1,3,4,5,8,9,5,5,9]
rects2 = ax.bar(ind+width, zvals, width, color='g')
kvals = [11,12,13,5,8,6,5,4,9]
rects3 = ax.bar(ind+width*2, kvals, width, color='b')

ax.set_ylabel('Cycles')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('blackschoels', 'bodytrack', 'canneal', 'dedup', 'fluidanimate', 'freqmine', 'streamcluster', 'swaptions', 'x264') )
ax.legend( (rects1[0], rects2[0], rects3[0]), ('LRU', 'LFU', 'SRRIP') )

def autolabel(rects):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%d'%int(h),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

plt.show()
