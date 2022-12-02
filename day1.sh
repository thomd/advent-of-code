#!/usr/bin/env bash

# https://adventofcode.com/2022/day/1


# --- Part One ---
awk '/[0-9]+/{c += $1} /^$/{print c; c = 0}' < input/day1.txt | sort -nr | head -n 1

# --- Part Two ---
awk '/[0-9]+/{c += $1} /^$/{print c; c = 0}' < input/day1.txt | sort -nr | head -n 3 | awk '{c += $1} END {print c}'
