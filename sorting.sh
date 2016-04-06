#!/bin/bash
numBarcodes=$1

sort --parallel=8 barcodes.txt > bc_temp.txt
uniq -c bc_temp.txt > bc_temp2.txt
sort --parallel=8 -hr bc_temp2.txt > barcodesSorted.txt

head -${numBarcodes} barcodesSorted.txt | awk '{print $2}' > topBarcodes.txt
sed 1,${numBarcodes}d barcodesSorted.txt | awk '{print $2}' > restBarcodes.txt

rm bc_temp*
