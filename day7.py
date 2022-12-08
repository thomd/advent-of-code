#!/usr/bin/env python

# https://adventofcode.com/2022/day/7

import fs # we use an in-memory filesystem: MemoryFS
import re

CD = re.compile(r'^\$ cd (.+)$')
MAKE_DIR = re.compile(r'^dir (.+)$')
MAKE_FILE = re.compile(r'^([0-9]+) (.+)$')


def get_size(_fs):
    size = 0
    for _, info in _fs.walk.info(namespaces=['details']):
        if info.is_file:
            size += info.size
    return size


def create_fs(data):
    p = ''
    root = fs.open_fs('mem://')
    with open(data) as f:
        term_outs = [line.rstrip() for line in f]
        for cmd in term_outs:
            if bool(CD.match(cmd)):
                _p = CD.search(cmd).group(1)
                if _p == '..':
                    p = re.sub(r'[^/]+/$', '', p)
                elif _p == '/':
                    p += '/'
                else:
                    p += _p + '/'
            if bool(MAKE_DIR.match(cmd)):
                _d = MAKE_DIR.search(cmd).group(1)
                root.makedir(p + _d)
            if bool(MAKE_FILE.match(cmd)):
                _s = MAKE_FILE.search(cmd).group(1)
                _f = MAKE_FILE.search(cmd).group(2)
                with root.open(p + _f, 'w') as f: f.write('0' * int(_s))

    # root.tree()
    return root



def part_one(data):
    root = create_fs(data)
    total = 0
    for dir_path in root.walk.dirs():
        _d = root.opendir(dir_path)
        s = get_size(_d)
        if s <= 100_000:
            total += s

    return total

def test_part_one():
    assert part_one('input/day7_test.txt') == 95437

print(f"part 1: {part_one('input/day7.txt')}")



def part_two(data):
    root = create_fs(data)
    spaces = []

    s = get_size(root.opendir('/'))
    unused = 70_000_000 - s
    spaces.append(s)

    for dir_path in root.walk.dirs():
        _d = root.opendir(dir_path)
        s = get_size(_d)
        spaces.append(s)

    for space in sorted(spaces):
        if unused + space >= 30_000_000:
            return space

def test_part_two():
    assert part_two('input/day7_test.txt') == 24933642

print(f"part 2: {part_two('input/day7.txt')}")

