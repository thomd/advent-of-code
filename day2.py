#!/usr/bin/env python

# opponent:
#   A: Rock
#   B: Paper
#   C: Scissors

# you:
#   X: Rock
#   Y: Paper
#   Z: Scissors



# --- Part One ---

# win:
#   A Y: your Paper defeats opponents Rock
#   B Z: your Scissors defeats opponents Paper
#   C X: your Rock defeats opponents Scissors

# same:
#   A X
#   B Y
#   C Z

# loose:
#   A Z: your Scissors loose opponents Rock
#   B X: your Rock loose opponents Paper
#   C Y: your Paper loose opponents Scissors



# --- Part Two ---

# how the round needs to end:
#   X: you need to lose (A X -> A Z, B X -> B X, C X -> C Y)
#   Y: you need to end the round in a draw (A Y -> A X, B Y -> B Y, C Y -> C Z)
#   Z: you need to win (A Z -> A Y, B Z -> B Z, C Z -> C X)


def calculateScore(result):
    score = 0
    you = result.split()[1]
    if you == 'X':
        score += 1
    if you == 'Y':
        score += 2
    if you == 'Z':
        score += 3
    if result in ['A X', 'B Y', 'C Z']:
        score += 3
    if result in ['A Y', 'B Z', 'C X']:
        score += 6
    return score

mapping = {
    'A X': 'A Z',
    'B X': 'B X',
    'C X': 'C Y',
    'A Y': 'A X',
    'B Y': 'B Y',
    'C Y': 'C Z',
    'A Z': 'A Y',
    'B Z': 'B Z',
    'C Z': 'C X'
}

with open('input/day2.txt') as file:
    results = [line.rstrip() for line in file]

total = sum([calculateScore(result) for result in results])
print(f'part 1: {total}')

total = sum([calculateScore(mapping[result]) for result in results])
print(f'part 2: {total}')

