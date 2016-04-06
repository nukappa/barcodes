import sys

d = dict()

with open('test.deletions_collapsed.map2000.AGC.tsv', 'r') as f:
	for line in f:
		key, val = line.split()
		d[key] = val

fi = open('topBarcodes.txt', 'r')
fo = open('topBarcodesNew.txt', 'w')

for line in fi:
	if line[0:12] in d:
		fo.write(d[line[0:12]] + '\n')
	else:
		fo.write(line)