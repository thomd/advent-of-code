#!/usr/bin/env bash

awk '/[0-9]+/{c += $1} /^$/{print c; c = 0}' < input/day1.txt | sort -nr | head -n 1
