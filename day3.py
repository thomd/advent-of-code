#!/usr/bin/env python

# https://adventofcode.com/2022/day/3


def priority(char):
    return ord(char) - 96 if char.islower() else ord(char) - 38


def part_one(file):
    with open(file) as f:
        rucksack = [line.rstrip() for line in f]

    priority_sum = 0

    for items in rucksack:
        shared = set(items[:len(items) // 2]) & set(items[len(items) // 2:])
        item_priority = sum([priority(s) for s in shared])
        priority_sum += item_priority

    return priority_sum

def test_part_one():
    items = part_one('input/day3_test.txt')
    assert items == 157


print(f"part 1: {part_one('input/day3.txt')}")


def part_two(file):
    with open(file) as f:
        rucksack = [line.rstrip() for line in f]

    group = []
    priority_sum = 0

    for i, items in enumerate(rucksack):
        group.append(items)
        if (i % 3 == 2):
            shared = set(group[0]) & set(group[1]) & set(group[2])
            item_priority = sum([priority(s) for s in shared])
            priority_sum += item_priority
            group = []

    return priority_sum

def test_part_two():
    items = part_two('input/day3_test.txt')
    assert items == 70


print(f"part 2: {part_two('input/day3.txt')}")

