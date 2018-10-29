import numpy as np
import matplotlib.pyplot as plt

N = 14
ind = np.arange(N)  # the x locations for the groups
width = 0.25      # the width of the bars

fig = plt.figure()
#ax = fig.add_subplot(111)
ax = fig.add_subplot(111)

LRU_vals = [1.0135693228970828, 0.8003812299943571, 0.12495579405144586, 1.479077765529804, 1.2108683888842253, 0.511230756890896, 1.4393459112704239, 0.6564833161470517, 1.058372201016964, 0.4640992482154139, 1.8196312878359289, 0.43846440382686336, 2.0235756079001606, 0.5752683203251878]
rects1 = ax.bar(ind, LRU_vals, width, color='r')

SRRIP_vals = [1.0156734308936928, 0.8218683995701119, 0.12941743488943835, 1.494695349003474, 1.2095115177538416, 0.5116383245304247, 1.4587933239814628, 0.6561019760078659, 1.0632155602462592, 0.46295760927369123, 1.8753646872388914, 0.4436073937892675, 2.0234035469686398, 0.5739264217651501]
rects2 = ax.bar(ind+width, SRRIP_vals, width, color='g')

LFU_vals = [1.0198706276976015, 0.7946078543318483, 0.12891245537818374, 1.4948487870469302, 1.2107883455401245, 0.5112137820954696, 1.456668457128385, 0.6646331015485224, 1.06113157585153, 0.4641208539389567, 1.8753783136434456, 0.4322892756012097, 2.0210527541002965, 0.5750442396619796]
rects3 = ax.bar(ind+width*2, LFU_vals, width, color='b')

ax.set_ylabel('IPC')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('bzip2', 'gcc', 'mcf', 'hmmer', 'sjeng', 'libquantum', 'xalan', 'milc', 'cactusADM', 'leslie3d', 'namd', 'soplex', 'calculix', 'lbm') )

ax.legend( (rects1[0], rects2[0], rects3[0]), ('LRU', 'SRRIP', 'LFU') )

def autolabel(rects):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%d'%int(h),
                ha='left', va='bottom', rotation = 60)

#autolabel(rects1)
#autolabel(rects2)
#autolabel(rects3)

plt.show()
