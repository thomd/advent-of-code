#!/usr/bin/env python

# https://adventofcode.com/2022/day/5

def part_one(file):
    with open(file) as f:
        data = [line.rstrip() for line in f]
        data_levels = data[:data.index('')]
        data_levels.reverse()
        crates = []
        for level in data_levels:
            cs = []
            for i, c in enumerate(level):
                if i % 4 == 1:
                    cs.append(c)
            crates.append(cs)
        m = len(crates[0])
        crates = [c  + [''] * (m - len(c)) for c in crates]
        crates = list(zip(*crates))
        crates = {cl[0]: [l for l in list(cl[1:]) if (l != ' ' and l)] for cl in crates}

        instructions = data[data.index('')+1:]
        for instruction in instructions:
            instruction = instruction.split(' ')
            a = instruction[1]
            f = instruction[3]
            t = instruction[5]
            for i in range(int(a)):
                crates[t] = crates[t] + crates[f][-1:]
                crates[f] = crates[f][:-1]

        message = ''
        for _, c in crates.items():
            message += c[-1]

        return message

def test_part_one():
    assert part_one('input/day5_test.txt') == 'CMZ'

print(f"part 1: {part_one('input/day5.txt')}")


def part_two(file):
    with open(file) as f:
        data = [line.rstrip() for line in f]
        data_levels = data[:data.index('')]
        data_levels.reverse()
        crates = []
        for level in data_levels:
            cs = []
            for i, c in enumerate(level):
                if i % 4 == 1:
                    cs.append(c)
            crates.append(cs)
        m = len(crates[0])
        crates = [c  + [''] * (m - len(c)) for c in crates]
        crates = list(zip(*crates))
        crates = {cl[0]: [l for l in list(cl[1:]) if (l != ' ' and l)] for cl in crates}

        instructions = data[data.index('')+1:]
        for instruction in instructions:
            instruction = instruction.split(' ')
            a = instruction[1]
            f = instruction[3]
            t = instruction[5]
            crates[t] = crates[t] + crates[f][-int(a):]
            crates[f] = crates[f][:-int(a)]

        message = ''
        for _, c in crates.items():
            message += c[-1]

        return message

def test_part_two():
    assert part_two('input/day5_test.txt') == 'MCD'

print(f"part 2: {part_two('input/day5.txt')}")
