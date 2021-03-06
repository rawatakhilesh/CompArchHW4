# Akhilesh Rawat
# walk the path and grab the lines
# leaves the single thread benchmarks

import os
import sys
import glob

debug = 1
total_cycles_list = {}
IPC_list = {}
MPKI_list = {}
# set to print debug messages

def get_val(str):
	# returns digit from the recived line
	return [s for s in str.split() if s.isdigit()]

def calculate(cycles_list, miss_list, bm_name):
	if debug:	
		print(cycles_list)
	#[westmere0, cycles, cCycles, total_instruction, westmere0, cycles, cCycles, total_instruction,...
	# [l3, mGETS, mGETXIM, mGETXSM, l3, mGETS, mGETXIM, mGETXSM....]
	j = 0;
	all_core_cycle_val = [] 
	total_instruction = 0
	while j < len(cycles_list):
		cycles = get_val(cycles_list[j+1])
		cCycles = get_val(cycles_list[j+2])
		if debug:
			print(cycles)
			print(cCycles)
			
		sum_cycles = float(cycles[0]) + float(cCycles[0])
		if debug:
			print(sum_cycles)
		all_core_cycle_val.append(sum_cycles)
	
		instructions = get_val(cycles_list[j+3])
		if debug:
			print(instructions)
		# adding instructions across all cores
		total_instruction += float(instructions[0])	
		j += 4		
	
	if debug:
		print(all_core_cycle_val)		

	total_cycles = max(all_core_cycle_val)
	print('total_cycles: {}'.format(total_cycles))
	print('total_instructions: {}'.format(total_instruction))
	total_cycles_list[bm_name] = total_cycles

	IPC = total_instruction/total_cycles
	print('IPC: {}'.format(IPC))
	IPC_list[bm_name] = IPC

	k = 0
	total_misses = 0
	if debug:	
		print(miss_list)
	while k < len(miss_list):
		mGETS = get_val(miss_list[k+1])
		mGETXIM = get_val(miss_list[k+2])
		mGETXSM = get_val(miss_list[k+3])
		if debug:
			print('{},{},{}'.format(mGETS, mGETXIM, mGETXSM))
		
		# for each core
		misses = float(mGETS[0]) + float(mGETXIM[0]) + float(mGETXSM[0])
		# total misses for all cores
		total_misses += misses
		k += 4
		
	print('total_misses: {}'.format(total_misses))

	MPKI = (total_misses/total_instruction) * 1000
	print('MPKI: {}'.format(MPKI))
	MPKI_list[bm_name] = MPKI
	
# As Dr. Bettati would say - programming at the level of a baboon. 
# but the next functions gets the work done.

#[434,437,438,439,447,450,451,452,460,463,464,465,.....
def more_lines_of_interest():
	# l30 - 7
	flag = 0
	counter = 434
	m_l_of_i = []
	while counter < 531: #last line containing l3 mGETXSM
		if flag <= 3:
			m_l_of_i.append(counter)
			counter += 1
			flag += 1
		elif flag == 4:
			flag = 0;
			counter += 7
		if flag == 1:
			counter += 2
			
	return m_l_of_i	

#[14, 15, 16, 17, 23, 24, 25, 26, 32, 33, 34, 35, 41, 42, 43, 44, 50, 51, 52, 53, 
# 59, 60, 61, 62, 68, 69, 70, 71, 77, 78, 79, 80]
def lines_of_interest():
	# westmere0 - 7
	flag = 0
	counter = 14
	l_of_i = []
	while counter < 81: # last line containing Instructions of westmere7
		if flag <= 3:
			l_of_i.append(counter)
			counter += 1
			flag += 1
		elif flag == 4:
			flag = 0;
			counter += 5
	return l_of_i		

def helper(root_dir):
	try:
		cycles_info = lines_of_interest() # lines containing cycles information
		miss_info = more_lines_of_interest() # lines containing cache miss info
		print('walking {} ...\n'.format(root_dir))
		for root, dirs, files in os.walk(root_dir, topdown=False):
			for bm_name in dirs:
				name_re = bm_name.split('_')
				if name_re[-1] == 'simlarge':
					dir = os.path.join(root, bm_name)
					print("for benchmark {} ...".format(bm_name))
					for sub_root, sub_dirs, sub_files in                     \
												   os.walk(dir, topdown=False):
						#reading .out files
						for file in glob.glob(os.path.join(sub_root, '*.out')):
							file_name = file.split('/')
							if debug:
								print('reading {} ...'.format(file_name[-1]))
							with open(file, 'r') as fp:
								c_list = []
								m_list = []
								for i, line in enumerate(fp):
									if i in cycles_info:
										# reading corresponding lines from the log file
										if debug:
											print(line.strip())
										c_list.append(line.strip())
									elif i in miss_info:
										if debug:
											print(line.strip())
										m_list.append(line.strip())
										
							calculate(c_list, m_list, bm_name)
							print('\n')

		print('total_cycles_list = {}'.format(total_cycles_list))
		print('IPC_list = {}'.format(IPC_list))
		print('MPKI_list = {}'.format(MPKI_list))

	except Exception as error:
		print(error)


#source directory path here
if __name__ == '__main__':
	if len(sys.argv) > 1:
		path = sys.argv[1].strip('\'')
		helper(path)
	else:
		print('Please pass the path as argument!')
