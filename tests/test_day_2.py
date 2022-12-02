from advent_of_code_2022.day_2 import part_1, part_2


RAW_DATA = """
A Y
B X
C Z
"""


def test_part_1():
    assert part_1(RAW_DATA) == 15


def test_part_2():
    assert part_2(RAW_DATA) == 12
