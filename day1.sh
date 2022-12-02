#!/usr/bin/env bash

# part 1
awk '/[0-9]+/{c += $1} /^$/{print c; c = 0}' < input/day1.txt | sort -nr | head -n 1

# part 2
awk '/[0-9]+/{c += $1} /^$/{print c; c = 0}' < input/day1.txt | sort -nr | head -n 3 | awk '{c += $1} END {print c}'
