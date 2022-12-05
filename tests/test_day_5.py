from advent_of_code_2022.day_5 import part_1, part_2

RAW_DATA = """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""


def test_part_1():
    assert part_1(RAW_DATA) == "CMZ"


def test_part_2():
    assert part_2(RAW_DATA) == "MCD"
