# Cache Simulator

## Overview
Simulates a cache using LRU (Least Recently Used) policy to analyze data cache performance, based on Valgrind traces. Outputs statistics such as hits, misses, and evictions.

## Requirements
- 64-bit system
- GCC compiler

## Quick Start
```bash
git clone https://github.com/sturla-freyr/simpleCacheSimulator.git
cd simpleCacheSimulator
make
./csim -s <set bits> -E <lines per set> -b <block bits> -t <trace file>

## Automated Simulation
For running a series of simulations with different configurations:
bash runSim.sh > useData/result.txt
