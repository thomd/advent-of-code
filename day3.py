#!/usr/bin/env python

# https://adventofcode.com/2022/day/3

with open('input/day3.txt') as file:
    rucksack = [line.rstrip() for line in file]

def priority(char):
    return ord(char) - 96 if char.islower() else ord(char) - 38


# --- Part One ---
priority_sum = 0
for items in rucksack:
    shared = set(items[:len(items) // 2]) & set(items[len(items) // 2:])
    item_priority = sum([priority(s) for s in shared])
    priority_sum += item_priority

print(f'part 1: {priority_sum}')


# --- Part Two ---
group = []
priority_sum = 0
for i, items in enumerate(rucksack):
    group.append(items)
    if (i % 3 == 2):
        shared = set(group[0]) & set(group[1]) & set(group[2])
        item_priority = sum([priority(s) for s in shared])
        priority_sum += item_priority
        group = []

print(f'part 2: {priority_sum}')

