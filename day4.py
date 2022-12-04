#!/usr/bin/env python

# https://adventofcode.com/2022/day/4

def section(ranges):
    r = ranges.split('-')
    return set(range(int(r[0]), int(r[1]) + 1))


def part_one(file):
    with open(file) as f:
        pairs = [line.rstrip().split(',') for line in f]

    fully_contained = 0
    for pair in pairs:
        sec1 = section(pair[0])
        sec2 = section(pair[1])
        if len(sec1 & sec2) == min(len(sec1), len(sec2)):
            fully_contained += 1

    return fully_contained

def test_part_one():
    assert part_one('input/day4_test.txt') == 2

print(f"part 1: {part_one('input/day4.txt')}")


def part_two(file):
    with open(file) as f:
        pairs = [line.rstrip().split(',') for line in f]

    overlap = 0
    for pair in pairs:
        sec1 = section(pair[0])
        sec2 = section(pair[1])
        if len(sec1 & sec2) > 0:
            overlap += 1

    return overlap

def test_part_two():
    assert part_two('input/day4_test.txt') == 4

print(f"part 2: {part_two('input/day4.txt')}")
