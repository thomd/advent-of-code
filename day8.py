#!/usr/bin/env python

# https://adventofcode.com/2022/day/8

import numpy as np

def create_trees_array(data):
    return np.array(list(''.join(data))).reshape(len(data), -1)

def visible_edge_trees(trees):
    return 2 * trees.shape[0] + 2 * trees.shape[1] - 4

def visible_interior_trees(t):
    visible = 0
    for i in range(1, t.shape[0] - 1):
        for j in range(1, t.shape[1] - 1):
            tree = t[i, j].astype(int)
            if t[:i,j].astype(int).max() < tree or t[i+1:,j].astype(int).max() < tree or t[i,:j].astype(int).max() < tree or t[i,j+1:].astype(int).max() < tree:
                visible += 1

    return visible

def highest_scenic_score(t):
    scores = []
    for i in range(1, t.shape[0] - 1):
        for j in range(1, t.shape[1] - 1):
            scores.append(scenic_score(t, i, j))

    return max(scores)

def scenic_score(t, i, j):
    tree = t[i, j].astype(int)

    up_score = 0
    for l in list(np.flip(t[:i, j])):
        up_score += 1
        if tree <= l.astype(int):
            break

    left_score = 0
    for l in list(np.flip(t[i, :j])):
        left_score += 1
        if tree <= l.astype(int):
            break

    right_score = 0
    for l in list(t[i, j+1:]):
        right_score += 1
        if tree <= l.astype(int):
            break

    down_score = 0
    for l in list(t[i+1:, j]):
        down_score += 1
        if tree <= l.astype(int):
            break

    return up_score * left_score * right_score * down_score



def part_one(data):
    with open(data) as f:
        trees = create_trees_array([line.rstrip() for line in f])
        return visible_edge_trees(trees) + visible_interior_trees(trees)

def test_part_one():
    assert part_one('input/day8_test.txt') == 21

print(f"part 1: {part_one('input/day8.txt')}")



def part_two(data):
    with open(data) as f:
        trees = create_trees_array([line.rstrip() for line in f])
        return highest_scenic_score(trees)

def test_part_two():
    with open('input/day8_test.txt') as f:
        trees = create_trees_array([line.rstrip() for line in f])
        assert scenic_score(trees, 1, 2) == 4
        assert scenic_score(trees, 3, 2) == 8

print(f"part 2: {part_two('input/day8.txt')}")
