from advent_of_code_2022.day_1 import part_1, part_2

RAW_DATA = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""


def test_part_1():
    assert part_1(RAW_DATA) == 24000


def test_part_2():
    assert part_2(RAW_DATA) == 45000
