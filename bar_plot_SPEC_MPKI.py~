import numpy as np
import matplotlib.pyplot as plt

N = 14
ind = np.arange(N)  # the x locations for the groups
width = 0.25      # the width of the bars

fig = plt.figure()
#ax = fig.add_subplot(111)
ax = fig.add_subplot(111)

LRU_vals = [2.8168531910891725, 2.5974919176735396, 80.99625944110946, 1.4202997355923572, 0.36229593992662945, 25.045565085507427, 2.0191493708059736, 14.945166989035757, 4.830405757123262, 23.84398527618963, 0.3716077108965009, 20.806163789637743, 0.05888974140704689, 30.952674014000753]
rects1 = ax.bar(ind, LRU_vals, width, color='r')

SRRIP_vals = [2.7250012793222, 2.3905294065225737, 76.92752075309967, 1.3674829331587075, 0.36929376262834923, 25.05029146425295, 1.9018297880237176, 14.953269813085754, 4.748896641746026, 23.882804091880917, 0.2682510817327352, 19.973408894664335, 0.05889534491193816, 30.993577439825042]
rects2 = ax.bar(ind+width, SRRIP_vals, width, color='g')

LFU_vals = [2.725362801850996, 2.6319631832153556, 77.41270272491076, 1.3726827385583098, 0.3621754003724153, 25.045605913290682, 1.9357537611306417, 14.944587125286134, 4.790573681000316, 23.837535441728896, 0.2681954460413262, 21.32582141536412, 0.05889121814155073, 30.962532310916895]
rects3 = ax.bar(ind+width*2, LFU_vals, width, color='b')

ax.set_ylabel('MPKI')
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
