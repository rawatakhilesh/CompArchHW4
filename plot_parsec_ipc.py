import numpy as np
import matplotlib.pyplot as plt

N = 9
ind = np.arange(N)  # the x locations for the groups
width = 0.20      # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)

LRU_vals = [10.917818309662806, 12.323533055083505, 2.3073839590364362, 9.938980815003507, 9.505213374203965, 2.9877941526582137, 5.644055421414172, 12.725514075362664, 11.834045557797147]

rects1 = ax.bar(ind, LRU_vals, width, color='r')

LFU_vals = [10.917805272100132, 12.115267562958426, 2.3686266941855005, 10.013203872705885, 9.509225539813977, 2.9794630579915697, 6.859914073341443, 12.725497346574649, 11.215472406092323]

rects2 = ax.bar(ind+width, LFU_vals, width, color='g')

SRRIP_vals = [10.9178063095188, 12.632542774462248, 2.3661928915677364, 9.831459569377474, 9.495108602929623, 2.9923658659326313, 8.041092246288006, 12.724949925353823, 11.241214489629076]

rects3 = ax.bar(ind+width*2, SRRIP_vals, width, color='b')

ax.set_ylabel('Cycles')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('blackscholes', 'bodytrack', 'canneal', 'dedup', 'fluidanimate', 'freqmine', 'streamcluster', 'swaptions', 'x264') )
ax.legend( (rects1[0], rects2[0], rects3[0]), ('LRU', 'LFU', 'SRRIP') )

def autolabel(rects):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%d'%int(h),
                ha='center', va='bottom')

#autolabel(rects1)
#autolabel(rects2)
#autolabel(rects3)

plt.show()
