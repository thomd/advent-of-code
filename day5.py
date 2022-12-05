#!/usr/bin/env python

# https://adventofcode.com/2022/day/5

def crates(data):
    data.reverse()
    crates = []
    for level in data:
        cs = []
        for i, c in enumerate(level):
            if i % 4 == 1:
                cs.append(c)
        crates.append(cs)
    max_crates = len(crates[0])
    crates = [c  + [''] * (max_crates - len(c)) for c in crates]
    crates = list(zip(*crates))
    crates = {cl[0]: [l for l in list(cl[1:]) if (l != ' ' and l)] for cl in crates}
    return crates

def test_crates():
    assert crates(['    [D]', '[N] [C]', '[Z] [M] [P]', ' 1   2   3']) == {'1': ['Z', 'N'], '2': ['M', 'C', 'D'], '3': ['P']}


def parse_instruction(instruction):
    instr = instruction.split(' ')
    return int(instr[1]), instr[3], instr[5]

def test_parse_instruction():
    assert parse_instruction('move 2 from 2 to 1') == (2, '2', '1')


def message(crates):
    msg = ''
    for _, c in crates.items():
        msg += c[-1]
    return msg

def test_message():
    assert message({'1': ['C'], '2': ['M'], '3': ['P', 'D', 'N', 'Z']}) == 'CMZ'


def part_one(file):
    with open(file) as f:
        data = [line.rstrip() for line in f]
        c = crates(data[:data.index('')])

        for instruction in data[data.index('')+1:]:
            a, f, t = parse_instruction(instruction)
            for i in range(a):
                c[t] = c[t] + c[f][-1:]
                c[f] = c[f][:-1]

        return message(c)

def test_part_one():
    assert part_one('input/day5_test.txt') == 'CMZ'

print(f"part 1: {part_one('input/day5.txt')}")


def part_two(file):
    with open(file) as f:
        data = [line.rstrip() for line in f]
        c = crates(data[:data.index('')])

        for instruction in data[data.index('')+1:]:
            a, f, t = parse_instruction(instruction)
            c[t] = c[t] + c[f][-a:]
            c[f] = c[f][:-a]

        return message(c)


def test_part_two():
    assert part_two('input/day5_test.txt') == 'MCD'

print(f"part 2: {part_two('input/day5.txt')}")
