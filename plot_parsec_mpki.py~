import numpy as np
import matplotlib.pyplot as plt

N = 9
ind = np.arange(N)  # the x locations for the groups
width = 0.20      # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)

LRU_vals = [0.007253058177079439, 0.03637395029283124, 13.234347146152546, 1.2980636870736912, 0.8982987409306431, 1.059613983570696, 5.621512023555888, 0.002241970181796582, 0.8175283099302676]

rects1 = ax.bar(ind, LRU_vals, width, color='r')

#LFU_vals = [1,3,4,5,8,9,5,5,9]
#rects2 = ax.bar(ind+width, LFU_vals, width, color='g')

SRRIP_vals = [0.0072486278794048455, 0.0278531808293608, 11.920473910487765, 1.2963319664191433, 0.8815785374565013, 1.0664328582981393, 1.9457962286848287, 0.0022419798737466734, 0.6630149686630252]
rects3 = ax.bar(ind+width*2, SRRIP_vals, width, color='b')

ax.set_ylabel('Cycles')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('blackscholes', 'bodytrack', 'canneal', 'dedup', 'fluidanimate', 'freqmine', 'streamcluster', 'swaptions', 'x264') )
#ax.legend( (rects1[0], rects2[0], rects3[0]), ('LRU', 'LFU', 'SRRIP') )

ax.legend( (rects1[0], rects3[0]), ('LRU', 'SRRIP') )

def autolabel(rects):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%d'%int(h),
                ha='center', va='bottom')

#autolabel(rects1)
#autolabel(rects2)
#autolabel(rects3)

plt.show()
