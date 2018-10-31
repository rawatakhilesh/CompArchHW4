import numpy as np
import matplotlib.pyplot as plt

N = 14
ind = np.arange(N)  # the x locations for the groups
width = 0.25      # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)

LRU_vals = [98677584.0, 124946622.0, 800285395.0, 67612090.0, 82590843.0, 195613530.0, 69479809.0, 152332738.0, 94495169.0, 215493245.0, 54956527.0, 228084757.0, 49426085.0, 173837744.0]
rects1 = ax.bar(ind, LRU_vals, width, color='#cccccc')

LFU_vals = [98076016.0, 125848566.0, 775722010.0, 66900651.0, 82591867.0, 195618613.0, 68656406.0, 150467438.0, 94243669.0, 215465050.0, 53323480.0, 231329928.0, 49486542.0, 173906166.0]
rects2 = ax.bar(ind+width, LFU_vals, width, color='#969696')

SRRIP_vals = [98470527.0, 121679101.0, 772696222.0, 66914864.0, 82679402.0, 195459449.0, 68559546.0, 152415537.0, 94061699.0, 216022720.0, 53332686.0, 225425359.0, 49425585.0, 174244055.0]
rects3 = ax.bar(ind+width*2, SRRIP_vals, width, color='#525252')



ax.set_ylabel('Cycles')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('bzip2', 'gcc', 'mcf', 'hmmer', 'sjeng', 'libquantum', 'xalan', 'milc', 'cactusADM', 'leslie3d', 'namd', 'soplex', 'calculix', 'lbm') )

ax.legend( (rects1[0], rects2[0], rects3[0]), ('LRU', 'LFU', 'SRRIP') )

def autolabel(rects):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%d'%int(h),
                ha='left', va='bottom', rotation = 60)

#autolabel(rects1)
#autolabel(rects2)
#autolabel(rects3)

plt.show()
