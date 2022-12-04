from advent_of_code_2022.day_3 import part_2
from advent_of_code_2022.day_3 import part_1


RAW_DATA = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""


def test_part_1():
    assert part_1(RAW_DATA) == 157


def test_part_2():
    assert part_2(RAW_DATA) == 70
