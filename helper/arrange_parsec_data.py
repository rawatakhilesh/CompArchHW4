# PARSEC benchmarks

int_bms = ['blackscholes', 'bodytrack', 'canneal', 'dedup', 'fluidanimate', 'freqmine', 'streamcluster', 'swaptions', 'x264']

#LRU
#total_cycles_list = {'x264_8c_simlarge': 422518717.0, 'blackscholes_8c_simlarge': 372116476.0, 'canneal_8c_simlarge': 746298547.0, 'bodytrack_8c_simlarge': 405730589.0, 'freqmine_8c_simlarge': 1673491846.0, 'dedup_8c_simlarge': 503073222.0, 'fluidanimate_8c_simlarge': 526027270.0, 'swaptions_8c_simlarge': 392916661.0, 'streamcluster_8c_simlarge': 885902764.0}

#SRRIP
#total_cycles_list = {'bodytrack_8c_simlarge': 395811931.0, 'fluidanimate_8c_simlarge': 526588511.0, 'freqmine_8c_simlarge': 1670937383.0, 'x264_8c_simlarge': 444796783.0, 'streamcluster_8c_simlarge': 621808110.0, 'canneal_8c_simlarge': 727718913.0, 'swaptions_8c_simlarge': 392932382.0, 'blackscholes_8c_simlarge': 372116872.0, 'dedup_8c_simlarge': 508576599.0}

#LFU
#total_cycles_list = {'blackscholes_8c_simlarge': 372116908.0, 'dedup_8c_simlarge': 499345847.0, 'canneal_8c_simlarge': 727013364.0, 'streamcluster_8c_simlarge': 728875544.0, 'swaptions_8c_simlarge': 392916650.0, 'freqmine_8c_simlarge': 1678171657.0, 'x264_8c_simlarge': 445819568.0, 'fluidanimate_8c_simlarge': 525815952.0, 'bodytrack_8c_simlarge': 412711519.0}

#LFU
#IPC_list = {'blackscholes_8c_simlarge': 10.917805272100132, 'dedup_8c_simlarge': 10.013203872705885, 'canneal_8c_simlarge': 2.3686266941855005, 'streamcluster_8c_simlarge': 6.859914073341443, 'swaptions_8c_simlarge': 12.725497346574649, 'freqmine_8c_simlarge': 2.9794630579915697, 'x264_8c_simlarge': 11.215472406092323, 'fluidanimate_8c_simlarge': 9.509225539813977, 'bodytrack_8c_simlarge': 12.115267562958426}

#LRU
#IPC_list = {'x264_8c_simlarge': 11.834045557797147, 'blackscholes_8c_simlarge': 10.917818309662806, 'canneal_8c_simlarge': 2.3073839590364362, 'bodytrack_8c_simlarge': 12.323533055083505, 'freqmine_8c_simlarge': 2.9877941526582137, 'dedup_8c_simlarge': 9.938980815003507, 'fluidanimate_8c_simlarge': 9.505213374203965, 'swaptions_8c_simlarge': 12.725514075362664, 'streamcluster_8c_simlarge': 5.644055421414172}

#SRRIP
#IPC_list = {'bodytrack_8c_simlarge': 12.632542774462248, 'fluidanimate_8c_simlarge': 9.495108602929623, 'freqmine_8c_simlarge': 2.9923658659326313, 'x264_8c_simlarge': 11.241214489629076, 'streamcluster_8c_simlarge': 8.041092246288006, 'canneal_8c_simlarge': 2.3661928915677364, 'swaptions_8c_simlarge': 12.724949925353823, 'blackscholes_8c_simlarge': 10.9178063095188, 'dedup_8c_simlarge': 9.831459569377474}

#SRRIP
#MPKI_list = {'bodytrack_8c_simlarge': 0.0278531808293608, 'fluidanimate_8c_simlarge': 0.8815785374565013, 'freqmine_8c_simlarge': 1.0664328582981393, 'x264_8c_simlarge': 0.6630149686630252, 'streamcluster_8c_simlarge': 1.9457962286848287, 'canneal_8c_simlarge': 11.920473910487765, 'swaptions_8c_simlarge': 0.0022419798737466734, 'blackscholes_8c_simlarge': 0.0072486278794048455, 'dedup_8c_simlarge': 1.2963319664191433}

#LRU
#MPKI_list = {'x264_8c_simlarge': 0.8175283099302676, 'blackscholes_8c_simlarge': 0.007253058177079439, 'canneal_8c_simlarge': 13.234347146152546, 'bodytrack_8c_simlarge': 0.03637395029283124, 'freqmine_8c_simlarge': 1.059613983570696, 'dedup_8c_simlarge': 1.2980636870736912, 'fluidanimate_8c_simlarge': 0.8982987409306431, 'swaptions_8c_simlarge': 0.002241970181796582, 'streamcluster_8c_simlarge': 5.621512023555888}

#LFU
MPKI_list = {'blackscholes_8c_simlarge': 0.007248627866915517, 'dedup_8c_simlarge': 1.247926079222961, 'canneal_8c_simlarge': 11.85006176289973, 'streamcluster_8c_simlarge': 3.2404659037047483, 'swaptions_8c_simlarge': 0.0022461731416092766, 'freqmine_8c_simlarge': 1.0616984859758987, 'x264_8c_simlarge': 0.7802307746151632, 'fluidanimate_8c_simlarge': 0.8779400057416423, 'bodytrack_8c_simlarge': 0.03659959130275049}

align = []

for bm in int_bms:
	for key,value in MPKI_list.items():
		if key.split('_')[0] == bm:
			align.append(value)

print(align)			
	
