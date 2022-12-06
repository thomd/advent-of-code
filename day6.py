#!/usr/bin/env python

# https://adventofcode.com/2022/day/6

def message_position(w, s):
    return [len(set(w[i-s+1:i+1])) for i in range(s-1, len(w))].index(s) + s

def test_message_position():
    assert message_position('bvwbjplbgvbhsrlpgdmjqwftvncz', 4) == 5
    assert message_position('nppdvjthqldpwncqszvftbrmjlhg', 4) == 6
    assert message_position('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 4) == 10
    assert message_position('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 4) == 11
    assert message_position('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 14) == 19
    assert message_position('bvwbjplbgvbhsrlpgdmjqwftvncz', 14) == 23
    assert message_position('nppdvjthqldpwncqszvftbrmjlhg', 14) == 23
    assert message_position('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 14) == 29
    assert message_position('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 14) == 26

with open('input/day6.txt') as f:
    data = [line.rstrip() for line in f]
    print(f"part 1: {message_position(data[0], 4)}")


with open('input/day6.txt') as f:
    data = [line.rstrip() for line in f]
    print(f"part 2: {message_position(data[0], 14)}")
