import sys

d = dict()

filename = sys.argv[1]

with open('collapseThem.txt', 'r') as f:
	for line in f:
		key, val = line.split()
		d[key] = val

fi = open(filename + '_1.fastq', 'r')
fo = open(filename + '_collapsed_1.fastq', 'w')

for line in fi:
	if line[0:12] in d:
		fo.write(d[line[0:12]] + line[12:20] + '\n')
	else:
		fo.write(line)
		
