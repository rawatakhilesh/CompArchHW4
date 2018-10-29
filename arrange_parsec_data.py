# PARSEC benchmarks

int_bms = ['blackscholes', 'bodytrack', 'canneal', 'dedup', 'fluidanimate', 'freqmine', 'streamcluster', 'swaptions', 'x264']

#LRU
#total_cycles_list = {'x264_8c_simlarge': 422518717.0, 'blackscholes_8c_simlarge': 372116476.0, 'canneal_8c_simlarge': 746298547.0, 'bodytrack_8c_simlarge': 405730589.0, 'freqmine_8c_simlarge': 1673491846.0, 'dedup_8c_simlarge': 503073222.0, 'fluidanimate_8c_simlarge': 526027270.0, 'swaptions_8c_simlarge': 392916661.0, 'streamcluster_8c_simlarge': 885902764.0}

#SRRIP
total_cycles_list = {'bodytrack_8c_simlarge': 395811931.0, 'fluidanimate_8c_simlarge': 526588511.0, 'freqmine_8c_simlarge': 1670937383.0, 'x264_8c_simlarge': 444796783.0, 'streamcluster_8c_simlarge': 621808110.0, 'canneal_8c_simlarge': 727718913.0, 'swaptions_8c_simlarge': 392932382.0, 'blackscholes_8c_simlarge': 372116872.0, 'dedup_8c_simlarge': 508576599.0}

#SRRIP
#MPKI_list = {'bodytrack_8c_simlarge': 0.0278531808293608, 'fluidanimate_8c_simlarge': 0.8815785374565013, 'freqmine_8c_simlarge': 1.0664328582981393, 'x264_8c_simlarge': 0.6630149686630252, 'streamcluster_8c_simlarge': 1.9457962286848287, 'canneal_8c_simlarge': 11.920473910487765, 'swaptions_8c_simlarge': 0.0022419798737466734, 'blackscholes_8c_simlarge': 0.0072486278794048455, 'dedup_8c_simlarge': 1.2963319664191433}

#LRU
MPKI_list = {'x264_8c_simlarge': 0.8175283099302676, 'blackscholes_8c_simlarge': 0.007253058177079439, 'canneal_8c_simlarge': 13.234347146152546, 'bodytrack_8c_simlarge': 0.03637395029283124, 'freqmine_8c_simlarge': 1.059613983570696, 'dedup_8c_simlarge': 1.2980636870736912, 'fluidanimate_8c_simlarge': 0.8982987409306431, 'swaptions_8c_simlarge': 0.002241970181796582, 'streamcluster_8c_simlarge': 5.621512023555888}

align = []

for bm in int_bms:
	for key,value in MPKI_list.items():
		if key.split('_')[0] == bm:
			align.append(value)

print(align)			
	
