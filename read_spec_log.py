# Akhilesh Rawat
# walk the path and grab the lines
# leaves the multi thread benchmarks

import os
import sys
import glob

debug = 1
total_cycles_list = {}
IPC_list = {}
MPKI_list = {}
# set to print debug messages

def get_val(str):
	return [s for s in str.split() if s.isdigit()]

def calculate(list, bm_name):
	#print(list)
	#[cycles, cCycles, total_instruction, mGETS, mGETXIM, mGETXSM]
	cycles = get_val(list[0])
	cCycles = get_val(list[1])
	if debug:
		print(cycles)
		print(cCycles)

	total_cycles = float(cycles[0]) + float(cCycles[0])
	print('total_cycles: {}'.format(total_cycles))
	total_cycles_list[bm_name] = total_cycles

	total_instruction = get_val(list[2])
	if debug:
		print(total_instruction)
	total_instruction = float(total_instruction[0])
	IPC = total_instruction/total_cycles
	print('IPC: {}'.format(IPC))
	IPC_list[bm_name] = IPC

	mGETS = get_val(list[3])
	mGETXIM = get_val(list[4])
	mGETXSM = get_val(list[5])
	if debug:
		print('{},{},{}'.format(mGETS, mGETXIM, mGETXSM))

	total_misses = float(mGETS[0]) + float(mGETXIM[0]) + float(mGETXSM[0])
	print('total_misses: {}'.format(total_misses))

	MPKI = (total_misses/total_instruction) * 1000
	print('MPKI: {}'.format(MPKI))
	MPKI_list[bm_name] = MPKI


def helper(root_dir):
	try:
		print('walking {} ...\n'.format(root_dir))
		for root, dirs, files in os.walk(root_dir, topdown=False):
			for bm_name in dirs:
				name_re = bm_name.split('_')
				if name_re[-1] != 'simlarge':
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
								list = []
								for i, line in enumerate(fp):
									# As Dr. Bettati would say - programming at the level of a baboon. 
									# but the next line gets the work done.
									if i in [15, 16, 17, 73, 74, 75]:
										# reading 3rd line
										if debug:
											print(line.strip())
										list.append(line.strip())
							calculate(list, bm_name)
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
