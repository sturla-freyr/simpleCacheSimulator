#!/bin/bash
# Stranglega bannað að breyta línu 1 í þessu skjali
# Ef permission denied þarf að gera: chmod 755 runSim.sh
# Annars bara keyra skrá með: bash runSim.sh > useData/result.txt

E=8
traces='mmulijk.trace ls.trace'
for t in $traces
do
  for i in 1 2 3 4 5 6 7 8 9 10 11 12
  do
    for j in 3 4 5 6 7 8 9 10 11 12 13 14
    do
        echo Results from s = $i E = $E b = $j t = traces/$t
        echo
        ./a.out -s $i -E $E -b $j -t traces/$t 
        echo 
    done
  done
done
