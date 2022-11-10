#!/bin/bash
# Stranglega bannað að breyta línu 1 í þessu skjali
# Ef permission denied þarf að gera: chmod 755 runSim.sh
# Annars bara keyra skrá með: bash runSim.sh > result.txt

sim=./a.out
s='-s 1'
b='-b 3'
E='-E 8'
yi='-t traces/yi.trace'

for i in 1 2 3 4 5 6 7 8 9 10 11 12
do
    for j in 3 4 5 6 7 8 9 10 11 12 13 14
    do
        ./a.out -s $i -b $j $E $yi 
        echo 
        echo Results from s = $i, b = $j
        echo
    done
done